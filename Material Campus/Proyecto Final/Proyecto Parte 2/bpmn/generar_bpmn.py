#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generador de diagramas BPMN 2.0 para la Parte 2 del TP Final (Dulxelitos).

    python3 bpmn/generar_bpmn.py bpmn/as-is.py            escribe .bpmn, .svg y .png
    python3 bpmn/generar_bpmn.py bpmn/as-is.py --validar  solo valida (no escribe)

Los tres archivos de salida quedan al lado de la especificacion (as-is.py ->
as-is.bpmn, as-is.svg, as-is.png). El PNG usa cairosvg: correr con el python de
la venv (.venv/bin/python); sin cairosvg se escriben .bpmn y .svg y se avisa.

Una especificacion es un modulo Python con una variable PROCESO:

    PROCESO = {
      "nombre": "Atender pedido de distribuidor (AS-IS)",
      "pools": [
        {"id": "dist", "nombre": "Distribuidor", "colapsado": True, "lanes": []},
        {"id": "empresa", "nombre": "Dulxelitos", "colapsado": False,
         "lanes": [{"id": "oficina", "nombre": "Oficina", "nodos": [
             {"id": "ini", "tipo": "inicio_mensaje", "texto": "Pedido recibido", "col": 0},
             ...]}]},
      ],
      "flujos":   [{"de": "ini", "a": "anotar", "texto": "opcional"}, ...],
      "mensajes": [{"de": "dist", "a": "ini", "texto": "opcional"}, ...],
      "anchos":   {8: 150},            # opcional: ancho de una columna, en px
    }

Nodos: "id", "tipo", "texto", "col" (columna de la grilla, puede ser decimal) y,
opcionales, "fila" (subfila dentro de la lane, 0 por defecto, puede ser decimal),
"ancho" (solo anotaciones), "ancho_etiqueta" (ancho maximo del texto de una
compuerta, 118 por defecto) y "etiqueta" ("arriba", "abajo", "izq", "der") para
elegir de que lado va el texto de una compuerta o evento.

Tipos: inicio, inicio_mensaje, fin, tarea, tarea_usuario, xor, and,
evento_tiempo, evento_mensaje, anotacion, datos.
  - evento_tiempo sin flujo de entrada es un inicio por tiempo; con entrada es un
    evento intermedio de tiempo.
  - Un flujo entre un nodo y una anotacion o un objeto de datos es una asociacion
    (punteada), no un flujo de secuencia. Tarea -> datos es una salida de datos (la
    flecha queda del lado del objeto); datos -> tarea es una entrada de datos (la
    flecha queda del lado de la tarea).
  - Un flujo de secuencia solo une nodos del mismo pool; un flujo de mensaje solo
    une pools distintos. Los pools colapsados no tienen lanes ni nodos: son origen
    o destino de mensajes (se nombran por el id del pool).

Flujos: "de", "a", "texto" y, opcionales, "ruta" ("hv", "vh", "hvh", "vhv",
"u_abajo", "u_arriba"), "pos" ("ini", "fin", "med": donde va el texto), "dx", "dy"
(corrimiento del texto) y "ancho_etiqueta".

Solo biblioteca estandar (mas cairosvg para el PNG).
"""

import importlib.util
import math
import os
import re
import sys
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape, quoteattr

sys.dont_write_bytecode = True

# --- medidas (px) -------------------------------------------------------------

FILA_H = 110            # alto de una fila de lane
COL_BASE = 160          # ancho de una columna con tareas
TAREA_W, TAREA_H = 128, 76
COMPUERTA = 46
EVENTO = 36
DATO_W, DATO_H = 30, 40
ANOT_W = 150
BANDA = 30              # banda con el nombre del pool y de cada lane
MARGEN = 20
TITULO_H = 34
POOL_COLAPSADO_H = 50
SEP_POOLS = 46
FUENTE = 13
FUENTE_CH = 12
INTERLINEA = 15
INTERLINEA_CH = 14
MARGEN_TEXTO = 9         # aire entre el texto de un flujo y los extremos del tramo
MIN_COL_COMPUERTA = 84
MIN_COL_EVENTO = 92
MIN_COL_DATO = 100

# --- tipos --------------------------------------------------------------------

TIPOS = ("inicio", "inicio_mensaje", "fin", "tarea", "tarea_usuario", "xor", "and",
         "evento_tiempo", "evento_mensaje", "anotacion", "datos")
TAREAS = ("tarea", "tarea_usuario")
COMPUERTAS = ("xor", "and")
ARTEFACTOS = ("anotacion", "datos")
EVENTOS = ("inicio", "inicio_mensaje", "fin", "evento_tiempo", "evento_mensaje")
PUEDEN_ENVIAR = ("tarea", "tarea_usuario", "evento_mensaje", "fin")
PUEDEN_RECIBIR = ("tarea", "tarea_usuario", "inicio_mensaje", "evento_mensaje")

NEGRO = "#1b1b1b"
GRIS_BANDA = "#e9ecef"
GRIS_LANE = "#f6f7f8"
ANOT_FONDO = "#fff8e1"
ANOT_BORDE = "#b45309"


# --- texto: medir y envolver ----------------------------------------------------

_ANCHOS = {}
for _cs, _w in (("iljI.,:;'!|", .24), ("ft/ ()[]-", .32), ("r", .34), ("sckvxyzJ", .5),
                ("abdeghnopqu0123456789?", .56), ("w", .72), ("mM", .84), ("W", .94),
                ("ACDGHNOQRU", .73), ("BEFKPSTVXYZL", .64)):
    for _c in _cs:
        _ANCHOS[_c] = _w


def ancho_texto(texto, fuente):
    """Ancho aproximado, en px, de una linea en Helvetica/Arial."""
    return sum(_ANCHOS.get(c, .56) for c in texto) * fuente * 1.04


def envolver(texto, ancho, fuente):
    """Parte el texto en lineas de hasta `ancho` px (respeta los saltos de linea)."""
    lineas = []
    for parrafo in str(texto or "").split("\n"):
        actual = ""
        for pal in parrafo.split():
            prueba = (actual + " " + pal).strip()
            if actual and ancho_texto(prueba, fuente) > ancho:
                lineas.append(actual)
                actual = pal
            else:
                actual = prueba
        if actual:
            lineas.append(actual)
    return lineas


# --- carga y analisis de la especificacion ---------------------------------------

def cargar_spec(ruta):
    spec = importlib.util.spec_from_file_location("spec_bpmn", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.PROCESO


def _es_participio(palabra):
    p = palabra.lower()
    return (p.endswith(("ado", "ada", "ados", "adas", "ido", "ida", "idos", "idas"))
            or p in ("hecho", "hecha", "dicho", "escrito", "escrita", "visto", "vista",
                     "puesto", "puesta", "abierto", "abierta", "resuelto", "resuelta",
                     "roto", "rota", "cubierto", "cubierta", "vuelto", "vuelta"))


def analizar(P):
    """Valida la especificacion y devuelve un dict con errores, avisos y los
    elementos ya clasificados (nodos, pools, secuencia, asociaciones, mensajes)."""
    errores, avisos = [], []
    A = {"errores": errores, "avisos": avisos, "nodos": {}, "pools": {}, "orden_pools": [],
         "secuencia": [], "asociaciones": [], "mensajes": []}
    nodos, pools = A["nodos"], A["pools"]

    if not isinstance(P, dict):
        errores.append("PROCESO no es un diccionario")
        return A
    for clave in ("nombre", "pools", "flujos", "mensajes"):
        if clave not in P:
            errores.append("a PROCESO le falta la clave '%s'" % clave)
    if not P.get("pools"):
        errores.append("PROCESO no tiene pools")
        return A

    # pools, lanes y nodos
    lanes_vistas = set()
    for p in P["pools"]:
        pid = p.get("id")
        if not pid or pid in pools:
            errores.append("pool con id vacio o repetido: %r" % pid)
            continue
        pools[pid] = p
        A["orden_pools"].append(pid)
        if not p.get("nombre"):
            errores.append("el pool '%s' no tiene nombre" % pid)
        lanes = p.get("lanes") or []
        if p.get("colapsado"):
            if lanes:
                errores.append("el pool colapsado '%s' no puede tener lanes" % pid)
            if p.get("nodos"):
                errores.append("el pool colapsado '%s' no puede tener nodos" % pid)
            continue
        if not lanes:
            errores.append("el pool '%s' no esta colapsado y no tiene lanes" % pid)
        for n in p.get("nodos") or []:
            errores.append("nodo sin lane: '%s' esta en el pool '%s' pero fuera de una lane"
                           % (n.get("id"), pid))
            nodos[n.get("id")] = dict(n, pool=pid, lane=None)
        for lane in lanes:
            lid = lane.get("id")
            if not lid or lid in lanes_vistas:
                errores.append("lane con id vacio o repetido: %r" % lid)
            lanes_vistas.add(lid)
            if not lane.get("nombre"):
                errores.append("la lane '%s' no tiene nombre" % lid)
            for n in lane.get("nodos") or []:
                nid = n.get("id")
                if not nid:
                    errores.append("nodo sin id en la lane '%s'" % lid)
                    continue
                if nid in nodos:
                    errores.append("nodo '%s' repetido: tiene que estar en exactamente una lane" % nid)
                    continue
                if nid in pools:
                    errores.append("el id '%s' es de un nodo y de un pool" % nid)
                if n.get("tipo") not in TIPOS:
                    errores.append("nodo '%s': tipo %r desconocido" % (nid, n.get("tipo")))
                if not isinstance(n.get("col"), (int, float)) or n.get("col") < 0:
                    errores.append("nodo '%s': falta 'col' (numero >= 0)" % nid)
                if n.get("tipo") != "anotacion" and n.get("tipo") not in COMPUERTAS and not n.get("texto"):
                    if n.get("tipo") in TAREAS + EVENTOS + ("datos",):
                        errores.append("nodo '%s': falta 'texto'" % nid)
                nodos[nid] = dict(n, pool=pid, lane=lid, lane_nombre=lane.get("nombre"))
    for pid in list(pools):
        if pid in nodos:
            errores.append("el id '%s' es de un nodo y de un pool" % pid)

    def pool_de(ref):
        if ref in nodos:
            return nodos[ref]["pool"]
        if ref in pools:
            return ref
        return None

    # flujos de secuencia y asociaciones
    for f in P.get("flujos") or []:
        de, a = f.get("de"), f.get("a")
        rotulo = "flujo %s -> %s" % (de, a)
        if de not in nodos and de not in pools or a not in nodos and a not in pools:
            errores.append("%s: algun extremo no existe" % rotulo)
            continue
        if de in pools or a in pools:
            errores.append("%s: un flujo de secuencia no puede tocar un pool; para eso "
                           "esta el flujo de mensaje" % rotulo)
            continue
        ta, tb = nodos[de].get("tipo"), nodos[a].get("tipo")
        art_a, art_b = ta in ARTEFACTOS, tb in ARTEFACTOS
        if art_a or art_b:
            if ta == tb:
                errores.append("%s: una asociacion no une dos artefactos del mismo tipo" % rotulo)
            elif nodos[de]["pool"] != nodos[a]["pool"]:
                errores.append("%s: la asociacion cruza de pool" % rotulo)
            else:
                A["asociaciones"].append(f)
            continue
        if nodos[de]["pool"] != nodos[a]["pool"]:
            errores.append("flujo de secuencia entre pools: %s (pool '%s') -> %s (pool '%s'); "
                           "entre pools va un flujo de mensaje"
                           % (de, nodos[de]["pool"], a, nodos[a]["pool"]))
            continue
        if ta == "fin":
            errores.append("%s: un evento de fin no tiene flujo de salida" % rotulo)
            continue
        if tb in ("inicio", "inicio_mensaje"):
            errores.append("%s: un evento de inicio no tiene flujo de entrada" % rotulo)
            continue
        A["secuencia"].append(f)

    # flujos de mensaje
    for m in P.get("mensajes") or []:
        de, a = m.get("de"), m.get("a")
        rotulo = "mensaje %s -> %s" % (de, a)
        pd, pa = pool_de(de), pool_de(a)
        if pd is None or pa is None:
            errores.append("%s: algun extremo no existe" % rotulo)
            continue
        if pd == pa:
            errores.append("flujo de mensaje dentro del pool '%s': %s -> %s; dentro de un "
                           "pool va un flujo de secuencia" % (pd, de, a))
            continue
        malo = False
        for ref, permitidos, verbo in ((de, PUEDEN_ENVIAR, "enviar"), (a, PUEDEN_RECIBIR, "recibir")):
            if ref in pools:
                if not pools[ref].get("colapsado"):
                    errores.append("%s: '%s' es un pool no colapsado; el mensaje tiene que salir "
                                   "o llegar a un nodo" % (rotulo, ref))
                    malo = True
            elif nodos[ref].get("tipo") not in permitidos:
                errores.append("%s: un nodo '%s' (%s) no puede %s mensajes"
                               % (rotulo, ref, nodos[ref].get("tipo"), verbo))
                malo = True
        if not malo:
            A["mensajes"].append(m)

    # conexion de cada nodo y evento de inicio / fin por pool
    entran, salen = {}, {}
    for f in A["secuencia"]:
        salen[f["de"]] = salen.get(f["de"], 0) + 1
        entran[f["a"]] = entran.get(f["a"], 0) + 1
    A["entran"], A["salen"] = entran, salen
    reciben_msg = {m["a"] for m in A["mensajes"]}
    for nid, n in nodos.items():
        t = n.get("tipo")
        if t in ARTEFACTOS or n.get("lane") is None:
            continue
        es_inicio = t in ("inicio", "inicio_mensaje") or (t == "evento_tiempo" and not entran.get(nid))
        n["es_inicio"] = es_inicio
        if es_inicio and salen.get(nid, 0) < 1:
            errores.append("el inicio '%s' no tiene flujo de salida" % nid)
        elif t == "fin":
            if entran.get(nid, 0) < 1:
                errores.append("el fin '%s' no tiene flujo de entrada" % nid)
        elif not es_inicio:
            if entran.get(nid, 0) < 1:
                errores.append("el nodo '%s' no tiene flujo de entrada (esta desconectado)" % nid)
            if salen.get(nid, 0) < 1:
                errores.append("el nodo '%s' no tiene flujo de salida (esta desconectado)" % nid)
        if t == "inicio_mensaje" and nid not in reciben_msg:
            errores.append("el inicio por mensaje '%s' no recibe ningun flujo de mensaje" % nid)
    for pid in A["orden_pools"]:
        if pools[pid].get("colapsado"):
            continue
        propios = [n for n in nodos.values() if n.get("pool") == pid]
        if not any(n.get("es_inicio") for n in propios):
            errores.append("el pool '%s' no tiene evento de inicio" % pid)
        if not any(n.get("tipo") == "fin" for n in propios):
            errores.append("el pool '%s' no tiene evento de fin" % pid)

    # compuertas XOR: pregunta y respuestas (regla de la Clase 6)
    for nid, n in nodos.items():
        if n.get("tipo") == "xor" and salen.get(nid, 0) > 1:
            if "?" not in (n.get("texto") or ""):
                errores.append("el XOR '%s' abre caminos y no tiene una pregunta (¿...?)" % nid)
            for f in A["secuencia"]:
                if f["de"] == nid and not f.get("texto"):
                    errores.append("salida del XOR '%s' hacia '%s' sin respuesta" % (nid, f["a"]))

    # nombres (avisos): tareas con verbo en infinitivo, eventos con participio
    for nid, n in nodos.items():
        palabras = (n.get("texto") or "").split()
        if not palabras:
            continue
        if n.get("tipo") in TAREAS and not palabras[0].lower().endswith(("ar", "er", "ir")):
            avisos.append("la tarea '%s' (%s) no empieza con un verbo en infinitivo"
                          % (nid, n["texto"]))
        if n.get("tipo") in EVENTOS and not _es_participio(palabras[-1]):
            avisos.append("el evento '%s' (%s) no termina en participio" % (nid, n["texto"]))
    return A


# --- geometria ---------------------------------------------------------------------

def rect(n):
    return (n["cx"] - n["w"] / 2.0, n["cy"] - n["h"] / 2.0,
            n["cx"] + n["w"] / 2.0, n["cy"] + n["h"] / 2.0)


def puerto(n, lado):
    x0, y0, x1, y1 = rect(n)
    return {"R": (x1, n["cy"]), "L": (x0, n["cy"]), "T": (n["cx"], y0), "B": (n["cx"], y1)}[lado]


def lado_de(n, punto):
    """Lado del nodo (R, L, T, B) donde esta un punto de su borde."""
    dx, dy = punto[0] - n["cx"], punto[1] - n["cy"]
    if abs(dx) / (n["w"] / 2.0) >= abs(dy) / (n["h"] / 2.0):
        return "R" if dx > 0 else "L"
    return "B" if dy > 0 else "T"


def recortar(n, hacia):
    """Punto del borde de n en la recta del centro de n hacia `hacia`."""
    dx, dy = hacia[0] - n["cx"], hacia[1] - n["cy"]
    if dx == 0 and dy == 0:
        return (n["cx"], n["cy"])
    hw, hh = n["w"] / 2.0, n["h"] / 2.0
    if n["tipo"] in COMPUERTAS:
        t = 1.0 / (abs(dx) / hw + abs(dy) / hh)
    elif n["tipo"] in EVENTOS:
        t = hw / math.hypot(dx, dy)
    else:
        t = min(hw / abs(dx) if dx else 1e9, hh / abs(dy) if dy else 1e9)
    return (n["cx"] + dx * t, n["cy"] + dy * t)


def segmento_corta(p, q, r, margen=3):
    """True si el segmento p-q atraviesa el rectangulo r (Liang-Barsky)."""
    x0, y0, x1, y1 = r[0] - margen, r[1] - margen, r[2] + margen, r[3] + margen
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq < 0:
                return False
        else:
            t = qq / pp
            if pp < 0:
                if t > t1:
                    return False
                t0 = max(t0, t)
            else:
                if t < t0:
                    return False
                t1 = min(t1, t)
    return t0 < t1 - 1e-9


def _signo(v):
    return (v > 0) - (v < 0)


def candidatos(S, T, hint=None):
    """Rutas ortogonales posibles de S a T, como {nombre: [puntos]}, en orden de preferencia."""
    dx, dy = T["cx"] - S["cx"], T["cy"] - S["cy"]
    h, h_op = ("R", "L") if dx >= 0 else ("L", "R")
    v, v_op = ("B", "T") if dy >= 0 else ("T", "B")
    c = {}
    if abs(dy) < 2 and dx != 0:
        c["directo"] = [puerto(S, h), puerto(T, h_op)]
    elif abs(dx) < 2 and dy != 0:
        c["directo"] = [puerto(S, v), puerto(T, v_op)]
    # horizontal y despues vertical (entra por arriba o abajo)
    p1, p3 = puerto(S, h), puerto(T, v_op)
    if dx != 0 and dy != 0 and _signo(T["cx"] - p1[0]) == _signo(dx):
        c["hv"] = [p1, (T["cx"], p1[1]), p3]
    # vertical y despues horizontal (entra por el costado)
    p1, p3 = puerto(S, v), puerto(T, h_op)
    if dx != 0 and dy != 0 and _signo(T["cy"] - p1[1]) == _signo(dy) and _signo(p3[0] - S["cx"]) == _signo(dx):
        c["vh"] = [p1, (p1[0], T["cy"]), p3]
    # escalones
    p1, p4 = puerto(S, h), puerto(T, h_op)
    if dx != 0 and _signo(p4[0] - p1[0]) == _signo(dx):
        mx = (p1[0] + p4[0]) / 2.0
        c["hvh"] = [p1, (mx, p1[1]), (mx, p4[1]), p4]
    p1, p4 = puerto(S, v), puerto(T, v_op)
    if dy != 0 and _signo(p4[1] - p1[1]) == _signo(dy):
        my = (p1[1] + p4[1]) / 2.0
        c["vhv"] = [p1, (p1[0], my), (T["cx"], my), p4]
    # por abajo o por arriba (flujos hacia atras)
    y_aba = max(rect(S)[3], rect(T)[3]) + 26
    c["u_abajo"] = [puerto(S, "B"), (S["cx"], y_aba), (T["cx"], y_aba), puerto(T, "B")]
    y_arr = min(rect(S)[1], rect(T)[1]) - 26
    c["u_arriba"] = [puerto(S, "T"), (S["cx"], y_arr), (T["cx"], y_arr), puerto(T, "T")]

    if hint:
        orden = [hint] if hint in c else []
    else:
        if "directo" in c:
            orden = ["directo"]
        elif S["tipo"] in COMPUERTAS:
            orden = ["vh", "hv", "hvh", "vhv"]
        else:
            orden = ["hv", "vh", "hvh", "vhv"]
        orden += ["u_abajo", "u_arriba"]
    return [(nombre, c[nombre]) for nombre in orden if nombre in c]


def elegir_ruta(S, T, obstaculos, hint=None):
    """Primera ruta sin cruces con otros nodos; si no hay, la que menos cruza."""
    mejor = None
    for nombre, pts in candidatos(S, T, hint):
        malos = [k for k, r in obstaculos.items() if k not in (S["id"], T["id"])
                 and any(segmento_corta(pts[i], pts[i + 1], r) for i in range(len(pts) - 1))]
        if not malos:
            return pts, []
        if mejor is None or len(malos) < len(mejor[1]):
            mejor = (pts, malos)
    return mejor if mejor else ([puerto(S, "R"), puerto(T, "L")], [])


# --- disposicion (layout) ---------------------------------------------------------

def tamano_nodo(n):
    t = n["tipo"]
    if t in TAREAS:
        return TAREA_W, TAREA_H
    if t in COMPUERTAS:
        return COMPUERTA, COMPUERTA
    if t in EVENTOS:
        return EVENTO, EVENTO
    if t == "datos":
        return DATO_W, DATO_H
    w = n.get("ancho", ANOT_W)
    lineas = envolver(n.get("texto"), w - 18, FUENTE_CH)
    return w, max(30, len(lineas) * INTERLINEA_CH + 14)


def disponer(P, A):
    """Calcula posiciones de pools, lanes y nodos, rutas de flujos y cajas de texto."""
    nodos, pools = A["nodos"], A["pools"]
    L = {"pools": {}, "lanes": {}, "flujos": [], "asoc": [], "msgs": [], "etiquetas": {},
         "avisos": []}

    # tamanos y anchos de columna
    for nid, n in nodos.items():
        n["id"] = nid
        n["w"], n["h"] = tamano_nodo(n)
        n.setdefault("fila", 0)
    ncols = int(max([math.floor(n["col"]) for n in nodos.values()] + [0])) + 1
    anchos = [MIN_COL_COMPUERTA] * ncols
    for c in range(ncols):
        propios = [n for n in nodos.values() if n["col"] == c]
        ancho = MIN_COL_COMPUERTA
        for n in propios:
            if n["tipo"] in TAREAS:
                ancho = max(ancho, n["w"] + 32, COL_BASE)
            elif n["tipo"] in COMPUERTAS:
                ancho = max(ancho, MIN_COL_COMPUERTA)
            elif n["tipo"] in EVENTOS:
                ancho = max(ancho, MIN_COL_EVENTO)
            elif n["tipo"] == "datos":
                ancho = max(ancho, MIN_COL_DATO)
        anchos[c] = ancho
    for c, w in (P.get("anchos") or {}).items():
        if 0 <= int(c) < ncols:
            anchos[int(c)] = w
    x_col, acum = [], 0
    for w in anchos:
        x_col.append(acum)
        acum += w
    ancho_cols = acum

    def centro_x(col):
        i = int(math.floor(col))
        c0 = x_col[i] + anchos[i] / 2.0
        if col == i:
            return c0
        j = min(i + 1, ncols - 1)
        c1 = x_col[j] + anchos[j] / 2.0
        return c0 + (c1 - c0) * (col - i)

    pool_x = MARGEN
    pool_w = BANDA * 2 + ancho_cols + 12
    x0_cols = pool_x + BANDA * 2

    # verticales: pools en el orden de la lista, lanes con las filas que necesiten
    y = MARGEN + TITULO_H
    for pid in A["orden_pools"]:
        p = pools[pid]
        if p.get("colapsado"):
            L["pools"][pid] = (pool_x, y, pool_w, POOL_COLAPSADO_H)
            y += POOL_COLAPSADO_H + SEP_POOLS
            continue
        y_pool = y
        for lane in p["lanes"]:
            propios = [n for n in nodos.values() if n["lane"] == lane["id"]]
            filas = max([math.ceil(n["fila"] + 1 - 1e-9) for n in propios] + [1])
            alto = filas * FILA_H
            L["lanes"][lane["id"]] = (pool_x + BANDA, y, pool_w - BANDA, alto)
            for n in propios:
                n["cx"] = x0_cols + centro_x(n["col"])
                n["cy"] = y + (n["fila"] + 0.5) * FILA_H
            y += alto
        L["pools"][pid] = (pool_x, y_pool, pool_w, y - y_pool)
        y += SEP_POOLS
    L["ancho"] = pool_x + pool_w + MARGEN
    L["alto"] = y - SEP_POOLS + MARGEN

    # avisos: nodos que se pisan
    ids = list(nodos)
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = rect(nodos[ids[i]]), rect(nodos[ids[j]])
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                L["avisos"].append("los nodos '%s' y '%s' se superponen" % (ids[i], ids[j]))

    obstaculos = {nid: rect(n) for nid, n in nodos.items()}

    # flujos de secuencia
    for f in A["secuencia"]:
        S, T = nodos[f["de"]], nodos[f["a"]]
        pts, malos = elegir_ruta(S, T, obstaculos, f.get("ruta"))
        if malos:
            L["avisos"].append("el flujo %s -> %s cruza %s" % (f["de"], f["a"], ", ".join(malos)))
        L["flujos"].append({"f": f, "pts": pts})

    # asociaciones: de centro a centro, recortadas en el borde
    for f in A["asociaciones"]:
        S, T = nodos[f["de"]], nodos[f["a"]]
        a = recortar(S, (T["cx"], T["cy"]))
        b = recortar(T, (S["cx"], S["cy"]))
        for k, r in obstaculos.items():
            if k not in (S["id"], T["id"]) and segmento_corta(a, b, r, 0):
                L["avisos"].append("la asociacion %s -> %s cruza '%s'" % (f["de"], f["a"], k))
        L["asoc"].append({"f": f, "pts": [a, b]})

    # mensajes: verticales hacia el pool (o entre nodos)
    for m in A["mensajes"]:
        de, a = m["de"], m["a"]
        if de in pools or a in pools:
            nodo = nodos[a if de in pools else de]
            pool = L["pools"][de if de in pools else a]
            x = nodo["cx"]
            y_pool_borde_sup, y_pool_borde_inf = pool[1], pool[1] + pool[3]
            nodo_arriba_del_pool = nodo["cy"] < pool[1]
            if nodo_arriba_del_pool:
                extremo_nodo, extremo_pool = (x, rect(nodo)[3]), (x, y_pool_borde_sup)
            else:
                extremo_nodo, extremo_pool = (x, rect(nodo)[1]), (x, y_pool_borde_inf)
            pts = [extremo_pool, extremo_nodo] if de in pools else [extremo_nodo, extremo_pool]
            for k, r in obstaculos.items():
                if k != nodo["id"] and segmento_corta(pts[0], pts[1], r, 0):
                    L["avisos"].append("el mensaje %s -> %s cruza '%s'" % (de, a, k))
        else:
            pts, malos = elegir_ruta(nodos[de], nodos[a], obstaculos, m.get("ruta"))
        L["msgs"].append({"f": m, "pts": pts})

    # lado de cada compuerta / evento que ya usa un flujo (para ubicar su texto)
    usados = {nid: set() for nid in nodos}
    for item in L["flujos"]:
        f, pts = item["f"], item["pts"]
        usados[f["de"]].add(lado_de(nodos[f["de"]], pts[0]))
        usados[f["a"]].add(lado_de(nodos[f["a"]], pts[-1]))
    for item in L["msgs"]:
        f, pts = item["f"], item["pts"]
        for ref, punto in ((f["de"], pts[0]), (f["a"], pts[-1])):
            if ref in nodos:
                usados[ref].add(lado_de(nodos[ref], punto))

    # cajas de texto de nodos
    for nid, n in nodos.items():
        t = n["tipo"]
        if t in COMPUERTAS + EVENTOS + ("datos",):
            if t == "datos":
                lineas = envolver(n.get("texto"), 96, FUENTE_CH)
            elif t in COMPUERTAS:
                lineas = envolver(n.get("texto"), n.get("ancho_etiqueta", 118), FUENTE_CH)
            else:
                lineas = envolver(n.get("texto"), 92, FUENTE_CH)
            if not lineas:
                continue
            ancho = max(ancho_texto(l, FUENTE_CH) for l in lineas)
            alto = len(lineas) * INTERLINEA_CH
            lado = n.get("etiqueta")
            if not lado:
                libres = {"arriba": "T", "abajo": "B", "izq": "L", "der": "R"}
                orden = ["abajo"] if t in EVENTOS + ("datos",) else ["arriba", "abajo", "izq", "der"]
                if t in EVENTOS:
                    orden = ["abajo", "arriba", "der", "izq"]
                lado = next((k for k in orden if libres[k] not in usados[nid]), orden[0])
            x0, y0, x1, y1 = rect(n)
            if lado == "arriba":
                caja = (n["cx"] - ancho / 2.0, y0 - 3 - alto, ancho, alto, "middle")
            elif lado == "abajo":
                caja = (n["cx"] - ancho / 2.0, y1 + 3, ancho, alto, "middle")
            elif lado == "izq":
                caja = (x0 - 5 - ancho, n["cy"] - alto / 2.0, ancho, alto, "end")
            else:
                caja = (x1 + 5, n["cy"] - alto / 2.0, ancho, alto, "start")
            L["etiquetas"][("nodo", nid)] = {"caja": caja[:4], "ancla": caja[4], "lineas": lineas}

    # cajas de texto de flujos
    for clave, items, ancho_def in (("flujos", L["flujos"], 92), ("msgs", L["msgs"], 220)):
        for k, item in enumerate(items):
            f, pts = item["f"], item["pts"]
            lineas = envolver(f.get("texto"), f.get("ancho_etiqueta", ancho_def), FUENTE_CH)
            if not lineas:
                continue
            if "pos" in f:
                pos = f["pos"]
            elif clave == "flujos":
                pos = "ini"
            elif f["de"] in pools:        # mensaje que sale de un pool: el texto va junto al pool
                pos = "ini"
            elif f["a"] in pools:
                pos = "fin"
            else:
                pos = "med"
            if pos == "med":
                largos = [math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1])
                          for i in range(len(pts) - 1)]
                idx = largos.index(max(largos))
            else:
                idx = 0 if pos == "ini" else len(pts) - 2
            # en un tramo horizontal el texto no puede pasar de un extremo del tramo: si no
            # entra en el ancho que hay, se vuelve a partir en lineas mas angostas
            disponible = abs(pts[idx + 1][0] - pts[idx][0]) - 2 * MARGEN_TEXTO
            if (abs(pts[idx][1] - pts[idx + 1][1]) < 1 and pos != "med"
                    and "ancho_etiqueta" not in f
                    and max(ancho_texto(l, FUENTE_CH) for l in lineas) > disponible >= 40):
                lineas = envolver(f.get("texto"), disponible, FUENTE_CH)
            ancho = max(ancho_texto(l, FUENTE_CH) for l in lineas)
            alto = len(lineas) * INTERLINEA_CH
            a, b = pts[idx], pts[idx + 1]
            if abs(a[1] - b[1]) < 1:                       # tramo horizontal: texto arriba
                sg = _signo(b[0] - a[0])
                if pos == "ini":
                    x = a[0] + MARGEN_TEXTO if sg > 0 else a[0] - MARGEN_TEXTO - ancho
                elif pos == "fin":
                    x = b[0] - MARGEN_TEXTO - ancho if sg > 0 else b[0] + MARGEN_TEXTO
                else:
                    x = (a[0] + b[0]) / 2.0 - ancho / 2.0
                yy = a[1] - 4 - alto
            else:                                          # tramo vertical: texto a la derecha
                sg = _signo(b[1] - a[1])
                x = a[0] + 6
                if pos == "ini":
                    yy = a[1] + 4 if sg > 0 else a[1] - 4 - alto
                elif pos == "fin":
                    yy = b[1] - 4 - alto if sg > 0 else b[1] + 4
                else:
                    yy = (a[1] + b[1]) / 2.0 - alto / 2.0
            x += f.get("dx", 0)
            yy += f.get("dy", 0)
            L["etiquetas"][(clave, k)] = {"caja": (x, yy, ancho, alto), "ancla": "start",
                                          "lineas": lineas}
    return L


# --- SVG ---------------------------------------------------------------------------

def _f(v):
    return ("%.1f" % v).rstrip("0").rstrip(".")


def _texto_svg(x, y_top, lineas, fuente, ancla="middle", inter=None, peso=None, color=NEGRO):
    inter = inter or (INTERLINEA if fuente >= 12 else INTERLINEA_CH)
    base = y_top + inter * 0.78
    out = ['<text x="%s" y="%s" font-size="%d" text-anchor="%s" fill="%s"%s>'
           % (_f(x), _f(base), fuente, ancla, color,
              ' font-weight="%s"' % peso if peso else "")]
    for i, ln in enumerate(lineas):
        out.append('<tspan x="%s" dy="%s">%s</tspan>' % (_f(x), "0" if i == 0 else inter, escape(ln)))
    out.append("</text>")
    return "".join(out)


def _flecha(p, q, hueca=False, abierta=False):
    """Punta de flecha en q, viniendo de p."""
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    largo, medio = 10.0, 4.5
    bx, by = q[0] - largo * math.cos(ang), q[1] - largo * math.sin(ang)
    ix, iy = -math.sin(ang) * medio, math.cos(ang) * medio
    pts = "%s,%s %s,%s %s,%s" % (_f(q[0]), _f(q[1]), _f(bx + ix), _f(by + iy), _f(bx - ix), _f(by - iy))
    if abierta:
        return ('<polyline points="%s,%s %s,%s %s,%s" fill="none" stroke="%s" stroke-width="1.4"/>'
                % (_f(bx + ix), _f(by + iy), _f(q[0]), _f(q[1]), _f(bx - ix), _f(by - iy), NEGRO))
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.4"/>' % (
        pts, "#fff" if hueca else NEGRO, NEGRO)


def _linea(pts, extra=""):
    return '<polyline points="%s" fill="none" stroke="%s" stroke-width="1.6"%s/>' % (
        " ".join("%s,%s" % (_f(x), _f(y)) for x, y in pts), NEGRO, extra)


def _sobre(cx, cy, ancho=14, alto=10, relleno="none", color=NEGRO):
    x, y = cx - ancho / 2.0, cy - alto / 2.0
    return ('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.3"/>'
            '<polyline points="%s,%s %s,%s %s,%s" fill="none" stroke="%s" stroke-width="1.3"/>'
            % (_f(x), _f(y), ancho, alto, relleno, color, _f(x), _f(y), _f(cx), _f(cy + 1),
               _f(x + ancho), _f(y), color))


def _reloj(cx, cy, r=9):
    out = ['<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="1.3"/>'
           % (_f(cx), _f(cy), r, NEGRO)]
    for k in range(12):
        a = math.radians(k * 30)
        l = 2.2 if k % 3 == 0 else 1.2
        out.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="0.9"/>' % (
            _f(cx + (r - l) * math.sin(a)), _f(cy - (r - l) * math.cos(a)),
            _f(cx + r * math.sin(a)), _f(cy - r * math.cos(a)), NEGRO))
    out.append('<polyline points="%s,%s %s,%s %s,%s" fill="none" stroke="%s" stroke-width="1.3"/>' % (
        _f(cx + 3.5), _f(cy - 3.5), _f(cx), _f(cy), _f(cx), _f(cy - 6.5), NEGRO))
    return "".join(out)


def dibujar_nodo(n):
    t, cx, cy, w, h = n["tipo"], n["cx"], n["cy"], n["w"], n["h"]
    x0, y0, x1, y1 = rect(n)
    s = []
    if t in TAREAS:
        s.append('<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="#fff" stroke="%s" '
                 'stroke-width="1.8"/>' % (_f(x0), _f(y0), w, h, NEGRO))
        lineas = envolver(n.get("texto"), w - 14, FUENTE)
        top = cy - len(lineas) * INTERLINEA / 2.0 + (4 if t == "tarea_usuario" else 0)
        s.append(_texto_svg(cx, top, lineas, FUENTE))
        if t == "tarea_usuario":      # figura de persona, arriba a la izquierda
            hx, hy = x0 + 12, y0 + 9
            s.append('<circle cx="%s" cy="%s" r="3.2" fill="#fff" stroke="%s" stroke-width="1.1"/>'
                     '<path d="M %s %s v -2 q 0 -4.5 5.5 -4.5 q 5.5 0 5.5 4.5 v 2 z" fill="#fff" '
                     'stroke="%s" stroke-width="1.1"/>'
                     % (_f(hx), _f(hy), NEGRO, _f(hx - 5.5), _f(hy + 10.5), NEGRO))
    elif t in COMPUERTAS:
        s.append('<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="#fff" stroke="%s" stroke-width="1.8"/>'
                 % (_f(cx), _f(y0), _f(x1), _f(cy), _f(cx), _f(y1), _f(x0), _f(cy), NEGRO))
        if t == "xor":
            d = 8
            s.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.2"/>'
                     '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.2"/>'
                     % (_f(cx - d), _f(cy - d), _f(cx + d), _f(cy + d), NEGRO,
                        _f(cx - d), _f(cy + d), _f(cx + d), _f(cy - d), NEGRO))
        else:
            d = 11
            s.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.4"/>'
                     '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="3.4"/>'
                     % (_f(cx - d), _f(cy), _f(cx + d), _f(cy), NEGRO,
                        _f(cx), _f(cy - d), _f(cx), _f(cy + d), NEGRO))
    elif t in EVENTOS:
        r = w / 2.0
        ancho_borde = 4.2 if t == "fin" else 1.8
        s.append('<circle cx="%s" cy="%s" r="%s" fill="#fff" stroke="%s" stroke-width="%s"/>'
                 % (_f(cx), _f(cy), _f(r), NEGRO, ancho_borde))
        intermedio = t == "evento_mensaje" or (t == "evento_tiempo" and not n.get("es_inicio"))
        if intermedio:
            s.append('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="1.4"/>'
                     % (_f(cx), _f(cy), _f(r - 3.5), NEGRO))
        if t in ("inicio_mensaje", "evento_mensaje"):
            s.append(_sobre(cx, cy))
        elif t == "evento_tiempo":
            s.append(_reloj(cx, cy, 9 if not intermedio else 8))
    elif t == "datos":
        d = 9
        s.append('<path d="M %s %s L %s %s L %s %s L %s %s L %s %s Z" fill="#fff" stroke="%s" '
                 'stroke-width="1.5"/><path d="M %s %s L %s %s L %s %s" fill="none" stroke="%s" '
                 'stroke-width="1.2"/>'
                 % (_f(x0), _f(y0), _f(x1 - d), _f(y0), _f(x1), _f(y0 + d), _f(x1), _f(y1),
                    _f(x0), _f(y1), NEGRO, _f(x1 - d), _f(y0), _f(x1 - d), _f(y0 + d),
                    _f(x1), _f(y0 + d), NEGRO))
    else:   # anotacion
        lineas = envolver(n.get("texto"), w - 18, FUENTE_CH)
        s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="none"/>'
                 % (_f(x0), _f(y0), w, h, ANOT_FONDO))
        s.append('<polyline points="%s,%s %s,%s %s,%s %s,%s" fill="none" stroke="%s" stroke-width="1.8"/>'
                 % (_f(x0 + 9), _f(y0), _f(x0), _f(y0), _f(x0), _f(y1), _f(x0 + 9), _f(y1), ANOT_BORDE))
        s.append(_texto_svg(x0 + 9, y0 + 7, lineas, FUENTE_CH, "start", INTERLINEA_CH))
    return "".join(s)


def generar_svg(P, A, L):
    nodos, pools = A["nodos"], A["pools"]
    W, H = L["ancho"], L["alto"]
    s = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="0 0 %s %s" '
         'font-family="Helvetica Neue, Helvetica, Arial, sans-serif">' % (_f(W), _f(H), _f(W), _f(H)),
         "<title>%s</title>" % escape(P.get("nombre", "")),
         '<rect x="0" y="0" width="%s" height="%s" fill="#fff"/>' % (_f(W), _f(H)),
         _texto_svg(MARGEN, MARGEN - 2, [P.get("nombre", "")], 16, "start", 20, "bold")]

    # pools y lanes
    for pid in A["orden_pools"]:
        x, y, w, h = L["pools"][pid]
        p = pools[pid]
        if p.get("colapsado"):
            s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.8"/>'
                     % (_f(x), _f(y), _f(w), _f(h), GRIS_BANDA, NEGRO))
            s.append(_texto_svg(x + w / 2.0, y + h / 2.0 - 8, [p["nombre"]], 14, "middle", 18, "bold"))
            continue
        s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#fff" stroke="%s" stroke-width="1.8"/>'
                 % (_f(x), _f(y), _f(w), _f(h), NEGRO))
        s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.8"/>'
                 % (_f(x), _f(y), BANDA, _f(h), GRIS_BANDA, NEGRO))
        s.append('<g transform="rotate(-90 %s %s)">%s</g>' % (
            _f(x + BANDA / 2.0), _f(y + h / 2.0),
            _texto_svg(x + BANDA / 2.0, y + h / 2.0 - 9, [p["nombre"]], 14, "middle", 18, "bold")))
        for lane in p["lanes"]:
            lx, ly, lw, lh = L["lanes"][lane["id"]]
            s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="none" stroke="%s" stroke-width="1.4"/>'
                     % (_f(lx), _f(ly), _f(lw), _f(lh), NEGRO))
            s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="%s" stroke="%s" stroke-width="1.4"/>'
                     % (_f(lx), _f(ly), BANDA, _f(lh), GRIS_LANE, NEGRO))
            s.append('<g transform="rotate(-90 %s %s)">%s</g>' % (
                _f(lx + BANDA / 2.0), _f(ly + lh / 2.0),
                _texto_svg(lx + BANDA / 2.0, ly + lh / 2.0 - 8, [lane["nombre"]], 13, "middle", 16, "bold")))

    # asociaciones, flujos de secuencia y de mensaje
    for item in L["asoc"]:
        a, b = item["pts"]
        f = item["f"]
        datos_salida = (nodos[f["de"]]["tipo"] in TAREAS and nodos[f["a"]]["tipo"] == "datos")
        datos_entrada = (nodos[f["de"]]["tipo"] == "datos" and nodos[f["a"]]["tipo"] in TAREAS)
        s.append(_linea([a, b], ' stroke-dasharray="2.5,3.5" stroke-linecap="round"'))
        if datos_salida or datos_entrada:
            s.append(_flecha(a, b, abierta=True))
    for item in L["flujos"]:
        s.append(_linea(item["pts"]))
        s.append(_flecha(item["pts"][-2], item["pts"][-1]))
    for item in L["msgs"]:
        pts = item["pts"]
        s.append(_linea(pts, ' stroke-dasharray="7,4"'))
        s.append('<circle cx="%s" cy="%s" r="3.6" fill="#fff" stroke="%s" stroke-width="1.4"/>'
                 % (_f(pts[0][0]), _f(pts[0][1]), NEGRO))
        s.append(_flecha(pts[-2], pts[-1], hueca=True))

    # nodos
    for nid, n in nodos.items():
        s.append(dibujar_nodo(n))

    # textos de nodos y de flujos (con fondo blanco para leerse sobre las lineas)
    for clave, e in L["etiquetas"].items():
        x, y, w, h = e["caja"]
        ancla = e["ancla"]
        if clave[0] != "nodo":
            s.append('<rect x="%s" y="%s" width="%s" height="%s" fill="#fff" fill-opacity="0.85"/>'
                     % (_f(x - 2), _f(y), _f(w + 4), _f(h)))
        x_texto = {"start": x, "middle": x + w / 2.0, "end": x + w}[ancla]
        s.append(_texto_svg(x_texto, y, e["lineas"], FUENTE_CH, ancla, INTERLINEA_CH))
    s.append("</svg>")
    return "\n".join(s)


# --- BPMN XML ----------------------------------------------------------------------

def _id(prefijo, texto):
    return "%s_%s" % (prefijo, re.sub(r"[^A-Za-z0-9_.-]", "_", str(texto)))


def generar_xml(P, A, L):
    nodos, pools = A["nodos"], A["pools"]
    entran, salen = A["entran"], A["salen"]
    x = []
    ap = x.append
    ids_nodo = {}
    for nid, n in nodos.items():
        t = n["tipo"]
        pref = {"tarea": "Activity", "tarea_usuario": "Activity", "xor": "Gateway", "and": "Gateway",
                "anotacion": "Annotation", "datos": "DataObjectReference"}.get(t, "Event")
        ids_nodo[nid] = _id(pref, nid)
    ids_ref = dict(ids_nodo)
    for pid in pools:
        ids_ref[pid] = _id("Participant", pid)

    # ids de flujos
    usados = set()

    def id_flujo(pref, de, a):
        base = "%s_%s_%s" % (pref, re.sub(r"[^A-Za-z0-9_.-]", "_", str(de)),
                             re.sub(r"[^A-Za-z0-9_.-]", "_", str(a)))
        nuevo, k = base, 2
        while nuevo in usados:
            nuevo = "%s_%d" % (base, k)
            k += 1
        usados.add(nuevo)
        return nuevo

    for item in L["flujos"]:
        item["xml"] = id_flujo("Flow", item["f"]["de"], item["f"]["a"])
    for item in L["msgs"]:
        item["xml"] = id_flujo("MessageFlow", item["f"]["de"], item["f"]["a"])
    for item in L["asoc"]:
        f = item["f"]
        salida_datos = nodos[f["de"]]["tipo"] in TAREAS and nodos[f["a"]]["tipo"] == "datos"
        entrada_datos = nodos[f["de"]]["tipo"] == "datos" and nodos[f["a"]]["tipo"] in TAREAS
        item["salida_datos"] = salida_datos
        item["entrada_datos"] = entrada_datos
        if salida_datos:
            pref_asoc = "DataOutputAssociation"
        elif entrada_datos:
            pref_asoc = "DataInputAssociation"
        else:
            pref_asoc = "Association"
        item["xml"] = id_flujo(pref_asoc, f["de"], f["a"])

    colab = "Collaboration_" + re.sub(r"[^A-Za-z0-9_.-]", "_", P.get("nombre", "proceso"))[:40]
    ap('<?xml version="1.0" encoding="UTF-8"?>')
    ap('<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" '
       'xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" '
       'xmlns:dc="http://www.omg.org/spec/DD/20100524/DC" '
       'xmlns:di="http://www.omg.org/spec/DD/20100524/DI" '
       'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="Definitions_1" '
       'targetNamespace="http://bpmn.io/schema/bpmn" exporter="generar_bpmn.py" '
       'exporterVersion="1.0">')
    ap('  <bpmn:collaboration id="%s">' % colab)
    for pid in A["orden_pools"]:
        p = pools[pid]
        if p.get("colapsado"):
            ap('    <bpmn:participant id="%s" name=%s />' % (ids_ref[pid], quoteattr(p["nombre"])))
        else:
            ap('    <bpmn:participant id="%s" name=%s processRef="%s" />'
               % (ids_ref[pid], quoteattr(p["nombre"]), _id("Process", pid)))
    for item in L["msgs"]:
        f = item["f"]
        nombre = " name=%s" % quoteattr(f["texto"]) if f.get("texto") else ""
        ap('    <bpmn:messageFlow id="%s"%s sourceRef="%s" targetRef="%s" />'
           % (item["xml"], nombre, ids_ref[f["de"]], ids_ref[f["a"]]))
    ap("  </bpmn:collaboration>")

    for pid in A["orden_pools"]:
        p = pools[pid]
        if p.get("colapsado"):
            continue
        propios = {nid: n for nid, n in nodos.items() if n["pool"] == pid}
        ap('  <bpmn:process id="%s" isExecutable="false">' % _id("Process", pid))
        ap('    <bpmn:laneSet id="%s">' % _id("LaneSet", pid))
        for lane in p["lanes"]:
            ap('      <bpmn:lane id="%s" name=%s>' % (_id("Lane", lane["id"]), quoteattr(lane["nombre"])))
            for n in lane["nodos"]:
                if n["tipo"] not in ARTEFACTOS:
                    ap("        <bpmn:flowNodeRef>%s</bpmn:flowNodeRef>" % ids_nodo[n["id"]])
            ap("      </bpmn:lane>")
        ap("    </bpmn:laneSet>")

        for nid, n in propios.items():
            t = n["tipo"]
            xid = ids_nodo[nid]
            nombre = " name=%s" % quoteattr(n["texto"]) if n.get("texto") and t != "anotacion" else ""
            ent = [i["xml"] for i in L["flujos"] if i["f"]["a"] == nid]
            sal = [i["xml"] for i in L["flujos"] if i["f"]["de"] == nid]
            flujos_io = "".join("\n      <bpmn:incoming>%s</bpmn:incoming>" % e for e in ent) + \
                        "".join("\n      <bpmn:outgoing>%s</bpmn:outgoing>" % e for e in sal)
            if t == "anotacion":
                continue
            if t == "datos":
                ap('    <bpmn:dataObject id="%s" />' % _id("DataObject", nid))
                ap('    <bpmn:dataObjectReference id="%s"%s dataObjectRef="%s" />'
                   % (xid, nombre, _id("DataObject", nid)))
                continue
            if t in TAREAS:
                salidas_datos = "".join(
                    '\n      <bpmn:dataOutputAssociation id="%s">\n        <bpmn:targetRef>%s</bpmn:targetRef>\n'
                    '      </bpmn:dataOutputAssociation>' % (i["xml"], ids_nodo[i["f"]["a"]])
                    for i in L["asoc"] if i["salida_datos"] and i["f"]["de"] == nid)
                entradas = [i for i in L["asoc"] if i["entrada_datos"] and i["f"]["a"] == nid]
                # como en bpmn.io: cada entrada apunta a una propiedad de la tarea. El esquema
                # pide todas las <property> antes de todas las <dataInputAssociation>
                props = [_id("Property", "%s_%d" % (nid, k + 1)) for k in range(len(entradas))]
                entradas_datos = "".join(
                    '\n      <bpmn:property id="%s" name="__targetRef_placeholder" />' % pp
                    for pp in props)
                entradas_datos += "".join(
                    '\n      <bpmn:dataInputAssociation id="%s">\n        <bpmn:sourceRef>%s</bpmn:sourceRef>\n'
                    '        <bpmn:targetRef>%s</bpmn:targetRef>\n'
                    '      </bpmn:dataInputAssociation>' % (i["xml"], ids_nodo[i["f"]["de"]], pp)
                    for i, pp in zip(entradas, props))
                etiqueta = "userTask" if t == "tarea_usuario" else "task"
                ap('    <bpmn:%s id="%s"%s>%s%s%s\n    </bpmn:%s>' % (etiqueta, xid, nombre, flujos_io, entradas_datos, salidas_datos, etiqueta))
            elif t in COMPUERTAS:
                if t == "xor":
                    etiqueta = "exclusiveGateway"
                else:
                    etiqueta = "parallelGateway"
                if len(sal) > 1:
                    direccion = "Diverging"
                elif len(ent) > 1:
                    direccion = "Converging"
                else:
                    direccion = "Unspecified"
                ap('    <bpmn:%s id="%s"%s gatewayDirection="%s">%s\n    </bpmn:%s>'
                   % (etiqueta, xid, nombre, direccion, flujos_io, etiqueta))
            else:
                if t == "fin":
                    etiqueta, definicion = "endEvent", ""
                elif t == "inicio":
                    etiqueta, definicion = "startEvent", ""
                elif t == "inicio_mensaje":
                    etiqueta, definicion = "startEvent", '\n      <bpmn:messageEventDefinition id="%s" />' % _id("MessageEventDefinition", nid)
                elif t == "evento_mensaje":
                    etiqueta, definicion = "intermediateCatchEvent", '\n      <bpmn:messageEventDefinition id="%s" />' % _id("MessageEventDefinition", nid)
                else:
                    etiqueta = "startEvent" if n.get("es_inicio") else "intermediateCatchEvent"
                    definicion = '\n      <bpmn:timerEventDefinition id="%s" />' % _id("TimerEventDefinition", nid)
                ap('    <bpmn:%s id="%s"%s>%s%s\n    </bpmn:%s>' % (etiqueta, xid, nombre, flujos_io, definicion, etiqueta))
        for item in L["flujos"]:
            f = item["f"]
            if nodos[f["de"]]["pool"] != pid:
                continue
            nombre = " name=%s" % quoteattr(f["texto"]) if f.get("texto") else ""
            ap('    <bpmn:sequenceFlow id="%s"%s sourceRef="%s" targetRef="%s" />'
               % (item["xml"], nombre, ids_nodo[f["de"]], ids_nodo[f["a"]]))
        for nid, n in propios.items():
            if n["tipo"] == "anotacion":
                ap('    <bpmn:textAnnotation id="%s">\n      <bpmn:text>%s</bpmn:text>\n    </bpmn:textAnnotation>'
                   % (ids_nodo[nid], escape(n["texto"])))
        for item in L["asoc"]:
            f = item["f"]
            if nodos[f["de"]]["pool"] != pid or item["salida_datos"] or item["entrada_datos"]:
                continue
            # la asociacion sale del elemento de flujo y llega al artefacto
            origen, destino = f["de"], f["a"]
            if nodos[origen]["tipo"] == "anotacion" or (
                    nodos[origen]["tipo"] == "datos" and nodos[destino]["tipo"] != "anotacion"):
                origen, destino = destino, origen
            ap('    <bpmn:association id="%s" associationDirection="None" sourceRef="%s" targetRef="%s" />'
               % (item["xml"], ids_nodo[origen], ids_nodo[destino]))
        ap("  </bpmn:process>")

    # diagrama (BPMNDI)
    ap('  <bpmndi:BPMNDiagram id="BPMNDiagram_1">')
    ap('    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="%s">' % colab)

    def bounds(x0, y0, w, h):
        return '<dc:Bounds x="%d" y="%d" width="%d" height="%d" />' % (round(x0), round(y0), round(w), round(h))

    for pid in A["orden_pools"]:
        px, py, pw, ph = L["pools"][pid]
        ap('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s" isHorizontal="true">' % (ids_ref[pid], ids_ref[pid]))
        ap("        " + bounds(px, py, pw, ph))
        ap("      </bpmndi:BPMNShape>")
        if pools[pid].get("colapsado"):
            continue
        for lane in pools[pid]["lanes"]:
            lx, ly, lw, lh = L["lanes"][lane["id"]]
            ap('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s" isHorizontal="true">'
               % (_id("Lane", lane["id"]), _id("Lane", lane["id"])))
            ap("        " + bounds(lx, ly, lw, lh))
            ap("      </bpmndi:BPMNShape>")
    for nid, n in nodos.items():
        xid = ids_nodo[nid]
        marca = ' isMarkerVisible="true"' if n["tipo"] == "xor" else ""
        ap('      <bpmndi:BPMNShape id="%s_di" bpmnElement="%s"%s>' % (xid, xid, marca))
        x0, y0, x1, y1 = rect(n)
        ap("        " + bounds(x0, y0, n["w"], n["h"]))
        e = L["etiquetas"].get(("nodo", nid))
        if e:
            ap("        <bpmndi:BPMNLabel>")
            ap("          " + bounds(*e["caja"]))
            ap("        </bpmndi:BPMNLabel>")
        ap("      </bpmndi:BPMNShape>")

    def borde(clave, k, item):
        ap('      <bpmndi:BPMNEdge id="%s_di" bpmnElement="%s">' % (item["xml"], item["xml"]))
        for px, py in item["pts"]:
            ap('        <di:waypoint x="%d" y="%d" />' % (round(px), round(py)))
        e = L["etiquetas"].get((clave, k))
        if e:
            ap("        <bpmndi:BPMNLabel>")
            ap("          " + bounds(*e["caja"]))
            ap("        </bpmndi:BPMNLabel>")
        ap("      </bpmndi:BPMNEdge>")

    for k, item in enumerate(L["flujos"]):
        borde("flujos", k, item)
    for k, item in enumerate(L["msgs"]):
        borde("msgs", k, item)
    for k, item in enumerate(L["asoc"]):
        borde("asoc", k, item)
    ap("    </bpmndi:BPMNPlane>")
    ap("  </bpmndi:BPMNDiagram>")
    ap("</bpmn:definitions>")
    return "\n".join(x) + "\n"


def revisar_xml(texto):
    """Chequeos de coherencia del XML generado: bien formado, referencias que existen,
    forma en el diagrama para cada elemento. Devuelve una lista de problemas."""
    problemas = []
    try:
        raiz = ET.fromstring(texto.encode("utf-8"))
    except ET.ParseError as e:
        return ["el .bpmn no es XML bien formado: %s" % e]
    ids = {}
    for el in raiz.iter():
        i = el.get("id")
        if i:
            if i in ids:
                problemas.append("id repetido en el .bpmn: %s" % i)
            ids[i] = el
    modelo = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"
    for el in raiz.iter():
        for attr in ("sourceRef", "targetRef", "processRef", "dataObjectRef"):
            ref = el.get(attr)
            if ref and ref not in ids:
                problemas.append("%s=%s no existe" % (attr, ref))
        if el.tag in (modelo + "incoming", modelo + "outgoing", modelo + "flowNodeRef") and el.text not in ids:
            problemas.append("referencia %s a un id que no existe: %s" % (el.tag.split("}")[1], el.text))
        if el.tag in (modelo + "targetRef", modelo + "sourceRef") and el.text not in ids:
            problemas.append("referencia %s a un id que no existe: %s" % (el.tag.split("}")[1], el.text))
    en_di = set()
    for el in raiz.iter():
        if el.tag.endswith("}BPMNShape") or el.tag.endswith("}BPMNEdge"):
            ref = el.get("bpmnElement")
            if ref not in ids:
                problemas.append("el diagrama dibuja '%s', que no existe" % ref)
            en_di.add(ref)
    sin_forma = ("laneSet", "process", "collaboration", "definitions", "flowNodeRef", "text",
                 "messageEventDefinition", "timerEventDefinition", "dataObject", "property")
    for i, el in ids.items():
        etiqueta = el.tag.split("}")[1] if "}" in el.tag else el.tag
        if el.tag.startswith(modelo) and etiqueta not in sin_forma and \
                not etiqueta.endswith("Diagram") and i not in en_di:
            problemas.append("'%s' (%s) no tiene forma en el diagrama" % (i, etiqueta))
    return problemas


# --- programa ----------------------------------------------------------------------

def construir(P):
    """Valida y arma las tres salidas. Devuelve (A, L, xml, svg)."""
    A = analizar(P)
    if A["errores"]:
        return A, None, None, None
    L = disponer(P, A)
    xml = generar_xml(P, A, L)
    svg = generar_svg(P, A, L)
    return A, L, xml, svg


def main(argv):
    solo_validar = "--validar" in argv
    rutas = [a for a in argv[1:] if not a.startswith("--")]
    if len(rutas) != 1:
        print(__doc__.split("\n\n")[0], file=sys.stderr)
        print("uso: generar_bpmn.py especificacion.py [--validar]", file=sys.stderr)
        return 2
    ruta = os.path.abspath(rutas[0])
    P = cargar_spec(ruta)
    A, L, xml, svg = construir(P)
    for av in A["avisos"] + (L["avisos"] if L else []):
        print("AVISO: " + av, file=sys.stderr)
    if A["errores"]:
        for e in A["errores"]:
            print("ERROR: " + e)
        print("%d errores: no se escribio nada." % len(A["errores"]))
        return 1
    problemas = revisar_xml(xml)
    if problemas:
        for e in problemas:
            print("ERROR: " + e)
        return 1
    n_nodos = len(A["nodos"])
    resumen = "%d nodos, %d flujos de secuencia, %d de mensaje, %d asociaciones" % (
        n_nodos, len(A["secuencia"]), len(A["mensajes"]), len(A["asociaciones"]))
    if solo_validar:
        print("OK: %s; sin errores (%d avisos)" % (resumen, len(A["avisos"]) + len(L["avisos"])))
        return 0

    base = os.path.splitext(ruta)[0]
    with open(base + ".bpmn", "w", encoding="utf-8") as fh:
        fh.write(xml)
    with open(base + ".svg", "w", encoding="utf-8") as fh:
        fh.write(svg)
    print("escribi %s.bpmn y %s.svg (%s)" % (os.path.basename(base), os.path.basename(base), resumen))
    try:
        import cairosvg
    except ImportError:
        print("falta cairosvg: no se genero el PNG (usar el python de .venv)", file=sys.stderr)
        return 1
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=base + ".png", scale=2,
                     background_color="white")
    print("escribi %s.png" % os.path.basename(base))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
