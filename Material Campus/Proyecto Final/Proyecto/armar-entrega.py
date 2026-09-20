#!/usr/bin/env python3
"""Arma el archivo unico de entrega a partir de las secciones sueltas.

    python3 armar-entrega.py

Lee los .md de esta carpeta y escribe "TP Final Parte 1 - Dulxelitos.md".
Volver a correrlo despues de editar cualquier seccion: el archivo de entrega
se regenera entero, no se edita a mano.
"""

import io, os, re, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
SALIDA = "TP Final Parte 1 - Dulxelitos.md"


def leer(nombre):
    with io.open(os.path.join(BASE, nombre), encoding="utf-8") as fh:
        return fh.read().split("\n")


def desde(lineas, marca):
    """Descarta el encabezado propio del archivo: arranca en la primera linea que empieza con `marca`."""
    for i, ln in enumerate(lineas):
        if ln.startswith(marca):
            return lineas[i:]
    raise SystemExit("no encontre %r" % marca)


def hasta(lineas, marca):
    for i, ln in enumerate(lineas):
        if ln.startswith(marca):
            return lineas[:i]
    return lineas


def demote(lineas, niveles=1):
    """Baja un nivel todos los encabezados (## -> ###)."""
    return [("#" * niveles + ln) if ln.startswith("#") else ln for ln in lineas]


def renombrar(lineas, mapa):
    salida = []
    for ln in lineas:
        for viejo, nuevo in mapa.items():
            if ln.startswith(viejo):
                ln = nuevo
                break
        salida.append(ln)
    return salida


hoy = datetime.date.today()

L = []
L.append("# Trabajo Práctico Final — Parte 1")
L.append("## Diagnóstico gerencial: Dulxelitos")
L.append("")
L.append("**Gestión Gerencial** · 5.º año, Ingeniería en Sistemas de Información")
L.append("Universidad Tecnológica Nacional — Facultad Regional San Rafael · Plan 2026")
L.append("Cátedra: Ing. Jeremías Pino e Ing. Martín Noguerol")
L.append("")
L.append("**Organización analizada:** Dulxelitos — fabricación, fraccionamiento y "
         "distribución de snacks. San Rafael, Mendoza. Fundada en 1973.")
L.append("")
L.append("**Equipo:** _(completar con los nombres de los integrantes)_")
L.append("")
L.append("**Fecha:** %s" % hoy.strftime("%d/%m/%Y"))
L.append("")
L.append("---")
L.append("")
L.append("## Contenido")
L.append("")
L.append("1. La organización")
L.append("2. El contexto")
L.append("3. Modelo de negocio actual (BMC AS-IS)")
L.append("4. Propuesta de valor actual (VPC AS-IS)")
L.append("5. Madurez y capacidades")
L.append("")
L.append("> La **Sección 6 (Problema gerencial priorizado)** no se incluye en esta entrega: "
         "se presenta por separado, según lo acordado con la cátedra.")
L.append("")
L.append("### Cómo leer las marcas de origen del dato")
L.append("")
L.append("Cada afirmación del informe indica de dónde sale, para que el lector pueda "
         "evaluar su peso:")
L.append("")
L.append("| Marca | Significado |")
L.append("|---|---|")
L.append("| ✅ | Confirmado por el equipo con acceso a la organización |")
L.append("| 🔎 | Verificado en fuentes públicas (sitio oficial, Instagram, listados de "
         "mayoristas y cadenas) |")
L.append("| ❓ | Dato que la organización no produce o que no pudo relevarse |")
L.append("")
L.append("Un integrante del equipo trabaja en la organización, lo que explica la "
         "proporción de datos confirmados. El control del sesgo que eso introduce se "
         "detalla en §1.6.")
L.append("")
L.append("---")
L.append("")

# ---- 1
s = desde(leer("01 - Organización.md"), "## 1.1 ")
L.append("## 1. La organización")
L.append("")
L += demote(s)
L.append("")
L.append("---")
L.append("")

# ---- 2
s = desde(leer("02 - Contexto.md"), "Se aplican cuatro herramientas")
# saca el parrafo de marcas de origen, que ya esta en la portada
s = [ln for ln in s if not ln.startswith("Marcas de origen del dato:")]
L.append("## 2. El contexto")
L.append("")
L += demote(s)
L.append("")
L.append("---")
L.append("")

# ---- 3: los nueve bloques + sintesis + lectura analitica
L.append("## 3. Modelo de negocio actual (BMC AS-IS)")
L.append("")
L.append("### 3.1 Los nueve bloques del canvas")
L.append("")
bmc = desde(leer("BMC - Dulxelitos.md"), "## 1. Segmentos de clientes")
fuentes = desde(bmc, "## Fuentes")          # se reserva para el anexo
bmc = hasta(bmc, "## Fuentes")
bmc = demote(demote(bmc))                    # ## -> ####
bmc = renombrar(bmc, {"#### Síntesis del canvas": "### 3.2 Síntesis del canvas"})
L += bmc
L.append("")
lect = desde(leer("03 - Lectura analítica del BMC.md"), "## 3.1 Lógica de valor")
lect = renombrar(demote(lect), {
    "### 3.1 Lógica de valor": "### 3.3 Lógica de valor",
    "### 3.2 Explotación vs. Exploración": "### 3.4 Explotación vs. Exploración (Run the Business vs. Change the Business)",
    "### 3.3 Debilidades y dependencias": "### 3.5 Debilidades y dependencias",
    "### 3.4 Tensiones del modelo actual": "### 3.6 Tensiones del modelo actual",
})
L += lect
L.append("")
L.append("---")
L.append("")

# ---- 4
s = desde(leer("04 - VPC - Distribuidor mayorista.md"), "## 4.1 ")
L.append("## 4. Propuesta de valor actual (VPC AS-IS)")
L.append("")
L += demote(s)
L.append("")
L.append("---")
L.append("")

# ---- 5
s = desde(leer("05 - Madurez y Costo de No Actuar.md"), "## 5.1 ")
L.append("## 5. Madurez y capacidades")
L.append("")
L += demote(s)
L.append("")
L.append("---")
L.append("")

# ---- anexo
L.append("## Anexo — Fuentes y limitaciones")
L.append("")
L += renombrar(demote(fuentes), {"### Fuentes": "### Fuentes consultadas"})
L.append("")
L.append("### Datos que la organización no produce")
L.append("")
L.append("Se declaran en lugar de estimarlos. Ninguno impide el diagnóstico; varios son, "
         "en sí mismos, evidencia de la Sección 5.")
L.append("")
L.append("| Dato | Sección afectada |")
L.append("|---|---|")
L.append("| Concentración de facturación de los cinco mayores distribuidores | §1.3, §2.2, §4.1 |")
L.append("| Horas extras mensuales pagadas por la saturación de planta | §5.5 |")
L.append("| Horas insumidas en rehacer la lista de precios | §5.5 |")
L.append("| Unidades de producto rotas en tránsito por mes | §5.5 |")
L.append("| Pedidos recortados o rechazados por falta de capacidad | §5.5 |")
L.append("| Altas y bajas de distribuidores de los últimos dos años, y sus causas | §2.4, §4.4 |")
L.append("| Productos sustitutos en el punto de venta | §2.2 |")
L.append("| Hitos históricos entre 1973 y la actualidad | §1.4 |")
L.append("| Competencia de marcas de alcance nacional en el canal | §2.2 |")
L.append("")

texto = "\n".join(L)
texto = re.sub(r"\n{4,}", "\n\n\n", texto)
with io.open(os.path.join(BASE, SALIDA), "w", encoding="utf-8") as fh:
    fh.write(texto.rstrip() + "\n")

palabras = len(texto.split())
print("%s  (%d lineas, ~%d palabras)" % (SALIDA, texto.count("\n") + 1, palabras))
