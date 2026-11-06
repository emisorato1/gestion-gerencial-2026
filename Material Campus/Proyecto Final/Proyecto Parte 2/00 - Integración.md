# Trabajo Práctico Final — Parte 2 · Dulxelitos
## Documento de integración

Este documento no agrega contenido: **traza cómo se encadenan las ocho secciones de la Parte 2**, igual que el de la Parte 1. La Parte 2 tiene que poder leerse como una sola línea de razonamiento (el problema, el proceso, las alternativas, el proceso nuevo, el negocio, las personas, los datos, las pruebas y el calendario) y cada decisión tiene que poder rastrearse hasta el diagnóstico. Esta es la evidencia de ese encadenamiento, y además sirve para no perderse cuando alguien toca una sección: dice qué otras secciones se apoyan en ella.

Es un documento de trabajo del grupo. **No forma parte del informe**: `armar-entrega.py` arma la entrega solo con las secciones 01 a 08, más portada, introducción, bibliografía y anexos.

---

## Archivos

Todos los archivos están en `Material Campus/Proyecto Final/Proyecto Parte 2/` (en esta tabla, `P2/`).

| Archivo | Sección del enunciado (Parte 2) | Estado |
|---|---|---|
| `01 - Problema y objetivos.md` | 1. Objetivo y alcance, más el **problema gerencial priorizado** que la Parte 1 dejó pendiente (su sección 6) y la **corrección a la Parte 1** | Completa, con 2 datos pendientes |
| `02 - Proceso actual y alternativas.md` | 2. Proceso actual (AS-IS) y alternativas de solución: matriz de descubrimiento, SIPOC, RECI, diagrama, tres lentes, alternativas, matriz multicriterio y recomendación | Completa, con 8 datos pendientes |
| `03 - Proceso futuro.md` | 3. Diseño del proceso futuro (TO-BE): diagrama, responsables, criterios de decisión, datos y controles | Completa, con 4 datos pendientes |
| `04 - Modelo de negocio y propuesta de valor.md` | 4. Transformación del modelo de negocio (BMC Shift), VPC TO-BE y supuestos clave | Completa, con 4 datos pendientes |
| `05 - Stakeholders.md` | 5. Stakeholders del proyecto de mejora (mapa, matriz poder/interés de Mendelow, estrategias) | Completa, con 3 datos pendientes |
| `06 - Arquitectura y datos.md` | 6. Arquitectura conceptual y flujo de datos | Completa, con 5 datos pendientes |
| `07 - Validación de supuestos.md` | 7. Derisking y validación de supuestos (incluye el piloto y la prueba técnica) | Completa, con 9 datos pendientes |
| `08 - Roadmap e indicadores.md` | 8. Roadmap preliminar, cómo se protege la operación, OKR e indicadores | Completa, con 10 datos pendientes |
| `bpmn/` | Diagramas de las secciones 2 y 3 | `as-is.py` y `to-be.py` son la especificación; `generar_bpmn.py` escribe el `.bpmn` (abre en Bizagi o Camunda), el `.svg` y el `.png`, que es el que entra al informe |
| `diagramas/` | Diagrama de la sección 6 | `generar_arquitectura.py` escribe `arquitectura.svg` y `arquitectura.png` |
| `00 - Diseño.md`, `00 - Plan.md` | — | Decisiones y plan de trabajo previos. Referencia interna, no se entregan |
| `verificar.py` | — | Corre las reglas sobre las secciones (ver abajo). Saltea los archivos `00 - *` |
| **`Entrega/`** | **lo que se entrega: md, docx, pdf y la presentación (pptx)** | **generada** — no editar a mano. El guion de exposición en PDF se suma cuando esté |
| `armar-entrega.py` | arma el md, el docx y el pdf desde las secciones | ver "Cómo se rearma" |
| `armar-presentacion.js` (con `package.json` y `package-lock.json`) | arma el pptx | ver "Cómo se rearma" |

Los datos pendientes de la tabla son los distintos que aparecen en cada archivo, sin repetir. La lista completa, y en qué secciones figura cada uno, está en el Anexo I del informe armado.

## Cómo se rearma

Siempre desde `P2/`. Lo pesado (el pdf y el pptx) va con `nice -n 10` y de a uno.

```bash
cd P2
.venv/bin/python verificar.py                              # debe decir OK
.venv/bin/python bpmn/generar_bpmn.py bpmn/as-is.py        # solo si cambió el diagrama
.venv/bin/python bpmn/generar_bpmn.py bpmn/to-be.py        # ídem; con --validar solo valida
.venv/bin/python diagramas/generar_arquitectura.py         # solo si cambió el diagrama de la sección 6
nice -n 10 .venv/bin/python armar-entrega.py               # md, docx y pdf en Entrega/
nice -n 10 node armar-presentacion.js "Entrega/Presentación TP Final Parte 2 - Dulxelitos.pptx"
```

El `node` necesita `npm install` una vez (`node_modules/` no se versiona), y el nombre de salida hay que pasarlo para que el pptx caiga en `Entrega/`.

**Se genera, no se edita.** Cada vez que alguien toca una sección hay que volver a correr `verificar.py` y `armar-entrega.py`, así la entrega nunca queda desfasada. Dos cosas se hacen a mano después de generarla:

- **Abrir el docx en Word, actualizar el índice (F9) y mirar las tablas anchas y el pie.** El docx se armó sin verlo renderizado: no hay Word en la máquina donde se generó.
- **Papel A4.** La Parte 1 salió en Letter; esta sale en A4 (ver "Decisiones que el grupo tiene que confirmar").

### Qué revisa `verificar.py`

| Regla | Qué exige | Para qué |
|---|---|---|
| `problema` | El problema gerencial de la sección 1 tiene hasta 60 palabras y no nombra ninguna herramienta (nada de "software", "sistema", "app", "módulo", "Discovery" ni "planilla") | La solución se elige recién en la sección 2 |
| `parte1` | Un archivo que junta la Parte 1 con el stock tiene que decir "corrige" o "corrección" | Que ninguna sección repita sin aviso lo que la Parte 1 afirmaba mal |
| `cifras` | Avisa de cualquier porcentaje, hora, mes o semana fuera de la lista del diseño (76, 24, 25, 30, 125, 20, 6 meses, 2 semanas) | Que no se cuele un número inventado. Es una advertencia, no una falla: los números propuestos (90 %, ~12 o 13 horas, los umbrales del piloto) salen ahí y se confirman a mano |
| `encabezados` | Cada archivo trae los `##` que pide su sección del enunciado | Que no falte una parte de lo pedido |
| `trazas` | Cada lane del BPMN AS-IS figura en el RECI de la sección 2, y cada indicador de la sección 8 trae su línea de base | Que el diagrama, la tabla de responsables y los indicadores hablen de lo mismo |
| `pendientes` | Lista cada `[dato pendiente: …]` con archivo y línea | Es la fuente del Anexo I |

## La cadena de la Parte 2

```
Parte 1 (diagnóstico)
   │  Gobierno 1.50 · planta saturada · Discovery desactualizado y sin integración
   │  distribuidor conforme · tienda sin catálogo desde 2020
   ▼
01 Problema, objetivos y alcance ◄── corrige la Parte 1: stock no registrado,
   │                                  recortes semanales, causa = mezcla y momento
   │  problema gerencial · 3 objetivos con línea de base (76 %, 20 %, ~25 horas)
   │  proceso "Atender pedido de distribuidor" · fuera de alcance
   ▼
02 AS-IS ──► tres lentes ──► una sola causa vista desde tres lados
   │  Do Nothing · A planilla · B stock de Discovery · C SaaS (evaluada y descartada)
   │  matriz multicriterio: A 36, B 35 → decide el argumento cualitativo
   ▼
   recomendación: B como solución, A como piloto de 2 semanas con papas fritas
   ▼
03 TO-BE: el proceso de B, con la regla "stock disponible = físico − reservado"
   │  carga diaria · reserva antes de confirmar · plan semanal contra pedidos
   ▼
04 BMC Shift y VPC TO-BE ──► 4 de 9 bloques cambian, casi todo backstage
   │  nueve supuestos (el 1 es el crítico)
   ▼
05 Stakeholders ──► quién carga, quién decide, quién frena (Mendelow, Heifetz, FUD, ADKAR)
   ▼
06 Arquitectura y datos ──► un solo lugar por dato, carga manual controlada, reglas de datos
   ▼
07 Validación ──► piloto (planilla, papas fritas) + prueba técnica de Discovery
   │  umbrales y tabla Go / No-Go
   ▼
08 Roadmap, OKR e indicadores ──► 5 fases en 6 meses, 4 indicadores con ficha,
                                   OKR = los 3 objetivos específicos de la sección 1
```

### Qué le pasa cada sección a la siguiente

| De → a | Qué pasa |
|---|---|
| **01 → 02** | El problema (se aceptan pedidos sin saber qué hay y se produce sin mirar las ventas), el proceso elegido y sus límites, y las tres líneas de base (76 %, 20 %, ~25 horas). La 02 abre con la corrección a la Parte 1 y mapea el mismo proceso, con los mismos límites |
| **02 AS-IS → 02 alternativas** | Las tres lentes (ineficiencia, tareas manuales, flujo de datos) no dan tres proyectos sino una causa vista desde tres lados. Con la pregunta del proceso balde (la gotera es no registrar el stock y producir sin mirar los pedidos), las alternativas se juzgan por si atacan la gotera o solo ponen baldes |
| **02 → 03** | La recomendación: B como solución y A como piloto. El TO-BE es el proceso de B, y el piloto corre el mismo flujo con la misma regla de stock; lo único que cambia es dónde vive el registro |
| **03 → 04** | Los cambios de trabajo (carga diaria, reserva antes de confirmar, plan semanal, reunión diaria, conteo) pasan a ser los bloques que cambian del canvas: actividades clave y un recurso clave nuevo, el registro de stock. Lo que el TO-BE da por cierto sin haberlo probado pasa a ser un supuesto |
| **04 → 05** | Los supuestos de factibilidad y deseabilidad (2: carga diaria con la planta saturada; 5: dueño e hijos deciden mirando pedidos) son de donde salen las resistencias. El cambio es técnico, con un borde adaptativo, para Producción; mixto para Oficina; y adaptativo para el dueño y los hijos |
| **03 + 05 → 06** | Los roles del RECI nuevo y los actores del mapa pasan a ser los responsables de cada dato. La 06 dice de dónde sale, adónde va y con qué reglas se mantiene limpio cada dato que el TO-BE necesita |
| **04 + 06 → 07** | Los nueve supuestos, cada uno con su probabilidad, impacto, señal temprana y mecanismo. El piloto contesta, al menos en parte, siete; el supuesto 3 (que Discovery reserve y que la factura consuma la reserva) tiene su prueba técnica; el 8 espera los datos de costo |
| **07 → 08** | Los umbrales y la tabla de decisión se ubican en el calendario como Go/No-Go (fase 3 y después de cada línea). Los tres objetivos de la 01 pasan a ser los resultados clave del OKR, y los cuatro indicadores traen su ficha, su contrapeso y su línea de base. **La cadena cierra el círculo:** lo que la 01 prometió es lo que la 08 mide |

## Trazabilidad de los hallazgos

Los hallazgos de la Parte 2 que más pesan. Las secciones son las de esta parte; "Parte 1" indica de dónde viene el dato anterior.

| Hallazgo | De dónde sale | Dónde se usa después |
|---|---|---|
| **El stock de producto terminado no se registra** (ni en Discovery ni en ningún otro lado) | Relevamiento con nuestro compañero que trabaja en Dulxelitos. **Corrige** la Parte 1 (§5.2 y §5.4) | 01 causa raíz técnica del problema · 02 tercera lente (flujo de datos, "el silo más grande") y alternativas A y B, que lo crean · 03 regla de stock disponible y momentos en que se genera el dato · 04 recurso clave nuevo · 06 reservas, partes de producción y conteos como datos, con sus reglas de alta, corrección y depuración · 07 conteo inicial del piloto y prueba técnica · 08 indicador 2 (exactitud), cuya línea de base sale del primer conteo |
| **30 de ~125 pedidos por semana salen recortados o demorados** (76 % completos y a tiempo, cuenta nuestra sobre una semana) | Datos del relevamiento. El 76 % es nuestra cuenta. **Corrige** la Parte 1 (§5.5: "poco frecuentes") | 01 problema gerencial y objetivo 1 · 02 matriz de descubrimiento y cuadro AS-IS · 04 VPC (los faltantes pasan todas las semanas, no "en algunas temporadas") y supuesto 9 (¿la semana es representativa?) · 05 ADKAR del dueño y los hijos (conciencia) · 07 por qué no sirve de base del piloto: son de todos los productos y hay que medir la semana 0 de papas fritas · 08 indicador 1, primer resultado clave y tablero |
| **La producción se carga 1 vez por semana** (20 % de los días hábiles) | Relevamiento: es el control propio de Producción, sin vínculo con ventas | 01 objetivo 2 · 02 AS-IS (dependencia informal) y tercera lente · 03 carga diaria al cierre de turno, con responsable por turno y suplente · 04 supuesto 2 · 05 resistencia esperada de Producción y trueque de negociación (reemplaza al control semanal) · 06 partes de producción · 07 umbral del piloto (8 de 10 días) · 08 indicador 3, segundo resultado clave y regla de freno |
| **~25 horas extras por mes** | Relevamiento. La Parte 1 lo tenía como dato pendiente del costo de no actuar (§5.5) | 01 objetivo 3 y meta de la mitad, que es supuesto · 02 costos del AS-IS, parte que es balde y parte que es saturación, y retorno de B como punto de equilibrio · 03 horas extras como excepción que se decide en el plan semanal · 04 supuestos 7 y 8 · 05 negociación (para quien las hace pueden ser un ingreso) · 06 dato que viene de la liquidación de sueldos al tablero · 07 supuesto 7 (se anota el motivo de cada hora extra) · 08 indicador 4, tercer resultado clave, regla de freno y conteo inicial fuera del total |
| **Mezcla y momento de producción, y no la capacidad total, explican la mayoría de los recortes** (supuesto 1, el crítico) | Hipótesis nuestra, razonada sobre cómo funciona el proceso, no medida. **Corrige** la Parte 1 (§2.1: "capacidad de planta") | 01 tercera corrección y por qué la meta es 90 % y no 100 % · 02 "qué podría cambiar la recomendación" · 03 plan semanal contra pedidos pendientes y stock mínimo · 04 supuesto 1 · 05 Heifetz: decidir la producción mirando pedidos es el cambio adaptativo · 07 la semana 0 anota la causa de cada recorte; las filas No-Go de la tabla de decisión · 08 tablero en rojo del indicador 1 y Go/No-Go de cierre, que revisa la meta |
| **Discovery tiene el módulo de stock, pedidos y reserva, y no se usa** (supuesto 3) | Lo que sabe nuestro compañero que trabaja en la empresa; nadie lo usó en Dulxelitos. Parte 1: Discovery desactualizado y sin integración | 02 alternativa B (recomendada), C descartada y el riesgo propio de B · 03 el TO-BE se dibuja en Discovery · 04 supuesto 3 y costos pendientes · 05 Buenos Aires Software como actor · 06 un solo lugar por dato, sin integración automática y con exportación a CSV · 07 prueba técnica de cinco pasos y preguntas por escrito al proveedor · 08 fase 4 (activar por línea), con costo y plazo como dependencias |
| **Se averigua dos veces si hay mercadería y el pedido se transcribe tres veces** | Relevamiento del proceso: primera y segunda lente de la 02 | 03 una consulta y una carga · 05 trueque con Oficina: reservar antes de confirmar a cambio de una consulta en lugar de dos y una nota en lugar de tres · 06 la nota de pedido y la lista de armado reemplazan las tres transcripciones · 08 cuidado de la carga de trabajo |
| **Qué producir lo decide el dueño o los hijos, por criterio propio y sin mirar los pedidos** | Relevamiento. Parte 1: conocimiento del negocio sin formalizar (§1.5) | 02 RECI (nadie consultado en "Decidir producción") · 03 plan semanal y tabla de quién decide qué · 04 supuesto 5 · 05 hijos como posible resistencia (hipótesis nuestra), Heifetz y FUD · 06 stock mínimo como dato maestro que fija Dirección · 07 señal temprana del supuesto 5 · 08 Dirección mira el tablero al planificar |
| **El responsable de sistemas es el líder, pero la gobernanza no la tenía asignada** | Parte 1: Gobierno 1.50 y 1 punto en gobernanza digital (§5) | 01 alcance: la propuesta se la asigna formalmente · 03 ejecuta los ajustes y el tablero · 05 sobrecarga como resistencia y [dato pendiente] de su tiempo · 06 varias tareas de las reglas de datos caen en él · 08 es el suplente más delicado y la fase 1 depende de su tiempo |
| **El distribuidor está conforme y el que sufre es la empresa** | Parte 1 (§4.2 y §4.4, encaje con el canal) | 04 "casi todo backstage", quién gana más y supuesto 6 · 05 distribuidores como afectados indirectos · 07 señal temprana del supuesto 6 (cancela o reclama) · 08 qué se les comunica |
| **Visibilidad de stock para el distribuidor y tienda online sin catálogo desde 2020** | Parte 1 (§3.2, §4.2 y §4.4) | 01 fuera de alcance · 04 por qué es "later": hoy no hay un stock confiable que mostrar · 06 no se integra · 08 "más adelante", cuando la exactitud se sostenga |
| **El dueño acepta invertir más si se demuestra el retorno** | Decisión del grupo | 02 tipo de inversión y retorno como punto de equilibrio, sin VAN · 04 mismo punto de equilibrio y supuesto 8 · 05 dueño como sponsor · 07 supuesto 8 · 08 el punto de equilibrio entra al Go/No-Go de la fase 3 |

> **El encadenamiento más importante de la Parte 2:** la causa de los recortes → qué se rediseña → cómo se prueba → qué se decide. "Mezcla y momento, no capacidad" (01, hipótesis nuestra) → por eso no alcanza con cargar stock: hay que planificar contra pedidos y stock mínimo (02 recomendación, 03 plan semanal) → es el supuesto 1, el que decide si la propuesta vale la pena (04) → la semana 0 anota la causa de cada recorte y el piloto mide cuántos bajan (07) → si no bajan y las causas son de capacidad, No-Go de B y se revisa la meta (07, 08). El informe no promete más de lo que la semana de registro y el piloto pueden respaldar.

> **Ninguna meta sale de una medición.** El 90 % de pedidos completos y a tiempo, las ~12 o 13 horas extras y los umbrales del piloto son propuestas nuestras, y cada sección lo dice donde las usa. Las únicas cifras de partida son las cuatro del relevamiento (30 de ~125, ~25 horas, 1 de 5 días) y el 76 %, que es una cuenta nuestra.

## Las correcciones a la Parte 1

Al relevar el proceso para esta parte, tres cosas que dijimos en el diagnóstico resultaron no ser del todo ciertas. Las dos de fondo son que el **stock de producto terminado no se registra** y que **los recortes no vienen de la capacidad total, sino de la mezcla y el momento de producción**; la tercera, que **los recortes no son raros: pasan todas las semanas**. La sección 1 las dice explícitamente y al principio, como la Parte 1 hizo con el catálogo web.

| Qué decía la Parte 1 | Qué dice la Parte 2 | Dónde está dicho |
|---|---|---|
| "Facturación y stock sí" digitalizados (§5.2) y "Facturación y stock están digitalizados" (§5.4) | La facturación sí está en Discovery. El stock de producto terminado no se lleva ni ahí ni en ningún otro registro. Se mira a ojo y se pregunta a producción | 01, "Lo que corrige el relevamiento", primer párrafo. Se retoma en la apertura de 02, 03, 04, 06, 07 y 08 |
| Los pedidos incompletos "son poco frecuentes y se resuelven fácil" (§5.5) | 30 de ~125 pedidos recortados o demorados en una semana de registro (~24 %), o ~76 % completos y a tiempo. El 76 % es cuenta nuestra sobre una sola semana | 01, segundo párrafo. En 04, "Una corrección al VPC" (los faltantes de papas fritas "en algunas temporadas"), y en 05, ADKAR del dueño y los hijos |
| Los faltantes de papas fritas se explican por "la capacidad de planta" (§2.1) | La planta sigue saturada, pero los recortes vienen sobre todo de la mezcla y el momento de producción. Es una hipótesis, no un dato, y se prueba en el piloto | 01, tercer párrafo. Es el supuesto 1 de 04 y la primera prueba de 07 |

La sección 1 aclara además dos cosas. Primero, que las tres correcciones **refuerzan** el diagnóstico de Gobierno (1.50) y explican por qué el costo de no actuar "no estaba bajo, estaba sin observar": ni el stock ni los recortes se registraban, así que no había nada que contar. Segundo, que **no volvemos a puntuar la encuesta**: dos ítems (automatización en Tecnología y Datos, y digitalización de los procesos clave en Procesos y Operaciones) quedaron sobreestimados, pero el nivel global sigue siendo Inicial. La Parte 1 queda como se entregó y la Parte 2 marca cuáles son esos dos ítems.

La regla `parte1` de `verificar.py` vigila que ninguna sección repita la afirmación vieja sin decir que la corrige. La introducción del informe armado también nombra las tres.

## Datos pendientes

Ninguno bloquea la entrega. Cada uno figura en el texto como `[dato pendiente: …]` y se junta, sin repetir, en el **Anexo I** del informe, que sale solo de `armar-entrega.py` a partir de la regla `pendientes`: hay alrededor de veinte datos distintos. Para ver la lista cruda, con archivo y línea, se corre `.venv/bin/python verificar.py` y se mira la salida de error.

Los que más conviene conseguir, porque cambian lo que el informe puede afirmar:

| Dato | Secciones | Cómo se consigue | Qué destraba |
|---|---|---|---|
| **Costo por hora extra** | 1, 2, 4, 7 y 8 | Preguntarle a Oficina (administración), que maneja la liquidación de sueldos | Con el costo mensual de B, completa el punto de equilibrio (B se paga si evita al menos tantas horas extras por mes como dé costo mensual de B ÷ costo por hora extra) y pone en pesos el costo de no actuar |
| **Costo de activar el módulo de stock, costo mensual de B, plazo de activación y soporte de Discovery** (incluye versión) | 2, 4, 5, 7 y 8 | Consulta por escrito a Buenos Aires Software, que la prueba técnica de la sección 7 ya prevé | El otro lado del punto de equilibrio, el plazo de la fase 4 y la dependencia del Go/No-Go de la fase 3 |
| **Quién cuenta** (responsable del conteo inicial y del semanal) | 3, 5, 6, 7 y 8 | Acordarlo con Depósito y con el dueño | Es dependencia de la fase 1: sin conteo no hay stock inicial, ni línea de base de la exactitud, ni piloto |
| **Línea de base de papas fritas en la semana 0** (pedidos de papas fritas recortados o demorados) | 7 | Se mide en la semana 0 con el registro de Oficina, con el mismo criterio del piloto | Sin ella no se puede evaluar el umbral "la mitad o menos": los 30 de ~125 son de todos los productos y no sirven de base para uno solo |

Del primer conteo salen también la **exactitud de stock inicial** (línea de base y meta del indicador 2) y la **diferencia en el conteo inicial** (base de la medida de conteo del piloto, cuya tolerancia es provisional hasta ese conteo). El **margen o valor de un pedido recortado** no hace falta para decidir: la cuenta del retorno es conservadora sin él. El resto son preguntas o acuerdos chicos con la empresa (quién carga cada turno y su suplente, quién convoca la reunión diaria, quién de Dirección responde por el plan semanal, cuánto tiempo semanal tiene el responsable de sistemas, el stock mínimo de cada producto, dónde figura la zona de cada distribuidor, qué listados exporta Discovery) y figuran todos en el Anexo I.

## Decisiones que el grupo tiene que confirmar

Son cosas que dejamos escritas como propuesta o hipótesis nuestra porque no teníamos el dato. Si el grupo las ve distintas, hay que cambiar el texto donde está dicho.

1. **Los hijos como posible resistencia** (sección 5). La ficha dice "posible, no relevada" y lo marca como hipótesis nuestra: que perder el criterio propio les cueste. Nadie nos dijo que sea así. Si nuestro compañero que trabaja en Dulxelitos lo ve distinto, se ajusta en la ficha, en el FUD y en el ADKAR de dueño e hijos.
2. **Hoja compartida de Oficina para el registro de recortes** (sección 6, y fuente del indicador 1 en la 08). Que Oficina lleve el registro semanal en una hoja simple es propuesta nuestra y no la hablamos con Oficina. Si ya existe otro registro o lo lleva otra persona, cambian el dueño y la fuente del indicador.
3. **Meta de horas extras de ~12 o 13 por mes** (secciones 1 y 8). Es la mitad de las ~25 de hoy y se apoya en el supuesto 7: que al menos la mitad se haga para completar pedidos que faltaron por mezcla y momento. Hay que confirmarla con el dueño, y se revisa si el motivo anotado resulta ser sobre todo saturación.
4. **Umbrales del piloto** (sección 7): carga en 8 de los 10 días hábiles, recortes a la mitad o menos que en la semana 0, conteos con una diferencia de hasta una décima parte de lo contado y 4 de cada 5 fechas cumplidas. Son propuesta nuestra, sin dato de la empresa, y el dueño tiene que acordarlos antes de arrancar.
5. **Papel A4 en vez de Letter** (`armar-entrega.py`). La Parte 1 salió en Letter. Elegimos A4 porque las hojas apaisadas con el BPMN se ven mal mezcladas con Letter. Volver a Letter es cambiar una línea del script (`size: A4` en el CSS, y `A4_W` y `A4_H`).

Otras propuestas nuestras que conviene mirar antes de entregar:

- **La meta de 90 %** de pedidos completos y a tiempo (sección 1): deja un 10 % de margen para roturas e imprevistos. Se revisa si el piloto muestra que la mezcla explica menos de lo que suponemos.
- **La matriz multicriterio** (sección 2): los puntajes son juicio nuestro, y A (36) y B (35) quedan empatadas. Recomendamos B con A como piloto por el argumento cualitativo, no por la suma.
- **Quién decide qué se hace con el faltante, quién autoriza las horas extras y quién de Dirección (el dueño o uno de los hijos) responde por el plan semanal** (secciones 2 y 3): la propuesta lo cierra, pero falta acordarlo con el dueño.
- **Que la carga diaria reemplace al control semanal propio de Producción** (secciones 5, 6 y 8): falta confirmar qué contiene ese control.
- **Las duraciones de las fases** (sección 8): son propuesta nuestra, y la fase 4 depende del plazo de activación y de la cantidad de líneas, que no sabemos.

## Nota sobre AS-IS y TO-BE

A diferencia de la Parte 1, que se escribió toda en estado actual, la Parte 2 sí propone: pide explícitamente una propuesta de transformación. Lo que se mantiene de la Parte 1 es la forma de trabajar: **ninguna cifra sin fuente** (lo que falta queda como dato pendiente), **supuestos declarados** y **la tecnología como medio**. Por eso el problema gerencial no nombra ninguna herramienta, y la herramienta se elige recién en la sección 2.
