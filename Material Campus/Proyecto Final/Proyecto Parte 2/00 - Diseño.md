# TP Final Parte 2 · Dulxelitos — Documento de diseño

Fecha: 2026-11-05. Estado: borrador para revisión del grupo.

Este documento fija las decisiones de la Parte 2 antes de escribirla. Quien redacte las secciones tiene que poder
hacerlo sin volver a preguntar. Lo que decidió el grupo está marcado como **(grupo)**; lo que decidió Claude, como
**(decisión de Claude)**, para que el grupo lo revise.

---

## 1. Para qué es y por qué

La Parte 2 convierte el diagnóstico de la Parte 1 en una **propuesta gerencial viable para una pyme**. La consigna
oficial está en `Material Campus/Proyecto Final/Trabajo Práctico Final - Parte 2.md` (8 secciones) y la guía resuelta
de la cátedra en `Guía Ejemplo Proyecto Final - Parte 2.md` (caso Distribuidora Montaña).

Lo que la cátedra va a mirar, según las clases:

- **La tecnología es un medio, no el fin.** El problema no nombra herramientas (Clase 3). Digitalizar sin rediseñar
  no mejora el tiempo de ciclo (Noguerol, 19-10, ejemplo de la firma digital de planos).
- **Proporcionalidad.** Una pyme de 15 a 20 personas: no se premia la sofisticación (enunciado y Clase 3).
- **Coherencia con la Parte 1.** Cada decisión tiene que poder rastrearse al diagnóstico, como en el documento de
  integración de la Parte 1.
- **Medir con línea de base.** "Sin línea de base no hay mejora" (Pino, 05-10). Datos faltantes: supuesto declarado.
- **Procesos balde.** Antes de mejorar un proceso, preguntar si agrega valor o solo contiene un error previo
  (Noguerol, 05-10).

## 2. El problema elegido (grupo)

**Gestión del stock de producto terminado**, que une ventas, depósito y producción.

Situación real relevada (grupo, fuente: Juanjo Geyer, que trabaja en Dulxelitos):

- **No se lleva stock de producto terminado en el depósito**: ni en Discovery ni en ningún otro registro.
- Producción lleva su propio control, **pero no se relaciona con las ventas**: son independientes.
- Los pedidos se comprometen **sin mirar** si hay mercadería.
- **Todas las semanas** hay faltantes o pedidos recortados.
- Entran **~25 pedidos por día** de distribuidores (~125 por semana).
- La producción la deciden **el dueño o los hijos** por criterio propio.
- También hay problemas con insumos y packaging, pero **quedan fuera de alcance** (ver §5).

### Corrección a la Parte 1 (obligatorio decirlo)

La Parte 1 afirma que el stock está en Discovery (§5.2, Tecnología y Datos / Procesos) y que los pedidos incompletos
"son poco frecuentes y se resuelven fácil" (§5.5). El relevamiento del proceso para la Parte 2 lo **corrige**: el
stock de producto terminado no se registra y los recortes son semanales. La Parte 2 lo dice explícitamente, al
principio, como la Parte 1 hizo con el catálogo web: el cruce de fuentes corrigió un dato. Esto además **refuerza** el
diagnóstico de Gobierno (1.50) y explica por qué el costo de no actuar no se podía cuantificar.

### Causa de los recortes (grupo)

Los recortes vienen sobre todo de **mezcla y momento**: se produce lo que no hace falta y falta lo que se pide, porque
la producción se decide sin mirar pedidos. La planta sigue saturada (Parte 1), pero los recortes semanales no se
explican por la capacidad total. Esto también matiza la Parte 1, que atribuía los faltantes a la capacidad: la
Parte 2 lo aclara junto con la corrección del stock. Consecuencia: planificar contra pedidos **ataca la causa**, y
las metas de "pedidos completos y a tiempo" pueden prometer una baja real de recortes. Aun así, que la mezcla explique
la mayoría de los recortes queda como **supuesto crítico a medir en el piloto** (decisión de Claude).

### Problema gerencial (§6 de la Parte 1, que estaba pendiente) — borrador

> Dulxelitos recorta o demora unos 30 de sus ~125 pedidos semanales porque los acepta sin conocer el stock de
> producto terminado, que no se registra, y decide la producción sin mirar las ventas. Esto genera faltantes,
> reprogramaciones y unas 25 horas extras mensuales sobre una planta saturada. Éxito: pedidos completos y a tiempo
> del 76 % al [meta] % en 6 meses.

(~55 palabras. La meta la fija quien redacte, con criterio realista para una pyme; por ejemplo 90 %.)

Reglas: máximo 60 palabras, sin "sistema", "software", "app" ni "módulo" (checklist de la Clase 3). Completar la
magnitud con los datos de Juanjo (§9). Se incluye como **sección inicial** de la Parte 2 (decisión de Claude), porque
la Parte 2 depende de él y la Parte 1 lo dejó para "entregar por separado".

## 3. El proceso (grupo, con supuestos marcados)

**Nombre:** "Atender pedido de distribuidor" (verbo + sustantivo).
**Empieza:** llega un pedido del distribuidor por WhatsApp o teléfono.
**Termina (camino feliz):** pedido facturado en Discovery y despachado.
**Volumen:** ~25 pedidos/día. **Áreas:** oficina, depósito, producción, dirección.

### AS-IS (grupo)

1. Oficina recibe el pedido (WhatsApp/teléfono) y lo anota **en papel o planilla**.
2. Para saber si hay mercadería: se **mira a ojo** en el depósito **y** se **pregunta a producción**.
3. Se pasa a **una lista** y depósito **prepara el pedido**.
4. Si falta producto: se **manda incompleto** avisando, o se **espera producción**, y si hace falta se hacen
   **horas extras**.
5. Oficina **factura en Discovery** y se **despacha** (flota propia o transporte tercerizado).
6. En paralelo e independiente: **dueño o hijos deciden qué producir**; producción registra lo suyo sin vínculo con
   pedidos.

**Pools y lanes (decisión de Claude):** pool Dulxelitos con lanes Oficina, Depósito, Producción, Dirección (dueño e
hijos); pool colapsado Distribuidor; pool colapsado Transporte tercerizado. Flujos de mensaje entre pools; flujo de
secuencia solo dentro del pool (Clase 6).

**Tres lentes (Clase 7), lectura esperada:**
- Ineficiencia: doble averiguación de disponibilidad (a ojo + preguntar); bucle de espera de producción.
- Tarea manual: chat → papel → lista, tres transcripciones del mismo pedido.
- Flujo de datos: producción, depósito y ventas no comparten ningún dato; no existe stock registrado.

### TO-BE (decisión de Claude, sobre la alternativa recomendada)

- Producción **carga cada día** lo producido en Discovery (ingreso de stock).
- Oficina **carga la nota de pedido en Discovery y reserva el stock** antes de confirmar (grupo: Discovery permite
  pedidos y reserva). **Stock disponible = stock físico − reservado por pedidos confirmados sin facturar**
  (decisión de Claude; la planilla del piloto usa la misma definición). Si falta, avisa al distribuidor en el momento
  con fecha estimada en vez de enterarse al armar.
- Depósito arma desde el pedido confirmado; la facturación en Discovery consume la reserva.
- Dirección planifica la producción semanal mirando **pedidos pendientes y un stock mínimo por producto**.
- Controles simples: conteo cíclico semanal, tablero con los 4 indicadores, responsable de carga por turno,
  **reunión corta diaria ventas–producción** (~10 min).

## 4. Alternativas y recomendación (grupo)

| Alternativa | Qué es |
|---|---|
| Do Nothing | Seguir igual: recortes semanales y horas extras |
| A. Planilla compartida | Incremental: Google Sheets de stock de producto terminado, carga diaria de producción, descuento por pedido, reunión diaria. Costo casi cero |
| B. Stock de Discovery | Intermedia: activar el módulo de stock que **ya tienen en la licencia y no usan** (grupo); conteo físico inicial |
| C. SaaS de gestión | Solo en la matriz como **evaluada y descartada** (decisión de Claude): costo, migración y no resuelve el problema de disciplina de carga |

**Recomendación (grupo):** **B como solución y A como piloto/MVP** de 2 semanas sobre **papas fritas** (el producto
que más falta). Lógica: si el equipo no sostiene la carga en una planilla simple, tampoco la va a sostener en
Discovery. El piloto es el experimento de la §7 y la decisión Go/No-Go de la §8.

**Matriz multicriterio:** los 10 criterios del enunciado (alineación, costo, viabilidad operativa, tiempo, adopción,
complejidad, capacidad interna, integración, flujo de caja, continuidad), escala 1 a 5 con justificación por celda
(decisión de Claude). Presupuesto: el dueño acepta **inversión mayor si se demuestra retorno** (grupo); usar el costo
de no actuar como techo y payback/VAN de la Clase 7 y el 19-10, sin inventar cifras.

## 5. Alcance

**Dentro:** stock de producto terminado; proceso de pedido desde recepción hasta despacho; planificación semanal de
producción contra pedidos; indicadores y rutina de seguimiento.

**Fuera (grupo y decisión de Claude):**
- Insumos y packaging (se declara como deuda; proveedor único de film ya está en la Parte 1).
- **Visibilidad de stock para el distribuidor** (grupo: solo interno). Va al roadmap como **"later"** junto con la
  tienda de 2020.
- Ampliación de planta, cambio de Discovery por otro sistema, CRM, costeo.

## 6. Personas y stakeholders

- **Sponsor: el dueño**, que aprueba presupuesto y Go/No-Go; **líder del proyecto: el responsable de sistemas**
  (grupo, confirmado). Ojo: la Parte 1 dice que ese rol no tiene asignada la gobernanza; la propuesta se la asigna
  formalmente como parte del cambio.
- Resistencias esperadas (grupo): **Producción** (cargar lo producido es trabajo nuevo con la planta saturada) y
  **Oficina** (consultar stock antes de confirmar suma un paso).
- Matriz **Mendelow (poder/interés)**, no influencia–impacto (la lámina 24 de la Clase 4 aclara que el TP pide
  Mendelow). Actores: dueño, hijos, responsable de sistemas, oficina, depósito, producción, Buenos Aires Software
  (proveedor de Discovery), distribuidores (afectados indirectos). Por actor: interés, poder, impacto, resistencias,
  estrategia. Incluir cómo cambian de cuadrante por fase (23-10).
- Herramientas de la Clase 4 para las estrategias: FUD (miedo, incertidumbre, duda), técnico vs. adaptativo
  (Heifetz: la carga en Discovery es técnica; que producción planifique contra pedidos es adaptativo), ADKAR.

## 7. Indicadores, OKR y plazos (grupo)

**Plazo del objetivo general: 6 meses** (grupo). Inicio en cualquier momento: demanda pareja todo el año (grupo).

| Indicador | Familia | Notas |
|---|---|---|
| Pedidos completos y a tiempo (%) | Resultado / experiencia | "A tiempo" = dentro del **plazo estándar por zona** (grupo; Patagonia hasta una semana, Parte 1). Contrapeso: pedidos rechazados o reprogramados de entrada |
| Exactitud de stock (%) | Calidad de datos | Conteo cíclico semanal vs. sistema |
| Días con producción cargada (%) | Adopción, indicador de avance | Avisa antes de que falle la exactitud |
| Horas extras por mes | Eficiencia / financiero | **Totales** de la liquidación de sueldos (decisión de Claude: la liquidación no distingue las no planificadas) |

Cada uno con la **ficha de 8 elementos** (título, propósito, unidad, fórmula, fuente, frecuencia, dueño, meta) y meta
en **5 partes** (acción, métrica, valor actual, objetivo, plazo) — Clase 5.

**OKR de la iniciativa (grupo: sí):** objetivo en palabras del tipo "Que cada pedido se confirme sabiendo qué hay",
con 3 resultados clave tomados de los indicadores (decisión de Claude sobre la redacción).

**Roadmap (decisión de Claude, ajustable):** now/next/later (23-10) con fases tipo guía: preparación y conteo
inicial → piloto planilla 2 semanas (papas fritas) → Go/No-Go → activar Discovery por línea de producto →
estabilización. "Later": visibilidad al distribuidor y tienda 2020. Proteger la operación: carga al cierre de turno,
suplente de carga, conteo inicial en fin de semana.

## 8. Formato y entregables (grupo)

- Igual que la Parte 1: secciones en `.md` en `Material Campus/Proyecto Final/Proyecto Parte 2/`, script que arma
  **docx y pdf**, **pptx** de 8–10 láminas (~10 min, 5 expositores) y **guion de exposición en PDF**.
- **No publicar Artifacts** desde esta cuenta (grupo).
- Portada con **los cinco**: Lepez Joaquín, Geyer Juan José, Lopez Juan, Olivares Manuel, Sorato Emiliano.
  Docentes: Ing. Jeremías Pino, Ing. Martín Noguerol.
- **BPMN generados por Claude** (grupo): archivos `.bpmn` (abren en Bizagi/Camunda) más imagen para el informe;
  AS-IS y TO-BE. Antes del BPMN: matriz de descubrimiento, SIPOC (4–6 pasos) y RECI (un solo responsable por
  actividad) — Clase 6.
- Mismo tono que la Parte 1: lenguaje llano, sin inventar datos, supuestos marcados, fuentes declaradas.

## 9. Datos pendientes

Datos recibidos del grupo (Juanjo, 2026-11-05):

| Dato | Valor | Uso |
|---|---|---|
| Pedidos recortados o demorados por semana (una semana de registro) | **30 por semana** | Sobre ~125 pedidos semanales (25/día × 5): **~24 % recortados o demorados → ~76 % completos y a tiempo**. Es la línea de base del indicador principal (el 76 % es un cálculo nuestro, declararlo así) |
| Horas extras mensuales | **~25 horas por mes** | Línea de base del indicador de horas extras y componente del costo de no actuar (falta el costo por hora: **[dato pendiente]**) |
| Carga de lo producido | **Hoy se carga una vez por semana** (en el control propio de producción, no vinculado a ventas) | Línea de base del indicador de adopción: hoy 1 de 5 días hábiles = **20 %**; meta TO-BE: carga diaria |
| Tiempo de armado de un pedido | No se mide; el grupo dice que es rápido y no hace falta | Se descarta: no es la restricción |

Pendiente para el costo de no actuar: costo de la hora extra y margen o valor promedio de un pedido recortado.

Mientras no estén (decisión de Claude): **no se inventan números**. Cada cifra faltante queda como hueco marcado
**[dato pendiente: …]** con la redacción lista para completar, igual que el "no observado" de la Parte 1. El retorno
se muestra como **punto de equilibrio y sensibilidad** ("B se paga si evita X horas extras por mes"), no como VAN con
cifras inventadas. Se escribe todo así desde el principio y se hace una pasada de reemplazo cuando lleguen los datos.

## 10. Qué queda a criterio de quien redacte

Puntajes de la matriz multicriterio, redacción final del OKR y de las metas (usando supuestos marcados), layout de
los BPMN, diseño de las láminas, y el cálculo del costo de no actuar en cuanto lleguen los datos.
