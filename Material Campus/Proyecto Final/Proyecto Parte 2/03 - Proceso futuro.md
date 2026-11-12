# Proceso futuro (TO-BE)

Así se atendería un pedido con la alternativa recomendada en la sección 2, el stock de Discovery. Antes se prueba durante 2 semanas con papas fritas sobre una planilla compartida, con el mismo flujo y la misma regla de stock; lo único que cambia es dónde se registra. Respecto de hoy, cambia el orden (primero se mira qué hay y después se confirma) y la producción pasa a conectarse con los pedidos.

## Diagrama TO-BE

![Proceso TO-BE](bpmn/to-be.png)

El diagrama usa los mismos carriles y actores externos que el AS-IS de la sección 2, y el ícono de persona marca los pasos que se hacen en Discovery. El diagrama completo se adjunta en formato BPMN. Los tres objetos "Stock en Discovery" son el mismo registro, repetido para no cruzar carriles.

Oficina carga la nota de pedido una sola vez y consulta el stock disponible antes de confirmar. Si hay, reserva y confirma, y Depósito arma con la lista que Discovery genera (sección 6). Después Oficina factura y la factura consume la reserva. El despacho es como hoy.

Si no hay, Oficina avisa en el momento con la fecha estimada que Producción confirma en la reunión diaria; si todavía no la confirmó, avisa del faltante sin fecha y la da después de la próxima reunión. El pedido queda pendiente, sin reserva, hasta que llega la fecha y Oficina vuelve a consultar. "Hay" quiere decir que alcanza para el pedido completo; si alcanza solo para una parte, se reserva esa parte y se despacha únicamente si el distribuidor lo acepta y, si no, el pedido espera completo (sección 6). Si el distribuidor cancela tras el aviso, el pedido cuenta como recortado (sección 7).

Cada semana Dirección planifica y Producción produce lo planificado. La carga diaria, con el cierre del turno, sube el stock físico en Discovery; en Repostería, producto de terceros que Dulxelitos solo envasa, se carga lo envasado.

Una vez por semana Depósito cuenta el stock; si hay diferencias, manda lo contado y el responsable de sistemas carga el ajuste con su motivo.

Hay tres cosas que el diagrama da por ciertas y todavía no probamos: que Discovery reserva, incluso una parte de un pedido, y que la factura consume la reserva (supuesto 3, que verifica la prueba técnica de la sección 7); que la fecha estimada se cumple (supuesto 4); y que el dueño y los hijos planifican mirando pedidos y stock mínimo (supuesto 5).

## Qué cambia

| Paso | Hoy (AS-IS) | Futuro (TO-BE) |
|---|---|---|
| Registrar el pedido | Se anota en papel o planilla y se pasa a una lista: el mismo pedido se anota tres veces (chat, papel o planilla y lista) | Se carga una sola vez como nota de pedido en Discovery |
| Saber si hay | Se mira en el depósito y se pregunta a Producción; el faltante aparece al armar, con el pedido ya aceptado | Una consulta del stock disponible en Discovery antes de confirmar |
| Avisar al distribuidor y resolver el faltante | Se acepta con una averiguación que no alcanza; si falta, tres salidas: mandar incompleto, esperar producción u horas extras | Se confirma lo que hay, con reserva; si falta, aviso en el momento con fecha y pedido pendiente a la vista de Dirección |
| Qué se produce | Lo decide el dueño o uno de los hijos, sin mirar los pedidos | Plan semanal contra pedidos pendientes y stock mínimo; sigue decidiendo Dirección |
| Cargar lo producido | Una vez por semana (20 % de los días), en un control propio sin relación con ventas | Todos los días, al cierre del turno, con responsable de carga por turno y suplente |
| Horas extras | Una de las tres salidas del faltante (parte de las horas extras del mes) | Excepción del plan semanal, con motivo anotado |

Siguen igual el ingreso del pedido por WhatsApp o teléfono, el armado manual en el depósito (según el relevamiento es rápido y no es la restricción) y el despacho, propio o tercerizado. El distribuidor tampoco ve el stock, algo que queda para más adelante (sección 1).

### La regla del stock disponible

Es la misma en Discovery y en la planilla del piloto, y con ella contesta Oficina al distribuidor:

**stock disponible = stock físico − reservado por pedidos confirmados sin facturar**

| Qué pasa | Stock físico | Reservado | Disponible |
|---|---|---|---|
| Producción carga lo producido | Sube | Igual | Sube |
| Oficina reserva al confirmar | Igual | Sube | Baja |
| Oficina factura (consume la reserva) | Baja | Baja | Igual |
| Se libera una reserva (cancelación o pedido rehecho) | Igual | Baja | Sube |
| El conteo encuentra una diferencia | Se ajusta a lo contado | Igual | Cambia con el físico |

## Responsables y decisiones

Seguimos el RECI de la sección 2, con una sola R por actividad; como en una pyme quien ejecuta suele ser quien responde, casi todo es R/E. Sumamos al responsable de sistemas, que ejecuta dos pasos (ajustes de stock y tablero) y, por ser un rol, no tiene carril. Los asteriscos marcan lo que falta acordar con cada área.

| Actividad | Oficina | Depósito | Producción | Dirección | Resp. de sistemas | Distribuidor (externo) |
|---|---|---|---|---|---|---|
| Cargar nota de pedido, consultar stock disponible y reservar | R/E | – | – | – | – | – |
| Confirmar pedido al distribuidor | R/E | I | – | – | – | I |
| Avisar faltante con fecha estimada | R/E | – | C | – | – | I |
| Preparar pedido | I | R/E | – | – | – | – |
| Facturar en Discovery | R/E | C | – | – | – | I |
| Planificar producción de la semana | C* | – | C* | R/E | – | – |
| Producir lo planificado | I | I | R/E | I | – | – |
| Cargar producción del día | I | I | R/E | – | – | – |
| Contar stock | – | R/E (a confirmar) | I | – | I | – |
| Ajustar diferencias de conteo | I | C | I | – | R/E | – |
| Reunión diaria ventas–producción* | C | – | C | R/E | – | – |
| Actualizar el tablero* | C | – | I | I | R/E | – |

Respecto del AS-IS, el faltante pasa a tener responsable, ya que Oficina avisa, Producción confirma la fecha y Dirección decide las horas extras en el plan semanal. Además, "Planificar" ahora tiene consultados: Oficina aporta los pedidos y Producción dice qué puede producir.

Oficina decide si se confirma un pedido con el stock disponible; solo el día en que el dato no está al día se confirma sin él (vuelta atrás, sección 7). La fecha la confirma Producción con el plan semanal y la producción en curso, y Oficina no promete una que Producción no confirmó. Dirección decide qué se produce con los pedidos pendientes, incluidos los avisados con faltante, el disponible frente al stock mínimo y el tablero. Va primero lo pedido que no hay y después lo que está bajo el mínimo; el criterio de Dirección sigue contando, pero deja de ser el único dato. Las diferencias de conteo las ajusta el responsable de sistemas en Discovery, con motivo y sin editar el stock a mano, a partir de la hoja de Depósito; si un producto difiere semana tras semana, se trata en la reunión diaria.

Quedan cuatro puntos abiertos para resolver con el dueño antes del piloto. Falta decidir cuál de los decisores, él o algún hijo, responde por el plan semanal. Para el conteo, inicial y semanal, proponemos a Depósito, pero no relevamos quién lo haría. También hay que nombrar al responsable de carga de cada turno y a su suplente. Y alguien tiene que convocar la reunión diaria; sugerimos a Dirección, aunque queda por definir si participa el dueño o un hijo todos los días.

## Datos y controles

Hoy el stock de producto terminado no se registra. En el proceso nuevo se genera en cinco momentos, todos en Discovery: la nota de pedido, la reserva, el parte de producción al cierre del turno, la factura y el ajuste del conteo semanal. Las reglas de carga, ajuste y depuración están en la sección 6.

### Controles

| Error de hoy | Control en el proceso nuevo | Cómo se ve si falla |
|---|---|---|
| Confirmar sin saber qué hay | Consultar el disponible antes de confirmar | Días en que se confirmó sin el dato al día, que el piloto anota (sección 7) |
| Producir sin mirar los pedidos | Plan semanal con pedidos pendientes y stock mínimo, y reunión diaria | Pedidos sin cubrir que la reunión no mueve (supuesto 5) y el indicador de pedidos completos que no sube |
| Stock cargado que no coincide con el real | Conteo cíclico semanal; manda lo contado | Exactitud de stock |
| Carga que se corta | Responsable de carga por turno, con suplente | Días con producción cargada |
| Reservas viejas que bajan el disponible | Oficina revisa cada semana las reservas abiertas; las que pasaron el plazo de su zona se confirman con el distribuidor y se facturan o se liberan | Reservas abiertas en esa revisión (sección 6) |
| Horas extras como arreglo habitual | Excepción del plan semanal, con motivo anotado | Horas extras por mes |

### Seguimiento simple

El tablero es una hoja de 4 indicadores que el responsable de sistemas actualiza cada semana con la exportación de Discovery y dos cargas manuales (sección 6); la ficha y la meta de cada uno están en la sección 8.

*Cierre de turno (responsable de carga o suplente)*

- [ ] Cargué lo realmente producido de cada producto, no lo planificado.
- [ ] Si me equivoqué en una carga de hoy, la ajusté el mismo día, con motivo.
- [ ] Si no pude cargar, lo avisé para anotarlo en la reunión.

*Antes de confirmar un pedido (Oficina)*

- [ ] Cargué el pedido una sola vez y consulté el stock disponible.
- [ ] Si alcanzaba, reservé antes de confirmar; si no, avisé del faltante con la fecha de Producción o sin fecha.

*Cada semana, un día fijo a acordar con Depósito (Depósito, Oficina y responsable de sistemas)*

- [ ] Depósito contó y dejó la hoja de conteo.
- [ ] Se cargaron los ajustes, cada uno con su motivo.
- [ ] Oficina revisó las reservas abiertas: las vencidas se confirmaron o se liberaron.
- [ ] Se actualizó el tablero.

El responsable de carga, una persona por turno con suplente, se encarga de que lo producido llegue a Discovery al cierre. Es el control más importante, ya que sin carga diaria no hay stock confiable, y es trabajo nuevo para Producción (sección 5); el tiempo de carga se reserva dentro del turno.

La reunión diaria entre ventas y producción dura unos 10 minutos y repasa qué hay y qué está pendiente, qué avisos hay abiertos y con qué fecha, y si hay que mover lo que se produce. Ahí se anotan la fecha y la decisión de producción, y se ven las reservas liberadas.
