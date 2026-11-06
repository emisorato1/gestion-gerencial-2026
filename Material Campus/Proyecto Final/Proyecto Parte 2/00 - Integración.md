# Trabajo Práctico Final — Parte 2 · Dulxelitos
## Documento de integración

Este documento no agrega contenido: **traza cómo se encadenan las ocho secciones de la Parte 2**, como el de la Parte 1. Cada decisión tiene que poder rastrearse hasta el diagnóstico. Es de trabajo del grupo y **no forma parte del informe**: `armar-entrega.py` arma la entrega con las secciones 01 a 08, más portada, introducción, bibliografía y anexos.

---

## Archivos

Todo está en `Material Campus/Proyecto Final/Proyecto Parte 2/` (`P2/`).

| Archivo | Sección del enunciado (Parte 2) | Estado |
|---|---|---|
| `01 - Problema y objetivos.md` | 1. Objetivo y alcance, más el **problema gerencial** que la Parte 1 dejó pendiente (su sección 6) y la **corrección a la Parte 1** | Completa, 5 datos pendientes |
| `02 - Proceso actual y alternativas.md` | 2. AS-IS y alternativas (SIPOC, RECI, tres lentes, matriz multicriterio, recomendación) | Completa, 10 |
| `03 - Proceso futuro.md` | 3. TO-BE | Completa, 4 |
| `04 - Modelo de negocio y propuesta de valor.md` | 4. BMC Shift, VPC TO-BE y supuestos | Completa, 4 |
| `05 - Stakeholders.md` | 5. Stakeholders (Mendelow) | Completa, 3 |
| `06 - Arquitectura y datos.md` | 6. Arquitectura conceptual y flujo de datos | Completa, 5 |
| `07 - Validación de supuestos.md` | 7. Derisking: piloto y prueba técnica | Completa, 9 |
| `08 - Roadmap e indicadores.md` | 8. Roadmap, protección de la operación, OKR e indicadores | Completa, 10 |
| `bpmn/` | Diagramas de 2 y 3: `as-is.py` y `to-be.py` son la especificación; `generar_bpmn.py` escribe `.bpmn` (abre en Bizagi o Camunda), `.svg` y `.png` | Completo |
| `diagramas/` | Diagrama de 6: `generar_arquitectura.py` escribe `arquitectura.svg` y `.png` | Completo |
| `verificar.py` | Reglas sobre las secciones (qué revisa cada una: su docstring). Saltea los `00 - *` | Da OK |
| `00 - Diseño.md`, `00 - Plan.md` | Decisiones y plan previos. Internos | — |
| **`Entrega/`** | **lo que se entrega: md, docx, pdf y pptx del informe, el guion de exposición en PDF, los dos `.bpmn` y el flujo de datos interactivo (html)** | **generada**, no editar a mano; el guion ya está |
| `armar-entrega.py`, `armar-presentacion.js` (con `package.json`), `guion-exposicion.html` | arman la entrega (y copian los `.bpmn`), el pptx y, con weasyprint, el guion en PDF | ver abajo |


## Cómo se rearma

Desde `P2/`; lo pesado, con `nice -n 10` y de a uno. Cada vez que alguien toca una sección hay que volver a correr, para que la entrega no quede desfasada:

```bash
.venv/bin/python verificar.py                      # debe decir OK
nice -n 10 .venv/bin/python armar-entrega.py       # md, docx y pdf en Entrega/
nice -n 10 node armar-presentacion.js "Entrega/Presentación TP Final Parte 2 - Dulxelitos.pptx"
nice -n 10 .venv/bin/weasyprint guion-exposicion.html "Entrega/Guion de exposición Parte 2 - Dulxelitos.pdf"
```

Si cambió un diagrama, antes: `bpmn/generar_bpmn.py bpmn/as-is.py` (o `to-be.py`) o `diagramas/generar_arquitectura.py`. El `node` necesita `npm install` una vez. A mano, después: abrir el docx en Word y actualizar el índice (F9); se armó sin verlo renderizado.

## Última pasada de texto

Las secciones 01 a 08 pasaron de ~25.500 a ~22.850 palabras (unas 2.700 menos), sin tocar las tablas ni lo que pide la consigna. Lo que se corrigió:

- **Reparto parcial** (reservar una parte y dejar el resto pendiente): se confirma con Buenos Aires Software en la prueba técnica, dentro del paso 2 de los cinco (06 reglas de nota de pedido y reserva; 07; también 03, 04 y 06 lo nombran en el supuesto 3).
- **Sin ambiente de prueba**: la prueba técnica pasa con los pasos que se pueden probar y el de la factura queda para el primer pedido real de la activación; no bloquea el Go (07, alineado con 02 y 08).
- **Orden de activación**: Salados va primero porque arranca con el piloto de papas fritas; lo pendiente es en qué orden se activan Dulces y Repostería (08).
- **Estilo**: "que verifica la prueba técnica" (02, 03) y "Depósito cuenta (quién, a confirmar)" (08).

Lo que se recortó, sin repetir en cada sección:

- **Tablero y datos**: la descripción completa queda solo en 08 ("Cómo se mira el tablero"); 03 y 06 tienen una frase con referencia, y 03 ya no repite la tabla de cuándo se genera cada dato (está en 06).
- **05**: FUD y ADKAR en una sola tabla y "Cómo negociamos" en tres viñetas. **06**: las reglas de alta, corrección y depuración, en una tabla por dato. **07**: "Hipótesis en una hoja" más corta (los umbrales quedan en "Qué se mide"), mecanismo y qué se anota en una sola columna y "Qué queda para después de activar" en un párrafo que remite a 08. **08**: sin las tres "Meta en una oración" que repetían la fila Meta (queda la del indicador 1, como ejemplo del formato de la Clase 5).
- **02**: el párrafo de sensibilidad de pesos más corto (post hoc, cruce en ~1,25, empate en 38, no prueba nada) y sin "Qué podría cambiar la recomendación", que ya dice la tabla de decisión de la 07.
- **Repeticiones sacadas**: el punto de equilibrio (04 remite a 02), la regla de stock disponible (06 y 07 remiten a 03), "Quién gana más" (04, en dos frases) y "Cómo se sabe que se cumplen" (06; la revisión de reglas en cada Go/No-Go sigue en 06 y 08).

Las cuentas de datos pendientes no cambian (25 filas en el Anexo I): solo cambió el texto del dato del orden de activación, que ahora es "en qué orden se activan Dulces y Repostería".

## La cadena

```
Parte 1: Gobierno 1.50 · planta saturada · Discovery desactualizado y sin integración
   │     distribuidor conforme · tienda sin catálogo desde 2020
   ▼
01 Problema, objetivos y alcance ◄── corrige la Parte 1 (stock, frecuencia, causa)
   │  pasa: problema gerencial, tres líneas de base (76 %, 20 %, ~25 horas), proceso y límites
   ▼
02 AS-IS ──► tres lentes ──► una sola causa vista desde tres lados (gotera, no baldes)
   │  pasa: Do Nothing · A planilla · B stock de Discovery · C SaaS (descartada)
   │  matriz: A 36, B 35 → decide el argumento cualitativo
   ▼
   recomendación: B como solución, A como piloto de 2 semanas con papas fritas
   ▼
03 TO-BE: el proceso de B, con "disponible = físico − reservado"
   │  pasa: carga diaria, reserva antes de confirmar, plan semanal; lo que da por cierto sin probar
   ▼
04 BMC y VPC TO-BE: 4 de 9 bloques cambian, casi todo backstage
   │  pasa: nueve supuestos (el 1 es el crítico)
   ▼
05 Stakeholders: quién carga, quién decide, quién frena
   ▼
06 Arquitectura y datos: un solo lugar por dato, carga manual controlada, reglas
   ▼
07 Validación: piloto (planilla, papas fritas) + prueba técnica de Discovery
   │  pasa: umbrales y tabla Go / No-Go
   ▼
08 Roadmap, OKR e indicadores: 5 fases en 6 meses; el OKR son los tres objetivos de la 01
```

La cadena cierra el círculo: lo que la 01 promete es lo que la 08 mide.

## Trazabilidad de los hallazgos

| Hallazgo | De dónde sale | Dónde se usa después |
|---|---|---|
| **El stock de producto terminado no se registra** | Relevamiento con nuestro compañero que trabaja en Dulxelitos. **Corrige** la Parte 1 (§5.2, §5.4) | 01 causa raíz · 02 tercera lente y alternativas A y B · 03 regla de disponible · 04 recurso clave nuevo · 06 reservas, partes y conteos, con reglas de alta, corrección y depuración · 07 conteo inicial y prueba técnica · 08 indicador 2, con línea de base del primer conteo |
| **30 de ~125 pedidos por semana recortados o demorados** (76 % completos y a tiempo, cuenta nuestra) | Relevamiento. **Corrige** la Parte 1 (§5.5, "poco frecuentes") | 01 problema y objetivo 1 · 02 matriz de descubrimiento · 04 VPC (todas las semanas, no "en algunas temporadas") y supuesto 9 · 05 ADKAR del dueño y los hijos · 07 no sirve de base del piloto: hay que medir la semana 0 de papas fritas · 08 indicador 1 y primer resultado clave |
| **La producción se carga 1 vez por semana** (20 %) | Relevamiento: control propio de Producción, sin vínculo con ventas | 01 objetivo 2 · 02 dependencia informal y tercera lente · 03 carga diaria con responsable y suplente · 04 supuesto 2 · 05 resistencia de Producción · 06 partes de producción · 07 umbral de 8 de 10 días · 08 indicador 3 y regla de freno |
| **~25 horas extras por mes** | Relevamiento. En la Parte 1 era dato pendiente del costo de no actuar (§5.5) | 01 objetivo 3 y meta (supuesto) · 02 costos y retorno de B como punto de equilibrio · 03 excepción del plan semanal · 04 supuestos 7 y 8 · 06 dato de la liquidación al tablero · 07 se anota el motivo de cada hora · 08 indicador 4 y regla de freno |
| **Mezcla y momento, no capacidad total, explican la mayoría de los recortes** (supuesto 1) | Hipótesis nuestra, no medida. **Corrige** la Parte 1 (§2.1, "capacidad de planta") | 01 por qué 90 % y no 100 % · 02 por qué A va primero · 03 plan contra pedidos y stock mínimo · 04 supuesto 1 · 05 Heifetz: cambio adaptativo · 07 la semana 0 anota la causa; filas No-Go · 08 tablero en rojo y Go/No-Go de cierre, que revisa la meta |
| **Discovery tiene módulo de stock, pedidos y reserva sin usar** (supuesto 3) | Lo que sabe nuestro compañero; nadie lo usó en Dulxelitos. Parte 1: Discovery desactualizado y sin integración | 02 alternativa B y riesgo propio · 03 TO-BE en Discovery · 04 supuesto 3 y costos pendientes · 05 Buenos Aires Software · 06 un solo lugar por dato, CSV · 07 prueba técnica de cinco pasos (el reparto parcial, en el paso 2) · 08 fase 4, con costo y plazo como dependencias |
| **Se averigua dos veces la disponibilidad y el pedido se transcribe tres veces** | Relevamiento: lentes 1 y 2 de la 02 | 03 una consulta y una carga · 05 trueque con Oficina · 06 nota de pedido y lista de armado · 08 carga de trabajo |
| **Dueño o hijos deciden qué producir por criterio propio, sin mirar pedidos** | Relevamiento. Parte 1: conocimiento sin formalizar (§1.5) | 02 RECI, nadie consultado · 03 plan semanal · 04 supuesto 5 · 05 hijos como posible resistencia (hipótesis nuestra) · 06 stock mínimo que fija Dirección · 07 señal del supuesto 5 · 08 Dirección mira el tablero |
| **El responsable de sistemas lidera sin gobernanza asignada** | Parte 1: Gobierno 1.50 (§5) | 01 se la asigna · 03 ejecuta ajustes y tablero · 05 sobrecarga y tiempo pendiente · 06 varias reglas caen en él · 08 suplente más delicado |
| **El distribuidor está conforme; visibilidad de stock y tienda de 2020** | Parte 1 (§3.2, §4.2, §4.4) | 01 fuera de alcance · 04 "later": hoy no hay stock confiable que mostrar, y supuesto 6 · 05 distribuidores informados · 07 señal del supuesto 6 · 08 "más adelante" |

> **El encadenamiento más importante:** la causa de los recortes → qué se rediseña → cómo se prueba → qué se decide. "Mezcla y momento" (01) → no alcanza con cargar stock, hay que planificar contra pedidos (02, 03) → es el supuesto 1, el que decide si la propuesta vale la pena (04) → la semana 0 anota la causa de cada recorte y el piloto mide cuántos bajan (07) → si no bajan y las causas son de capacidad, No-Go de B y se revisa la meta (07, 08). Ninguna meta sale de una medición: son propuestas nuestras.

## Las correcciones a la Parte 1

Son tres. Las dos de fondo: el **stock no se registra**, y **los recortes no vienen de la capacidad total sino de mezcla y momento**. La tercera: **los recortes pasan todas las semanas**. La 01 las dice al principio, como la Parte 1 hizo con el catálogo web. La regla `parte1` de `verificar.py` vigila que nadie repita la afirmación vieja sin aviso.

| Qué decía la Parte 1 | Qué dice la Parte 2 | Dónde |
|---|---|---|
| "Facturación y stock" digitalizados (§5.2, §5.4) | La factura sí está en Discovery; el stock no se lleva en ningún registro | 01 primer párrafo (solo ahí: las demás secciones la citan sin repetirla) |
| Incompletos "poco frecuentes y se resuelven fácil" (§5.5) | 30 de ~125 en una semana (~24 %): ~76 % completos y a tiempo, cuenta nuestra | 01 segundo párrafo; 04 "Una corrección al VPC"; 05 ADKAR |
| Faltantes por "capacidad de planta" (§2.1) | Planta saturada sí, pero los recortes vienen sobre todo de mezcla y momento; hipótesis a probar | 01 tercer párrafo; supuesto 1 de 04; 07 |

La 01 aclara además que **no se vuelve a puntuar la encuesta**: dos ítems (automatización y digitalización de procesos clave) quedaron sobreestimados, y el nivel global sigue Inicial.

## Datos pendientes

Ninguno bloquea la entrega. Se juntan, sin repetir (25 filas hoy), en el **Anexo I** del informe (sale de `armar-entrega.py`; la lista cruda con archivo y línea, de `verificar.py`, por la salida de error). Los que conviene conseguir antes:

- **Costo por hora extra** (1, 2, 4, 7 y 8): preguntarle a Oficina (administración), que maneja la liquidación. Con el costo mensual de B completa el punto de equilibrio.
- **Costo de activar el módulo, costo mensual de B, plazo, versión y soporte de Discovery** (2, 4, 5, 7 y 8): consulta por escrito a Buenos Aires Software.
- **Quién cuenta**, el conteo inicial y el semanal (3, 5, 6, 7 y 8): acordarlo con Depósito y el dueño. Sin conteo no hay stock inicial ni piloto.
- **Línea de base de papas fritas en la semana 0** (7): sin ella no se evalúa "la mitad o menos".
- **Si la semana base incluyó rechazados de entrada** (1 y 8), **cuántos turnos tiene la planta** (1) y **cómo entran hoy los pedidos de Aiello y del viajante** (1): tres preguntas a nuestro compañero que trabaja en Dulxelitos.

El resto son preguntas o acuerdos chicos; el margen de un pedido recortado no hace falta para decidir.

## Decisiones que el grupo tiene que confirmar

1. **Hijos como posible resistencia** (05): hipótesis nuestra, "no relevada". Si nuestro compañero que trabaja en Dulxelitos lo ve distinto, se ajusta la ficha y la tabla de FUD y ADKAR.
2. **Hoja compartida de Oficina para el registro de recortes** (06, y fuente del indicador 1 en 08): propuesta nuestra, no hablada con Oficina.
3. **Meta de horas extras de ~12 o 13** (01, 08): la mitad de las ~25, supuesto que se apoya en el supuesto 7. A confirmar con el dueño. Lo mismo la **meta provisional de exactitud** (9 de cada 10 productos dentro de la tolerancia, 01, 07 y 08) y el **orden en que se activan Dulces y Repostería** (Salados va primero, porque arranca con el piloto de papas fritas, 08).
4. **Umbrales del piloto** (07): 8 de 10 días con carga, recortes a la mitad o menos, conteo con diferencia de hasta una décima parte, 4 de cada 5 fechas cumplidas. Propuesta nuestra; el dueño los acuerda antes de arrancar.
5. **A4 en vez de Letter** (`armar-entrega.py`): la Parte 1 salió en Letter, pero las hojas apaisadas del BPMN se ven mal mezcladas. Volver a Letter es una línea (`size: A4` en el CSS, `A4_W` y `A4_H`).

También son propuestas nuestras: la meta de 90 %, los puntajes de la matriz (A y B casi empatan), quién decide el faltante, las horas extras y el plan semanal, que la carga diaria reemplace al control semanal de Producción y las duraciones de las fases.
