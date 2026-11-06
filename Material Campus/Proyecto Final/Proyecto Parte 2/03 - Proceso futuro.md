# Proceso futuro (TO-BE)

Esta sección diseña cómo se atiende un pedido de distribuidor cuando la propuesta está andando: el proceso de la alternativa recomendada en la sección 2 (el stock de Discovery como solución), probada antes con una planilla compartida en un piloto de 2 semanas con papas fritas. El piloto corre este mismo flujo con la misma regla de stock; solo cambia dónde vive el registro. El proceso nuevo no acelera lo de hoy: cambia el orden (primero se mira qué hay, después se confirma) y conecta la producción con los pedidos. Responsables, criterios y rutinas son propuesta nuestra, a acordar con cada área antes del piloto (sección 5).

## Diagrama TO-BE

![Proceso TO-BE](bpmn/to-be.png)

**Cómo se lee.** Usa los mismos carriles y actores externos que el AS-IS de la sección 2, para comparar de un vistazo; el muñequito marca los pasos que se hacen en Discovery. El archivo `Proceso TO-BE - Dulxelitos.bpmn` se entrega aparte y abre en Bizagi o Camunda. Los tres objetos "Stock en Discovery" son el mismo registro, repetido para no cruzar carriles (la flecha en la tarea es una lectura; en el objeto, una escritura). Cuatro cosas arrancan por su cuenta: el pedido, con el mensaje del distribuidor; la semana de producción, con el reloj de Dirección; la carga del día, con el cierre del turno; y el conteo, con el reloj de Depósito.

- **El pedido.** Oficina carga la nota de pedido una sola vez en Discovery y consulta el stock disponible antes de confirmar. Si hay, reserva (la reserva se escribe en el stock), confirma al distribuidor y Depósito arma desde la lista de armado que Discovery da para ese pedido confirmado (sección 6). Después Oficina factura en Discovery, y la factura consume la reserva. El despacho es como hoy.
- **Si no hay.** Oficina avisa en el momento, con una fecha estimada que Producción confirma en la reunión diaria; si todavía no la confirmó, avisa igual del faltante, sin prometer fecha, y se la da después de la próxima reunión. El pedido queda pendiente (sin reserva, y se revisa en la reunión diaria) y, cuando llega la fecha, Oficina vuelve a consultar: si ya hay, reserva y sigue; si no, avisa de nuevo con otra fecha. Después del aviso el distribuidor puede cancelar: ese pedido cuenta como recortado (sección 7). "Hay" quiere decir que alcanza para el pedido completo. Si alcanza solo para una parte, se reserva esa parte y se despacha solo si el distribuidor lo acepta; si no, el pedido espera completo; el resto queda pendiente, sin reserva (sección 6). Lo que desaparece del AS-IS es mandar incompleto por decisión de la empresa cuando el faltante aparece al armar: ahora una parte sale solo si el distribuidor la aceptó antes.
- **La producción.** Cada semana Dirección planifica leyendo los pedidos pendientes (los avisados con faltante entre ellos), el stock mínimo y el tablero, y Producción produce lo planificado. La carga es otra rutina, que arranca todos los días con el cierre del turno: Producción carga lo producido y eso sube el stock físico en Discovery (hoy se carga una vez por semana). En Repostería, que es producto de terceros que Dulxelitos solo envasa, lo que se carga es lo envasado.
- **El conteo.** Una vez por semana Depósito cuenta el stock; quién lo hace queda a confirmar ([dato pendiente: responsable del conteo inicial y del semanal]). Si hay diferencias, manda lo contado y el responsable de sistemas, que es un rol y no un área, carga el ajuste con motivo; por eso aparece en la nota del diagrama y no como un paso con carril propio.
- **Las notas.** La reunión diaria de ~10 minutos entre ventas y producción, el tablero de 4 indicadores (lo actualiza el responsable de sistemas; Oficina, Producción y Depósito lo ven, Dirección lo mira al planificar y se lee en el informe al dueño y en cada Go/No-Go, sección 8) y las horas extras como excepción decidida en el plan semanal.

**Lo que el diagrama da por cierto y no está probado.** Que Discovery reserva y que la factura consume la reserva (supuesto 3 de la sección 4, que prueba la prueba técnica de la sección 7); que la fecha estimada se cumple (supuesto 4); y que el dueño y los hijos planifican mirando pedidos y stock mínimo (supuesto 5). En el piloto con planilla, al facturar se baja el físico y se descuenta la reserva a mano.

## Qué cambia

| Paso | Hoy (AS-IS) | Futuro (TO-BE) |
|---|---|---|
| **Registrar el pedido** | Se anota en papel o planilla y se pasa a una lista: tres transcripciones del mismo pedido | Se carga una sola vez, como nota de pedido en Discovery, y de ahí sale la lista de armado |
| **Saber si hay** | Se mira a ojo en el depósito y se pregunta a producción | Una sola consulta del stock disponible en Discovery |
| **Cuándo aparece el faltante** | Al armar el pedido, con el pedido ya aceptado | Antes de confirmar, en la compuerta "¿Hay stock disponible?" |
| **Qué se le dice al distribuidor** | Se acepta con una averiguación que no alcanza (a ojo y preguntando a producción); si falta, se manda incompleto avisando o se espera producción | Se confirma lo que hay, con reserva; si falta, aviso en el momento, con la fecha que confirmó Producción o, si todavía no la confirmó, sin fecha hasta la próxima reunión diaria |
| **Resolver el faltante** | Tres salidas: mandar incompleto, esperar producción u horas extras | El pedido queda pendiente hasta la fecha estimada y vuelve a consultarse; Dirección lo ve en el plan semanal |
| **Facturar** | Después de resolver el faltante, sin relación con ningún stock | La factura consume la reserva del pedido |
| **Qué se produce** | Lo decide el dueño o uno de los hijos por criterio propio, sin mirar los pedidos | Plan semanal contra pedidos pendientes y stock mínimo por producto; sigue decidiendo Dirección |
| **Cargar lo producido** | Una vez por semana (20 % de los días), en un control propio sin relación con ventas | Todos los días, al cierre del turno, en Discovery, con un responsable de carga por turno y suplente |
| **Controlar el stock** | No existe: no hay stock registrado | Conteo cíclico semanal; manda lo contado |
| **Horas extras** | Una de las tres salidas del faltante (~25 horas por mes) | Excepción que se decide en el plan semanal, con el motivo anotado |
| **Seguimiento** | Ninguno | Tablero de 4 indicadores y reunión diaria de ~10 minutos |

**Lo que no cambia, a propósito.** El pedido sigue entrando por WhatsApp o teléfono. El armado en el depósito sigue siendo manual: según el relevamiento es rápido y no es la restricción. El despacho, con flota propia o transporte tercerizado, queda igual. Qué producir lo sigue decidiendo el dueño o uno de los hijos, ahora con pedidos y stock a la vista. Y el distribuidor no ve el stock: eso queda para "later" (sección 1).

**Qué responde a cada lente de la sección 2.** La doble averiguación pasa a una consulta, las tres transcripciones a una carga y el silo de datos a un stock cargado todos los días con una sola regla: se ataca la gotera, no los baldes.

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

Usamos el criterio del RECI de la sección 2: una sola R por actividad y, como en una pyme quien ejecuta suele ser quien responde, casi todas las filas son R/E. Agregamos la columna del responsable de sistemas, que ejecuta dos pasos (los ajustes de stock y el tablero) y no tiene carril. Despachar con flota propia y entregar a transporte tercerizado no cambian y quedan como en la sección 2. Los asteriscos marcan propuestas nuestras que todavía no hablamos con cada área.

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

- **El faltante tiene dueño.** En la sección 2 no relevamos quién decide qué se hace con el faltante ni quién autoriza las horas extras. La propuesta lo cierra así: si el disponible no alcanza, Oficina avisa; la fecha la confirma Producción; las horas extras las decide Dirección en el plan semanal. Falta acordarlo con el dueño.
- **"Planificar" tiene consultados.** El AS-IS no tenía a nadie consultado en "Decidir producción". Ahora Oficina aporta los pedidos pendientes y Producción dice qué puede producir.
- **Dirección sigue siendo más de una persona.** Hay una sola R, pero decide el dueño o uno de los hijos: [dato pendiente: cuál responde por el plan semanal].
- **Quién cuenta no está definido.** Proponemos que cuente Depósito, pero no relevamos quién lo haría, ni en el conteo inicial ni en el semanal: [dato pendiente: responsable del conteo inicial y del semanal].
- **La carga diaria tiene una persona con nombre.** Un responsable de carga por turno, con suplente, porque una carga que depende de alguien que falta se corta: [dato pendiente: quién es el responsable de carga de cada turno y su suplente].
- **La reunión diaria tiene que tener quién la convoque.** Proponemos a Dirección, porque es quien decide qué producir: [dato pendiente: quién convoca la reunión diaria y si participa el dueño o un hijo todos los días].

### Quién decide qué, y con qué dato

| Decisión | Quién | Con qué dato | Criterio |
|---|---|---|---|
| ¿Se confirma el pedido? | Oficina | Stock disponible, de Discovery | Si alcanza, se reserva y se confirma. Si no, no se confirma sin avisar. No se confirma sin consultar ni a ojo, salvo el día en que el dato no está al día (vuelta atrás, sección 7) |
| ¿Qué fecha se da? | Producción la confirma; Oficina la comunica | Plan semanal y producción en curso, vistos en la reunión diaria | La fecha sale de la reunión diaria. Oficina no la inventa: si Producción todavía no la confirmó, avisa del faltante sin prometer fecha y se la da después de la próxima reunión diaria |
| ¿Qué se produce esta semana? | Dirección (dueño o hijos) | Pedidos pendientes, stock disponible frente al stock mínimo de cada producto, y el tablero | Primero lo que está pedido y no hay; después lo que está por debajo del mínimo. El criterio propio sigue contando, pero ya no es el único dato |
| ¿Hay horas extras? | Dirección, en el plan semanal | Pedidos pendientes que la producción normal no cubre | Excepción con el motivo anotado (completar un pedido que faltó o saturación). No es el arreglo habitual del faltante |
| ¿Cómo se corrige una diferencia de conteo? | Manda lo contado; el responsable de sistemas carga el ajuste | La hoja de conteo de Depósito | Se ajusta Discovery, con motivo, sin editar el stock a mano. Si el mismo producto difiere semana tras semana, se trata en la reunión diaria |
| ¿Se libera una reserva? | Oficina, que la creó | Plazo estándar de la zona del distribuidor y su confirmación | La que pasó el plazo sin facturarse se confirma con el distribuidor y se factura o se libera |
| ¿Se avanza a la siguiente fase? | El dueño, como sponsor | Tablero y resultado del piloto | Go/No-Go de las secciones 7 y 8; no es una decisión del día a día |

## Datos y controles

### Cuándo se genera el dato que hoy falta

Hoy el dato del stock no se genera nunca. En el proceso nuevo se genera en cinco momentos, todos en Discovery:

| Momento | Dato que se genera | Quién lo carga |
|---|---|---|
| Al recibir el pedido | Nota de pedido (distribuidor, productos y cantidades) | Oficina |
| Al confirmarlo | Reserva del stock | Oficina |
| Al cierre de cada turno | Parte de producción: lo realmente producido | Responsable de carga del turno, con suplente |
| Al facturar | La factura baja el stock físico y consume la reserva | Oficina |
| Una vez por semana | Conteo físico y ajuste de diferencias | Depósito (a confirmar quién) cuenta; el responsable de sistemas ajusta |

El origen, el destino y las reglas de alta, corrección y depuración de cada dato están en la sección 6.

### Controles

Cada control corresponde a un error que hoy no se detecta:

| Error de hoy | Control en el proceso nuevo | Cómo se ve si falla |
|---|---|---|
| Confirmar sin saber qué hay | Consultar el disponible es un paso del flujo, antes de confirmar | Los días en que se confirmó a ojo porque el dato no estaba al día, que el piloto anota (sección 7) |
| Producir sin mirar los pedidos | Plan semanal con pedidos pendientes y stock mínimo, y reunión diaria | La reunión diaria no cambia lo que se produce con pedidos sin cubrir (supuesto 5, sección 7), y el indicador de pedidos completos y a tiempo no sube |
| Stock cargado que no coincide con el real | Conteo cíclico semanal; manda lo contado | Exactitud de stock |
| Carga que se corta | Responsable de carga por turno con suplente, y carga al cierre del turno | Días con producción cargada |
| Reservas viejas que bajan el disponible sin motivo | Oficina revisa cada semana las reservas abiertas | Reservas abiertas que encuentra la revisión semanal de Oficina (sección 6) |
| Horas extras como arreglo habitual | Excepción decidida en el plan semanal, con el motivo anotado | Horas extras por mes |

### Seguimiento simple

Son los cuatro instrumentos que pide la consigna, y caben en una pyme sin sumar un sistema.

**Tablero de 4 indicadores.** Pedidos completos y a tiempo, exactitud de stock, días con producción cargada y horas extras por mes. Lo actualiza el responsable de sistemas cada semana, con la exportación de Discovery y dos cargas manuales (sección 6). Queda a la vista de Oficina, Producción y Depósito; Dirección lo mira al planificar la semana, la reunión diaria mira solo la carga y el disponible, y los cuatro indicadores se leen en el informe al dueño y en cada Go/No-Go. La ficha, la fórmula y la meta de cada indicador están en la sección 8.

**Checklist.** Tres listas cortas, una por rutina:

*Cierre de turno (responsable de carga o suplente)*

- [ ] Cargué la cantidad realmente producida de cada producto, no la planificada ni la estimada.
- [ ] Si me equivoqué en una carga de hoy, la corregí el mismo día, con su motivo.
- [ ] Si no pude cargar, lo avisé para anotarlo en la reunión.

*Antes de confirmar un pedido (Oficina)*

- [ ] El pedido está cargado una sola vez, con el producto y el distribuidor elegidos de la lista.
- [ ] Consulté el stock disponible.
- [ ] Si alcanza, reservé antes de confirmar. Si no, avisé del faltante: con la fecha que confirmó Producción o, si todavía no la confirmó, sin fecha, y la doy después de la próxima reunión diaria.

*Cada semana, un día fijo a acordar con Depósito (Depósito, Oficina y responsable de sistemas)*

- [ ] Depósito contó el stock y dejó la hoja de conteo. [dato pendiente: responsable del conteo inicial y del semanal]
- [ ] El responsable de sistemas cargó los ajustes, cada uno con su motivo.
- [ ] Oficina revisó las reservas abiertas: las que pasaron el plazo de su zona se confirmaron o se liberaron.
- [ ] Se actualizó el tablero.

**Responsable de carga.** Una persona por turno, con suplente, que responde porque lo producido llegue a Discovery al cierre. Es el control más importante: sin carga diaria no hay stock en el que confiar, y es trabajo nuevo para Producción (sección 5). El tiempo de carga se reserva dentro del turno.

**Reunión diaria ventas–producción.** Dura ~10 minutos y tiene tres preguntas: ¿qué hay y qué está pendiente?, ¿qué avisos hay abiertos y qué fecha confirma Producción?, ¿hay que mover lo que se produce? Termina con la fecha y la decisión de producción anotadas, y es el lugar donde se tratan las diferencias de conteo que se repiten y las reservas liberadas. Hoy Oficina le pregunta a Producción pedido por pedido; la reunión junta esa pregunta en un solo momento.

**Fuentes:** relevamiento del proceso y secciones 1, 2, 4, 5, 6 y 7 de esta parte. Los responsables, los criterios de decisión y las rutinas son propuesta nuestra, no datos de la empresa.
