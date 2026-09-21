# Trabajo Práctico Final — Parte 1 · Dulxelitos
## Documento de integración

Este documento no agrega contenido: **traza cómo se encadenan las secciones**. La rúbrica de la cátedra evalúa explícitamente que las herramientas no estén aisladas —"¿las oportunidades del FODA surgen realmente del PESTEL y las 5 Fuerzas?"— y esta es la evidencia de ese encadenamiento. En nuestro caso el lugar del PESTEL lo ocupan los factores del entorno de §2.1, por los motivos que explica §2 y `herramientas.md`.

---

## Archivos

| Archivo | Sección del enunciado | Estado |
|---|---|---|
| `01 - Organización.md` | 1. Organización | Completa |
| `02 - Contexto.md` | 2. Contexto | Completa |
| `BMC - Dulxelitos.md` + `BMC - Dulxelitos.pdf` | 3. Modelo de negocio actual (canvas) | Completa — el póster manda, ver abajo |
| `03 - Lectura analítica del BMC.md` | 3. Modelo de negocio actual (lectura) | Completa |
| `04 - VPC - Distribuidor mayorista.md` | 4. Propuesta de valor actual | Completa |
| `05 - Madurez y Costo de No Actuar.md` | 5. Madurez y capacidades | Completa, con 4 datos pendientes en el CoI |
| — | 6. Problema gerencial priorizado | **No incluida** (se entrega después) |
| **`Entrega/`** | **lo que se entrega: md, docx y pdf** | **generada** — no editar a mano |
| `armar-entrega.py` | arma el archivo de entrega desde las secciones | correr `python3 armar-entrega.py` |

## El archivo de entrega

La carpeta `Entrega/` es lo que se le da al profesor: las cinco secciones en un solo
documento, con portada, índice y un anexo de fuentes y limitaciones, en tres formatos
(`.md`, `.docx` y `.pdf`).

**Se genera, no se edita.** Cada vez que alguien toca una sección hay que volver a correr:

```bash
python3 armar-entrega.py
```

Así la entrega nunca queda desfasada de las secciones. Lo único que hay que completar a
mano después de generarla son **los nombres de los integrantes** en la portada.

Necesita `pandoc` para el docx y `weasyprint` para el pdf. Si falta alguno, el script
avisa y genera igual lo que pueda.

## El pipeline analítico

```
§1 Organización
   │  planta saturada + horas extras
   │  funciones reales, sin formalizar
   │  acceso interno declarado
   ▼
§2 Contexto
   Factores del entorno ─┐
   5 Fuerzas ────────────┼──► oportunidades y amenazas
   Cadena de Valor ──────┼──► fortalezas y debilidades
                         ▼
                        FODA
   │
   ├──────────────► §3 tensiones del modelo
   ├──────────────► §4 elección del segmento
   └──────────────► §5 evidencia por dimensión
                         │
                         ▼
                    §6 problema gerencial (pendiente)
```

## Trazabilidad de los hallazgos

| Hallazgo | De dónde sale | Dónde se usa después |
|---|---|---|
| Planta saturada absorbida con horas extras | §1.4, relevamiento interno | §2 Cadena de Valor (operaciones) · §3 segunda tensión · §5 Procesos · **CoI componente agregado** |
| El costo por producto no se conoce | BMC bloque 9 + §1.6 | §2.1 factores económicos e implicancia de precios · §3 primera tensión · §5 Tecnología y Datos |
| El sector es cómodo (Porter) | §2.2 | §3.2 explica por qué la exploración desestructurada fue sostenible 53 años |
| Set competitivo enteramente regional | §2.2, relevamiento interno | §2 FODA (O5) · matiza la urgencia de toda la sección 5 |
| Un solo proveedor de film | §2.2 fuerza 2 | §2 FODA (D5, A2) · §3.3 dependencia 1 · §5 Gobierno (riesgo no gestionado) |
| Margen se crea en operaciones y logística, se pierde en dirección y tecnología | §2.3 Cadena de Valor | Origen directo de las fortalezas y debilidades del FODA §2.4 |
| El canal está conforme ("compromiso y precio") | §4.2, relevamiento interno | §4.4 encaje bueno · reencuadra el diagnóstico hacia lo interno · §5 Clientes y Canales |
| El distribuidor no puede consultar stock sin llamar | §4.2 | §2.4 FODA (debilidad 7) · §4.4 brecha 1 · §5 Clientes y Canales |
| Tienda online armada y sin catálogo desde 2020 | §3.2 + verificación del sitio | §2 FODA (O1) · §2.5 iniciativa DO · §4.4 cierre de la brecha |
| "No, muy pyme" — estadísticas operativas sin tablero de dirección | §5, relevamiento interno | §2 Cadena de Valor (infraestructura) · §5 Gobierno 1.50 · **explica por qué el CoI no se puede cuantificar** |
| Conocimiento del negocio sin formalizar | §1.5 | §3.3 dependencia de fondo · §5 Gobierno (sucesión no gestionada) |

> **Dos herramientas quedaron afuera a propósito.** El **PESTEL completo**, porque cuatro de sus seis dimensiones volvían vacías en este caso, y el **FODA cruzado**, porque su producto son iniciativas y esta entrega es diagnóstico. La guía de la cátedra respalda las dos decisiones: su ejemplo resuelto usa "FODA + factores clave" en vez de un PESTEL, y su FODA no está cruzado. Está justificado en §2 y en `herramientas.md`.

> **El encadenamiento más importante del trabajo:** "no, muy pyme" (§5) → estadísticas operativas que no se integran en indicadores de dirección → Gobierno en 1.50 (§5.3) → la empresa no puede cuantificar su propio CoI (§5.5). El diagnóstico muestra así la distancia entre **producir datos** y **usarlos sistemáticamente para decidir y controlar**.

## El canvas manda

`BMC - Dulxelitos.pdf` es el póster de los nueve bloques, armado el 4 de septiembre.
Es el punto de partida del trabajo y **no se toca**: se entrega tal cual está.

`BMC - Dulxelitos.md` es el mismo canvas desarrollado, con la tabla de distribuidores
por provincia, el catálogo completo y lo que fuimos averiguando en cada bloque. Dice lo
mismo que el póster, con más detalle. Si algún día hay que corregir un bloque, se corrige
primero en el póster y después acá.

Las dos cosas que el relevamiento sí cerró y que el póster dejaba abiertas:

| Dónde | Qué pasó |
|---|---|
| Segmento 1 | Preguntamos por la concentración de facturación entre los 57 distribuidores: **el dato no existe**. La empresa no la mide. La ausencia es el hallazgo, y se retoma en §5 |
| Domicilios | La página oficial y los listados comerciales daban tres direcciones distintas. Confirmado: **planta, depósito y oficina están los tres en Av. Pedro Vargas 2400** |

## Datos pendientes

Ninguno bloquea la entrega. Se dejan declarados como limitación, que es lo que corresponde metodológicamente.

| Dato | Sección afectada | Reconstruible |
|---|---|---|
| **Horas extras mensuales pagadas** | §5.5 CoI | **Sí, inmediato** — está en la liquidación de sueldos |
| **Horas para rehacer la lista de precios** | §5.5 CoI | **Sí** — quien la hace lo puede estimar |
| Concentración de facturación de los 5 mayores distribuidores | §1.3, §4.1, §2.2 fuerza 3 | La empresa no lo mide |
| Unidades de paquetes rotos por mes | §5.5 CoI | La empresa no lo mide |
| Pedidos recortados por falta de capacidad | §5.5 CoI | La empresa no lo mide |
| Altas y bajas de distribuidores (2 años) y causas | §2.4 (A4), §4.4 | La empresa no lo registra |
| Productos sustitutos en el punto de venta | §2.2 fuerza 5 | No relevado |
| Hitos históricos entre 1973 y hoy | §1.4 | La organización no conserva registro |
| Competencia de marcas nacionales en el canal | §2.2 fuerza 1 | No relevado |

> Las dos primeras filas son las únicas que **conviene conseguir antes de entregar**: con ellas, dos de los cuatro componentes del CoI pasan de "no observado" a cuantificado, y la Sección 5 gana mucho. Las demás son ausencias que el informe usa como evidencia, no como deuda.

## Nota sobre AS-IS

Todo el trabajo está escrito en **estado actual (AS-IS)**, como pide el enunciado: no se propone solución. Las slides de la Clase 2 planteaban un entregable con BMC y VPC en **To-Be** más una hipótesis de oportunidad tecnológica; se siguió el enunciado oficial del trabajo práctico, que es posterior y explícito en pedir el modelo actual y en advertir que no se proponga todavía una solución.

Por eso mismo **no hicimos el FODA cruzado**: su producto son iniciativas, y proponer iniciativas es justo lo que esta entrega no debe hacer. El FODA simple sí está, en §2.4, que es además la forma que usa la guía de la cátedra en su ejemplo resuelto.
