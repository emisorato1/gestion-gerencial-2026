# Arquitectura conceptual y flujo de datos

Esta sección dibuja la alternativa recomendada (la B: el stock de Discovery, probado antes con una planilla compartida) como cajas y flechas, y dice qué datos se mueven, quién los carga, cómo pasan de un lugar a otro y qué reglas los mantienen limpios.

La guía de la cátedra pregunta si una empresa chica necesita un diagrama de la NASA o un flujo simple. Para una pyme de 15 a 20 personas la respuesta es el flujo simple: **un solo sistema, y ya lo tienen.** Es Discovery, que hoy usan para facturar, más una planilla compartida que existe solo durante el piloto de 2 semanas y un tablero con cuatro indicadores. No hay ningún sistema nuevo que comprar (el costo de activar el módulo de stock está pendiente, sección 4), ninguna integración automática ni ningún canal nuevo: las áreas aportan sus datos a un solo lugar, y de ahí salen la lista para armar cada pedido y los números que miran la dirección y el responsable de sistemas.

## Diagrama

![Arquitectura y flujo de datos](diagramas/arquitectura.png)

Para la exposición hay además una versión interactiva del flujo de datos, el archivo `Flujo de datos interactivo - Dulxelitos.html` de la carpeta de entrega, que se abre en el navegador.

### Cómo se lee

- **Tres áreas aportan, un solo lugar guarda.** Oficina carga la nota de pedido y reserva el stock antes de confirmar; Producción carga lo producido todos los días, al cierre del turno; Depósito aporta la hoja del conteo semanal, que el responsable de sistemas carga como ajuste (quién cuenta: [dato pendiente: responsable del conteo inicial y del semanal]). Los tres aportes entran juntos a Discovery, y de ahí sale para cada pedido confirmado la lista de armado que usa Depósito: es lo que se gana por cargar el pedido una sola vez.
- **Una sola regla de stock.** Dentro de Discovery, **stock disponible = stock físico − reservado por pedidos confirmados sin facturar.** Oficina consulta el disponible antes de confirmar; la reserva lo baja, y la factura baja el stock físico y consume la reserva. La producción del día suma al stock físico y el conteo lo corrige.
- **La planilla de stock es solo del piloto.** Va punteada en el diagrama porque dura 2 semanas, con papas fritas, el producto que más falta. Recibe los mismos tres aportes (por eso el diagrama los muestra juntos antes de bifurcar) y usa la misma regla de stock disponible. Después del Go/No-Go se archiva.
- **El tablero no guarda nada propio.** Muestra los cuatro indicadores de la sección 8 y se alimenta de la exportación CSV de Discovery, el registro semanal de pedidos recortados o demorados y las horas extras de la liquidación de sueldos. Puede ser una hoja simple: el formato lo fija la sección 8.
- **El distribuidor queda afuera de los datos.** Sigue pidiendo por WhatsApp o teléfono y recibe el aviso si falta algo, pero no ve el stock: esa visibilidad queda para "later" (sección 1).

**Lo que el diagrama da por cierto y no está probado.** Supone que el módulo de stock de Discovery permite pedidos y reserva, que la facturación consume la reserva y que el módulo está dentro de la licencia que ya pagan. Es lo que sabe nuestro compañero que trabaja en la empresa, pero nadie lo usó en Dulxelitos: falta confirmarlo por escrito con Buenos Aires Software (versión, soporte y costo, pendientes en las secciones 2, 4, 5 y 7). Es el supuesto 3 de la sección 4. Los datos no dependen de la herramienta (la planilla del piloto maneja los mismos con la misma regla): si Discovery no se comporta así, el flujo sigue en pie con la planilla (alternativa A) y solo cambia dónde está el registro.

## Datos

Cada fila dice qué dato es, de dónde sale, adónde va, para qué se usa y quién responde por él. Los responsables son roles, no personas, y salen del proceso futuro de la sección 3. Los que llevan asterisco (*) son propuestas nuestras que todavía no hablamos con cada área.

### Datos maestros

Cambian poco y todo lo demás se apoya en ellos. Si un maestro está mal, está mal en cada pedido, parte y conteo.

| Dato | Origen | Destino | Uso | Responsable |
|---|---|---|---|---|
| **Productos** (código, nombre, presentación) | Discovery, donde ya existen por la facturación | Discovery (pedidos, stock, facturación) y planilla del piloto | Que pedido, parte de producción y conteo hablen del mismo producto. Falta revisar que la lista coincida con lo que se produce | Responsable de sistemas; Dirección pide las altas |
| **Distribuidores** (57 en 7 provincias) | Discovery, donde ya existen como clientes | Discovery | Identificar al que pide y su zona, que define el plazo estándar de entrega (en la Patagonia, hasta una semana). [dato pendiente: dónde queda registrada la zona de cada distribuidor] | Oficina (administración) |
| **Stock mínimo por producto** | Dirección (dueño e hijos), que fija el valor | Discovery, si el módulo tiene ese campo; si no, una lista que mantiene el responsable de sistemas | Planificar la producción semanal junto con los pedidos pendientes. [dato pendiente: stock mínimo de cada producto, a fijar con el primer conteo] | Dirección fija el valor; responsable de sistemas lo carga |

### Datos transaccionales

Se generan todos los días con el trabajo. Son los que hoy no existen o están repartidos en papel, chat y planillas sueltas.

| Dato | Origen | Destino | Uso | Responsable |
|---|---|---|---|---|
| **Notas de pedido** (distribuidor, productos, cantidades) | Pedido del distribuidor por WhatsApp o teléfono, recibido por Oficina | Discovery | Confirmar sabiendo qué hay, armar el pedido, facturar y contar los pedidos recibidos. Reemplaza las tres transcripciones de hoy (chat, papel, lista) | Oficina |
| **Reservas** (producto y cantidad por pedido confirmado sin facturar) | La nota de pedido, en el momento de confirmarla | Discovery (stock reservado) | Calcular el stock disponible. La factura la consume | Oficina |
| **Partes de producción** (producto y cantidad producida en el día) | Producción, al cierre del turno | Discovery (suma al stock físico) | Tener el stock físico al día y planificar contra pedidos. Reemplaza al control semanal propio de Producción (falta confirmar qué contiene) | Responsable de carga del turno, con suplente |
| **Conteos físicos** (producto, cantidad contada, fecha) | Depósito, que deja la hoja de conteo en el conteo cíclico semanal | Discovery, como ajuste con motivo que carga el responsable de sistemas, y el cálculo de exactitud | Corregir el stock físico y medir la exactitud de stock. [dato pendiente: responsable del conteo inicial y del semanal] | Depósito deja la hoja de conteo; responsable de sistemas carga el ajuste |
| **Lista de armado** (productos y cantidades de cada pedido confirmado) | Discovery, a partir de la nota de pedido confirmada | Depósito, impresa o en pantalla | Armar el pedido desde un solo registro, sin volver a pasar el chat al papel y el papel a una lista. Ver el listado en Integraciones | Oficina, al confirmar el pedido |
| **Facturas** | La nota de pedido confirmada, cuando Oficina factura | Discovery | Cobrar y cerrar el pedido. Baja el stock físico y consume la reserva (a confirmar en el supuesto 3) | Oficina (facturación) |
| **Registro semanal de pedidos recortados o demorados** | Oficina, que sabe qué pedidos salieron incompletos o fuera de plazo, en una hoja compartida simple | Tablero | Indicador de pedidos completos y a tiempo. Es el registro que dio la semana base | Oficina* |
| **Horas extras del mes** (totales) | Liquidación de sueldos | Tablero | Indicador de horas extras. La liquidación no distingue las planificadas de las no planificadas | Oficina (administración)* |

**El registro semanal de recortes, columna por columna.** Una línea por pedido, con la fecha, el distribuidor, el producto que faltó, qué pasó (recortado, demorado, rechazado o reprogramado de entrada, o cancelado tras el aviso) y el motivo. Oficina anota además el total semanal de pedidos recibidos, que es el denominador del indicador 1 de la sección 8 e incluye los que no llegan a nota de pedido.

### Datos calculados

Nadie los carga: se calculan solos o con una fórmula fija.

- **Stock disponible**, por producto: stock físico − reservado por pedidos confirmados sin facturar. Lo calcula Discovery (o la planilla, en el piloto) y es la cifra con la que Oficina contesta al distribuidor.
- **Los cuatro indicadores del tablero:** pedidos completos y a tiempo, exactitud de stock, días con producción cargada y horas extras por mes. Las fórmulas y las fichas están en la sección 8.

## Integraciones

**No hay ninguna integración automática, y es a propósito.** La Parte 1 mostró que Discovery está desactualizado, tiene errores y no se puede integrar con otros sistemas, así que no hay API a la que conectarse. Y aunque la hubiera no la necesitaríamos: lo que se mueve entre un lugar y otro son pocas cargas por día, y el problema no es la velocidad del dato sino que hoy no existe. Lo que sí hay es **carga manual controlada** y **exportación CSV**.

| Flujo | Cómo | Cuándo | Quién | Cómo se controla |
|---|---|---|---|---|
| Pedido del distribuidor → Discovery | Carga manual, una sola vez, directo en Discovery | Al recibir el pedido; la reserva, al confirmarlo | Oficina | Producto y distribuidor se eligen de los maestros, no se escriben a mano. No se confirma sin consultar el disponible |
| Producción → Discovery | Carga manual del parte del día | Todos los días, al cierre del turno | Responsable de carga del turno, con suplente | Una carga por producto producido. Si un día no se carga, el indicador de días con producción cargada lo muestra |
| Discovery → Depósito | Lista de armado por pedido confirmado, impresa o en pantalla [dato pendiente: qué listado de armado emite Discovery] | Al confirmar cada pedido | Oficina confirma; Depósito arma | Depósito arma solo desde pedidos confirmados, que ya tienen la reserva hecha |
| Depósito → Discovery | Hoja de conteo, y después el ajuste cargado a mano | Una vez por semana | Depósito deja la hoja de conteo; el responsable de sistemas carga el ajuste | Se compara contra Discovery antes de ajustar. La diferencia queda registrada y es la exactitud de stock |
| Discovery → tablero | Exportación CSV | Cada semana* | Responsable de sistemas | Los totales del tablero se pueden recalcular desde el CSV. Si el resultado no coincide con Discovery, manda Discovery |
| Registro de recortes → tablero | Carga manual | Cada semana* | Oficina* | Se anota un pedido por línea, con el motivo del recorte o de la demora |
| Liquidación de sueldos → tablero | Carga manual de las horas extras totales | Una vez por mes, porque la liquidación es mensual | Oficina (administración)* | Se carga el total de la liquidación, no una estimación |
| Planilla del piloto → tablero | CSV o carga manual | Solo durante las 2 semanas del piloto | Responsable de sistemas | El mismo criterio de stock disponible que Discovery, para que los números sean comparables |

**Un supuesto sobre la exportación.** Damos por hecho que Discovery puede sacar listados a CSV o a una planilla de cálculo, a confirmar con el proveedor junto con el supuesto 3: [dato pendiente: listados que Discovery puede exportar]. Si no pudiera, los números que necesita el tablero (pedidos recibidos, producción cargada por día y diferencias de conteo) son pocos por semana y se pasan a mano: se pierde comodidad, no la propuesta.

**Qué vuelve "controlada" a la carga manual.** Cada dato se carga en un solo lugar y una sola vez; cada carga tiene una persona responsable con suplente, porque una carga que depende de alguien que falta se corta; y hay un control que avisa cuando algo falla: el conteo semanal mide si lo cargado coincide con lo que hay, y los días con producción cargada miden si la carga se hace.

**Lo que no integramos y por qué.**

- **WhatsApp con Discovery.** El pedido sigue entrando por chat y se carga a mano: conectarlos pediría una API que no existe y un CRM, que es otro problema y está fuera de alcance.
- **SaaS de gestión, tienda online y portal del distribuidor.** El SaaS se evaluó y se descartó en la sección 2. La tienda y el portal no hacen falta para este problema y quedan fuera del alcance.
- **Discovery con el distribuidor.** El distribuidor no consulta el stock. Primero tiene que haber un stock confiable; recién después se le puede mostrar ("later").
- **Costeo, listas de precios, insumos y packaging.** No son parte de este problema (sección 1).

## Reglas de datos

Las reglas valen para los datos críticos: el stock físico, las reservas, los productos, los distribuidores y el stock mínimo. Son simples a propósito, porque las tiene que poder cumplir una empresa de 15 a 20 personas con la planta saturada. Tres principios las sostienen:

1. **Un solo lugar por dato.** Cada dato de pedidos y stock vive en Discovery. La planilla de stock solo existe en el piloto, y solo para el producto del piloto. Dos datos viven afuera porque Discovery no los tiene: el registro semanal de recortes, en una hoja compartida simple que lleva Oficina, y las horas extras, que salen de la liquidación de sueldos.
2. **No se borra, se corrige.** Un error se arregla con un movimiento nuevo y un motivo escrito, que deja rastro. Nadie pisa un número.
3. **Lo que se cuenta manda sobre lo que se cargó.** Si el conteo físico y Discovery no coinciden, se corrige Discovery.

### Quién puede qué

| Rol | Puede cargar | No toca |
|---|---|---|
| Oficina | Notas de pedido, reservas, facturas, y altas y correcciones de distribuidores | El stock físico ni los productos |
| Producción (responsable de carga del turno y suplente) | Partes de producción, y la corrección de sus propios partes el mismo día | Reservas ni facturas |
| Depósito | La hoja de conteo | Los ajustes de stock |
| Responsable de sistemas | Productos y stock mínimo, ajustes de stock, depuración de maestros y permisos | Pedidos ni partes, salvo para corregirlos |
| Dirección | Fija el stock mínimo y pide las altas de productos | Discovery: no carga ahí |

Si Discovery no permite separar los permisos así, la regla se sostiene por procedimiento y se revisa en el conteo semanal. Varias de estas tareas caen en el responsable de sistemas (ajustes, maestros, exportación), así que el tiempo que puede dedicarle cada semana, que la sección 5 deja como dato pendiente, también decide si las reglas se sostienen.

### Alta

- **Producto nuevo.** Lo pide Dirección y lo da de alta el responsable de sistemas, con código único, nombre, presentación y stock mínimo. Hasta que no está de alta, Producción no lo puede cargar ni Oficina reservarlo. Empieza con stock físico cero y suma con el primer parte de producción o con un conteo.
- **Distribuidor nuevo.** Lo da de alta Oficina (administración) antes de tomarle el primer pedido, con su zona. Antes de crearlo se busca, para no duplicarlo.
- **Stock mínimo.** Lo fijan el dueño y los hijos, y lo carga el responsable de sistemas. Se revisa cuando Dirección lo pide, no antes.
- **Stock inicial.** Sale del conteo físico inicial (alternativa B), no de la planilla del piloto ni de lo que se cree que hay. En el piloto, el stock inicial de papas fritas sale de un conteo de ese producto.
- **Nota de pedido y reserva.** La nota se carga una sola vez, al recibir el pedido. La reserva se crea al confirmarlo, nunca antes ni después. Si falta producto, se reserva lo que hay (esa parte se despacha solo si el distribuidor la acepta; si no, el pedido espera completo) y el resto queda anotado como pendiente, sin reserva, con la fecha estimada que Producción confirmó en la reunión diaria, si la confirmó. Cómo se anota ese resto depende de lo que permita Discovery, y se prueba en el piloto (supuesto 3).
- **Parte de producción.** Lo carga el responsable del turno al cerrarlo, con la cantidad realmente producida. No se carga lo planificado ni lo estimado.

### Corrección

- **Diferencia de conteo.** Manda lo contado. Depósito deja la hoja de conteo; el responsable de sistemas carga un ajuste con motivo (rotura, error de carga, merma u otro) y avisa a Producción si la diferencia viene de un parte. No se edita el stock directamente. Si el mismo producto difiere semana tras semana, el motivo se trata en la reunión diaria.
- **Parte de producción mal cargado.** Lo corrige el mismo día el responsable de carga del turno, que es quien lo cargó, con una corrección que resta lo mal cargado y carga lo correcto. Es la única corrección de stock que no pasa por el responsable de sistemas. Si se descubre después, lo recoge el conteo y el ajuste ya es del responsable de sistemas.
- **Nota de pedido equivocada.** Antes de facturar se corrige la nota y se rehace la reserva. Una factura emitida no se edita: se corrige con el procedimiento contable que ya usa administración, y si la mercadería quedó mal, se ajusta por conteo.
- **Reserva que no corresponde.** La libera Oficina, que fue quien la creó, y deja el motivo (el distribuidor canceló, el pedido se rehízo, se cargó mal).
- **Quién corrige.** Quien cargó el dato. Los ajustes de stock físico son del responsable de sistemas, con una sola excepción: el parte de producción mal cargado, que corrige el mismo día quien lo cargó. Los productos y su depuración son del responsable de sistemas; los datos de los distribuidores los corrige Oficina, y los duplicados, el responsable de sistemas. En todos los casos con motivo escrito.

### Depuración

- **Reservas viejas.** Una reserva sin facturar sigue restando del disponible. Si queda abierta, el stock parece más chico de lo que es y Oficina vuelve a dudar de la cifra. Oficina revisa cada semana las reservas abiertas. La que pasó el plazo estándar de su zona sin facturarse (en la Patagonia, hasta una semana) se confirma con el distribuidor y se factura o se libera. Lo que se libera se comenta en la reunión diaria.
- **Productos que ya no se fabrican.** No se borran: el responsable de sistemas los marca como inactivos, para que no admitan pedidos y se conserve el historial.
- **Duplicados.** Si un producto o un distribuidor aparece repetido, el responsable de sistemas se queda con uno y deja el otro inactivo. Nunca se borra un código que tenga movimientos.
- **Cierre de la planilla del piloto.** Al terminar las 2 semanas se archiva en solo lectura y no se sigue usando, para que no haya dos fuentes del mismo dato.
- **El tablero no es una fuente.** Si un número del tablero no coincide con Discovery, manda Discovery y el tablero se recalcula.

### Cómo se sabe que se cumplen

Dos de los cuatro indicadores miden estas reglas sin agregar trabajo. La **exactitud de stock** dice si lo cargado coincide con lo contado, y los **días con producción cargada** dicen si las cargas se hacen. Si alguno baja, primero se revisan la capacitación, la carga de trabajo, los incentivos y las reglas, antes que el compromiso de la gente (sección 5). La revisión de las reglas es parte de cada Go/No-Go.

**Fuentes:** secciones 2 a 5 de esta parte; relevamiento del proceso; Parte 1 (Discovery, sus límites de integración y el canal).
