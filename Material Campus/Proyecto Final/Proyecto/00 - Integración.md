# Trabajo Práctico Final — Parte 1 · Dulxelitos
## Documento de integración

Este documento no agrega contenido: **traza cómo se encadenan las secciones**. La rúbrica de la cátedra evalúa explícitamente que las herramientas no estén aisladas —"¿las oportunidades del FODA surgen realmente del PESTEL y las 5 Fuerzas?"— y esta es la evidencia de ese encadenamiento.

---

## Archivos

| Archivo | Sección del enunciado | Estado |
|---|---|---|
| `01 - Organización.md` | 1. Organización | Completa |
| `02 - Contexto.md` | 2. Contexto | Completa |
| `BMC - Dulxelitos.md` + `BMC - Dulxelitos.pdf` | 3. Modelo de negocio actual (canvas) | Completa — **requiere dos correcciones**, ver abajo |
| `03 - Lectura analítica del BMC.md` | 3. Modelo de negocio actual (lectura) | Completa |
| `04 - VPC - Distribuidor mayorista.md` | 4. Propuesta de valor actual | Completa |
| `05 - Madurez y Costo de No Actuar.md` | 5. Madurez y capacidades | Completa, con 4 datos pendientes en el CoI |
| — | 6. Problema gerencial priorizado | **No incluida** (se entrega después) |

## El pipeline analítico

```
§1 Organización
   │  planta saturada + horas extras
   │  funciones reales + segunda generación
   │  acceso interno declarado
   ▼
§2 Contexto
   PESTEL ──────────┐
   5 Fuerzas ───────┼──► oportunidades y amenazas
   Cadena de Valor ─┼──► fortalezas y debilidades
                    ▼
              FODA cruzado ──► iniciativas (FO / FA / DO / DA)
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
| El costo por producto no se conoce | BMC bloque 9 + §1.6 | §2 PESTEL económico e implicancia de precios · §3 primera tensión · §5 Tecnología y Datos |
| El sector es cómodo (Porter) | §2.2 | §3.2 explica por qué la exploración desestructurada fue sostenible 53 años |
| Set competitivo enteramente regional | §2.2, relevamiento interno | §2 FODA (O5) · matiza la urgencia de toda la sección 5 |
| Un solo proveedor de film | §2.2 fuerza 2 | §2 FODA (D5, A2) · §3.3 dependencia 1 · §5 Gobierno (riesgo no gestionado) |
| Margen se crea en operaciones y logística, se pierde en dirección y tecnología | §2.3 Cadena de Valor | Origen directo de las fortalezas y debilidades del FODA §2.4 |
| El canal está conforme ("compromiso y precio") | §4.2, relevamiento interno | §4.4 encaje bueno · reencuadra el diagnóstico hacia lo interno · §5 Clientes y Canales |
| El distribuidor no puede consultar stock sin llamar | §4.2 | §2 FODA cruzado (DO) · §4.4 brecha 1 · §5 Clientes y Canales |
| Capa de e-commerce construida y desactivada | §3.2 + verificación del sitio | §2 FODA (O1) · §2.5 iniciativa DO · §4.4 cierre de la brecha |
| "No, muy pyme" — estadísticas operativas sin tablero de dirección | §5, relevamiento interno | §2 Cadena de Valor (infraestructura) · §5 Gobierno 1.50 · **explica por qué el CoI no se puede cuantificar** |
| Segunda generación operando | §1.5 | §2 FODA (F5) · §3.3 corrige el BMC · §5 Gobierno (continuidad parcial) |

> **El encadenamiento más importante del trabajo:** "no, muy pyme" (§5) → estadísticas operativas que no se integran en indicadores de dirección → Gobierno en 1.50 (§5.3) → la empresa no puede cuantificar su propio CoI (§5.5). El diagnóstico muestra así la distancia entre **producir datos** y **usarlos sistemáticamente para decidir y controlar**.

## Correcciones al BMC

El canvas fue escrito antes del relevamiento con el integrante que trabaja en la empresa. Las siguientes correcciones **ya están aplicadas en `BMC - Dulxelitos.md`**:

| # | Dónde | Qué decía | Qué dice ahora |
|---|---|---|---|
| 1 | Bloque 3 (Canales) | "el catálogo está vacío" | El catálogo **está publicado**; lo vacío es el carrito. La tienda está construida y sin operar |
| 2 | Bloque 3, nota al pie | "Evidencia de abandono del canal digital" | Canal **terminado y desactivado**, no abandonado a medio hacer |
| 3 | Bloque 6 (Recursos clave) | Conocimiento concentrado en los dueños, sin matices | Se agrega la **segunda generación operando**: lo concentrado es el criterio estratégico, no la operación |
| 4 | Síntesis, punto 4 | Dependencia crítica de los dueños | Continuidad operativa cubierta; decisión estratégica concentrada |
| 5 | Síntesis, punto 5 | "nunca se puso a producir... catálogo vacío" | Canal completo **dejado apagado**: capacidad instalada sin usar, la oportunidad más barata del modelo |
| 6 | Segmento 1 | ❓ concentración de facturación pendiente de relevar | Consultado: **el dato no existe**, la empresa no mide la concentración de su cartera. La ausencia es el hallazgo |
| 7 | Nota sobre domicilios | ❓ pendiente de confirmar | Resuelta: **planta, depósito y oficina en Av. Pedro Vargas 2400** |
| 8 | Pie del documento | "Pendiente: lectura analítica" | Remite a `03 - Lectura analítica del BMC.md` |

> ⚠️ **El PDF del canvas quedó desactualizado.** `BMC - Dulxelitos.pdf` es el diagrama visual de los nueve bloques y todavía dice *"Sin tienda online operativa — el sitio existe, el catálogo está vacío"* y *"Conocimiento concentrado en los dueños"*. Fue generado desde un HTML que no está en esta carpeta, así que **hay que regenerarlo con esas dos celdas corregidas antes de entregar**. Si se entrega el PDF sin corregir, contradice al `.md`.

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

Las iniciativas derivadas del FODA cruzado (§2.5) se presentan como **derivación analítica de la herramienta**, no como propuesta: es lo que la propia técnica del FODA cruzado produce, y el enunciado pide aplicarla.
