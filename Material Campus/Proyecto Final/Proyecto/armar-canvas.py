#!/usr/bin/env python3
"""Arma el poster del Business Model Canvas en A3 apaisado.

    python3 armar-canvas.py

El contenido sale de este archivo, no del .md: el .md es el desarrollo escrito
y el poster es la version resumida para mirar de un vistazo. Si se corrige un
bloque hay que corregirlo en los dos lados.

Necesita weasyprint.
"""
import io, os, shutil, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(BASE, "BMC - Dulxelitos.pdf")

BLOQUES = {
 "socios": ("8", "Socios clave", "¿Quiénes son los aliados?", [
   ("Packaging y film impreso", "un solo proveedor, mínimos de compra y arte propio de la marca"),
   ("Materia prima a granel", "crítica pero sustituible"),
   ("Producto terminado a granel", "abastece la línea de fraccionamiento"),
   ("Los 57 distribuidores", "socios y clientes a la vez"),
   ("Transportistas tercerizados", ""),
   ("Aiello Supermercados", ""),
   ("Proveedor del sistema y del sitio", ""),
 ]),
 "actividades": ("7", "Actividades clave", "¿Qué hace para entregar valor?", [
   ("Producción", "extrusión, freído y saborizado"),
   ("Fraccionamiento y envasado", ""),
   ("Distribución y logística", "el diferencial que la empresa declara"),
   ("Compras de materia prima y packaging", ""),
   ("Administración y cobranza", "entre planillas y sistema, sin integrar"),
 ]),
 "recursos": ("6", "Recursos clave", "¿Qué activos necesita?", [
   ("La red de 57 distribuidores", "el activo más valioso y el menos reconocido"),
   ("Línea de producción al límite", "hoy es el cuello de botella"),
   ("El saber de la familia", "recetas, costos y contactos. Con segunda generación operando"),
   ("Marca de 53 años", ""),
   ("Flota propia", ""),
   ("Planilla de costos por producto", "de ella depende el precio, y es imprecisa"),
   ("Habilitaciones RNE y RNPA", "barrera frente a la competencia informal"),
 ]),
 "propuesta": ("2", "Propuesta de valor", "¿Qué problema resuelve?", [
   ("Le vende rentabilidad al canal", "no snacks al consumidor final"),
   ("Precio competitivo", "por control de costos"),
   ("La logística como diferencial", "llega donde el canal no llega solo"),
   ("Catálogo amplio en un solo proveedor", ""),
   ("Formatos de 1 y 2 Kg", "para que el minorista fraccione y saque margen"),
   ("Liderazgo en costos", "no diferenciación"),
 ]),
 "relacion": ("4", "Relación con clientes", "¿Cómo los sostiene?", [
   ("La relación la lleva la empresa", "no el viajante: la cartera no se va con él"),
   ("Exclusividad territorial", "acordada con los distribuidores"),
   ("Atención en horario acotado", "sin autogestión fuera de esa franja"),
   ("Sin CRM ni política de fidelización", "el cliente se queda por costumbre y precio"),
 ]),
 "canales": ("3", "Canales", "¿Cómo llega a ellos?", [
   ("Flota propia y transporte tercerizado", ""),
   ("Retiro en fábrica", ""),
   ("Viajante con zona asignada", "entrega y presencia, no administra cartera"),
   ("WhatsApp y teléfono", "por donde entran los pedidos"),
   ("Contacto directo con Aiello", ""),
   ("Tienda online construida y apagada", "el catálogo está publicado; lo vacío es el carrito"),
 ]),
 "segmentos": ("1", "Segmentos de clientes", "¿Para quién crea valor?", [
   ("57 distribuidores mayoristas", "en 7 provincias"),
   ("La Patagonia concentra el 61%", "35 de 57. Mendoza, la provincia de origen, reúne 6"),
   ("Aiello Supermercados", "única cadena, trato directo, San Luis"),
   ("Nunca al consumidor final", "no existe segmento minorista"),
 ]),
 "costos": ("9", "Estructura de costos", "¿Cuáles son los principales costos?", [
   ("Materia prima", "el componente más pesado"),
   ("Packaging y film impreso", "más de 25 combinaciones, cada una con su arte"),
   ("Mano de obra", "15 a 20 personas, más las horas extras que tapan la planta saturada"),
   ("Logística y flete", "mucho volumen y poco peso, con el 61% de la cartera lejos"),
   ("Energía y mantenimiento", "agravado por trabajar al límite"),
   ("Costo financiero", "cuenta corriente a 30 días y cheques diferidos"),
 ]),
 "ingresos": ("5", "Fuentes de ingreso", "¿Por qué pagan los clientes?", [
   ("Venta mayorista a distribuidores", "la fuente principal, por volumen"),
   ("Venta directa a Aiello", ""),
   ("Venta de producto fraccionado", "repostería y formatos de 1 y 2 Kg"),
   ("Contado, cuenta corriente a 30 días y cheques diferidos", ""),
   ("Demanda pareja todo el año", "sin estacionalidad marcada"),
 ]),
}

REMATE = ("La empresa reconoce que su costeo por producto es impreciso: "
          "compite por precio sobre una base que sabe equivocada.")


def bloque(clave, extra=""):
    n, titulo, pregunta, items = BLOQUES[clave]
    li = []
    for fuerte, resto in items:
        li.append('<li><b>%s</b>%s</li>' % (fuerte, (" — " + resto) if resto else ""))
    return ('<div class="blk %s%s"><div class="hd"><span class="num">%s</span>'
            '<h3>%s</h3></div><p class="q">%s</p><ul>%s</ul></div>'
            % (clave, extra, n, titulo, pregunta, "".join(li)))


HTML = """<!doctype html><html lang="es"><head><meta charset="utf-8"><style>
@page { size: A3 landscape; margin: 11mm; }
* { box-sizing: border-box; }
body { margin:0; font-family: Arial, Helvetica, sans-serif; color:#1B2B34; }
.top { display:flex; align-items:flex-end; justify-content:space-between;
       border-bottom:2px solid #1B2B34; padding-bottom:5mm; margin-bottom:5mm; }
.top h1 { margin:0; font-size:19pt; letter-spacing:.06em; }
.top .sub { font-size:9.5pt; color:#55636B; margin:1.5mm 0 0; }
.top .tag { font-size:8.5pt; letter-spacing:.14em; text-transform:uppercase; color:#8A7250; }
.grid { display:grid; grid-template-columns:repeat(5,1fr);
        grid-template-rows:88mm 88mm 52mm; gap:1.8mm; }
.blk { border:0.5pt solid #B9C2C8; border-top:2.2pt solid #55636B; padding:3.4mm 3.6mm;
       overflow:hidden; }
.hd { display:flex; align-items:baseline; gap:2mm; }
.num { font-size:8.6pt; font-weight:bold; color:#9AA6AD; }
.blk h3 { margin:0; font-size:11.5pt; letter-spacing:.02em; }
.q { margin:.7mm 0 2.4mm; font-size:7.8pt; color:#8A949B; font-style:italic; }
.blk ul { margin:0; padding-left:3.6mm; }
.blk li { font-size:8.4pt; line-height:1.38; margin-bottom:1.8mm; }
.blk li b { font-weight:bold; }
.socios { grid-row:span 2; } .propuesta { grid-row:span 2; } .segmentos { grid-row:span 2; }
.costos { grid-column:span 3; } .ingresos { grid-column:span 2; }
.propuesta { border-top-color:#C8791E; background:#FBF6EE; }
.segmentos { border-top-color:#C8791E; }
.costos { border-top-color:#A33B22; background:#FCF3F0; }
.ingresos { border-top-color:#2F6B5E; background:#F2F8F5; }
.costos .num, .costos h3 { color:#A33B22; }
.ingresos .num, .ingresos h3 { color:#2F6B5E; }
.propuesta .num, .propuesta h3, .segmentos .num, .segmentos h3 { color:#A9670F; }
.remate { margin-top:5mm; border-left:3pt solid #A33B22; padding-left:3.5mm;
          font-size:10pt; font-weight:bold; }
.pie { margin-top:3mm; font-size:7pt; color:#8A949B; }
</style></head><body>
<div class="top">
  <div>
    <h1>BUSINESS MODEL CANVAS &middot; DULXELITOS</h1>
    <p class="sub">Fabricación, fraccionamiento y distribución de snacks &middot;
       San Rafael, Mendoza &middot; desde 1973</p>
  </div>
  <p class="tag">Estado actual (AS-IS)</p>
</div>
<div class="grid">%(socios)s%(actividades)s%(propuesta)s%(relacion)s%(segmentos)s%(recursos)s%(canales)s%(costos)s%(ingresos)s</div>
<p class="remate">%(remate)s</p>
<p class="pie">Trabajo Práctico Final, Parte 1 &middot; Gestión Gerencial &middot; UTN Facultad Regional San Rafael. El desarrollo escrito de cada bloque está en el informe.</p>
</body></html>"""

html = HTML % {
    "socios": bloque("socios"), "actividades": bloque("actividades"),
    "propuesta": bloque("propuesta"), "relacion": bloque("relacion"),
    "segmentos": bloque("segmentos"), "recursos": bloque("recursos"),
    "canales": bloque("canales"), "costos": bloque("costos"),
    "ingresos": bloque("ingresos"), "remate": REMATE,
}
tmp = os.path.join(BASE, "_canvas.html")
io.open(tmp, "w", encoding="utf-8").write(html)
# Se renderiza con el navegador y no con weasyprint: weasyprint todavia no
# implementa bien CSS Grid con `span` y se cae al maquetar el canvas.
BRAVE = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
if not os.path.exists(BRAVE):
    raise SystemExit("falta el navegador para renderizar (%s)" % BRAVE)
subprocess.run(["nice", "-n", "10", BRAVE, "--headless", "--disable-gpu",
                "--no-pdf-header-footer", "--print-to-pdf=" + SALIDA,
                "file://" + tmp], check=True, capture_output=True, timeout=180)
os.remove(tmp)
print("escrito:", os.path.basename(SALIDA))
