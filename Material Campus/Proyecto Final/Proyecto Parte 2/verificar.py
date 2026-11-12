#!/usr/bin/env python3
"""Verificador de las secciones de la Parte 2 del TP Final (Dulxelitos).

    python3 verificar.py [archivo.md ...]

Sin argumentos revisa todos los "NN - *.md" de esta carpeta menos los "00 - *".
Salida:
  - stdout: "OK", o una linea por falla con "archivo:linea regla mensaje".
  - stderr: las advertencias (regla cifras) y la lista de huecos (regla
    pendientes). No hacen fallar nada.
  - codigo de salida 1 si hay alguna falla.

Reglas
  problema     en "01 - Problema y objetivos.md": el primer bloque citado bajo
               "## Problema gerencial" tiene hasta 60 palabras y ninguna de las
               palabras que nombran una herramienta (software, sistema, app,
               modulo, Discovery, planilla; tambien en plural).
  delatores    nada que delate como se armo el trabajo: clases, transcripciones,
               catedra, guia de ejemplo, enunciado o consigna, docentes, huecos
               "[dato pendiente" ni la Parte 1 contada como error (corrige,
               correccion, equivocado, sobreestimado).
  cifras       porcentajes, horas, meses y semanas fuera de la lista blanca
               (76, 24, 25, 30, 125, 20 / 6 meses / 2 semanas): advertencia.
  encabezados  cada archivo tiene los "##" que exige su tarea (se chequean
               solo los archivos que existen).
  trazas       02: cada lane de bpmn/as-is.py aparece en "## RECI".
               08: cada indicador aparece con su linea de base, en su propio
               bloque "###" (el numero exacto: "176 %" no vale por 76 %;
               exactitud pide el hueco o el porcentaje en una linea que diga
               "base").
               Si el archivo que hace falta no existe todavia, se saltea.
  pendientes   lista cada "[dato pendiente" con archivo y linea.

Solo biblioteca estandar. Las funciones se pueden importar (por ejemplo,
pendientes() para armar el anexo de datos pendientes de la entrega).
"""

import glob
import importlib.util
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True

BASE = os.path.dirname(os.path.abspath(__file__))

# --- datos de las reglas ----------------------------------------------------

# Encabezados "##" obligatorios por archivo (regla encabezados).
ENCABEZADOS = {
    "01 - Problema y objetivos.md": [
        "Lo que encontramos en el relevamiento", "Problema gerencial",
        "Objetivo general", "Objetivos específicos", "Alcance",
        "Fuera de alcance",
    ],
    "02 - Proceso actual y alternativas.md": [
        "Matriz de descubrimiento", "SIPOC", "RECI", "Diagrama AS-IS",
        "Tres lentes", "Alternativas", "Matriz multicriterio", "Recomendación",
    ],
    "03 - Proceso futuro.md": [
        "Diagrama TO-BE", "Qué cambia", "Responsables y decisiones",
        "Datos y controles",
    ],
    "04 - Modelo de negocio y propuesta de valor.md": [
        "Cambios en el BMC", "VPC TO-BE", "Supuestos clave",
    ],
    "05 - Stakeholders.md": [
        "Mapa de actores", "Matriz poder/interés",
        "Estrategias de involucramiento", "Cómo cambia por fase",
    ],
    "06 - Arquitectura y datos.md": [
        "Diagrama", "Datos", "Integraciones", "Reglas de datos",
    ],
    "07 - Validación de supuestos.md": [
        "Supuestos críticos", "Piloto", "Criterio de decisión",
    ],
    "08 - Roadmap e indicadores.md": [
        "Roadmap", "Cómo se protege la operación", "OKR", "Indicadores",
    ],
}

ARCHIVO_PROBLEMA = "01 - Problema y objetivos.md"
ARCHIVO_PROCESO = "02 - Proceso actual y alternativas.md"
ARCHIVO_ROADMAP = "08 - Roadmap e indicadores.md"

MAX_PALABRAS_PROBLEMA = 60

# Palabras que nombran una herramienta: el problema no las puede usar.
PROHIBIDAS = re.compile(
    r"(?<!\w)(software|sistemas?|apps?|m[óo]dulos?|discovery|planillas?)(?!\w)",
    re.IGNORECASE)

# Lista blanca de cifras (diseño §9 y plazos del grupo).
CIFRAS_OK = {"76", "24", "25", "30", "125", "20"}
DURACIONES_OK = {"meses": {"6"}, "semanas": {"2"}}

# Indicadores de 08 con su linea de base: (nombre, patron de la base, texto).
# NOSOL: el numero no puede ir pegado a otra cifra ("176 %", "120 %", "125 horas").
NOSOL = r"(?<![\d.,])"
INDICADORES = [
    ("Pedidos completos y a tiempo", NOSOL + r"76\s*%", "76 %"),
    # exactitud: el hueco o el porcentaje tienen que estar en una linea que diga
    # "base"; un porcentaje cualquiera (la meta, por ejemplo) no alcanza
    ("Exactitud de stock",
     r"\bbase\b[^\n]*?(?:primer conteo|conteo inicial|" + NOSOL + r"\d+(?:[.,]\d+)?\s*%)",
     "el primer conteo o un porcentaje en la línea de la base"),
    ("Días con producción cargada", NOSOL + r"20\s*%", "20 %"),
    ("Horas extras", NOSOL + r"25\s*(?:horas|hs|h)\b", "~25 horas"),
]

NUM = r"\d+(?:[.,]\d+)?"
RE_CIFRA = re.compile(
    r"(?<![\w.,])(%s)(?:\s*(?:–|-|a|y)\s*(%s))?\s*"
    r"(%%|horas?\b|hs\b|h\b|mes(?:es)?\b|semanas?\b)" % (NUM, NUM),
    re.IGNORECASE)
RE_PENDIENTE = re.compile(r"\[dato pendiente[^\]]*(?:\]|$)", re.IGNORECASE)


# --- utilidades -------------------------------------------------------------

def nfc(texto):
    return unicodedata.normalize("NFC", texto)


def leer(ruta):
    """Lineas del archivo, normalizadas (NFC), sin el salto de linea."""
    with open(ruta, encoding="utf-8") as fh:
        return [nfc(l) for l in fh.read().splitlines()]


def buscar_encabezado(lineas, titulo):
    """Indice (desde 0) de la linea '## titulo' exacta, o None."""
    for i, ln in enumerate(lineas):
        if ln.rstrip() == "## " + titulo:
            return i
    return None


def seccion(lineas, titulo):
    """(indice de inicio, lineas) del cuerpo de '## titulo' hasta el proximo ##."""
    ini = buscar_encabezado(lineas, titulo)
    if ini is None:
        return None, []
    fin = len(lineas)
    for j in range(ini + 1, len(lineas)):
        if lineas[j].startswith("## "):
            fin = j
            break
    return ini + 1, lineas[ini + 1:fin]


def parrafos(lineas):
    """Parrafos separados por lineas en blanco: (linea de inicio desde 1, texto)."""
    res, actual, ini = [], [], 0
    for i, ln in enumerate(lineas, 1):
        if ln.strip():
            if not actual:
                ini = i
            actual.append(ln)
        elif actual:
            res.append((ini, "\n".join(actual)))
            actual = []
    if actual:
        res.append((ini, "\n".join(actual)))
    return res


# --- reglas: cada una devuelve una lista de (linea, mensaje) -----------------

def regla_problema(lineas):
    ini = buscar_encabezado(lineas, "Problema gerencial")
    if ini is None:
        return [(1, "no encuentro '## Problema gerencial'")]
    bloque, primera = [], None
    for j in range(ini + 1, len(lineas)):
        ln = lineas[j]
        if ln.startswith("## "):
            break
        if ln.lstrip().startswith(">"):
            if primera is None:
                primera = j + 1
            bloque.append((j + 1, ln.lstrip()[1:]))
        elif bloque:
            break  # termino el primer bloque citado
    if not bloque:
        return [(ini + 1, "no hay bloque citado ('> ...') bajo '## Problema gerencial'")]
    fallas = []
    palabras = sum(len(t.split()) for _, t in bloque)
    if palabras > MAX_PALABRAS_PROBLEMA:
        fallas.append((primera, "el problema tiene %d palabras (máximo %d)"
                       % (palabras, MAX_PALABRAS_PROBLEMA)))
    for nro, texto in bloque:
        for m in PROHIBIDAS.finditer(texto):
            fallas.append((nro, "el problema nombra una herramienta: '%s'"
                           % m.group(1)))
    return fallas


DELATORES = [
    (re.compile(r"\bclases?\s+(?:\d|del\b)|\ben\s+(?:la\s+)?clase\b", re.I), "nombra una clase"),
    (re.compile(r"transcripci", re.I), "nombra transcripciones"),
    (re.compile(r"c[áa]tedra", re.I), "nombra la cátedra"),
    (re.compile(r"gu[íi]a\s+(?:de\s+)?ejemplo|\bla\s+gu[íi]a\b", re.I), "nombra la guía"),
    (re.compile(r"\b(?:enunciado|consigna)\b", re.I), "nombra la consigna"),
    (re.compile(r"\b(?:profes?|profesor(?:es|a|as)?|docentes?)\b", re.I), "nombra a los docentes"),
    (re.compile(r"\[dato pendiente", re.I), "hueco [dato pendiente]"),
    (re.compile(r"\bcorrig|\bcorrige|correcci[óo]n|equivocad|sobreestimad", re.I), "cuenta algo como corrección o error"),
]


def regla_delatores(lineas):
    fallas = []
    for nro, ln in enumerate(lineas, 1):
        for patron, msg in DELATORES:
            m = patron.search(ln)
            if m:
                fallas.append((nro, "%s: '%s'" % (msg, m.group(0))))
    return fallas


def regla_cifras(lineas):
    """Advertencias: porcentajes, horas, meses y semanas fuera de la lista blanca."""
    avisos = []
    for nro, ln in enumerate(lineas, 1):
        for m in RE_CIFRA.finditer(ln):
            unidad = m.group(3).lower()
            if unidad.startswith("mes"):
                permitidos = DURACIONES_OK["meses"]
            elif unidad.startswith("semana"):
                permitidos = DURACIONES_OK["semanas"]
            else:
                permitidos = CIFRAS_OK
            for num in (m.group(1), m.group(2)):
                if num and num not in permitidos:
                    avisos.append((nro, "advertencia: '%s' no está en la lista "
                                   "blanca; confirmar que viene del diseño §9 o de "
                                   "una cuenta declarada" % m.group(0).strip()))
                    break
    return avisos


def regla_encabezados(lineas, nombre):
    fallas = []
    for titulo in ENCABEZADOS.get(nombre, []):
        if buscar_encabezado(lineas, titulo) is None:
            fallas.append((1, "falta el encabezado '## %s'" % titulo))
    return fallas


def pendientes(lineas):
    """Lista de (linea, texto del hueco) con cada '[dato pendiente...]'."""
    res = []
    for nro, ln in enumerate(lineas, 1):
        for m in RE_PENDIENTE.finditer(ln):
            res.append((nro, m.group(0)))
    return res


def trazas_lanes(lineas, carpeta):
    """02: cada lane de bpmn/as-is.py tiene que figurar en '## RECI'."""
    ruta = os.path.join(carpeta, "bpmn", "as-is.py")
    if not os.path.isfile(ruta):
        return []  # todavia no existe: se saltea
    try:
        spec = importlib.util.spec_from_file_location("as_is_spec", ruta)
        modulo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(modulo)
        lanes = [nfc(l["nombre"]) for p in modulo.PROCESO["pools"]
                 for l in p.get("lanes", [])]
    except Exception as e:  # el spec esta roto: se avisa en vez de caerse
        return [(1, "no pude leer las lanes de bpmn/as-is.py: %s: %s"
                 % (type(e).__name__, e))]
    ini, cuerpo = seccion(lineas, "RECI")
    if ini is None:
        return [(1, "no hay '## RECI' contra el cual comparar las lanes de as-is.py")]
    reci = "\n".join(cuerpo)
    return [(ini, "la lane '%s' de bpmn/as-is.py no aparece en el RECI" % lane)
            for lane in dict.fromkeys(lanes) if lane not in reci]


def trazas_indicadores(lineas):
    """08: cada indicador aparece con su linea de base, dentro de '## Indicadores'."""
    ini, cuerpo = seccion(lineas, "Indicadores")
    if ini is None:
        return [(1, "no hay '## Indicadores' para trazar las líneas de base")]
    # bloques: la seccion partida en cada subtitulo (###); sin subtitulos, uno solo
    bloques, actual = [], []
    for ln in cuerpo:
        if re.match(r"#{3,}\s", ln) and actual:
            bloques.append(actual)
            actual = []
        actual.append(ln)
    bloques.append(actual)
    fallas = []
    for nombre, patron, base in INDICADORES:
        clave = nombre.lower()
        # La ficha del indicador es el bloque que lo titula (###). Los demas lo
        # nombran (contrapesos, tablero, fuentes) y traen cifras ajenas: no
        # cuentan. Sin subtitulos se busca el nombre en cualquier bloque.
        propios = [b for b in bloques
                   if b and re.match(r"#{3,}\s", b[0]) and clave in b[0].lower()]
        con_nombre = propios or [b for b in bloques
                                 if clave in "\n".join(b).lower()]
        if not con_nombre:
            fallas.append((ini, "falta el indicador '%s'" % nombre))
        elif not any(re.search(patron, "\n".join(b), re.IGNORECASE) for b in con_nombre):
            fallas.append((ini, "el indicador '%s' no trae su línea de base (%s)"
                           % (nombre, base)))
    return fallas


# --- armado y salida --------------------------------------------------------

def revisar(ruta):
    """Corre las reglas sobre un archivo: (fallas, avisos, huecos)."""
    nombre = nfc(os.path.basename(ruta))
    carpeta = os.path.dirname(os.path.abspath(ruta))
    lineas = leer(ruta)
    fallas = []  # (linea, regla, mensaje)

    def anotar(regla, resultado):
        fallas.extend((nro, regla, msg) for nro, msg in resultado)

    if nombre == ARCHIVO_PROBLEMA:
        anotar("problema", regla_problema(lineas))
    anotar("delatores", regla_delatores(lineas))
    anotar("encabezados", regla_encabezados(lineas, nombre))
    if nombre == ARCHIVO_PROCESO:
        anotar("trazas", trazas_lanes(lineas, carpeta))
    if nombre == ARCHIVO_ROADMAP:
        anotar("trazas", trazas_indicadores(lineas))
    avisos = [(nro, "cifras", msg) for nro, msg in regla_cifras(lineas)]
    huecos = [(nro, "pendientes", txt) for nro, txt in pendientes(lineas)]
    return fallas, avisos, huecos


def archivos_por_defecto():
    pats = glob.glob(os.path.join(BASE, "[0-9][0-9] - *.md"))
    return sorted(p for p in pats
                  if not nfc(os.path.basename(p)).startswith("00 - "))


def main(argv):
    rutas = argv or archivos_por_defecto()
    hubo_fallas = False
    for ruta in rutas:
        if not os.path.isfile(ruta):
            print("%s:0 archivo no existe" % ruta)
            hubo_fallas = True
            continue
        fallas, avisos, huecos = revisar(ruta)
        for nro, regla, msg in fallas:
            print("%s:%d %s %s" % (ruta, nro, regla, msg))
            hubo_fallas = True
        for nro, regla, msg in avisos + huecos:
            print("%s:%d %s %s" % (ruta, nro, regla, msg), file=sys.stderr)
        if huecos:
            print("%s pendientes: %d" % (ruta, len(huecos)), file=sys.stderr)
    if not hubo_fallas:
        print("OK")
    return 1 if hubo_fallas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
