"""Material del campus en texto, para poder leerlo o buscarlo rapido.

Dos cosas que sync.py no hace por si solo:

1. Las clases del campus son enlaces a Google Slides. Se exportan a PDF y quedan
   al lado del .webloc, en la carpeta de su unidad.
2. De cada PDF se extrae el texto a Markdown, todo junto en Material Campus/00-TEXTO/,
   con nombres planos del estilo "Unidad 2 - Clase 04.md".

El texto se extrae con `pdftotext` (viene con poppler). Si no esta instalado, se avisa
y se sigue sin generar los .md.
"""

import os
import re
import shutil
import subprocess
import urllib.request
from datetime import datetime

CARPETA_TEXTO = "00-TEXTO"
CARPETA_FOROS = "Foros"  # ya es texto: no se vuelve a copiar
EXT_TEXTO = {".md", ".txt"}
MB = 1024 * 1024
LIMITE_TEXTO_MB = 20.0  # por encima de esto no se pasa a texto (son los libros);
                        # se puede cambiar con "limite_texto_mb" en config.json


def hay_pdftotext():
    return shutil.which("pdftotext") is not None


def id_google(url):
    """Saca el id de un documento de Google de su url, o None si no es de Google."""
    m = re.search(r"docs\.google\.com/(presentation|document)/d/([\w-]+)", url or "")
    return (m.group(1), m.group(2)) if m else None


def exportar_slides(snap, destino_base, carpeta_de_seccion, nombre_seguro):
    """Baja como PDF las clases que en el campus son enlaces a Google Slides/Docs."""
    bajados = []
    for sec in snap["secciones"]:
        carpeta = carpeta_de_seccion(sec["name"])
        for mod in sec.get("modules", []):
            if mod["modname"] != "url":
                continue
            url = next((c.get("fileurl") for c in mod.get("contents", []) or []
                        if c.get("fileurl")), None)
            ident = id_google(url) if url else None
            if not ident:
                continue
            tipo, doc_id = ident
            destino_dir = os.path.join(destino_base, carpeta)
            os.makedirs(destino_dir, exist_ok=True)
            destino = os.path.join(destino_dir, nombre_seguro(mod["name"]) + ".pdf")
            if os.path.exists(destino):
                continue
            export = f"https://docs.google.com/{tipo}/d/{doc_id}/export/pdf"
            try:
                with urllib.request.urlopen(export, timeout=120) as r:
                    contenido = r.read()
                if not contenido.startswith(b"%PDF"):
                    print(f"  {mod['name']}: la exportacion no es un PDF "
                          "(quizas el enlace no es publico)")
                    continue
                with open(destino, "wb") as fh:
                    fh.write(contenido)
                bajados.append(destino)
            except Exception as exc:  # noqa: BLE001
                print(f"  no se pudo exportar {mod['name']}: {exc}")
    return bajados


def texto_de_pdf(ruta):
    salida = subprocess.run(["pdftotext", "-layout", ruta, "-"],
                            capture_output=True, text=True, timeout=180)
    if salida.returncode != 0:
        return None
    lineas = [ln.rstrip() for ln in salida.stdout.splitlines()]
    # colapsa las corridas de lineas vacias que deja el layout de las slides
    limpio, vacias = [], 0
    for ln in lineas:
        if ln:
            limpio.append(ln)
            vacias = 0
        else:
            vacias += 1
            if vacias == 1:
                limpio.append("")
    return "\n".join(limpio).strip()


def paginas_de_pdf(ruta):
    if not shutil.which("pdfinfo"):
        return None
    salida = subprocess.run(["pdfinfo", ruta], capture_output=True, text=True)
    m = re.search(r"^Pages:\s+(\d+)", salida.stdout, re.M)
    return int(m.group(1)) if m else None


def generar_textos(destino_base, url_por_nombre=None, limite_mb=None):
    """Pasa a Markdown cada PDF de Material Campus/ dentro de 00-TEXTO/."""
    if not hay_pdftotext():
        print("  aviso: falta `pdftotext` (brew install poppler); no se genero 00-TEXTO/")
        return []

    url_por_nombre = url_por_nombre or {}
    limite_mb = LIMITE_TEXTO_MB if limite_mb is None else float(limite_mb)
    dir_texto = os.path.join(destino_base, CARPETA_TEXTO)
    os.makedirs(dir_texto, exist_ok=True)
    generados, salteados = [], []

    for carpeta in sorted(os.listdir(destino_base)):
        ruta_carpeta = os.path.join(destino_base, carpeta)
        if not os.path.isdir(ruta_carpeta) or carpeta in (CARPETA_TEXTO, CARPETA_FOROS):
            continue
        for archivo in sorted(os.listdir(ruta_carpeta)):
            ext = os.path.splitext(archivo)[1].lower()
            if ext != ".pdf" and ext not in EXT_TEXTO:
                continue
            origen = os.path.join(ruta_carpeta, archivo)
            tamano = os.path.getsize(origen) / MB
            base = os.path.splitext(archivo)[0]
            destino = os.path.join(dir_texto, f"{carpeta} - {base}.md")
            if os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(origen):
                continue

            paginas = None
            if ext == ".pdf":
                if tamano > limite_mb:
                    salteados.append(f"{carpeta}/{archivo} ({tamano:.1f} MB)")
                    continue
                cuerpo = texto_de_pdf(origen)
                origen_desc = "Texto extraido de"
                paginas = paginas_de_pdf(origen)
            else:
                # los apuntes que el campus publica ya en .md/.txt: se copian tal cual
                with open(origen, encoding="utf-8", errors="replace") as fh:
                    cuerpo = fh.read().strip()
                origen_desc = "Copia de"

            if not cuerpo:
                salteados.append(f"{carpeta}/{archivo} (sin texto extraible)")
                continue
            enc = [f"# {base}", ""]
            enc.append(f"> {origen_desc} `{carpeta}/{archivo}`"
                       + (f", {paginas} paginas" if paginas else "")
                       + f". Generado el {datetime.now():%Y-%m-%d %H:%M} por "
                       "`sincronizacion-campus`. No editar a mano.")
            if base in url_por_nombre:
                enc.append(">")
                enc.append(f"> Original en el campus: {url_por_nombre[base]}")
            enc += ["", "---", "", cuerpo, ""]
            with open(destino, "w", encoding="utf-8") as fh:
                fh.write("\n".join(enc))
            generados.append(os.path.relpath(destino, destino_base))

    indice = [f"# Material del campus en texto", ""]
    indice.append(f"_Generado por `sincronizacion-campus/sync.py` el "
                  f"{datetime.now():%Y-%m-%d %H:%M}. No editar a mano._")
    indice.append("")
    indice.append("Un `.md` por cada PDF o apunte de `Material Campus/`. Sirve para leer o "
                  "buscar el material sin abrir los PDF: "
                  "`grep -ri \"modelo de madurez\" \"Material Campus/00-TEXTO\"`. "
                  "Los foros estan aparte, en `Material Campus/Foros/`.")
    indice.append("")
    archivos_md = sorted(a for a in os.listdir(dir_texto)
                         if a.endswith(".md") and a != "00-INDICE.md")
    for a in archivos_md:
        lineas = sum(1 for _ in open(os.path.join(dir_texto, a), encoding="utf-8"))
        indice.append(f"- `{a}` ({lineas} lineas)")
    if salteados:
        indice += ["", "## Sin version en texto", ""]
        indice.append(f"Los PDF de mas de {limite_mb:g} MB no se convierten "
                      "(son los libros: conviene leerlos directo, por capitulo).")
        indice.append("")
        for s in sorted(set(salteados)):
            indice.append(f"- {s}")
    indice.append("")
    with open(os.path.join(dir_texto, "00-INDICE.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(indice))

    return generados
