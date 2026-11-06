#!/usr/bin/env python3
"""Arma diagramas/arquitectura.svg y arquitectura.png (seccion 6 de la Parte 2).

    .venv/bin/python diagramas/generar_arquitectura.py

Dibuja la arquitectura conceptual de la alternativa recomendada (stock de
Discovery) con la planilla compartida solo en el piloto. Cajas y flechas simples,
en castellano, con letra de 14 px o mas sobre un ancho de 1200 px.

El PNG usa cairosvg: correr con el python de la venv. Sin cairosvg se escribe
solo el SVG y se avisa. El ancho de los textos se mide con Pillow si esta
disponible (para avisar cuando un texto no entra en su caja).
"""

import os
import sys
from xml.sax.saxutils import escape

sys.dont_write_bytecode = True

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 1235
FUENTE = "Arial, Helvetica, sans-serif"
MIN_LETRA = 14

# Paleta de la presentacion (armar-presentacion.js), con el mismo uso en todos los
# graficos: oscuro = texto y flujo definitivo; tinta neutra = personas y areas;
# azul = sistemas y datos (Discovery); naranja = solo en el piloto (la planilla);
# verde = lo que mide la mejora (el tablero); gris = hojas manuales.
TINTA = "#1B2B34"        # DARK
GRIS = "#55636B"         # GREY
NEUTRO = "#EFEADC"       # T_NEUTRAL
AZUL = "#1E5C85"         # BLUE
AZUL_T = "#DDE8EF"       # T_BLUE
NARANJA = "#C8791E"      # ORANGE (trazos)
NARANJA_TXT = "#9E5C15"  # ORANGE oscurecido, para texto chico sobre blanco (5,3:1)
NARANJA_T = "#F6EBD8"    # T_ORANGE
VERDE = "#2F6B5E"        # GREEN
VERDE_T = "#DCEAE3"      # T_GREEN

try:
    from PIL import ImageFont
    _FUENTES = {}

    def _fuente(tam, negrita):
        clave = (tam, negrita)
        if clave not in _FUENTES:
            _FUENTES[clave] = ImageFont.truetype(
                "/System/Library/Fonts/Helvetica.ttc", tam, index=1 if negrita else 0)
        return _FUENTES[clave]

    def medir(texto, tam, negrita=False):
        return _fuente(tam, negrita).getlength(texto)
except Exception:  # sin Pillow o sin la tipografia: aproximacion
    def medir(texto, tam, negrita=False):
        return len(texto) * tam * (0.56 if negrita else 0.52)

out = []
avisos = []


def envolver(texto, tam, ancho, negrita=False):
    """Parte el texto en lineas que entran en `ancho` px. '\n' fuerza un corte."""
    lineas = []
    for parrafo in texto.split("\n"):
        actual = ""
        for palabra in parrafo.split():
            prueba = (actual + " " + palabra).strip()
            if medir(prueba, tam, negrita) <= ancho or not actual:
                actual = prueba
            else:
                lineas.append(actual)
                actual = palabra
        lineas.append(actual)
    return lineas


def texto(x, y, s, tam=15, ancla="middle", negrita=False, color=TINTA):
    if tam < MIN_LETRA:
        avisos.append("letra de %d px (minimo %d): %s" % (tam, MIN_LETRA, s))
    out.append('<text x="%g" y="%g" font-size="%d" text-anchor="%s" fill="%s"%s>%s</text>'
               % (x, y, tam, ancla, color, ' font-weight="bold"' if negrita else "",
                  escape(s)))


def caja(x, y, w, h, titulo, cuerpo="", relleno="#fff", borde=TINTA, trazo=1.8,
         punteada=False, tam_titulo=17, tam_cuerpo=15, radio=8):
    out.append('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" '
               'stroke-width="%g"%s/>' % (x, y, w, h, radio, relleno, borde, trazo,
                                          ' stroke-dasharray="9 6"' if punteada else ""))
    ancho = w - 24
    lt = envolver(titulo, tam_titulo, ancho, True)
    lc = envolver(cuerpo, tam_cuerpo, ancho) if cuerpo else []
    paso_t, paso_c, sep = tam_titulo + 4, tam_cuerpo + 4, 5 if lc else 0
    alto = len(lt) * paso_t + sep + len(lc) * paso_c
    if alto > h - 10:
        avisos.append("el texto de '%s' no entra en la caja (%d > %d)" % (titulo, alto, h - 10))
    yy = y + (h - alto) / 2 + tam_titulo
    for ln in lt:
        texto(x + w / 2, yy, ln, tam_titulo, negrita=True)
        yy += paso_t
    yy += sep
    for ln in lc:
        texto(x + w / 2, yy - 2, ln, tam_cuerpo)
        yy += paso_c


def flecha(puntos, punteada=False, punta=True, color=TINTA, trazo=2.2):
    pts = " ".join("%g,%g" % p for p in puntos)
    extra = ' stroke-dasharray="9 6"' if punteada else ""
    id_punta = "punta-p" if punteada else ("punta-a" if color == AZUL else "punta")
    marca = ' marker-end="url(#%s)"' % id_punta if punta else ""
    out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%g"%s%s/>'
               % (pts, color, trazo, extra, marca))


# --- dibujo -------------------------------------------------------------------

out.append('<?xml version="1.0" encoding="UTF-8"?>')
out.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
           'font-family="%s">' % (W, H, W, H, FUENTE))
out.append('<title>Arquitectura conceptual y flujo de datos (alternativa B, con piloto en planilla)</title>')
out.append('<defs>'
           '<marker id="punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
           'markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
           '<marker id="punta-p" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
           'markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
           '<marker id="punta-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
           'markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="%s"/></marker>'
           '</defs>' % (TINTA, NARANJA, AZUL))
out.append('<rect x="0" y="0" width="%d" height="%d" fill="#fff"/>' % (W, H))

texto(40, 40, "Arquitectura conceptual y flujo de datos", 24, "start", True)
texto(40, 68, "Alternativa B (stock de Discovery), probada antes con una planilla compartida",
      16, "start", color=GRIS)

# columnas de las personas, encima del registro: Deposito, Produccion, Oficina
XD, XP, XO, WA = 40, 320, 600, 250
SD, SP, SO = 240, XP + WA / 2, XO + WA / 2   # donde baja la carga de cada una

# fila 1: el distribuidor, encima de Oficina
caja(XO, 95, WA, 100, "Distribuidor", "Pide por WhatsApp o teléfono. No ve el stock (queda para más adelante).",
     relleno=NEUTRO)
flecha([(XO + 60, 195), (XO + 60, 265)])
texto(XO + 70, 238, "pedido", 14, "start")
flecha([(XO + 190, 265), (XO + 190, 195)])
texto(XO + 200, 238, "aviso con fecha, si falta", 14, "start")

# fila 2: quienes aportan datos
caja(XD, 265, WA, 125, "Depósito",
     "Arma con la lista de cada pedido confirmado. Cuenta una vez por semana (quién, "
     "a confirmar) y deja la hoja de conteo.", relleno=NEUTRO)
caja(XP, 265, WA, 125, "Producción",
     "Carga lo producido, todos los días, al cierre de turno.", relleno=NEUTRO)
caja(XO, 265, WA, 125, "Oficina",
     "Carga la nota de pedido y reserva el stock antes de confirmar. Factura.", relleno=NEUTRO)

# Discovery le devuelve a Deposito la lista de armado (flecha hacia arriba, sin cruzar el bus)
flecha([(70, 520), (70, 390)], color=AZUL)
texto(78, 427, "lista de armado", 14, "start", color=AZUL)
texto(78, 444, "por pedido confirmado", 14, "start", color=AZUL)

# bus: las tres cargas entran juntas a Discovery (solido) o a la planilla (punteado, piloto)
Y_BUS = 462
for cx, et in ((SD, "hoja de conteo"), (SP, "ingreso de stock"), (SO, "nota de pedido y reserva")):
    flecha([(cx, 390), (cx, Y_BUS)], punta=False)
    texto(cx + 9, 427, et, 14, "start")
texto(SD + 9, 444, "(ajuste: sistemas)", 14, "start")
flecha([(SD, Y_BUS), (SO, Y_BUS)], punta=False)
X_PLAN = 1030
flecha([(SO, Y_BUS), (X_PLAN, Y_BUS), (X_PLAN, 520)], punteada=True, color=NARANJA)
texto(905, Y_BUS - 9, "los tres aportes, solo en el piloto", 14, "start", color=NARANJA_TXT)
flecha([(SP, Y_BUS), (SP, 520)])

# fila 3: Discovery y la planilla
XDI, YDI, WDI, HDI = 40, 520, 810, 315
caja(XDI, YDI, WDI, HDI, "", relleno=AZUL_T, borde=AZUL, trazo=2.6, radio=10)
texto(XDI + 20, YDI + 32, "Discovery (Buenos Aires Software)", 19, "start", True, color=AZUL)
texto(XDI + 20, YDI + 56, "Se activa el módulo de stock, pedidos y reserva, que hoy no se usa.",
      15, "start")
texto(XDI + 20, YDI + 77, "Sin probar en Dulxelitos: es el supuesto 3 de la sección 4.", 15, "start")

YC, HC = 615, 105
caja(60, YC, 200, HC, "Pedidos y reservas", "Nota de pedido. La reserva se crea al confirmar.",
     borde=AZUL)
caja(335, YC, 230, HC, "Stock de producto terminado", "Físico, reservado y disponible.",
     borde=AZUL)
caja(640, YC, 190, HC, "Facturación", "Factura el pedido confirmado.", borde=AZUL)
flecha([(260, YC + 62), (335, YC + 62)], color=AZUL)
texto(297.5, YC + 50, "reserva", 14, color=AZUL)
flecha([(640, YC + 62), (565, YC + 62)], color=AZUL)
texto(602.5, YC + 30, "consume", 14, color=AZUL)
texto(602.5, YC + 47, "la reserva", 14, color=AZUL)
caja(60, 745, 770, 62, "", relleno="#fff", borde=AZUL, radio=8)
texto(445, 782, "Datos maestros: productos, distribuidores y stock mínimo por producto",
      15, "middle", True)

caja(900, 520, 260, 235, "Planilla compartida",
     "Solo en el piloto: 2 semanas, solo papas fritas. Recibe los mismos tres aportes y usa el "
     "mismo criterio: disponible = físico − reservado. Reemplaza a Discovery en la prueba y "
     "después se archiva.",
     relleno=NARANJA_T, borde=NARANJA, trazo=2.2, punteada=True)

# fila 4: lo que alimenta al tablero
YT, HT = 915, 110
XT, WT = 370, 410
caja(40, YT, 250, HT, "Registro semanal de recortes",
     "Pedidos recortados o demorados, en una hoja de Oficina.", borde=GRIS, trazo=1.6)
caja(900, YT, 260, HT, "Liquidación de sueldos", "Horas extras del mes, totales. Carga manual.",
     borde=GRIS, trazo=1.6)
caja(XT, YT, WT, HT, "Tablero de 4 indicadores",
     "Pedidos completos y a tiempo, exactitud de stock, días con producción cargada y horas "
     "extras por mes.", relleno=VERDE_T, borde=VERDE, trazo=2.6)
flecha([(40 + 250, YT + 55), (XT, YT + 55)])
texto((40 + 250 + XT) / 2, YT + 43, "a mano", 14)
flecha([(900, YT + 55), (XT + WT, YT + 55)])
texto((900 + XT + WT) / 2, YT + 43, "a mano, por mes", 14)
flecha([(520, 835), (520, YT)], color=AZUL)
texto(530, 880, "exportación CSV", 14, "start", color=AZUL)
flecha([(X_PLAN, 755), (X_PLAN, 872), (700, 872), (700, YT)], punteada=True, color=NARANJA)
texto(1020, 862, "CSV o a mano, solo piloto", 14, "end", color=NARANJA_TXT)

# fila 5: quien mira
caja(320, 1070, 510, 100, "Dirección y responsable de sistemas",
     "Miran el tablero. Dirección planifica la producción de la semana con los pedidos "
     "pendientes y el stock mínimo.", relleno=NEUTRO)
flecha([(575, YT + HT), (575, 1070)])
texto(585, 1052, "indicadores", 14, "start")

# leyenda
out.append('<line x1="40" y1="1204" x2="100" y2="1204" stroke="%s" stroke-width="2.2" '
           'marker-end="url(#punta)"/>' % TINTA)
texto(112, 1209, "Flujo definitivo", 14, "start")
out.append('<line x1="270" y1="1204" x2="330" y2="1204" stroke="%s" stroke-width="2.2" '
           'stroke-dasharray="9 6" marker-end="url(#punta-p)"/>' % NARANJA)
texto(342, 1209, "Solo en el piloto", 14, "start")
texto(520, 1209, "Todo es carga manual controlada o exportación CSV: no hay API.", 14, "start",
      color=GRIS)

out.append("</svg>")
svg = "\n".join(out) + "\n"

ruta_svg = os.path.join(AQUI, "arquitectura.svg")
with open(ruta_svg, "w", encoding="utf-8") as fh:
    fh.write(svg)
print("escribi arquitectura.svg")
try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                     write_to=os.path.join(AQUI, "arquitectura.png"), scale=2,
                     background_color="#ffffff")
    print("escribi arquitectura.png")
except ImportError:
    print("falta cairosvg: no se genero el PNG (usar el python de .venv)", file=sys.stderr)
for a in avisos:
    print("aviso:", a, file=sys.stderr)
sys.exit(1 if avisos else 0)
