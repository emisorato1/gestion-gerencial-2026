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
FUENTE = "Helvetica Neue, Helvetica, Arial, sans-serif"
TINTA = "#1b1b1b"
MIN_LETRA = 14

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
    marca = ' marker-end="url(#%s)"' % ("punta-p" if punteada else "punta") if punta else ""
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
           'markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8a5a00"/></marker>'
           '</defs>' % TINTA)
out.append('<rect x="0" y="0" width="%d" height="%d" fill="#fff"/>' % (W, H))

texto(40, 40, "Arquitectura conceptual y flujo de datos", 24, "start", True)
texto(40, 68, "Alternativa B (stock de Discovery), probada antes con una planilla compartida",
      16, "start")

# columnas de las personas, encima del registro: Deposito, Produccion, Oficina
XD, XP, XO, WA = 40, 320, 600, 250
SD, SP, SO = 240, XP + WA / 2, XO + WA / 2   # donde baja la carga de cada una

# fila 1: el distribuidor, encima de Oficina
caja(XO, 95, WA, 100, "Distribuidor", "Pide por WhatsApp o teléfono. No ve el stock (queda para más adelante).",
     relleno="#f1f3f5")
flecha([(XO + 60, 195), (XO + 60, 265)])
texto(XO + 70, 238, "pedido", 14, "start")
flecha([(XO + 190, 265), (XO + 190, 195)])
texto(XO + 200, 238, "aviso con fecha, si falta", 14, "start")

# fila 2: quienes aportan datos
AZUL = "#e6eefb"
caja(XD, 265, WA, 125, "Depósito",
     "Arma con la lista de cada pedido confirmado. Cuenta el stock una vez por semana y "
     "deja la hoja de conteo.", relleno=AZUL)
caja(XP, 265, WA, 125, "Producción",
     "Carga lo producido, todos los días, al cierre de turno.", relleno=AZUL)
caja(XO, 265, WA, 125, "Oficina",
     "Carga la nota de pedido y reserva el stock antes de confirmar. Factura.", relleno=AZUL)

# Discovery le devuelve a Deposito la lista de armado (flecha hacia arriba, sin cruzar el bus)
flecha([(70, 520), (70, 390)], color="#2b6e3f")
texto(78, 427, "lista de armado", 14, "start", color="#2b6e3f")
texto(78, 444, "por pedido confirmado", 14, "start", color="#2b6e3f")

# bus: las tres cargas entran juntas a Discovery (solido) o a la planilla (punteado, piloto)
Y_BUS = 462
for cx, et in ((SD, "hoja de conteo"), (SP, "ingreso de stock"), (SO, "nota de pedido y reserva")):
    flecha([(cx, 390), (cx, Y_BUS)], punta=False)
    texto(cx + 9, 427, et, 14, "start")
texto(SD + 9, 444, "(ajuste: sistemas)", 14, "start")
flecha([(SD, Y_BUS), (SO, Y_BUS)], punta=False)
X_PLAN = 1030
flecha([(SO, Y_BUS), (X_PLAN, Y_BUS), (X_PLAN, 520)], punteada=True, color="#8a5a00")
texto(905, Y_BUS - 9, "los tres aportes, solo en el piloto", 14, "start", color="#8a5a00")
flecha([(SP, Y_BUS), (SP, 520)])

# fila 3: Discovery y la planilla
XDI, YDI, WDI, HDI = 40, 520, 810, 315
caja(XDI, YDI, WDI, HDI, "", relleno="#f1f8f2", borde="#2b6e3f", trazo=2.6, radio=10)
texto(XDI + 20, YDI + 32, "Discovery (Buenos Aires Software)", 19, "start", True)
texto(XDI + 20, YDI + 56, "Se activa el módulo de stock, pedidos y reserva, que hoy no se usa.",
      15, "start")
texto(XDI + 20, YDI + 77, "Sin probar en Dulxelitos: es el supuesto 3 de la sección 4.", 15, "start")

VERDE = "#2b6e3f"
YC, HC = 615, 105
caja(60, YC, 200, HC, "Pedidos y reservas", "Nota de pedido. La reserva se crea al confirmar.",
     borde=VERDE)
caja(335, YC, 230, HC, "Stock de producto terminado", "Físico, reservado y disponible.",
     borde=VERDE)
caja(640, YC, 190, HC, "Facturación", "Factura el pedido confirmado.", borde=VERDE)
flecha([(260, YC + 62), (335, YC + 62)], color=VERDE)
texto(297.5, YC + 50, "reserva", 14, color=VERDE)
flecha([(640, YC + 62), (565, YC + 62)], color=VERDE)
texto(602.5, YC + 30, "consume", 14, color=VERDE)
texto(602.5, YC + 47, "la reserva", 14, color=VERDE)
caja(60, 745, 770, 62, "", relleno="#fff", borde=VERDE, radio=8)
texto(445, 782, "Datos maestros: productos, distribuidores y stock mínimo por producto",
      15, "middle", True)

caja(900, 520, 260, 235, "Planilla compartida",
     "Solo en el piloto: 2 semanas, solo papas fritas. Recibe los mismos tres aportes y usa el "
     "mismo criterio: disponible = físico − reservado. Reemplaza a Discovery en la prueba y "
     "después se archiva.",
     relleno="#fff7e0", borde="#8a5a00", punteada=True)

# fila 4: lo que alimenta al tablero
YT, HT = 915, 110
XT, WT = 370, 410
caja(40, YT, 250, HT, "Registro semanal de recortes",
     "Pedidos recortados o demorados, en una hoja de Oficina.", relleno="#f3ecfa")
caja(900, YT, 260, HT, "Liquidación de sueldos", "Horas extras del mes, totales. Carga manual.",
     relleno="#f3ecfa")
caja(XT, YT, WT, HT, "Tablero de 4 indicadores",
     "Pedidos completos y a tiempo, exactitud de stock, días con producción cargada y horas "
     "extras por mes.", relleno="#eef1f5", trazo=2.4)
flecha([(40 + 250, YT + 55), (XT, YT + 55)])
texto((40 + 250 + XT) / 2, YT + 43, "a mano", 14)
flecha([(900, YT + 55), (XT + WT, YT + 55)])
texto((900 + XT + WT) / 2, YT + 43, "a mano, por mes", 14)
flecha([(520, 835), (520, YT)], color=VERDE)
texto(530, 880, "exportación CSV", 14, "start", color=VERDE)
flecha([(X_PLAN, 755), (X_PLAN, 872), (700, 872), (700, YT)], punteada=True, color="#8a5a00")
texto(1020, 862, "CSV o a mano, solo piloto", 14, "end", color="#8a5a00")

# fila 5: quien mira
caja(320, 1070, 510, 100, "Dirección y responsable de sistemas",
     "Miran el tablero. Dirección planifica la producción de la semana con los pedidos "
     "pendientes y el stock mínimo.", relleno=AZUL)
flecha([(575, YT + HT), (575, 1070)])
texto(585, 1052, "indicadores", 14, "start")

# leyenda
out.append('<line x1="40" y1="1204" x2="100" y2="1204" stroke="%s" stroke-width="2.2" '
           'marker-end="url(#punta)"/>' % TINTA)
texto(112, 1209, "Flujo definitivo", 14, "start")
out.append('<line x1="270" y1="1204" x2="330" y2="1204" stroke="#8a5a00" stroke-width="2.2" '
           'stroke-dasharray="9 6" marker-end="url(#punta-p)"/>')
texto(342, 1209, "Solo en el piloto", 14, "start")
texto(520, 1209, "Todo es carga manual controlada o exportación CSV: no hay API.", 14, "start")

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
