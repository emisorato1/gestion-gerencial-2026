#!/usr/bin/env python3
"""Arma la carpeta de entrega de la Parte 2 a partir de las secciones sueltas.

    nice -n 10 .venv/bin/python armar-entrega.py

Escribe en Entrega/ el md, el docx y el pdf. Las secciones sueltas (01 a 08)
son la fuente: si alguien toca una, hay que volver a correr esto. El archivo de
entrega no se edita a mano porque se pisa en la proxima corrida.

Es la misma idea que ../Proyecto/armar-entrega.py (Parte 1): caratula, indice,
introduccion, secciones, bibliografia y anexos; docx con estilos de Word y
pdf con weasyprint. Lo propio de la Parte 2:

  - las secciones traen sus propios titulos y se numeran por el prefijo del
    archivo (01 es el capitulo 1);
  - si falta una seccion se avisa y se la saltea;
  - los diagramas BPMN (bpmn/*.png) van solos en una hoja apaisada, tanto en
    el pdf (pagina con nombre) como en el docx (seccion de Word apaisada);
  - el anexo de datos pendientes sale de pendientes() de verificar.py.

Necesita pandoc (docx y html) y weasyprint (pdf). Si falta alguno, avisa y
sigue.
"""

import io, os, re, shutil, struct, subprocess, sys
from xml.sax.saxutils import escape

BASE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(BASE, "Entrega")
NOMBRE = "TP Final Parte 2 - Dulxelitos"

TITULO = "Trabajo Práctico Final - Parte 2"
SUBTITULO = "Propuesta de transformación de Dulxelitos"
INTEGRANTES = ("Lepez Joaquín - Geyer Juan José - Lopez Juan - "
               "Olivares Manuel - Sorato Emiliano")
DOCENTES = "Ing. Jeremías Pino - Ing. Martín Noguerol"

# Orden de las secciones. El numero del capitulo sale del prefijo del archivo.
SECCIONES = [
    "01 - Problema y objetivos.md",
    "02 - Proceso actual y alternativas.md",
    "03 - Proceso futuro.md",
    "04 - Modelo de negocio y propuesta de valor.md",
    "05 - Stakeholders.md",
    "06 - Arquitectura y datos.md",
    "07 - Validación de supuestos.md",
    "08 - Roadmap e indicadores.md",
]

sys.dont_write_bytecode = True
sys.path.insert(0, BASE)
import verificar  # noqa: E402  (pendientes() y nfc())

PB = "<!--PAGEBREAK-->"        # salto duro (caratula, indice)
PBH = "<!--PAGEBREAK-H-->"     # salto antes de un capitulo: en docx y pdf lo
                               # hace el estilo del titulo 1, en el md es un ---


# ----------------------------------------------------------------- utilidades

def aviso(txt):
    print("  AVISO: " + txt, file=sys.stderr)


def leer(nombre):
    with io.open(os.path.join(BASE, nombre), encoding="utf-8") as fh:
        return [verificar.nfc(l) for l in fh.read().split("\n")]


def encabezado(l):
    """(nivel, texto) si la linea es un titulo de markdown, o None."""
    m = re.match(r"^(#{1,6})\s+(.*?)\s*$", l)
    return (len(m.group(1)), m.group(2)) if m else None


def sin_fences(lineas):
    """Pares (linea, esta_en_codigo) para no tocar titulos dentro de ```."""
    en_codigo = False
    for l in lineas:
        if l.lstrip().startswith("```"):
            en_codigo = not en_codigo
            yield l, True
        else:
            yield l, en_codigo


def capitulo(n, lineas):
    """Pasa una seccion suelta a capitulo: '# N. Titulo' y '## N.k Punto'.

    El primer '#' de la seccion es el titulo del capitulo. Los '##' son los
    puntos y se numeran N.1, N.2... Los '###' y siguientes quedan como estan.
    """
    titulo, resto = None, []
    for i, l in enumerate(lineas):
        h = encabezado(l)
        if h and h[0] == 1:
            titulo, resto = h[1], lineas[i + 1:]
            break
    if titulo is None:
        raise SystemExit("la seccion %d no tiene un titulo '# ...'" % n)
    while resto and not resto[0].strip():
        resto = resto[1:]
    out = ["# %d. %s" % (n, titulo), ""]
    k = 0
    for l, codigo in sin_fences(resto):
        h = None if codigo else encabezado(l)
        if h and h[0] == 2:
            k += 1
            out.append("## %d.%d %s" % (n, k, h[1]))
        else:
            out.append(l)
    return titulo, out


def lista_dato(txt):
    """Texto del hueco: saca '[dato pendiente:' y el corchete de cierre."""
    t = re.sub(r"^\[dato pendiente\s*:?\s*", "", txt.strip(), flags=re.I)
    t = t.rstrip("]").strip().rstrip(".")
    t = re.sub(r"\s+", " ", t)
    return t[:1].upper() + t[1:] if t else t


def unir(nums):
    nums = [str(x) for x in nums]
    if len(nums) <= 1:
        return "".join(nums)
    return ", ".join(nums[:-1]) + " y " + nums[-1]


# --------------------------------------------------------------------- armado

hechos = []        # (numero, titulo del capitulo, lineas)
huecos = {}        # clave -> [texto, [capitulos]]
for nombre in SECCIONES:
    ruta = os.path.join(BASE, nombre)
    if not os.path.isfile(ruta):
        aviso("falta '%s': se saltea (el capitulo queda sin armar)" % nombre)
        continue
    n = int(nombre[:2])
    lineas = leer(nombre)
    titulo, cuerpo = capitulo(n, lineas)
    hechos.append((n, titulo, cuerpo))
    for _, txt in verificar.pendientes(lineas):
        dato = lista_dato(txt)
        reg = huecos.setdefault(dato.lower(), [dato, []])
        if n not in reg[1]:
            reg[1].append(n)


def fusionar(huecos):
    """Un dato escrito corto en una seccion y largo en otra es el mismo dato.

    Si el texto de uno (de al menos 12 letras) esta entero dentro del de otro,
    queda el mas largo con las secciones de los dos.
    """
    claves = sorted(huecos, key=len)
    for c in claves:
        for mayor in sorted(huecos, key=len):
            if mayor != c and len(c) >= 12 and c in mayor and c in huecos:
                for n in huecos[c][1]:
                    if n not in huecos[mayor][1]:
                        huecos[mayor][1].append(n)
                del huecos[c]
                break
    return huecos


huecos = fusionar(huecos)

NUM_BIBLIO = 9
NUM_ANEXOS = 10

L = []
L.append("<!--PORTADA-->")
L.append("")
L.append(PB)
L.append("")
L.append("<!--INDICE-->")
L.append("")
L.append(PB)
L.append("")

# ---------------------------------------------------------------- introduccion
L.append("# Introducción")
L.append("")
L.append("Este trabajo es la segunda parte del proyecto integrador de Gestión Gerencial. "
         "En la primera hicimos un diagnóstico gerencial de Dulxelitos, una empresa "
         "familiar de San Rafael que fabrica, fracciona y distribuye snacks desde 1973. "
         "En esta pasamos de diagnosticar a proponer: definimos el problema gerencial que "
         "la Parte 1 había dejado pendiente, mapeamos el proceso actual y el futuro, "
         "comparamos alternativas y armamos el plan para llevar la mejora a la práctica y "
         "medir si funciona.")
L.append("")
L.append("Seguimos sobre el mismo caso, pero al relevar de nuevo el proceso de atender un "
         "pedido con nuestro compañero que trabaja en la empresa encontramos que tres cosas "
         "de la Parte 1 estaban mal o incompletas: el stock de producto terminado no se "
         "registra en ningún lado, los pedidos recortados no son raros sino semanales, y "
         "esos recortes vienen de la mezcla y el momento de producción más que de la "
         "capacidad total de la planta. La corrección está al comienzo de la sección 1, y "
         "todo lo que sigue se apoya en la versión corregida.")
L.append("")
L.append("El documento va del problema a la forma de medirlo. La sección 1 plantea el "
         "problema, los objetivos y el alcance. La 2 describe el proceso actual y compara "
         "las alternativas hasta recomendar una, y la 3 muestra el proceso futuro. La 4 "
         "revisa el modelo de negocio y la propuesta de valor, la 5 mapea a las personas "
         "involucradas y la 6 define la arquitectura y los datos. La 7 explica cómo se "
         "validan los supuestos con un piloto, y la 8 cierra con el roadmap, el OKR y los "
         "indicadores. Lo que no sabemos queda marcado como «dato pendiente» y se junta "
         "en el Anexo I.")
L.append("")

# ------------------------------------------------------------------ capitulos
for n, titulo, cuerpo in hechos:
    L.append(PBH)
    L.append("")
    L += cuerpo
    L.append("")

# --------------------------------------------------------------- bibliografia
L.append(PBH)
L.append("")
L.append("# %d. Bibliografía" % NUM_BIBLIO)
L.append("")
L.append("**Herramientas de análisis**")
L.append("")
L.append("- Doerr, J. (2018). *Measure What Matters*. Portfolio / Penguin.")
L.append("- Freund, J. y Rücker, B. (2019). *Real-Life BPMN* (4.ª ed.). Camunda.")
L.append("- Heifetz, R. A. y Laurie, D. L. (1997). The work of leadership. *Harvard Business Review*, 75(1), 124-134.")
L.append("- Heifetz, R., Grashow, A. y Linsky, M. (2009). *The Practice of Adaptive Leadership*. Harvard Business Press.")
L.append("- Hiatt, J. M. (2006). *ADKAR: A Model for Change in Business, Government and Our Community*. Prosci.")
L.append("- Mendelow, A. L. (1981). Environmental scanning: the impact of the stakeholder concept. *Proceedings of the Second International Conference on Information Systems*, 407-418.")
L.append("- Osterwalder, A. y Pigneur, Y. (2010). *Business Model Generation*. John Wiley & Sons.")
L.append("- Osterwalder, A., Pigneur, Y., Bernarda, G. y Smith, A. (2014). *Value Proposition Design*. John Wiley & Sons.")
L.append("- Rogers, D. L. (2023). *davidrogers.digital* [sitio web]. Citado en la Clase 7.")
L.append("- Savoia, A. (2019). *The Right It*. HarperOne.")
L.append("")
L.append("**Material de cátedra (UTN FRSR)**")
L.append("")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 3: transformación digital, madurez y gestión bimodal.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 4: gestión del cambio y liderazgo adaptativo.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 5: medir la estrategia (objetivos, OKR, KPI y tablero).")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 6: modelado de procesos con BPMN.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase 7: de procesos a estrategia digital.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase del 05-10: línea de base y procesos balde.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase del 19-10: evaluación de tecnologías.")
L.append("- Cátedra de Gestión Gerencial (2026). Clase del 23-10: partes interesadas y roadmap.")
L.append("- Cátedra de Gestión Gerencial (2026). Trabajo Práctico Final, Parte 2: consigna y guía de ejemplo.")
L.append("")
L.append("**Fuentes primarias del caso**")
L.append("")
L.append("- Lepez, J., Geyer, J. J., Lopez, J. y Sorato, E. (2026). *Trabajo Práctico Final - Parte 1: diagnóstico gerencial de Dulxelitos*.")
L.append("- Relevamiento del proceso de atención de pedidos con un integrante del equipo que trabaja en Dulxelitos (2026), y entrevistas y observación directa del equipo en la organización (Parte 1).")
L.append("")

# --------------------------------------------------------------------- anexos
L.append(PBH)
L.append("")
L.append("# %d. Anexos" % NUM_ANEXOS)
L.append("")
L.append("## Anexo I: datos pendientes")
L.append("")
L.append("Lo dejamos escrito en vez de inventar una cifra. Cada uno de estos datos aparece "
         "en el texto marcado como «dato pendiente» y acá se juntan sin repetir los que "
         "figuran en más de una sección. Algunos salen del primer conteo físico, otros se "
         "le preguntan al proveedor o se sacan de la liquidación de sueldos de la empresa.")
L.append("")
if huecos:
    L.append("| Dato | Sección |")
    L.append("|------------------------------------------------------------|----------|")
    for dato, caps in huecos.values():
        L.append("| %s | %s |" % (dato.replace("|", "\\|"), unir(sorted(caps))))
else:
    L.append("No quedan datos pendientes.")
L.append("")

crudo = re.sub(r"\n{3,}", "\n\n", "\n".join(L)).rstrip() + "\n"

# --------------------------------------------------------------- caratula e indice

def portada_html():
    return "\n".join([
        '<div class="portada">', "",
        '<p class="p-titulo">%s</p>' % TITULO,
        '<p class="p-sub">%s</p>' % SUBTITULO,
        '<p class="p-materia">Gestión Gerencial</p>',
        '<p class="p-carrera">Ingeniería en Sistemas de Información</p>',
        '<p class="p-equipo">Integrantes: %s</p>' % INTEGRANTES.replace(" - ", ", "),
        '<p class="p-docente">Docentes: %s</p>' % DOCENTES.replace(" - ", ", "),
        "", "</div>"])


def portada_docx():
    """Cada linea con su estilo de Word (Title, Subtitle y los de la portada)."""
    def d(estilo, texto):
        return '::: {custom-style="%s"}\n%s\n:::\n' % (estilo, texto)
    return "\n".join([
        d("Title", TITULO),
        d("Subtitle", SUBTITULO),
        d("Portada Materia", "Gestión Gerencial"),
        d("Portada Carrera", "Ingeniería en Sistemas de Información"),
        d("Portada Equipo", "Integrantes: " + INTEGRANTES.replace(" - ", ", ")),
        d("Portada Docentes", "Docentes: " + DOCENTES.replace(" - ", ", ")),
    ])


def titulos_de(texto, hasta_nivel=2):
    """Titulos (nivel, texto) del cuerpo, sin tocar lo que esta dentro de ```."""
    res = []
    for l, codigo in sin_fences(texto.split("\n")):
        h = None if codigo else encabezado(l)
        if h and h[0] <= hasta_nivel:
            res.append(h)
    return res


# Indice del .md: lista escrita. En docx es un campo TOC de Word (se actualiza
# con F9) y en el pdf lo arma pandoc con numeros de pagina.
principales = [t for nivel, t in titulos_de(crudo, 1)]
indice_md = "# Índice\n\n" + "\n".join(
    "- " + re.sub(r"^(\d+)\.", r"\1\\.", t) for t in principales)


def sustituir_marcas(texto, portada, indice):
    return texto.replace("<!--PORTADA-->", portada).replace("<!--INDICE-->", indice)


# --------------------------------------------------------------------- md final
def rutas_del_md(texto):
    """Entrega/ esta un nivel abajo: las imagenes relativas suben una carpeta."""
    return re.sub(r"(!\[[^\]]*\]\()(?!https?://|/|\.\./)([^)\s]+\))", r"\1../\2", texto)


md = ("---\nlang: es\n---\n"
      + rutas_del_md(sustituir_marcas(crudo, portada_html(), indice_md))
      .replace(PBH, "---").replace(PB, "---"))

# ------------------------------------------------------- anchos de las tablas
SEPARADOR = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")


def celdas(l):
    l = l.strip()
    if l.startswith("|"):
        l = l[1:]
    if l.endswith("|") and not l.endswith("\\|"):
        l = l[:-1]
    return re.split(r"(?<!\\)\|", l)


def largo_visible(c):
    c = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", c)
    return len(re.sub(r"[*_`]", "", c).strip())


def repartir(filas, n):
    """Ancho de cada columna, en caracteres, para que ninguna parta una palabra.

    Cada columna pide algo segun su contenido (mezcla de largo medio y maximo)
    y no puede ser menor que su palabra mas larga. Lo que sobra del ancho de la
    hoja se reparte entre las demas en proporcion a lo que piden.
    """
    total = 125.0 if n >= 6 else 110.0   # caracteres que entran en el ancho util
    pide, minimo = [], []
    for c in range(n):
        largos = [largo_visible(f[c]) for f in filas]
        mezcla = (sum(largos) / len(largos) + min(max(largos), 90)) / 2.0
        pide.append(max(6.0, mezcla) ** 0.85)
        palabra = max(len(w) for f in filas
                      for w in re.sub(r"[*_`]", "", f[c]).split() or [""])
        minimo.append(1.2 * palabra + 3.0)
    fijo = {}
    while True:
        libre = [c for c in range(n) if c not in fijo]
        resto = total - sum(fijo.values())
        suma = sum(pide[c] for c in libre)
        nuevo = [c for c in libre if pide[c] * resto / suma < minimo[c]]
        if not nuevo or resto <= 0:
            break
        for c in nuevo:
            fijo[c] = minimo[c]
    resto = max(total - sum(fijo.values()), 1.0)
    suma = sum(pide[c] for c in range(n) if c not in fijo) or 1.0
    return [fijo.get(c, pide[c] * resto / suma) for c in range(n)]


def ajustar_anchos(texto):
    """Reparte el ancho de cada tabla segun el largo de su contenido.

    Pandoc toma los anchos relativos de las rayas del separador. Con todas
    iguales, una columna de dos palabras ocupa lo mismo que una de dos
    renglones. Esto reescribe el separador (solo en los archivos que van a
    pandoc, no en el md) para que el texto largo tenga mas lugar.
    """
    ls = texto.split("\n")
    i = 0
    while i < len(ls) - 1:
        if ls[i].lstrip().startswith("|") and SEPARADOR.match(ls[i + 1]) \
                and ls[i + 1].lstrip().startswith("|"):
            j = i + 2
            while j < len(ls) and ls[j].lstrip().startswith("|"):
                j += 1
            filas = [celdas(l) for l in ls[i:i + 1] + ls[i + 2:j]]
            n = len(celdas(ls[i + 1]))
            if n >= 2 and all(len(f) == n for f in filas):
                anchos = repartir(filas, n)
                partes = []
                for c, orig in enumerate(celdas(ls[i + 1])):
                    r = orig.strip()
                    rayas = max(5, int(round(100.0 * anchos[c] / sum(anchos))))
                    ini = ":" if r.startswith(":") else ""
                    fin = ":" if r.endswith(":") else ""
                    partes.append(ini + "-" * rayas + fin)
                ls[i + 1] = "|" + "|".join(partes) + "|"
            i = j
        else:
            i += 1
    return "\n".join(ls)


# --------------------------------------------------- imagenes y hojas apaisadas
def dims_png(ruta):
    try:
        with open(ruta, "rb") as fh:
            h = fh.read(24)
        if h[:8] == b"\x89PNG\r\n\x1a\n":
            return struct.unpack(">II", h[16:24])
    except OSError:
        pass
    return None


def pulgadas(ruta, max_w, max_h):
    """Ancho en pulgadas que entra en max_w x max_h conservando la proporcion."""
    d = dims_png(os.path.join(BASE, ruta))
    if not d:
        return max_w
    return min(max_w, max_h * d[0] / float(d[1]))


# Hojas A4 con margenes (en twips, 1 cm = 567). El ancho util sale de aca.
A4_W, A4_H = 11906, 16838
VERTICAL = ('<w:sectPr><w:pgSz w:w="%d" w:h="%d"/><w:pgMar w:top="1304" w:right="1247" '
            'w:bottom="1247" w:left="1247" w:header="708" w:footer="708" w:gutter="0"/>'
            '</w:sectPr>' % (A4_W, A4_H))
APAISADA = ('<w:sectPr><w:pgSz w:w="%d" w:h="%d" w:orient="landscape"/><w:pgMar w:top="1134" '
            'w:right="850" w:bottom="850" w:left="850" w:header="567" w:footer="567" '
            'w:gutter="0"/></w:sectPr>' % (A4_H, A4_W))


def corte_de_seccion(sect):
    """Parrafo casi invisible que cierra una seccion de Word con esas propiedades."""
    return ('```{=openxml}\n<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" '
            'w:lineRule="exact"/>%s</w:pPr></w:p>\n```' % sect)


TAMANOS = {}   # texto alternativo -> (ancho en pulgadas, ruta), para ajustar el docx

RE_IMG = re.compile(r"^!\[([^\]]*)\]\(([^)\s]+)\)\s*$")


def preparar_imagenes(texto, modo):
    """Imagenes de bpmn/ solas en una hoja apaisada; el resto, con ancho acotado.

    El titulo que antecede al diagrama se lleva a la hoja apaisada para que no
    quede suelto al pie de la hoja anterior. modo es 'docx' o 'html'.
    """
    ls = texto.split("\n")
    out = []
    for l in ls:
        m = RE_IMG.match(l)
        if not m:
            out.append(l)
            continue
        alt, ruta = m.group(1), m.group(2)
        if not ruta.startswith("bpmn/"):
            if modo == "docx":
                w = pulgadas(ruta, 6.4, 7.0)
                TAMANOS[alt] = (w, ruta)
                l = "![%s](%s){width=%.2fin}" % (alt, ruta, w)
            out.append(l)
            continue
        # el titulo inmediato anterior (saltando renglones en blanco)
        k = len(out) - 1
        while k >= 0 and not out[k].strip():
            k -= 1
        titulo = []
        if k >= 0 and encabezado(out[k]) and encabezado(out[k])[0] >= 2:
            titulo = [out[k], ""]
            del out[k:]
            while out and not out[-1].strip():
                out.pop()
        if modo == "docx":
            w = pulgadas(ruta, 10.4, 5.6)
            TAMANOS[alt] = (w, ruta)
            bloque = ["", corte_de_seccion(VERTICAL), ""] + titulo + [
                "![%s](%s){width=%.2fin}" % (alt, ruta, w),
                "", corte_de_seccion(APAISADA), ""]
        else:
            bloque = ["", '::: bpmn'] + titulo + [l, ":::", ""]
        out += bloque
    return "\n".join(out)


# -------------------------------------------------------- versiones docx y html
def sin_saltos_de_capitulo(texto):
    return texto.replace(PBH + "\n\n", "")


SALTO_HTML = '<div class="pb"></div>'

# docx: portada con sus estilos, el indice como campo de Word y nada de saltos
# manuales, porque el estilo Titulo 1 ya empieza hoja nueva.
def toc_docx(texto):
    items = [(n, t) for n, t in titulos_de(texto, 2)
             if not (n == 1 and t == "Índice")]

    def par(n, t, ini=False, fin=False):
        estilo = '<w:pPr><w:pStyle w:val="TOC%d"/></w:pPr>' % n
        x = "<w:p>" + estilo
        if ini:
            x += ('<w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r>'
                  '<w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
                  '<w:r><w:fldChar w:fldCharType="separate"/></w:r>')
        x += '<w:r><w:t xml:space="preserve">%s</w:t></w:r>' % escape(t)
        if fin:
            x += '<w:r><w:fldChar w:fldCharType="end"/></w:r>'
        return x + "</w:p>"

    cuerpo = "".join(par(n, t, i == 0, i == len(items) - 1)
                     for i, (n, t) in enumerate(items))
    return ('::: {custom-style="TOC Heading"}\nÍndice\n:::\n\n'
            '```{=openxml}\n%s\n```\n' % cuerpo)


md_docx = sustituir_marcas(crudo, portada_docx(), toc_docx(crudo))
md_docx = md_docx.replace(PB + "\n\n", "")
md_docx = ajustar_anchos(preparar_imagenes(sin_saltos_de_capitulo(md_docx), "docx"))
md_docx = "---\nlang: es\n---\n" + md_docx

sin_indice = crudo.replace("<!--INDICE-->\n\n" + PB + "\n\n", "")
md_html = sustituir_marcas(sin_saltos_de_capitulo(sin_indice), portada_html(), "")
md_html = ajustar_anchos(preparar_imagenes(md_html.replace(PB, SALTO_HTML), "html"))
md_html = "---\nlang: es\n---\n" + md_html

os.makedirs(DEST, exist_ok=True)
ruta_md = os.path.join(DEST, NOMBRE + ".md")
with io.open(ruta_md, "w", encoding="utf-8") as fh:
    fh.write(md)
tmp_docx = os.path.join(DEST, "_tmp_docx.md")
tmp_html = os.path.join(DEST, "_tmp_html.md")
with io.open(tmp_docx, "w", encoding="utf-8") as fh:
    fh.write(md_docx)
with io.open(tmp_html, "w", encoding="utf-8") as fh:
    fh.write(md_html)
print("%s.md  (%d lineas, ~%d palabras)" % (NOMBRE, md.count("\n") + 1, len(md.split())))

CSS = """
@page {
  size: A4; margin: 2.6cm 2.2cm 2.2cm;
  @top-center {
    content: "Integrantes: @@INT@@\\A @@TIT@@\\A @@SUB@@";
    white-space: pre; font-family: Arial, Helvetica, sans-serif; font-size: 8pt;
    line-height: 1.3; text-align: center; color: #000;
  }
  @bottom-center {
    content: counter(page); font-family: Arial, Helvetica, sans-serif;
    font-size: 8pt; color: #000;
  }
}
/* la caratula no lleva encabezado ni numero */
@page :first { margin: 0; @top-center { content: none; } @bottom-center { content: none; } }

/* hoja apaisada para los diagramas BPMN: se leen ampliados */
@page apaisada { size: A4 landscape; margin: 2.4cm 1.4cm 1.5cm; }

body { font-family: Arial, Helvetica, sans-serif; font-size: 11pt;
  line-height: 1.45; color: #000; }
p { margin: 0 0 .7em; text-align: justify; overflow-wrap: break-word; }

/* titulos de capitulo centrados y en hoja nueva; los de punto y subpunto, a la izquierda */
h1 { font-size: 14pt; font-weight: bold; text-align: center; margin: 0 0 .9em;
     page-break-before: always; page-break-after: avoid; }
h2 { font-size: 11pt; font-weight: bold; margin: 1.1em 0 .4em; page-break-after: avoid; }
h3 { font-size: 11pt; font-weight: bold; margin: 1em 0 .35em; page-break-after: avoid; }
h4 { font-size: 11pt; font-weight: bold; font-style: italic; margin: .9em 0 .3em;
     page-break-after: avoid; }

table { border-collapse: collapse; margin: .9em auto; font-size: 8.5pt;
  line-height: 1.3; width: 100%; table-layout: fixed; }
table.ancha { font-size: 7.5pt; line-height: 1.25; }
tr { page-break-inside: avoid; }
thead { display: table-header-group; }
th, td { border: 1px solid #000; padding: 3px 5px; text-align: left; vertical-align: top;
  overflow-wrap: anywhere; word-break: normal; hyphens: manual; }
table.ancha th, table.ancha td { padding: 2px 3px; }
th { font-weight: bold; background: #f4f6f8; }
td p, th p { margin: 0 0 .3em; text-align: left; }
ul, ol { margin: 0 0 .7em 1.4em; padding: 0; }
li { margin-bottom: .2em; text-align: justify; }
hr { display: none; }
.pb { page-break-after: always; }
code { font-family: Consolas, Menlo, monospace; font-size: 9.5pt; }
blockquote { margin: .7em 0 .7em 1.2em; padding-left: .8em; border-left: 2px solid #999; }

/* ------------------------------ imagenes ------------------------------- */
figure { margin: .8em 0; text-align: center; }
figure img { max-width: 100%; max-height: 13cm; width: auto; height: auto; }
figcaption { font-size: 9pt; font-style: italic; margin-top: .3em; text-align: center; }
.bpmn { page: apaisada; }
.bpmn h2, .bpmn h3 { margin-top: 0; }
.bpmn figure { margin: .4em 0 0; }
.bpmn figure img { width: 100%; max-height: 15cm; object-fit: contain; }

/* ------------------------------- caratula ------------------------------- */
.portada { padding: 0 2.2cm; height: 100%; position: relative; }
.portada::before {
  content: ""; display: block; height: 3.2cm; margin: 0 0 0 -2.2cm; width: calc(100% + 4.4cm);
  background: linear-gradient(105deg, #f4f6f8 62%, #e8edf1 62%);
  border-bottom: 1px solid #cfd6dc;
}
.portada p { text-align: right; margin: 0; }
.p-titulo { font-size: 24pt; color: #17495c; line-height: 1.25; margin-top: 11cm !important; }
.p-sub { font-size: 16pt; color: #5a6b74; margin-top: .25em !important; }
.p-materia { font-size: 13pt; color: #5a6b74; margin-top: .6em !important; }
.p-carrera { font-size: 11pt; font-weight: bold; margin-top: 1.6em !important; }
.p-equipo { font-size: 10.5pt; margin-top: 4cm !important; }
.p-docente { font-size: 10.5pt; margin-top: .5em !important; }

/* -------------------------------- indice -------------------------------- */
#TOC h2 { font-size: 14pt; font-weight: bold; text-align: center; margin: 0 0 1em; }
#TOC ul { list-style: none; padding-left: 0; margin: 0; }
#TOC ul ul { padding-left: 1.2em; }
#TOC li { margin: .3em 0; text-align: left; }
#TOC a { text-decoration: none; color: #17495c; }
#TOC a::after { content: " " leader(".") " " target-counter(attr(href url), page); color: #000; }
"""

# -------------------------------------------------------------- herramientas

def herramienta(nombre):
    """pandoc y weasyprint: primero el que esta junto al python en uso (el venv)."""
    al_lado = os.path.join(os.path.dirname(sys.executable), nombre)
    if os.path.isfile(al_lado):
        return al_lado
    return shutil.which(nombre)


def corre(cmd, que, entregable=True):
    try:
        subprocess.run(cmd, check=True, capture_output=True, cwd=BASE)
        if entregable:
            print("%s.%s" % (NOMBRE, que))
        else:
            print("  (paso intermedio, no se entrega: %s)" % que)
        return True
    except FileNotFoundError:
        print("  falta la herramienta para el %s, no se genero" % que)
    except subprocess.CalledProcessError as e:
        print("  fallo el %s: %s" % (que, e.stderr.decode()[-400:]))
    return False


LINEA = '<w:%s w:val="single" w:sz="4" w:space="0" w:color="000000"/>'
BORDES_TABLA = ("<w:tblBorders>" + "".join(
    LINEA % lado for lado in ("top", "left", "bottom", "right", "insideH", "insideV"))
    + "</w:tblBorders>")
RPR_TABLA = '<w:rPr><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>'

# estilos de la portada y del indice que se agregan a la plantilla de Word
ESTILOS_EXTRA = """
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/>
 <w:next w:val="BodyText"/><w:uiPriority w:val="10"/><w:qFormat/>
 <w:pPr><w:spacing w:before="4400" w:after="80" w:line="240" w:lineRule="auto"/><w:jc w:val="right"/></w:pPr>
 <w:rPr><w:color w:val="17495C"/><w:sz w:val="48"/><w:szCs w:val="48"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/>
 <w:next w:val="BodyText"/><w:uiPriority w:val="11"/><w:qFormat/>
 <w:pPr><w:spacing w:before="0" w:after="120" w:line="240" w:lineRule="auto"/><w:jc w:val="right"/></w:pPr>
 <w:rPr><w:color w:val="5A6B74"/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr></w:style>
<w:style w:type="paragraph" w:customStyle="1" w:styleId="PortadaMateria"><w:name w:val="Portada Materia"/>
 <w:basedOn w:val="Normal"/><w:qFormat/>
 <w:pPr><w:spacing w:before="120" w:after="0"/><w:jc w:val="right"/></w:pPr>
 <w:rPr><w:color w:val="5A6B74"/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:style>
<w:style w:type="paragraph" w:customStyle="1" w:styleId="PortadaCarrera"><w:name w:val="Portada Carrera"/>
 <w:basedOn w:val="Normal"/><w:qFormat/>
 <w:pPr><w:spacing w:before="360" w:after="0"/><w:jc w:val="right"/></w:pPr>
 <w:rPr><w:b/><w:bCs/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:style>
<w:style w:type="paragraph" w:customStyle="1" w:styleId="PortadaEquipo"><w:name w:val="Portada Equipo"/>
 <w:basedOn w:val="Normal"/><w:qFormat/>
 <w:pPr><w:spacing w:before="3200" w:after="0"/><w:jc w:val="right"/></w:pPr>
 <w:rPr><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr></w:style>
<w:style w:type="paragraph" w:customStyle="1" w:styleId="PortadaDocentes"><w:name w:val="Portada Docentes"/>
 <w:basedOn w:val="Normal"/><w:qFormat/>
 <w:pPr><w:spacing w:before="100" w:after="0"/><w:jc w:val="right"/></w:pPr>
 <w:rPr><w:sz w:val="21"/><w:szCs w:val="21"/></w:rPr></w:style>
<w:style w:type="table" w:customStyle="1" w:styleId="TablaAncha"><w:name w:val="Tabla ancha"/>
 <w:basedOn w:val="Table"/><w:uiPriority w:val="59"/><w:qFormat/>
 <w:rPr><w:sz w:val="15"/><w:szCs w:val="15"/></w:rPr>
 <w:tblPr><w:tblCellMar><w:left w:w="60" w:type="dxa"/><w:right w:w="60" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
<w:style w:type="paragraph" w:styleId="TOC1"><w:name w:val="toc 1"/><w:basedOn w:val="Normal"/>
 <w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:unhideWhenUsed/>
 <w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9400"/></w:tabs><w:spacing w:before="60" w:after="40"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="TOC2"><w:name w:val="toc 2"/><w:basedOn w:val="Normal"/>
 <w:next w:val="Normal"/><w:uiPriority w:val="39"/><w:unhideWhenUsed/>
 <w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9400"/></w:tabs><w:spacing w:before="0" w:after="30"/><w:ind w:left="284"/></w:pPr></w:style>
"""


def plantilla_word(destino):
    """Arma un reference.docx: es la plantilla de estilos que usa Word.

    Partimos del que trae pandoc (que ya define Title, Subtitle, Heading 1..6,
    TOC Heading y Compact) y le cambiamos la tipografia, el color de los
    titulos y el tamano de pagina (A4). Titulo 1 empieza hoja nueva, la
    portada tiene sus estilos y las tablas llevan bordes y letra mas chica.
    Asi el docx sale con estilos de verdad y no con parrafos formateados a mano.
    """
    import zipfile, tempfile
    base = os.path.join(tempfile.gettempdir(), "_ref_pandoc.docx")
    with open(base, "wb") as fh:
        subprocess.run([PANDOC, "--print-default-data-file", "reference.docx"],
                       check=True, stdout=fh, stderr=subprocess.DEVNULL)
    zin = zipfile.ZipFile(base)
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            datos = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                x = datos.decode("utf-8")
                # tipografia unica en todo el documento (tambien la de los titulos,
                # que en la plantilla de pandoc viene como fuente del tema)
                x = re.sub(r"<w:rFonts[^>]*/>",
                           '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:eastAsia="Arial" w:cs="Arial"/>',
                           x)
                # cuerpo en 11 pt, como el pdf
                x = x.replace('<w:sz w:val="24" />', '<w:sz w:val="22" />', 1)
                x = x.replace('<w:szCs w:val="24" />', '<w:szCs w:val="22" />', 1)
                # titulos en azul oscuro, como en un informe academico
                x = x.replace('<w:color w:val="365F91"', '<w:color w:val="1F3864"')
                x = x.replace('<w:color w:val="4F81BD"', '<w:color w:val="1F3864"')
                x = x.replace('<w:color w:val="0F4761"', '<w:color w:val="1F3864"')
                # idioma espanol, para que el corrector de Word no marque todo
                x = re.sub(r'<w:lang w:val="[^"]*"', '<w:lang w:val="es-AR"', x)
                # cada capitulo (Titulo 1) arranca en hoja nueva
                x = re.sub(r'(<w:style [^>]*w:styleId="Heading1">.*?<w:keepLines\s*/>)',
                           r"\1<w:pageBreakBefore/>", x, count=1, flags=re.S)
                # Title y Subtitle de la portada se redefinen mas abajo
                for sid in ("Title", "Subtitle"):
                    x = re.sub(r'<w:style [^>]*w:styleId="%s">.*?</w:style>' % sid,
                               "", x, count=1, flags=re.S)
                # tablas: bordes finos, letra de 9 pt y encabezado en negrita. El
                # orden de los hijos es el del esquema: rPr antes de tblPr, y dentro
                # de tblPr los bordes antes de los margenes de celda.
                def estilo_tabla(m):
                    t = m.group(0)
                    t = t.replace("<w:tblPr>", RPR_TABLA + "<w:tblPr>", 1)
                    return t.replace("<w:tblCellMar>", BORDES_TABLA + "<w:tblCellMar>", 1)
                x = re.sub(r'<w:style [^>]*w:styleId="Table">.*?</w:style>',
                           estilo_tabla, x, count=1, flags=re.S)
                x = x.replace('<w:tblStylePr w:type="firstRow">',
                              '<w:tblStylePr w:type="firstRow"><w:rPr><w:b/><w:bCs/></w:rPr>', 1)
                x = x.replace("</w:styles>", ESTILOS_EXTRA + "</w:styles>")
                datos = x.encode("utf-8")
            elif item.filename == "word/document.xml":
                # pandoc toma el tamano de pagina del ultimo sectPr de la plantilla
                x = datos.decode("utf-8")
                final = VERTICAL.replace(
                    "<w:sectPr>", '<w:sectPr><w:footnotePr><w:numRestart w:val="eachSect"/>'
                    '</w:footnotePr>')
                if "<w:sectPr" in x:
                    x = re.sub(r"<w:sectPr>.*?</w:sectPr>", lambda m: final, x, flags=re.S)
                else:
                    x = x.replace("</w:body>", final + "</w:body>")
                datos = x.encode("utf-8")
            zout.writestr(item, datos)
    zin.close()
    return destino


PIE_REL = "rIdPie"
PIE_XML = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
           '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
           'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
           '<w:p><w:pPr><w:spacing w:before="0" w:after="0"/><w:jc w:val="center"/></w:pPr>'
           '<w:fldSimple w:instr=" PAGE "><w:r><w:rPr><w:sz w:val="16"/><w:szCs w:val="16"/>'
           '</w:rPr><w:t>1</w:t></w:r></w:fldSimple></w:p></w:ftr>')


def ajustar_docx(ruta):
    """Retoques al docx que pandoc no hace solo. Devuelve (imagenes, tablas anchas).

    - Pandoc achica toda imagen al ancho de la hoja vertical, y las apaisadas
      no entran asi: se fija el tamano de cada una (EMU, 914400 por pulgada).
    - Las tablas de 6 o mas columnas pasan al estilo "Tabla ancha" (7,5 pt y
      margenes de celda chicos) para que no se partan las palabras.
    - Pie de pagina con el numero de pagina, sin pie en la portada.
    """
    import zipfile
    tmp = ruta + ".tmp"
    cuentas = {"imagenes": 0, "tablas": 0}
    with zipfile.ZipFile(ruta) as zin:
        partes = [(i, zin.read(i.filename)) for i in zin.infolist()]
    salida = []
    for item, datos in partes:
        nombre = item.filename
        if nombre == "word/document.xml":
            x = datos.decode("utf-8")

            def dibujo(m):
                bloque = m.group(0)
                d = re.search(r'<wp:docPr[^>]*descr="([^"]*)"', bloque)
                alt = d.group(1) if d else None
                if alt not in TAMANOS:
                    return bloque
                w, rel = TAMANOS[alt]
                dim = dims_png(os.path.join(BASE, rel))
                if not dim:
                    return bloque
                cx = int(w * 914400)
                cy = int(cx * dim[1] / float(dim[0]))
                bloque = re.sub(r'(<wp:extent )cx="\d+" cy="\d+"',
                                r'\1cx="%d" cy="%d"' % (cx, cy), bloque)
                bloque = re.sub(r'(<a:ext )cx="\d+" cy="\d+"',
                                r'\1cx="%d" cy="%d"' % (cx, cy), bloque)
                cuentas["imagenes"] += 1
                return bloque
            x = re.sub(r"<w:drawing>.*?</w:drawing>", dibujo, x, flags=re.S)

            def tabla(m):
                t = m.group(0)
                if len(re.findall(r"<w:gridCol\b", t)) < 6:
                    return t
                t, k = re.subn(r'<w:tblStyle w:val="Table"\s*/>',
                               '<w:tblStyle w:val="TablaAncha"/>', t, count=1)
                cuentas["tablas"] += k
                return t
            x = re.sub(r"<w:tbl>.*?</w:tbl>", tabla, x, flags=re.S)

            contador = [0]

            def seccion(m):
                contador[0] += 1
                # la primera seccion arranca con la portada: sin pie en la primera hoja
                extra = "<w:titlePg/>" if contador[0] == 1 else ""
                return ('<w:sectPr><w:footerReference w:type="default" r:id="%s"/>%s%s'
                        '</w:sectPr>' % (PIE_REL, m.group(1), extra))
            x = re.sub(r"<w:sectPr>(.*?)</w:sectPr>", seccion, x, flags=re.S)
            datos = x.encode("utf-8")
        elif nombre == "[Content_Types].xml":
            datos = datos.decode("utf-8").replace(
                "</Types>",
                '<Override PartName="/word/footer1.xml" ContentType="application/'
                'vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/></Types>'
            ).encode("utf-8")
        elif nombre == "word/_rels/document.xml.rels":
            datos = datos.decode("utf-8").replace(
                "</Relationships>",
                '<Relationship Id="%s" Type="http://schemas.openxmlformats.org/'
                'officeDocument/2006/relationships/footer" Target="footer1.xml"/>'
                "</Relationships>" % PIE_REL).encode("utf-8")
        salida.append((item, datos))
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item, datos in salida:
            zout.writestr(item, datos)
        zout.writestr("word/footer1.xml", PIE_XML)
    os.replace(tmp, ruta)
    return cuentas["imagenes"], cuentas["tablas"]


# Orden de los hijos que exige el esquema de Word en los elementos que
# tocamos a mano (Word se queja de un "contenido ilegible" si no se respeta).
ORDEN_OOXML = {
    "pPr": ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr",
            "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs",
            "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct",
            "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
            "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents",
            "suppressOverlap", "jc", "textDirection", "textAlignment",
            "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr",
            "pPrChange"],
    "tblPr": ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
              "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd",
              "tblBorders", "shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption",
              "tblDescription"],
    "style": ["name", "aliases", "basedOn", "next", "link", "autoRedefine", "hidden",
              "uiPriority", "semiHidden", "unhideWhenUsed", "qFormat", "locked",
              "personal", "personalCompose", "personalReply", "rsid", "pPr", "rPr",
              "tblPr", "trPr", "tcPr", "tblStylePr"],
    "tblStylePr": ["pPr", "rPr", "tblPr", "trPr", "tcPr"],
    "sectPr": ["headerReference", "footerReference", "footnotePr", "endnotePr", "type",
               "pgSz", "pgMar", "paperSrc", "pgBorders", "lnNumType", "pgNumType",
               "cols", "formProt", "vAlign", "noEndnote", "titlePg", "textDirection",
               "bidi", "rtlGutter", "docGrid", "printerSettings"],
    "tcPr": ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd",
             "noWrap", "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"],
}


def validar_orden_docx(ruta):
    """Revisa el orden de los hijos en document.xml, styles.xml y el pie.

    Devuelve la lista de faltas (vacia si todo esta en orden).
    """
    import zipfile
    import xml.etree.ElementTree as ET
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    faltas = []
    with zipfile.ZipFile(ruta) as z:
        for parte in ("word/document.xml", "word/styles.xml", "word/footer1.xml"):
            if parte not in z.namelist():
                continue
            raiz = ET.fromstring(z.read(parte))
            for el in raiz.iter():
                if not isinstance(el.tag, str) or not el.tag.startswith(W):
                    continue
                orden = ORDEN_OOXML.get(el.tag[len(W):])
                if not orden:
                    continue
                ultimo = -1
                for hijo in el:
                    h = hijo.tag[len(W):] if hijo.tag.startswith(W) else None
                    if h not in orden:
                        continue
                    i = orden.index(h)
                    if i < ultimo:
                        faltas.append("%s: <%s> viene despues de <%s> dentro de <%s>"
                                      % (parte, h, orden[ultimo], el.tag[len(W):]))
                    ultimo = max(ultimo, i)
    return faltas


PANDOC = herramienta("pandoc")
WEASY = herramienta("weasyprint")
# subscript y superscript no: "~25 horas ... ~24 %" no es un subindice.
ENTRADA = "markdown-subscript-superscript-tex_math_dollars"

if PANDOC:
    ref = os.path.join(DEST, "_ref.docx")
    try:
        plantilla_word(ref)
    except Exception as e:
        print("  no se pudo armar la plantilla de estilos (%s), se usa la de pandoc" % e)
        ref = None
    ruta_docx = os.path.join(DEST, NOMBRE + ".docx")
    if corre([PANDOC, tmp_docx, "-o", ruta_docx,
              "--from", ENTRADA, "--resource-path", BASE]
             + (["--reference-doc", ref] if ref else []), "docx"):
        ajustadas, anchas = ajustar_docx(ruta_docx)
        if ajustadas != len(TAMANOS):
            aviso("docx: se ajustaron %d de %d imagenes" % (ajustadas, len(TAMANOS)))
        print("  docx: %d imagenes y %d tablas anchas ajustadas" % (ajustadas, anchas))
        faltas = validar_orden_docx(ruta_docx)
        for f in faltas[:10]:
            aviso("docx fuera de orden: " + f)
        if not faltas:
            print("  docx: orden de los elementos de Word verificado")
    html = os.path.join(DEST, "_tmp.html")
    css = os.path.join(DEST, "_tmp.css")
    with io.open(css, "w", encoding="utf-8") as fh:
        fh.write(CSS.replace("@@INT@@", INTEGRANTES.replace(" - ", ", "))
                 .replace("@@TIT@@", TITULO).replace("@@SUB@@", SUBTITULO))
    if corre([PANDOC, tmp_html, "-o", html, "--standalone", "--from", ENTRADA,
              "--resource-path", BASE, "--toc", "--toc-depth=2",
              "--metadata", "pagetitle=" + NOMBRE,
              "--css", "_tmp.css"], "html", entregable=False):
        # Pandoc deja este orden: titulo, indice, cuerpo. La caratula necesita
        # otro: bloque institucional, titulo y equipo, todo junto y en su propia
        # hoja, y recien despues el indice.
        h = io.open(html, encoding="utf-8").read()
        # --css solo sirve para que pandoc no meta sus estilos por defecto (un
        # ancho maximo de 36 em, por ejemplo); la hoja la carga weasyprint con -s
        h = re.sub(r'<link[^>]*_tmp\.css[^>]*>\s*', "", h)

        def sacar(patron):
            m = re.search(patron, h, re.S)
            return (m.group(0), h.replace(m.group(0), "", 1)) if m else ("", h)

        toc, h = sacar(r'<nav id="TOC".*?</nav>')
        toc = toc.replace('<nav id="TOC" role="doc-toc">',
                          '<nav id="TOC" role="doc-toc"><h2>Índice</h2>')
        # Pandoc pone el indice arriba de todo; tiene que ir despues de la
        # caratula, o sea despues del primer salto de pagina. Se busca con
        # expresion regular porque pandoc reescribe el html crudo y un find
        # por texto exacto falla sin avisar.
        m = re.search(r'<div class="pb"\s*/?>\s*</div>|<div class="pb"\s*/>', h)
        if not m:
            raise SystemExit("no encontre el salto de pagina de la caratula en el html")
        corte = m.end()
        h = h[:corte] + toc + SALTO_HTML + h[corte:]

        # tablas de 6 o mas columnas: letra mas chica
        def marcar(mt):
            tabla = mt.group(0)
            cols = len(re.findall(r"<th\b", tabla.split("</tr>", 1)[0]))
            return tabla.replace("<table", '<table class="ancha"', 1) if cols >= 6 else tabla
        h = re.sub(r"<table\b.*?</table>", marcar, h, flags=re.S)
        io.open(html, "w", encoding="utf-8").write(h)
        if WEASY:
            corre([WEASY, "-u", BASE + os.sep, "-s", css, html,
                   os.path.join(DEST, NOMBRE + ".pdf")], "pdf")
        else:
            print("  falta weasyprint, no se genero el pdf")
    # ARMAR_CONSERVAR=1 deja los intermedios para depurar
    for t in (html, css, tmp_docx, tmp_html, ref or ""):
        if t and os.path.exists(t) and not os.environ.get("ARMAR_CONSERVAR"):
            os.remove(t)
else:
    print("  falta pandoc: solo se genero el .md")
