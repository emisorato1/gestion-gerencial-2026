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
L = []
L.append("# Trabajo Práctico Final, Parte 1")
L.append("")
L.append("## Diagnóstico gerencial de Dulxelitos")
L.append("")
L.append("Gestión Gerencial. Quinto año de Ingeniería en Sistemas de Información.")
L.append("Universidad Tecnológica Nacional, Facultad Regional San Rafael. Plan 2026.")
L.append("Cátedra: Ing. Jeremías Pino e Ing. Martín Noguerol.")
L.append("")
L.append("**Organización analizada:** Dulxelitos, fabricación, fraccionamiento y "
         "distribución de snacks. San Rafael, Mendoza. Desde 1973.")
L.append("")
L.append("**Integrantes:** _(completar)_")
L.append("")
L.append("**Fecha:** %s" % hoy.strftime("%d/%m/%Y"))
L.append("")
L.append("---")
L.append("")
L.append("### Contenido")
L.append("")
L.append("1. La organización")
L.append("2. El contexto")
L.append("3. Modelo de negocio actual")
L.append("4. Propuesta de valor actual")
L.append("5. Madurez y capacidades")
L.append("")
L.append("La sección 6, el problema gerencial priorizado, no va en esta entrega: la "
         "presentamos aparte.")
L.append("")
L.append("### De dónde sale la información")
L.append("")
L.append("Uno de nosotros trabaja en Dulxelitos, así que buena parte de lo que dice este "
         "informe está confirmado adentro de la empresa. El resto lo sacamos de la página "
         "oficial, del Instagram, de listados de mayoristas de la zona y de la página de "
         "Aiello. Cuando un dato no lo pudimos conseguir lo decimos, en vez de estimarlo. "
         "En el punto 1.6 explicamos cómo tratamos de cuidarnos del sesgo que trae tener "
         "a alguien adentro.")
L.append("")
L.append("---")
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
L.append("## Anexo: fuentes y datos que no conseguimos")
L.append("")
L += renombrar(demote(fuentes), {"### Fuentes": "### Fuentes consultadas"})
L.append("")
L.append("### Lo que la empresa no mide")
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

md = re.sub(r"\n{4,}", "\n\n\n", "\n".join(L)).rstrip() + "\n"

os.makedirs(DEST, exist_ok=True)
ruta_md = os.path.join(DEST, NOMBRE + ".md")
with io.open(ruta_md, "w", encoding="utf-8") as fh:
    fh.write(md)
print("%s.md  (%d lineas, ~%d palabras)" % (NOMBRE, md.count("\n") + 1, len(md.split())))

CSS = """
@page { size: A4; margin: 2.2cm 2cm; @bottom-center {
  content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #666; } }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt;
  line-height: 1.5; color: #1a1a1a; }
h1 { font-size: 20pt; margin: 0 0 .2em; line-height: 1.2; }
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

if shutil.which("pandoc"):
    corre(["pandoc", ruta_md, "-o", os.path.join(DEST, NOMBRE + ".docx"),
           "--from", "markdown", "--toc", "--toc-depth=2"], "docx")
    html = os.path.join(DEST, "_tmp.html")
    css = os.path.join(DEST, "_tmp.css")
    io.open(css, "w", encoding="utf-8").write(CSS)
    if corre(["pandoc", ruta_md, "-o", html, "--standalone", "--css", "_tmp.css",
              "--metadata", "title=" + NOMBRE], "html intermedio"):
        # pandoc agrega su propio bloque de titulo ademas del H1 del documento:
        # queda duplicado en la portada del pdf, asi que lo sacamos.
        h = io.open(html, encoding="utf-8").read()
        h = re.sub(r'<header id="title-block-header">.*?</header>', "", h, flags=re.S)
        io.open(html, "w", encoding="utf-8").write(h)
        if shutil.which("weasyprint"):
            corre(["weasyprint", html, os.path.join(DEST, NOMBRE + ".pdf")], "pdf")
        else:
            print("  falta weasyprint, no se genero el pdf")
    for t in (html, css):
        if os.path.exists(t):
            os.remove(t)
else:
    print("  falta pandoc: solo se genero el .md")
