# Proceso futuro (TO-BE)

Esta sección diseña cómo se atiende un pedido de distribuidor cuando la propuesta está andando: el proceso de la alternativa recomendada en la sección 2 (el stock de Discovery), probado antes con una planilla compartida en un piloto de 2 semanas con papas fritas, que corre este mismo flujo con la misma regla de stock; solo cambia dónde vive el registro. El proceso nuevo cambia el orden (primero se mira qué hay, después se confirma) y conecta la producción con los pedidos. Responsables, criterios y rutinas son propuesta nuestra, a acordar con cada área antes del piloto (sección 5).

## Diagrama TO-BE

![Proceso TO-BE](bpmn/to-be.png)

**Cómo se lee.** Usa los mismos carriles y actores externos que el AS-IS de la sección 2, para comparar de un vistazo; el muñequito marca los pasos que se hacen en Discovery. El archivo `Proceso TO-BE - Dulxelitos.bpmn` se entrega aparte y abre en Bizagi o Camunda. Los tres objetos "Stock en Discovery" son el mismo registro, repetido para no cruzar carriles (la flecha en la tarea es una lectura; en el objeto, una escritura). Cuatro cosas arrancan por su cuenta: el pedido, con el mensaje del distribuidor; la semana de producción, con el reloj de Dirección; la carga del día, con el cierre del turno; y el conteo, con el reloj de Depósito.

- **El pedido.** Oficina carga la nota de pedido una sola vez en Discovery y consulta el stock disponible antes de confirmar. Si hay, reserva (la reserva se escribe en el stock), confirma al distribuidor y Depósito arma desde la lista de armado que Discovery da para ese pedido confirmado (sección 6). Después Oficina factura en Discovery, y la factura consume la reserva. El despacho es como hoy.
- **Si no hay.** Oficina avisa en el momento, con una fecha estimada que Producción confirma en la reunión diaria; si todavía no la confirmó, avisa del faltante sin prometer fecha y se la da después de la próxima reunión. El pedido queda pendiente, sin reserva, y cuando llega la fecha Oficina vuelve a consultar. "Hay" quiere decir que alcanza para el pedido completo; si alcanza solo para una parte, se reserva esa parte y se despacha solo si el distribuidor lo acepta, y si no el pedido espera completo (sección 6). Si el distribuidor cancela después del aviso, el pedido cuenta como recortado (sección 7).
- **La producción.** Cada semana Dirección planifica leyendo los pedidos pendientes (los avisados con faltante entre ellos), el stock mínimo y el tablero, y Producción produce lo planificado. La carga es otra rutina, que arranca todos los días con el cierre del turno: Producción carga lo producido y eso sube el stock físico en Discovery (hoy se carga una vez por semana). En Repostería, que es producto de terceros que Dulxelitos solo envasa, lo que se carga es lo envasado.
- **El conteo.** Una vez por semana Depósito cuenta el stock; quién lo hace queda a confirmar ([dato pendiente: responsable del conteo inicial y del semanal]). Si hay diferencias, manda lo contado y el responsable de sistemas, que es un rol y no un área, carga el ajuste con motivo; por eso aparece en la nota del diagrama y no como un paso con carril propio.
- **Las notas.** La reunión diaria de ~10 minutos entre ventas y producción, el tablero de 4 indicadores (sección 8) y las horas extras como excepción decidida en el plan semanal.

**Lo que el diagrama da por cierto y no está probado.** Que Discovery reserva, que permite reservar solo una parte de un pedido y que la factura consume la reserva (supuesto 3 de la sección 4, que verifica la prueba técnica de la sección 7); que la fecha estimada se cumple (supuesto 4); y que el dueño y los hijos planifican mirando pedidos y stock mínimo (supuesto 5). En el piloto con planilla, al facturar se baja el físico y se descuenta la reserva a mano.

## Qué cambia

| Paso | Hoy (AS-IS) | Futuro (TO-BE) |
|---|---|---|
| **Registrar el pedido** | Se anota en papel o planilla y se pasa a una lista: tres transcripciones del mismo pedido | Se carga una sola vez, como nota de pedido en Discovery, y de ahí sale la lista de armado |
| **Saber si hay, y cuándo aparece el faltante** | Se mira a ojo en el depósito y se pregunta a producción; el faltante aparece al armar el pedido, con el pedido ya aceptado | Una sola consulta del stock disponible en Discovery, antes de confirmar, en la compuerta "¿Hay stock disponible?" |
| **Qué se le dice al distribuidor y cómo se resuelve el faltante** | Se acepta con una averiguación que no alcanza; si falta, tres salidas: mandar incompleto avisando, esperar producción u horas extras | Se confirma lo que hay, con reserva; si falta, aviso en el momento, con la fecha que confirmó Producción (sin fecha si todavía no la confirmó), y el pedido queda pendiente hasta esa fecha, a la vista de Dirección en el plan semanal |
| **Qué se produce** | Lo decide el dueño o uno de los hijos por criterio propio, sin mirar los pedidos | Plan semanal contra pedidos pendientes y stock mínimo por producto; sigue decidiendo Dirección |
| **Cargar lo producido** | Una vez por semana (20 % de los días), en un control propio sin relación con ventas | Todos los días, al cierre del turno, en Discovery, con un responsable de carga por turno y suplente |
| **Horas extras** | Una de las tres salidas del faltante (~25 horas por mes) | Excepción que se decide en el plan semanal, con el motivo anotado |

**Lo que no cambia, a propósito.** El pedido sigue entrando por WhatsApp o teléfono; el armado en el depósito sigue siendo manual (según el relevamiento es rápido y no es la restricción); el despacho, con flota propia o transporte tercerizado, queda igual; qué producir lo sigue decidiendo el dueño o uno de los hijos, ahora con pedidos y stock a la vista; y el distribuidor no ve el stock: eso queda para "later" (sección 1).

### La regla del stock disponible

Es la misma en Discovery y en la planilla del piloto, y es la cifra con la que Oficina contesta al distribuidor:

**stock disponible = stock físico − reservado por pedidos confirmados sin facturar**

| Qué pasa | Stock físico | Reservado | Disponible |
|---|---|---|---|
| Producción carga lo producido al cierre del turno | Sube | Igual | Sube |
| Oficina reserva al confirmar un pedido | Igual | Sube | Baja |
| Oficina factura el pedido (consume la reserva) | Baja | Baja | Igual |
| Se libera una reserva (cancelación o pedido rehecho) | Igual | Baja | Sube |
| El conteo encuentra una diferencia | Se corrige a lo contado | Igual | Cambia con el físico |

Confirmar un pedido baja lo que se puede prometer sin tocar lo que hay, y recién la factura baja lo que hay; por eso el disponible no se mueve al facturar, ya se había descontado al reservar. Las reglas para cargar, corregir y depurar estos datos están en la sección 6.

## Responsables y decisiones

Usamos el criterio del RECI de la sección 2: una sola R por actividad y, como en una pyme quien ejecuta suele ser quien responde, casi todas las filas son R/E. Agregamos al responsable de sistemas, que ejecuta dos pasos (los ajustes de stock y el tablero) y no tiene carril. Los asteriscos marcan propuestas nuestras que todavía no hablamos con cada área.

| Actividad | Oficina | Depósito | Producción | Dirección | Resp. de sistemas | Distribuidor (externo) |
|---|---|---|---|---|---|---|
| Cargar nota de pedido en Discovery | R/E | – | – | – | – | – |
| Consultar stock disponible | R/E | – | – | – | – | – |
| Reservar stock | R/E | – | – | – | – | – |
| Confirmar pedido al distribuidor | R/E | I | – | – | – | I |
| Avisar faltante con fecha estimada | R/E | – | C | – | – | I |
| Preparar pedido | I | R/E | – | – | – | – |
| Facturar en Discovery | R/E | C | – | – | – | I |
| Planificar producción de la semana | C* | – | C* | R/E | – | – |
| Producir lo planificado | I | I | R/E | I | – | – |
| Cargar producción del día | I | I | R/E | – | – | – |
| Contar stock | – | R/E (a confirmar) | I | – | I | – |
| Ajustar diferencias de conteo (nota del diagrama) | I | C | I | – | R/E | – |
| Reunión diaria ventas–producción* | C | – | C | R/E | – | – |
| Actualizar el tablero* | C | – | I | I | R/E | – |

Qué cambia en las responsabilidades respecto del AS-IS:

- **El faltante tiene dueño.** La sección 2 no relevó quién decide qué se hace con el faltante ni quién autoriza las horas extras. La propuesta: si el disponible no alcanza, Oficina avisa; la fecha la confirma Producción; las horas extras las decide Dirección en el plan semanal. Falta acordarlo con el dueño.
- **"Planificar" tiene consultados.** El AS-IS no tenía a nadie consultado en "Decidir producción"; ahora Oficina aporta los pedidos pendientes y Producción dice qué puede producir.
- **Hay cuatro cosas sin definir.** Cuál de los decisores responde por el plan semanal [dato pendiente: cuál responde por el plan semanal]; quién cuenta, porque proponemos a Depósito pero no relevamos quién lo haría, ni en el conteo inicial ni en el semanal [dato pendiente: responsable del conteo inicial y del semanal]; quién es el responsable de carga de cada turno y su suplente, porque una carga que depende de alguien que falta se corta [dato pendiente: quién es el responsable de carga de cada turno y su suplente]; y quién convoca la reunión diaria, que proponemos que sea Dirección [dato pendiente: quién convoca la reunión diaria y si participa el dueño o un hijo todos los días].

### Quién decide qué, y con qué dato

| Decisión | Quién | Con qué dato | Criterio |
|---|---|---|---|
| ¿Se confirma el pedido? | Oficina | Stock disponible, de Discovery | Si alcanza, se reserva y se confirma; si no, no se confirma sin avisar. No se confirma a ojo, salvo el día en que el dato no está al día (vuelta atrás, sección 7) |
| ¿Qué fecha se da? | Producción la confirma; Oficina la comunica | Plan semanal y producción en curso, vistos en la reunión diaria | Oficina no la inventa: si Producción todavía no la confirmó, avisa del faltante sin fecha y la da después de la próxima reunión diaria |
| ¿Qué se produce esta semana? | Dirección (dueño o hijos) | Pedidos pendientes, stock disponible frente al stock mínimo de cada producto, y el tablero | Primero lo pedido que no hay; después lo que está por debajo del mínimo. El criterio propio sigue contando, pero ya no es el único dato |
| ¿Cómo se corrige una diferencia de conteo? | Manda lo contado; el responsable de sistemas carga el ajuste | La hoja de conteo de Depósito | Se ajusta Discovery, con motivo, sin editar el stock a mano. Si un producto difiere semana tras semana, se trata en la reunión diaria |
| ¿Se libera una reserva? | Oficina, que la creó | Plazo estándar de la zona del distribuidor y su confirmación | La que pasó el plazo sin facturarse se confirma con el distribuidor y se factura o se libera |

## Datos y controles

Hoy el dato del stock no se genera nunca. En el proceso nuevo se genera en cinco momentos, todos en Discovery: al recibir el pedido (la nota de pedido), al confirmarlo (la reserva), al cierre de cada turno (el parte de producción), al facturar (que baja el físico y consume la reserva) y en el conteo semanal (el ajuste). Quién carga cada dato y sus reglas de alta, corrección y depuración están en la sección 6.

### Controles

Cada control corresponde a un error que hoy no se detecta:

| Error de hoy | Control en el proceso nuevo | Cómo se ve si falla |
|---|---|---|
| Confirmar sin saber qué hay | Consultar el disponible es un paso del flujo, antes de confirmar | Días en que se confirmó a ojo porque el dato no estaba al día, que el piloto anota (sección 7) |
| Producir sin mirar los pedidos | Plan semanal con pedidos pendientes y stock mínimo, y reunión diaria | La reunión no cambia lo que se produce con pedidos sin cubrir (supuesto 5, sección 7) y el indicador de pedidos completos no sube |
| Stock cargado que no coincide con el real | Conteo cíclico semanal; manda lo contado | Exactitud de stock |
| Carga que se corta | Responsable de carga por turno con suplente, y carga al cierre del turno | Días con producción cargada |
| Reservas viejas que bajan el disponible sin motivo | Oficina revisa cada semana las reservas abiertas | Reservas abiertas en la revisión semanal (sección 6) |
| Horas extras como arreglo habitual | Excepción decidida en el plan semanal, con el motivo anotado | Horas extras por mes |

### Seguimiento simple

Son los cuatro instrumentos que pide la consigna, y caben en una pyme sin sumar un sistema.

**Tablero de 4 indicadores.** Una hoja simple que actualiza el responsable de sistemas cada semana, con la exportación de Discovery y dos cargas manuales (sección 6). La ficha, la fórmula y la meta de cada indicador, quién lo ve y cómo se lee están en la sección 8.

**Checklist.** Tres listas cortas, una por rutina:

*Cierre de turno (responsable de carga o suplente)*

- [ ] Cargué la cantidad realmente producida de cada producto, no la planificada ni la estimada.
- [ ] Si me equivoqué en una carga de hoy, la corregí el mismo día, con su motivo.
- [ ] Si no pude cargar, lo avisé para anotarlo en la reunión.

*Antes de confirmar un pedido (Oficina)*

- [ ] El pedido está cargado una sola vez, con el producto y el distribuidor elegidos de la lista.
- [ ] Consulté el stock disponible.
- [ ] Si alcanza, reservé antes de confirmar. Si no, avisé del faltante, con la fecha que confirmó Producción o, si todavía no la confirmó, sin fecha.

*Cada semana, un día fijo a acordar con Depósito (Depósito, Oficina y responsable de sistemas)*

- [ ] Depósito contó el stock y dejó la hoja de conteo. [dato pendiente: responsable del conteo inicial y del semanal]
- [ ] El responsable de sistemas cargó los ajustes, cada uno con su motivo.
- [ ] Oficina revisó las reservas abiertas: las que pasaron el plazo de su zona se confirmaron o se liberaron.
- [ ] Se actualizó el tablero.

**Responsable de carga.** Una persona por turno, con suplente, que responde porque lo producido llegue a Discovery al cierre. Es el control más importante: sin carga diaria no hay stock en el que confiar, y es trabajo nuevo para Producción (sección 5). El tiempo de carga se reserva dentro del turno.

**Reunión diaria ventas–producción.** Dura ~10 minutos y tiene tres preguntas: ¿qué hay y qué está pendiente?, ¿qué avisos hay abiertos y qué fecha confirma Producción?, ¿hay que mover lo que se produce? Termina con la fecha y la decisión de producción anotadas, y es el lugar donde se tratan las diferencias de conteo que se repiten y las reservas liberadas.

**Fuentes:** relevamiento del proceso y secciones 1, 2, 4, 5, 6 y 7 de esta parte. Los responsables, los criterios de decisión y las rutinas son propuesta nuestra, no datos de la empresa.
