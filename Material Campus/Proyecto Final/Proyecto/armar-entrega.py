#!/usr/bin/env python3
"""Arma la carpeta de entrega a partir de las secciones sueltas.

    python3 armar-entrega.py

Escribe en Entrega/ el md, el docx y el pdf. Las secciones sueltas son la
fuente: si alguien toca una, hay que volver a correr esto. El archivo de
entrega no se edita a mano porque se pisa en la proxima corrida.

Necesita pandoc (docx) y weasyprint (pdf). Si falta alguno, avisa y sigue.
"""

import io, os, re, shutil, subprocess, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(BASE, "Entrega")
NOMBRE = "TP Final Parte 1 - Dulxelitos"


def leer(n):
    with io.open(os.path.join(BASE, n), encoding="utf-8") as fh:
        return fh.read().split("\n")


def desde(ls, marca):
    for i, ln in enumerate(ls):
        if ln.startswith(marca):
            return ls[i:]
    raise SystemExit("no encontre %r" % marca)


def hasta(ls, marca):
    for i, ln in enumerate(ls):
        if ln.startswith(marca):
            return ls[:i]
    return ls


def demote(ls, n=1):
    return [("#" * n + l) if l.startswith("#") else l for l in ls]


def renombrar(ls, mapa):
    out = []
    for l in ls:
        for viejo, nuevo in mapa.items():
            if l.startswith(viejo):
                l = nuevo
                break
        out.append(l)
    return out


hoy = datetime.date.today()
PB = "<!--PAGEBREAK-->"

# La portada va como metadatos: pandoc los mapea a los estilos Title y Subtitle
# de Word, en vez de a un parrafo cualquiera en negrita.
META = """---
title: "Trabajo Práctico Final, Parte 1"
subtitle: "Diagnóstico gerencial de Dulxelitos"
author:
  - "Universidad Tecnológica Nacional, Facultad Regional San Rafael"
  - "Ingeniería en Sistemas de Información, Plan 2026"
  - "Cátedra: Gestión Gerencial, quinto año"
  - "Docentes: Ing. Jeremías Pino e Ing. Martín Noguerol"
  - "Organización analizada: Dulxelitos, San Rafael, Mendoza, desde 1973"
  - "Integrantes: (completar con apellido y nombre de cada integrante)"
date: "%s"
lang: es
---
""" % hoy.strftime("%d/%m/%Y")

L = []

# ---------------------------------------------------------------- introduccion
L.append("## Introducción")
L.append("")
L.append("Este trabajo es la primera parte del proyecto integrador de Gestión Gerencial. "
         "Consiste en un diagnóstico gerencial de una organización real, y la que elegimos "
         "fue Dulxelitos, una empresa familiar de San Rafael que fabrica, fracciona y "
         "distribuye snacks desde 1973.")
L.append("")
L.append("El objetivo de esta etapa es entender cómo funciona la empresa hoy y detectar, "
         "con evidencia, cuál es su problema gerencial. Todavía no proponemos ninguna "
         "solución: eso viene después. Por eso todo el análisis está hecho sobre el estado "
         "actual y no sobre un escenario deseado.")
L.append("")
L.append("El documento sigue las cinco secciones que pide el enunciado. Arranca "
         "describiendo la organización, sigue con el análisis del contexto aplicando PESTEL, "
         "las cinco fuerzas de Porter, la cadena de valor y un FODA cruzado, después "
         "presenta el modelo de negocio actual con un Business Model Canvas y su lectura, "
         "continúa con la propuesta de valor vista desde el cliente con un Value Proposition "
         "Canvas, y cierra evaluando la madurez de la empresa con el modelo de la cátedra y "
         "estimando el costo de no actuar.")
L.append("")
L.append("La sección 6 del enunciado, el problema gerencial priorizado, no está en esta "
         "entrega: la presentamos por separado.")
L.append("")
L.append("Elegimos Dulxelitos por una razón práctica que conviene decir de entrada: uno de "
         "nosotros trabaja ahí. Eso nos dio un nivel de acceso que no hubiéramos tenido de "
         "otra manera, y también un riesgo de sesgo que explicamos y tratamos de controlar "
         "en el punto 1.6.")
L.append("")
L.append("En el documento aparte `herramientas.md` está el detalle de qué herramienta "
         "aplicamos en cada sección y cómo se encadenan entre sí.")
L.append("")
L.append(PB)
L.append("")

# 1
L.append("## 1. La organización")
L.append("")
L += demote(desde(leer("01 - Organización.md"), "## 1.1 "))
L += ["", "---", ""]

# 2
L.append("## 2. El contexto")
L.append("")
L += demote(desde(leer("02 - Contexto.md"), "Para esta parte usamos"))
L += ["", "---", ""]

# 3
L.append("## 3. Modelo de negocio actual")
L.append("")
L.append("### 3.1 Los nueve bloques del canvas")
L.append("")
bmc = desde(leer("BMC - Dulxelitos.md"), "## 1. Segmentos de clientes")
fuentes = desde(bmc, "## Fuentes")
bmc = hasta(bmc, "## Fuentes")
bmc = renombrar(demote(bmc, 2), {"#### Síntesis del canvas": "### 3.2 Síntesis del canvas"})
L += bmc
L.append("")
lect = desde(leer("03 - Lectura analítica del BMC.md"), "## 3.1 Lógica de valor")
L += renombrar(demote(lect), {
    "### 3.1 Lógica de valor": "### 3.3 Lógica de valor",
    "### 3.2 Explotación y exploración": "### 3.4 Explotación y exploración",
    "### 3.3 Debilidades y dependencias": "### 3.5 Debilidades y dependencias",
    "### 3.4 Tensiones del modelo": "### 3.6 Tensiones del modelo",
})
L += ["", "---", ""]

# 4
L.append("## 4. Propuesta de valor actual")
L.append("")
L += demote(desde(leer("04 - VPC - Distribuidor mayorista.md"), "## 4.1 "))
L += ["", "---", ""]

# 5
L.append("## 5. Madurez y capacidades")
L.append("")
L += demote(desde(leer("05 - Madurez y Costo de No Actuar.md"), "## 5.1 "))
L += ["", "---", ""]

# anexo
L.append("## 6. Conclusiones del diagnóstico")
L.append("")
L.append("Al empezar el trabajo dábamos por sentado que íbamos a encontrar los problemas "
         "de Dulxelitos del lado del cliente. Nos pasó lo contrario, y eso terminó "
         "ordenando todo el análisis.")
L.append("")
L.append("El canal está conforme. Los distribuidores eligen a la empresa por compromiso y "
         "precio, casi no hay quejas, y la entrega a la Patagonia llega en menos de una "
         "semana sobre 1.500 kilómetros. La propuesta de valor funciona.")
L.append("")
L.append("Los problemas están puertas adentro, y son tres. La empresa compite por precio "
         "sin saber cuánto le cuesta cada producto, porque el costeo vive en una planilla "
         "que ellos mismos reconocen imprecisa. La planta está saturada desde hace tiempo y "
         "en vez de resolverlo lo absorben con horas extras, que es un gasto mensual que "
         "nadie midió. Y el activo más valioso que tienen, la red de 57 distribuidores "
         "armada en 53 años, no tiene ningún sistema detrás: no saben cuánto factura cada "
         "uno ni se enteran cuando alguno se va.")
L.append("")
L.append("La evaluación de madurez dio 1.79 sobre 5, nivel Inicial. Tres dimensiones llegan "
         "a Básico, pero las dos más bajas son Estrategia y Gobierno, que justamente no son "
         "sobre herramientas sino sobre decidir y controlar. Una empresa que lleva 53 años y "
         "sostiene siete provincias no está mal gestionada. Lo que le pasa es que decide sin "
         "instrumentos.")
L.append("")
L.append("No pudimos cuantificar el costo de no actuar, y eso es parte del diagnóstico. "
         "Cuando preguntamos por las magnitudes, la empresa no las tenía, y la percepción "
         "interna es que los problemas son menores. Es la respuesta esperable de una "
         "organización que no mide: el costo no está bajo, está sin observar. Con dos cifras "
         "que ya existen, las horas extras del último año y el tiempo que lleva rehacer la "
         "lista de precios, se podría cuantificar la mitad sin salir a relevar nada nuevo.")
L.append("")
L.append("Sobre el trabajo en sí: tener a alguien adentro nos dio mucho acceso y también "
         "nos obligó a cuidarnos. El cruce con fuentes públicas sirvió en las dos "
         "direcciones, y de hecho nos corrigió un error que habíamos cometido mirando la "
         "página web de la empresa.")
L.append("")
L.append(PB)
L.append("")
L.append("## 7. Bibliografía")
L.append("")
L.append("**Herramientas de análisis**")
L.append("")
L.append("- Aguilar, F. J. (1967). *Scanning the Business Environment*. Macmillan.")
L.append("- Osterwalder, A. y Pigneur, Y. (2010). *Business Model Generation*. John Wiley & Sons.")
L.append("- Osterwalder, A., Pigneur, Y., Bernarda, G. y Smith, A. (2014). *Value Proposition Design*. John Wiley & Sons.")
L.append("- Porter, M. E. (1979). How competitive forces shape strategy. *Harvard Business Review*, 57(2), 137-145.")
L.append("- Porter, M. E. (1980). *Competitive Strategy: Techniques for Analyzing Industries and Competitors*. Free Press.")
L.append("- Porter, M. E. (1985). *Competitive Advantage: Creating and Sustaining Superior Performance*. Free Press.")
L.append("")
L.append("**Material de cátedra**")
L.append("")
L.append("- Cátedra de Gestión Gerencial (2026). Presentación introductoria al cursado. UTN FRSR.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 1: gobernanza de TI y valor de negocio. UTN FRSR.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 2: análisis estratégico y modelos de negocio. UTN FRSR.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 3: transformación digital, madurez y gestión bimodal. UTN FRSR.")
L.append("- Cátedra de Gestión Gerencial (2026). Modelo de madurez digital. UTN FRSR.")
L.append("- Cátedra de Gestión Gerencial (2026). Trabajo Práctico Final, Parte 1: consigna y guía del caso Distribuidora Montaña. UTN FRSR.")
L.append("")
L.append("**Fuentes primarias del caso**")
L.append("")
L.append("- Dulxelitos. Sitio oficial dulxelitos.com.ar, secciones Bienvenido, Productos, Nosotros y Distribuidores. Consultado el 4 de septiembre de 2026.")
L.append("- Dulxelitos. Perfil de Instagram @dulxelitos.")
L.append("- Aiello Supermercados. Sitio oficial superaiello.com.ar, secciones Nuestra Historia y Sucursales.")
L.append("- Listados de mayoristas regionales de la zona de influencia.")
L.append("- Entrevistas y observación directa del equipo en la organización.")
L.append("")
L.append(PB)
L.append("")
L.append("## 8. Anexos")
L.append("")
L.append("Además de este documento entregamos dos archivos de apoyo: `herramientas.md`, "
         "con el detalle de las herramientas de análisis y cómo se encadenan, y una planilla "
         "de cálculo con la encuesta de madurez completa, el FODA y esa misma tabla de "
         "herramientas.")
L.append("")
L.append("### Anexo I: datos que la empresa no mide")
L.append("")
L.append("Lo dejamos escrito en vez de estimarlo. Nada de esto impide el diagnóstico, y "
         "varios de estos huecos son en sí mismos parte de lo que encontramos en la "
         "sección 5.")
L.append("")
L.append("| Dato | Dónde nos hacía falta |")
L.append("|---|---|")
L.append("| Cuánto factura cada uno de los cinco distribuidores más grandes | 1.3, 2.2 y 4.1 |")
L.append("| Horas extras que se pagan por mes | 5.5 |")
L.append("| Horas que lleva rehacer la lista de precios | 5.5 |")
L.append("| Unidades que se rompen en el viaje por mes | 5.5 |")
L.append("| Pedidos que se recortan o rechazan por falta de capacidad | 5.5 |")
L.append("| Altas y bajas de distribuidores de los últimos dos años y sus motivos | 2.4 y 4.4 |")
L.append("| Qué producto compite con el snack en el punto de venta | 2.2 |")
L.append("| Hitos de la empresa entre 1973 y hoy | 1.4 |")
L.append("| Si las marcas nacionales les compiten en el canal | 2.2 |")
L.append("")

crudo = re.sub(r"\n{4,}", "\n\n\n", "\n".join(L)).rstrip() + "\n"

# Indice: en el .md es una lista escrita; en docx y pdf lo genera pandoc (--toc),
# que en Word es un campo TDC de verdad, actualizable con F9.
titulos = [l[3:].strip() for l in crudo.split("\n") if l.startswith("## ")]
indice_md = "## Índice\n\n" + "\n".join("%d. %s" % (i, t) for i, t in enumerate(titulos, 1))

# El titulo del documento vive en los metadatos, asi que el cuerpo arranca un
# nivel mas abajo de lo necesario: subimos todo uno. Las secciones pasan a ser
# Titulo 1, sus puntos Titulo 2 y los subpuntos Titulo 3, que es lo que toma
# el indice automatico de Word (TOC \o "1-3").
def subir_nivel(texto):
    return "\n".join(l[1:] if l.startswith("##") else l for l in texto.split("\n"))

crudo = subir_nivel(crudo)
indice_md = subir_nivel(indice_md)

md = META + crudo.replace("<!--INDICE-->", indice_md).replace(PB, "---")

SALTO_DOCX = "```{=openxml}\n<w:p><w:r><w:br w:type=\"page\"/></w:r></w:p>\n```"
SALTO_HTML = '<div style="page-break-after: always;"></div>'
sin_marca = crudo.replace("<!--INDICE-->\n\n" + PB + "\n\n", "")
md_docx = META + sin_marca.replace(PB, SALTO_DOCX)
md_html = META + sin_marca.replace(PB, SALTO_HTML)

os.makedirs(DEST, exist_ok=True)
ruta_md = os.path.join(DEST, NOMBRE + ".md")
with io.open(ruta_md, "w", encoding="utf-8") as fh:
    fh.write(md)
tmp_docx = os.path.join(DEST, "_tmp_docx.md")
tmp_html = os.path.join(DEST, "_tmp_html.md")
io.open(tmp_docx, "w", encoding="utf-8").write(md_docx)
io.open(tmp_html, "w", encoding="utf-8").write(md_html)
print("%s.md  (%d lineas, ~%d palabras)" % (NOMBRE, md.count("\n") + 1, len(md.split())))

CSS = """
@page { size: A4; margin: 2.2cm 2cm; @bottom-center {
  content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #666; } }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt;
  line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 24pt; margin: 3.5cm 0 .3em; line-height: 1.2; text-align: center; }
h1 + h2 { font-size: 15pt; border: none; text-align: center; font-weight: normal;
  font-style: italic; margin: 0 0 2.5cm; color: #333; }
h1 + h2 + p, h1 + h2 + p ~ p { text-align: center; }
h2 { font-size: 14pt; margin: 1.6em 0 .5em; border-bottom: 1px solid #ccc;
  padding-bottom: .2em; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: 1.2em 0 .4em; page-break-after: avoid; }
h4 { font-size: 10.5pt; margin: 1em 0 .3em; font-style: italic;
  page-break-after: avoid; }
p { margin: 0 0 .6em; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin: .8em 0; font-size: 9pt;
  page-break-inside: avoid; }
th, td { border: 1px solid #bbb; padding: 4px 6px; text-align: left;
  vertical-align: top; }
th { background: #eee; font-weight: bold; }
ul, ol { margin: 0 0 .6em 1.2em; padding: 0; }
li { margin-bottom: .25em; }
hr { border: none; border-top: 1px solid #ddd; margin: 1.5em 0; }
code { font-family: Menlo, monospace; font-size: 9pt; }
/* portada */
#title-block-header { margin-top: 4cm; text-align: center; }
/* la regla general de p justifica el texto y le gana a la alineacion heredada */
#title-block-header p, #title-block-header h1 { text-align: center; }
#title-block-header .title { font-size: 24pt; font-weight: bold; display: block;
  margin-bottom: .3em; }
#title-block-header .subtitle { font-size: 15pt; font-style: italic; color: #333;
  display: block; margin-bottom: 3cm; }
#title-block-header .author { display: block; font-size: 10.5pt; margin: .35em 0; }
#title-block-header .date { display: block; margin-top: 2cm; font-size: 10.5pt; }
/* indice con numero de pagina */
#TOC h2 { margin-top: 0; }
#TOC ul { list-style: none; padding-left: 0; }
#TOC ul ul { padding-left: 1.4em; font-size: 9.5pt; }
#TOC li { margin: .18em 0; }
#TOC a { text-decoration: none; color: inherit; }
#TOC a::after { content: "  " leader(".") "  " target-counter(attr(href), page); }
"""

def corre(cmd, que):
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("%s.%s" % (NOMBRE, que))
        return True
    except FileNotFoundError:
        print("  falta la herramienta para el %s, no se genero" % que)
    except subprocess.CalledProcessError as e:
        print("  fallo el %s: %s" % (que, e.stderr.decode()[:200]))
    return False

def plantilla_word(destino):
    """Arma un reference.docx: es la plantilla de estilos que usa Word.

    Partimos del que trae pandoc (que ya define Title, Subtitle, Heading 1..6,
    TOC y Compact) y le cambiamos la tipografia y el color de los titulos.
    Asi el docx sale con estilos de verdad y no con parrafos formateados a mano.
    """
    import zipfile, tempfile
    base = os.path.join(tempfile.gettempdir(), "_ref_pandoc.docx")
    with open(base, "wb") as fh:
        subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"],
                       check=True, stdout=fh, stderr=subprocess.DEVNULL)
    zin = zipfile.ZipFile(base)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            datos = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                x = datos.decode("utf-8")
                # tipografia unica en todo el documento
                x = re.sub(r'w:ascii="[^"]*"', 'w:ascii="Arial"', x)
                x = re.sub(r'w:hAnsi="[^"]*"', 'w:hAnsi="Arial"', x)
                x = re.sub(r'w:cs="[^"]*"', 'w:cs="Arial"', x)
                # titulos en azul oscuro, como en un informe academico
                x = x.replace('<w:color w:val="365F91"', '<w:color w:val="1F3864"')
                x = x.replace('<w:color w:val="4F81BD"', '<w:color w:val="1F3864"')
                # idioma espanol, para que el corrector de Word no marque todo
                x = re.sub(r'<w:lang w:val="[^"]*"', '<w:lang w:val="es-AR"', x)
                datos = x.encode("utf-8")
            zout.writestr(item, datos)
    zin.close()
    return destino


if shutil.which("pandoc"):
    ref = os.path.join(DEST, "_ref.docx")
    try:
        plantilla_word(ref)
    except Exception as e:
        print("  no se pudo armar la plantilla de estilos (%s), se usa la de pandoc" % e)
        ref = None
    corre(["pandoc", tmp_docx, "-o", os.path.join(DEST, NOMBRE + ".docx"),
           "--from", "markdown", "--toc", "--toc-depth=3"]
          + (["--reference-doc", ref] if ref else []), "docx")
    html = os.path.join(DEST, "_tmp.html")
    css = os.path.join(DEST, "_tmp.css")
    io.open(css, "w", encoding="utf-8").write(CSS)
    if corre(["pandoc", tmp_html, "-o", html, "--standalone", "--css", "_tmp.css",
              "--toc", "--toc-depth=3"], "html intermedio"):
        # el bloque de titulo de pandoc es la portada: le metemos el salto de
        # pagina y dejamos el indice en su propia hoja.
        h = io.open(html, encoding="utf-8").read()
        h = h.replace('</header>', '</header><div style="page-break-after: always;"></div>')
        h = h.replace('<nav id="TOC" role="doc-toc">',
                      '<nav id="TOC" role="doc-toc"><h2>Índice</h2>')
        h = h.replace('</nav>', '</nav><div style="page-break-after: always;"></div>')
        io.open(html, "w", encoding="utf-8").write(h)
        if shutil.which("weasyprint"):
            corre(["weasyprint", html, os.path.join(DEST, NOMBRE + ".pdf")], "pdf")
        else:
            print("  falta weasyprint, no se genero el pdf")
    for t in (html, css, tmp_docx, tmp_html, ref or ""):
        if t and os.path.exists(t):
            os.remove(t)
else:
    print("  falta pandoc: solo se genero el .md")
