#!/usr/bin/env python3
"""
Sincronizador del campus (Moodle FRSR-UTN) para la materia Ingenieria y Calidad de Software.

Uso:
    python3 sync.py                 # sincroniza y regenera ESTADO.md
    python3 sync.py --descargar     # ademas baja los archivos nuevos a ../Material Campus/
    python3 sync.py --login         # pide usuario/clave y renueva el token
    python3 sync.py --curso 1503    # sincroniza otra materia (ver config.json)

No guarda la contrasena: solo el token de web service en .secrets/wstoken.
"""

import argparse
import getpass
import json
import os
import re
import html
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta

import texto as mod_texto

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
SECRETS_DIR = os.path.join(BASE_DIR, ".secrets")
TOKEN_PATH = os.path.join(SECRETS_DIR, "wstoken")
DATA_DIR = os.path.join(BASE_DIR, "data")
MATERIA_DIR = os.path.dirname(BASE_DIR)
DESCARGAS_DIR = os.path.join(MATERIA_DIR, "Material Campus")


# ---------------------------------------------------------------- utilidades

def cargar_config():
    with open(CONFIG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def leer_token():
    if os.environ.get("MOODLE_WSTOKEN"):
        return os.environ["MOODLE_WSTOKEN"].strip()
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, encoding="utf-8") as fh:
            return fh.read().strip()
    return None


def guardar_token(token):
    os.makedirs(SECRETS_DIR, exist_ok=True)
    with open(TOKEN_PATH, "w", encoding="utf-8") as fh:
        fh.write(token + "\n")
    os.chmod(TOKEN_PATH, 0o600)


def post(url, params):
    datos = urllib.parse.urlencode(params, doseq=True).encode()
    req = urllib.request.Request(url, data=datos)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def login(cfg, usuario=None, clave=None):
    usuario = usuario or input("Usuario (legajo): ").strip()
    clave = clave or getpass.getpass("Contrasena: ")
    resp = post(cfg["moodle_url"] + "/login/token.php", {
        "username": usuario,
        "password": clave,
        "service": "moodle_mobile_app",
    })
    if "token" not in resp:
        sys.exit("No se pudo obtener el token: " + resp.get("error", str(resp)))
    guardar_token(resp["token"])
    print("Token guardado en .secrets/wstoken")
    return resp["token"]


def ws(cfg, token, funcion, **params):
    params.update({
        "wstoken": token,
        "moodlewsrestformat": "json",
        "wsfunction": funcion,
    })
    resp = post(cfg["moodle_url"] + "/webservice/rest/server.php", params)
    if isinstance(resp, dict) and resp.get("exception"):
        raise RuntimeError(f"{funcion}: {resp.get('errorcode')} - {resp.get('message')}")
    return resp


def limpiar(texto):
    texto = re.sub(r"<br\s*/?>|</p>|</li>", "\n", texto or "")
    texto = re.sub(r"<[^>]+>", " ", texto)
    texto = html.unescape(texto)
    texto = re.sub(r"[ \t]+", " ", texto)
    return re.sub(r"\n{3,}", "\n\n", texto).strip()


def fecha(ts):
    return datetime.fromtimestamp(ts) if ts else None


def fmt(ts):
    f = fecha(ts)
    return f.strftime("%Y-%m-%d %H:%M") if f else "-"


# ------------------------------------------------------------ recoleccion

def recolectar(cfg, token, courseid):
    info = ws(cfg, token, "core_webservice_get_site_info")
    userid = info["userid"]

    secciones = ws(cfg, token, "core_course_get_contents", courseid=courseid)

    tareas = []
    resp = ws(cfg, token, "mod_assign_get_assignments", **{"courseids[0]": courseid})
    for curso in resp.get("courses", []):
        for a in curso.get("assignments", []):
            estado = ws(cfg, token, "mod_assign_get_submission_status", assignid=a["id"])
            tareas.append({"assign": a, "estado": estado})

    avisos = []
    for sec in secciones:
        for mod in sec.get("modules", []):
            if mod["modname"] == "forum" and mod.get("instance"):
                try:
                    disc = ws(cfg, token, "mod_forum_get_forum_discussions",
                              forumid=mod["instance"], perpage=15)
                    for d in disc.get("discussions", []):
                        avisos.append({
                            "foro": mod["name"],
                            "asunto": d.get("subject"),
                            "fecha": d.get("timemodified") or d.get("created"),
                            "autor": d.get("userfullname"),
                            "mensaje": limpiar(d.get("message")),
                        })
                except RuntimeError:
                    pass

    notas = []
    try:
        gr = ws(cfg, token, "gradereport_user_get_grade_items",
                courseid=courseid, userid=userid)
        for u in gr.get("usergrades", []):
            for it in u.get("gradeitems", []):
                if it.get("graderaw") is not None or it.get("gradeformatted") not in (None, "-"):
                    nombre = it.get("itemname")
                    if not nombre:
                        nombre = "Total del curso" if it.get("itemtype") == "course" else "(sin nombre)"
                    notas.append({
                        "item": nombre,
                        "nota": limpiar(it.get("gradeformatted")),
                        "sobre": it.get("grademax"),
                    })
    except RuntimeError:
        pass

    return {
        "sincronizado": datetime.now().isoformat(timespec="seconds"),
        "courseid": courseid,
        "userid": userid,
        "usuario": info.get("fullname"),
        "secciones": secciones,
        "tareas": tareas,
        "avisos": avisos,
        "notas": notas,
    }


# ------------------------------------------------------------ comparacion

def indexar_modulos(snap):
    idx = {}
    for sec in snap.get("secciones", []):
        for mod in sec.get("modules", []):
            idx[mod["id"]] = {
                "seccion": sec["name"],
                "nombre": mod["name"],
                "tipo": mod["modname"],
                "url": mod.get("url"),
            }
    return idx


def novedades(anterior, actual):
    if not anterior:
        return [], []
    viejo, nuevo = indexar_modulos(anterior), indexar_modulos(actual)
    agregados = [v for k, v in nuevo.items() if k not in viejo]

    def clave_tarea(t):
        return (t["assign"]["id"], t["assign"].get("duedate"), t["assign"].get("timemodified"))

    prev = {t["assign"]["id"]: clave_tarea(t) for t in anterior.get("tareas", [])}
    cambios = []
    for t in actual.get("tareas", []):
        aid = t["assign"]["id"]
        if aid in prev and prev[aid] != clave_tarea(t):
            cambios.append(t["assign"]["name"])
    return agregados, cambios


# ------------------------------------------------------------ reporte

def estado_tarea(t):
    ult = t["estado"].get("lastattempt") or {}
    envio = ult.get("submission") or ult.get("teamsubmission") or {}
    return envio.get("status", "sin datos"), ult.get("gradingstatus")


def archivos_entregados(t):
    ult = t["estado"].get("lastattempt") or {}
    envio = ult.get("submission") or ult.get("teamsubmission") or {}
    salida = []
    for p in envio.get("plugins", []) or []:
        for fa in p.get("fileareas", []) or []:
            for f in fa.get("files", []) or []:
                salida.append(f["filename"])
    return salida


def generar_estado(snap, agregados, cambios, ruta, nombre_curso):
    ahora = datetime.now()
    L = []
    L.append(f"# Estado del campus - {nombre_curso}")
    L.append("")
    L.append(f"_Generado por `sync.py` el {ahora:%Y-%m-%d %H:%M}. No editar a mano._")
    L.append("")
    L.append(f"Alumno: {snap.get('usuario')} | curso {snap['courseid']}")
    L.append("")

    if agregados or cambios:
        L.append("## NOVEDADES desde la ultima sincronizacion")
        L.append("")
        for a in agregados:
            L.append(f"- NUEVO ({a['tipo']}) **{a['nombre']}** - seccion _{a['seccion']}_")
        for c in cambios:
            L.append(f"- CAMBIO en la tarea **{c}** (fecha o consigna modificada)")
        L.append("")

    pendientes, entregadas = [], []
    for t in snap["tareas"]:
        st, _ = estado_tarea(t)
        (entregadas if st == "submitted" else pendientes).append(t)

    L.append("## Trabajos practicos")
    L.append("")
    L.append("| TP | Cierre | Estado | Archivos entregados |")
    L.append("|---|---|---|---|")
    for t in sorted(snap["tareas"], key=lambda x: x["assign"].get("duedate") or 0):
        a = t["assign"]
        st, gs = estado_tarea(t)
        etiqueta = {"submitted": "ENTREGADO", "new": "SIN ENTREGAR",
                    "draft": "BORRADOR", "reopened": "REABIERTO"}.get(st, st)
        if st != "submitted" and a.get("duedate"):
            venc = fecha(a["duedate"])
            dias = (venc - ahora).days
            if venc < ahora:
                etiqueta += " (VENCIDO)"
            elif dias <= 3:
                etiqueta += f" (URGENTE, faltan {(venc - ahora).days}d {(venc - ahora).seconds // 3600}h)"
        if gs == "graded":
            etiqueta += " / corregido"
        arch = ", ".join(archivos_entregados(t)) or "-"
        L.append(f"| {a['name']} | {fmt(a.get('duedate'))} | {etiqueta} | {arch} |")
    L.append("")

    if pendientes:
        L.append("### Pendientes con detalle")
        L.append("")
        for t in sorted(pendientes, key=lambda x: x["assign"].get("duedate") or 0):
            a = t["assign"]
            L.append(f"#### {a['name']}")
            L.append(f"- Cierre: {fmt(a.get('duedate'))}")
            intro = limpiar(a.get("intro"))
            if intro:
                L.append(f"- Consigna: {intro[:800]}")
            for f in a.get("introattachments", []) or []:
                L.append(f"- Adjunto de la consigna: {f['filename']}")
            L.append("")

    if snap.get("notas"):
        L.append("## Notas cargadas")
        L.append("")
        for n in snap["notas"]:
            L.append(f"- {n['item']}: {n['nota']}")
        L.append("")

    L.append("## Contenido del curso")
    L.append("")
    for sec in snap["secciones"]:
        mods = sec.get("modules", [])
        if not mods and not limpiar(sec.get("summary")):
            continue
        L.append(f"### {sec['name']}")
        for m in mods:
            fechas = ""
            for d in m.get("dates", []) or []:
                fechas += f" [{d['label']} {fmt(d['timestamp'])}]"
            L.append(f"- ({m['modname']}) {m['name']}{fechas}")
        L.append("")

    if snap.get("avisos"):
        L.append("## Avisos recientes del foro")
        L.append("")
        for av in sorted(snap["avisos"], key=lambda x: x.get("fecha") or 0, reverse=True)[:10]:
            L.append(f"- **{av['asunto']}** ({fmt(av.get('fecha'))}, {av.get('autor')})")
            if av.get("mensaje"):
                L.append(f"  - {av['mensaje'][:300]}")
        L.append("")

    with open(ruta, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


# ------------------------------------------------------------ descargas

VIDEO_EXT = {".mp4", ".mov", ".avi", ".mkv", ".webm", ".m4v"}
CARPETA_FOROS = "Foros"


def nombre_seguro(texto):
    """Nombre de archivo o carpeta usable, conservando acentos."""
    limpio = re.sub(r'[/:*?"<>|]', "-", texto or "").strip()
    return re.sub(r"\s+", " ", limpio)


_CFG = None  # lo setea main(); carpeta_de_seccion lo necesita como callback


def carpeta_de_seccion(nombre):
    """Carpeta local para una seccion del campus.

    Manda la tabla `organizacion.secciones` de config.json. Sin regla:
    'Unidad N 1' -> 'Unidad 1', 'Clase 1' -> 'Clase 1', y el resto conserva su
    nombre. 'General' y las secciones vacias de Moodle ('Tema 7') caen en 'Catedra'.
    """
    nombre = (nombre or "").strip()
    reglas = (_CFG or {}).get("organizacion", {}).get("secciones", {})
    if nombre in reglas:
        return reglas[nombre]

    m = re.search(r"unidad\s*n?[\u00b0\u00ba]?\s*(\d+)", nombre, re.I)
    if m:
        return f"Unidad {int(m.group(1))}"
    m = re.match(r"clase\s*n?[\u00b0\u00ba]?\s*(\d+)$", nombre, re.I)
    if m:
        return f"Clase {int(m.group(1))}"
    if not nombre or re.match(r"(general|tema\s*\d+)$", nombre, re.I):
        return "C\u00e1tedra"
    return nombre_seguro(nombre)


def ubicar(cfg, seccion, mod_nombre, filename):
    """Devuelve (subcarpeta, nombre) dentro de Material Campus/ para un archivo del campus.

    Primero manda la tabla explicita de config.json; si no esta, se ubica por la seccion.
    """
    reglas = cfg.get("organizacion", {}).get("archivos", {})
    if filename in reglas:
        carpeta, nombre = os.path.split(reglas[filename])
        return carpeta or ".", nombre

    if re.search(r"bibliograf", mod_nombre or "", re.I):
        carpeta = "Bibliograf\u00eda"
    else:
        carpeta = carpeta_de_seccion(seccion)

    nombre = nombre_seguro(filename)
    if os.path.splitext(nombre)[1].lower() in VIDEO_EXT and not nombre.startswith("Video - "):
        nombre = "Video - " + nombre
    return carpeta, nombre


def descargar(cfg, token, snap):
    os.makedirs(DESCARGAS_DIR, exist_ok=True)
    pendientes = []

    for sec in snap["secciones"]:
        for mod in sec.get("modules", []):
            for c in mod.get("contents", []) or []:
                if c.get("type") == "file" and c.get("fileurl"):
                    carpeta, nombre = ubicar(cfg, sec["name"], mod["name"], c["filename"])
                    pendientes.append((carpeta, nombre, c["fileurl"]))

    for t in snap["tareas"]:
        for f in t["assign"].get("introattachments", []) or []:
            carpeta, nombre = ubicar(cfg, "", t["assign"]["name"], f["filename"])
            pendientes.append((carpeta, nombre, f["fileurl"]))

    bajados = []
    for carpeta, nombre, url in pendientes:
        destino_dir = os.path.join(DESCARGAS_DIR, carpeta)
        os.makedirs(destino_dir, exist_ok=True)
        destino = os.path.join(destino_dir, nombre)
        if os.path.exists(destino):
            continue
        sep = "&" if "?" in url else "?"
        try:
            with urllib.request.urlopen(url + sep + "token=" + token, timeout=120) as r:
                contenido = r.read()
            with open(destino, "wb") as fh:
                fh.write(contenido)
            bajados.append(os.path.relpath(destino, MATERIA_DIR))
        except Exception as exc:  # noqa: BLE001
            print(f"  no se pudo bajar {nombre}: {exc}")
    return bajados


def exportar_foros(cfg, token, snap):
    """Un .md por foro en Material Campus/Foros/, con cada hilo y sus respuestas.

    Los foros no se pueden "bajar" como archivo: esto los vuelca a texto para que
    queden junto al resto del material y se puedan buscar con grep.
    """
    foros = [m for sec in snap["secciones"] for m in sec.get("modules", [])
             if m["modname"] == "forum" and m.get("instance")]
    if not foros:
        return []

    destino_dir = os.path.join(DESCARGAS_DIR, CARPETA_FOROS)
    os.makedirs(destino_dir, exist_ok=True)
    escritos = []

    for foro in foros:
        try:
            disc = ws(cfg, token, "mod_forum_get_forum_discussions",
                      forumid=foro["instance"], perpage=100)
        except RuntimeError as exc:
            print(f"  no se pudo leer el foro {foro['name']}: {exc}")
            continue

        hilos = sorted(disc.get("discussions", []),
                       key=lambda d: d.get("created") or 0, reverse=True)
        L = [f"# Foro: {foro['name']}", ""]
        L.append(f"_Volcado por `sincronizacion-campus/sync.py` el {datetime.now():%Y-%m-%d %H:%M}. "
                 "No editar a mano._")
        L.append("")
        L.append(f"En el campus: {foro.get('url')}")
        L.append("")
        L.append(f"{len(hilos)} hilo(s), del mas nuevo al mas viejo.")
        L.append("")

        for d in hilos:
            did = d.get("discussion") or d.get("id")
            L.append("---")
            L.append("")
            L.append(f"## {d.get('subject')}")
            L.append("")
            L.append(f"_{d.get('userfullname')} - {fmt(d.get('created') or d.get('timemodified'))}_")
            L.append("")
            try:
                posts = ws(cfg, token, "mod_forum_get_discussion_posts", discussionid=did)
                mensajes = sorted(posts.get("posts", []), key=lambda x: x.get("timecreated") or 0)
            except RuntimeError:
                mensajes = [{"message": d.get("message"), "timecreated": d.get("created"),
                             "author": {"fullname": d.get("userfullname")}, "hasparent": False}]
            for i, m in enumerate(mensajes):
                autor = (m.get("author") or {}).get("fullname") or "(sin autor)"
                if i > 0 or m.get("hasparent"):
                    L.append(f"**Respuesta de {autor}** ({fmt(m.get('timecreated'))})")
                    L.append("")
                cuerpo = limpiar(m.get("message"))
                L.append(cuerpo if cuerpo else "_(sin texto)_")
                L.append("")

        destino = os.path.join(destino_dir, nombre_seguro(foro["name"]) + ".md")
        contenido = "\n".join(L)
        anterior = None
        if os.path.exists(destino):
            with open(destino, encoding="utf-8") as fh:
                anterior = fh.read()
        # la linea del "_Volcado ... _" cambia siempre: compara ignorandola
        def sin_fecha(t):
            return "\n".join(ln for ln in (t or "").splitlines() if not ln.startswith("_Volcado"))
        if sin_fecha(anterior) != sin_fecha(contenido):
            with open(destino, "w", encoding="utf-8") as fh:
                fh.write(contenido)
            escritos.append(os.path.relpath(destino, MATERIA_DIR))

    return escritos


def escribir_enlaces(snap):
    """Los modulos url (clases en Google Slides) quedan como .webloc en su unidad."""
    creados = []
    for sec in snap["secciones"]:
        carpeta = carpeta_de_seccion(sec["name"])
        for mod in sec.get("modules", []):
            if mod["modname"] != "url":
                continue
            url = next((c.get("fileurl") for c in mod.get("contents", []) or []
                        if c.get("fileurl")), None)
            if not url:
                continue
            destino_dir = os.path.join(DESCARGAS_DIR, carpeta)
            os.makedirs(destino_dir, exist_ok=True)
            destino = os.path.join(destino_dir, nombre_seguro(mod["name"]) + ".webloc")
            plist = (
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
                '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
                '<plist version="1.0">\n<dict>\n\t<key>URL</key>\n'
                f'\t<string>{html.escape(url)}</string>\n</dict>\n</plist>\n'
            )
            anterior = None
            if os.path.exists(destino):
                with open(destino, encoding="utf-8") as fh:
                    anterior = fh.read()
            if anterior != plist:
                with open(destino, "w", encoding="utf-8") as fh:
                    fh.write(plist)
                creados.append(os.path.relpath(destino, MATERIA_DIR))
    return creados


def urls_de_clases(snap):
    """{nombre del modulo url: su url} para poder citar la fuente en los .md."""
    urls = {}
    for sec in snap["secciones"]:
        for mod in sec.get("modules", []):
            if mod["modname"] == "url":
                url = next((c.get("fileurl") for c in mod.get("contents", []) or []
                            if c.get("fileurl")), None)
                if url:
                    urls[nombre_seguro(mod["name"])] = url
    return urls


def generar_indice_material(cfg, snap, nombre_curso):
    """Escribe Material Campus/00-INDICE.md a partir de lo que hay en el disco."""
    if not os.path.isdir(DESCARGAS_DIR):
        return

    # de que seccion del campus salio cada archivo, para poder citarlo en el indice
    origen = {}
    for sec in snap["secciones"]:
        for mod in sec.get("modules", []):
            for c in mod.get("contents", []) or []:
                if c.get("type") == "file" and c.get("fileurl"):
                    carpeta, nombre = ubicar(cfg, sec["name"], mod["name"], c["filename"])
                    origen[(carpeta, nombre)] = sec["name"]
            if mod["modname"] == "url":
                origen[(carpeta_de_seccion(sec["name"]),
                        nombre_seguro(mod["name"]) + ".webloc")] = sec["name"]

    L = [f"# Material del campus - {nombre_curso}", ""]
    L.append(f"_Generado por `sincronizacion-campus/sync.py` el {datetime.now():%Y-%m-%d %H:%M}. "
             "No editar a mano._")
    L.append("")
    L.append("Todo el material en texto (para leer o buscar rapido) esta en `00-TEXTO/`, "
             "un `.md` por cada PDF o apunte del campus. Ver `00-TEXTO/00-INDICE.md`.")
    L.append("")
    L.append("Reordenado para que sea mas simple que el campus: un solo nivel de carpetas. "
             "`C\u00e1tedra/` lo administrativo y los enlaces fijos, `Bibliograf\u00eda/` los libros, "
             "`Foros/` el contenido de los foros volcado a texto, y una carpeta por clase o "
             "unidad con todo lo de ese tema junto (apuntes, pr\u00e1cticas y videos con el "
             "prefijo `Video - `). Los `.webloc` abren el enlace original en el navegador.")
    L.append("")

    def orden(nombre):
        m = re.match(r"(?:Unidad|Clase) (\d+)$", nombre)
        if m:
            return (2, int(m.group(1)), nombre)
        fijas = {"C\u00e1tedra": 0, "Bibliograf\u00eda": 1, CARPETA_FOROS: 4}
        return (fijas.get(nombre, 3), 0, nombre)

    carpetas = sorted((d for d in os.listdir(DESCARGAS_DIR)
                       if os.path.isdir(os.path.join(DESCARGAS_DIR, d))
                       and d != mod_texto.CARPETA_TEXTO), key=orden)
    for carpeta in carpetas:
        archivos = sorted(a for a in os.listdir(os.path.join(DESCARGAS_DIR, carpeta))
                          if not a.startswith("."))
        if not archivos:
            continue
        L.append(f"## {carpeta}/")
        L.append("")
        for a in archivos:
            ruta = os.path.join(DESCARGAS_DIR, carpeta, a)
            mb = os.path.getsize(ruta) / (1024 * 1024)
            if a.endswith(".webloc"):
                with open(ruta, encoding="utf-8") as fh:
                    url = re.search(r"<string>(.*?)</string>", fh.read())
                detalle = html.unescape(url.group(1)) if url else "enlace"
                L.append(f"- **{a[:-7]}** (enlace) - {detalle}")
            else:
                proc = origen.get((carpeta, a))
                nota = f" - del campus en _{proc}_" if proc and proc != carpeta else ""
                L.append(f"- **{a}** ({mb:.1f} MB){nota}")
        L.append("")

    faltantes = [f"{m['name']} ({m['modname']})" for sec in snap["secciones"]
                 for m in sec.get("modules", [])
                 if m["modname"] in ("attendance", "quiz")]
    if faltantes:
        L.append("## Solo online (no se puede bajar)")
        L.append("")
        for f in faltantes:
            L.append(f"- {f}")
        L.append("")
        L.append("Las entregas y su estado estan en `sincronizacion-campus/ESTADO.md`.")
        L.append("")

    with open(os.path.join(DESCARGAS_DIR, "00-INDICE.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")


# ------------------------------------------------------------ main

def main():
    ap = argparse.ArgumentParser(description="Sincroniza el campus Moodle de la FRSR")
    ap.add_argument("--login", action="store_true", help="renovar el token")
    ap.add_argument("--usuario")
    ap.add_argument("--clave")
    ap.add_argument("--descargar", action="store_true", help="bajar archivos nuevos")
    ap.add_argument("--curso", type=int, help="id de curso (por defecto el de config.json)")
    args = ap.parse_args()

    global _CFG
    cfg = cargar_config()
    _CFG = cfg
    courseid = args.curso or cfg["courseid"]

    token = leer_token()
    if args.login or not token:
        token = login(cfg, args.usuario, args.clave)

    try:
        snap = recolectar(cfg, token, courseid)
    except RuntimeError as exc:
        if "invalidtoken" in str(exc) or "accessexception" in str(exc):
            print("Token invalido o vencido. Corre: python3 sync.py --login")
            sys.exit(1)
        raise

    os.makedirs(DATA_DIR, exist_ok=True)
    ruta_snap = os.path.join(DATA_DIR, f"snapshot-{courseid}.json")
    anterior = None
    if os.path.exists(ruta_snap):
        with open(ruta_snap, encoding="utf-8") as fh:
            anterior = json.load(fh)

    agregados, cambios = novedades(anterior, snap)

    with open(ruta_snap, "w", encoding="utf-8") as fh:
        json.dump(snap, fh, ensure_ascii=False, indent=1)

    nombre_estado = "ESTADO.md" if courseid == cfg["courseid"] else f"ESTADO-{courseid}.md"
    nombre_curso = (cfg["curso_nombre"] if courseid == cfg["courseid"]
                    else cfg.get("otros_cursos", {}).get(str(courseid), f"curso {courseid}"))
    generar_estado(snap, agregados, cambios, os.path.join(BASE_DIR, nombre_estado), nombre_curso)

    print(f"Sincronizado curso {courseid} -> {nombre_estado}")
    if agregados:
        print(f"  {len(agregados)} elemento(s) nuevo(s):")
        for a in agregados:
            print(f"    - ({a['tipo']}) {a['nombre']}  [{a['seccion']}]")
    if cambios:
        print(f"  {len(cambios)} tarea(s) modificada(s): {', '.join(cambios)}")
    if not anterior:
        print("  (primera sincronizacion: no hay con que comparar todavia)")
    elif not agregados and not cambios:
        print("  sin novedades")

    sin_entregar = [t["assign"]["name"] for t in snap["tareas"]
                    if estado_tarea(t)[0] != "submitted"]
    if sin_entregar:
        print("  SIN ENTREGAR: " + "; ".join(sin_entregar))

    if args.descargar:
        bajados = descargar(cfg, token, snap)
        enlaces = escribir_enlaces(snap)
        foros = exportar_foros(cfg, token, snap)
        print(f"  archivos bajados: {len(bajados)}")
        for b in bajados:
            print(f"    + {b}")
        if enlaces:
            print(f"  enlaces de clases actualizados: {len(enlaces)}")
            for e in enlaces:
                print(f"    ~ {e}")
        if foros:
            print(f"  foros volcados a texto: {len(foros)}")
            for f in foros:
                print(f"    ~ {f}")

        slides = mod_texto.exportar_slides(snap, DESCARGAS_DIR,
                                           carpeta_de_seccion, nombre_seguro)
        if slides:
            print(f"  clases exportadas de Google Slides: {len(slides)}")
            for sl in slides:
                print(f"    + {os.path.relpath(sl, MATERIA_DIR)}")

        textos = mod_texto.generar_textos(DESCARGAS_DIR, urls_de_clases(snap),
                                          cfg.get("limite_texto_mb"))
        if textos:
            print(f"  textos generados en 00-TEXTO/: {len(textos)}")
            for t in textos:
                print(f"    + {t}")

        generar_indice_material(cfg, snap, nombre_curso)


if __name__ == "__main__":
    main()
