# Arquitectura conceptual y flujo de datos

Esta sección dibuja la alternativa recomendada (la B: el stock de Discovery, probado antes con una planilla compartida) como cajas y flechas, y dice qué datos se mueven, quién los carga, cómo pasan de un lugar a otro y qué reglas los mantienen limpios.

La guía de la cátedra pregunta si una empresa chica necesita un diagrama de la NASA o un flujo simple. Para una pyme de 15 a 20 personas la respuesta es el flujo simple: **un solo sistema, y ya lo tienen.** Es Discovery, que hoy usan para facturar, más una planilla compartida que existe solo durante el piloto de 2 semanas y un tablero con cuatro indicadores. No hay sistema nuevo que comprar (el costo de activar el módulo de stock está pendiente, sección 4), ni integración automática, ni canal nuevo: las áreas aportan sus datos a un solo lugar, y de ahí salen la lista para armar cada pedido y los números del tablero.

## Diagrama

![Arquitectura y flujo de datos](diagramas/arquitectura.png)

Para la exposición hay además una versión interactiva del flujo de datos, el archivo `Flujo de datos interactivo - Dulxelitos.html` de la carpeta de entrega, que se abre en el navegador.

### Cómo se lee

- **Tres áreas aportan, un solo lugar guarda.** Oficina carga la nota de pedido y reserva el stock antes de confirmar; Producción carga lo producido al cierre del turno; Depósito deja la hoja del conteo semanal, que el responsable de sistemas carga como ajuste (quién cuenta: [dato pendiente: responsable del conteo inicial y del semanal]). Los tres aportes entran juntos a Discovery y de ahí sale, para cada pedido confirmado, la lista de armado que usa Depósito: lo que se gana por cargar el pedido una sola vez.
- **La planilla de stock es solo del piloto.** Va punteada en el diagrama porque dura 2 semanas, con papas fritas, el producto que más falta. Recibe los mismos tres aportes (por eso el diagrama los muestra juntos antes de bifurcar), usa la misma regla de stock disponible que Discovery (sección 3) y, después del Go/No-Go, se archiva.
- **El tablero no guarda nada propio.** Se alimenta de la exportación CSV de Discovery, el registro semanal de Oficina y las horas extras de la liquidación; qué muestra y cómo se mira, en la sección 8.
- **El distribuidor queda afuera de los datos.** Sigue pidiendo por WhatsApp o teléfono y recibe el aviso si falta algo, pero no ve el stock: esa visibilidad queda para "later" (sección 1).

**Lo que el diagrama da por cierto y no está probado.** Supone que el módulo de stock de Discovery permite pedidos y reserva (también reservar solo una parte de un pedido), que la factura consume la reserva y que el módulo está dentro de la licencia que ya pagan. Lo sabe nuestro compañero que trabaja en la empresa, pero nadie lo usó en Dulxelitos: falta confirmarlo por escrito con Buenos Aires Software (supuesto 3 de la sección 4). Los datos no dependen de la herramienta: si Discovery no se comporta así, el flujo sigue en pie con la planilla (alternativa A) y solo cambia dónde está el registro.

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
| **Notas de pedido** (distribuidor, productos, cantidades) | Pedido del distribuidor por WhatsApp o teléfono, recibido por Oficina | Discovery | Confirmar sabiendo qué hay, armar, facturar y contar los pedidos recibidos. Reemplaza las tres transcripciones de hoy | Oficina |
| **Reservas** (producto y cantidad por pedido confirmado sin facturar) | La nota de pedido, al confirmarla | Discovery (stock reservado) | Calcular el stock disponible; la factura la consume | Oficina |
| **Partes de producción** (producto y cantidad producida en el día) | Producción, al cierre del turno | Discovery (suma al stock físico) | Stock físico al día y planificación contra pedidos. Reemplaza al control semanal propio de Producción (falta confirmar qué contiene) | Responsable de carga del turno, con suplente |
| **Conteos físicos** (producto, cantidad contada, fecha) | Depósito, en la hoja del conteo cíclico semanal | Discovery, como ajuste con motivo que carga el responsable de sistemas, y el cálculo de exactitud | Corregir el stock físico y medir la exactitud. [dato pendiente: responsable del conteo inicial y del semanal] | Depósito deja la hoja; responsable de sistemas carga el ajuste |
| **Lista de armado** (productos y cantidades de cada pedido confirmado) | Discovery, desde la nota de pedido confirmada | Depósito, impresa o en pantalla | Armar desde un solo registro, sin pasar el chat al papel y el papel a una lista (ver Integraciones) | Oficina, al confirmar el pedido |
| **Facturas** | La nota de pedido confirmada, cuando Oficina factura | Discovery | Cobrar y cerrar el pedido; baja el stock físico y consume la reserva (a confirmar en el supuesto 3) | Oficina (facturación) |
| **Registro semanal de pedidos recortados o demorados** | Oficina, que sabe qué pedidos salieron incompletos o fuera de plazo, en una hoja compartida simple | Tablero | Indicador de pedidos completos y a tiempo; es el registro que dio la semana base | Oficina* |
| **Horas extras del mes** (totales) | Liquidación de sueldos | Tablero | Indicador de horas extras; la liquidación no distingue las planificadas de las no planificadas | Oficina (administración)* |

**El registro semanal de recortes, columna por columna.** Una línea por pedido, con la fecha, el distribuidor, el producto que faltó, qué pasó (recortado, demorado, rechazado o reprogramado de entrada, o cancelado tras el aviso) y el motivo. Oficina anota además el total semanal de pedidos recibidos, que es el denominador del indicador 1 de la sección 8 e incluye los que no llegan a nota de pedido.

**Datos calculados.** Nadie los carga: el **stock disponible** de cada producto (stock físico − reservado por pedidos confirmados sin facturar, sección 3) lo calcula Discovery, o la planilla en el piloto, y es la cifra con la que Oficina contesta al distribuidor; los **cuatro indicadores del tablero** salen de las fórmulas de la sección 8.

## Integraciones

**No hay ninguna integración automática, y es a propósito.** La Parte 1 mostró que Discovery está desactualizado, tiene errores y no se puede integrar con otros sistemas, así que no hay API a la que conectarse. Y no la necesitaríamos: se mueven pocas cargas por día y el problema no es la velocidad del dato sino que hoy no existe. Lo que hay es **carga manual controlada** y **exportación CSV**.

| Flujo | Cómo | Cuándo | Quién | Cómo se controla |
|---|---|---|---|---|
| Pedido del distribuidor → Discovery | Carga manual, una sola vez; la reserva, al confirmar | Al recibir el pedido | Oficina | Producto y distribuidor se eligen de los maestros, no se escriben. No se confirma sin consultar el disponible |
| Producción → Discovery | Carga manual del parte del día | Todos los días, al cierre del turno | Responsable de carga del turno, con suplente | Una carga por producto producido; si un día no se carga, lo muestra el indicador de días con producción cargada |
| Discovery → Depósito | Lista de armado por pedido confirmado, impresa o en pantalla [dato pendiente: qué listado de armado emite Discovery] | Al confirmar cada pedido | Oficina confirma; Depósito arma | Depósito arma solo desde pedidos confirmados, que ya tienen la reserva |
| Depósito → Discovery | Hoja de conteo y después el ajuste cargado a mano | Una vez por semana | Depósito deja la hoja; el responsable de sistemas carga el ajuste | Se compara contra Discovery antes de ajustar; la diferencia queda registrada y es la exactitud de stock |
| Discovery (y la planilla, en el piloto) → tablero | Exportación CSV; en el piloto, CSV o carga manual desde la planilla, con el mismo criterio de stock disponible | Cada semana* | Responsable de sistemas | Los totales se pueden recalcular desde el CSV; si no coinciden con Discovery, manda Discovery |
| Registro de recortes → tablero | Carga manual | Cada semana* | Oficina* | Un pedido por línea, con el motivo del recorte o la demora |
| Liquidación de sueldos → tablero | Carga manual de las horas extras totales | Una vez por mes | Oficina (administración)* | Se carga el total de la liquidación, no una estimación |

**Un supuesto sobre la exportación.** Damos por hecho que Discovery saca listados a CSV o a una planilla de cálculo, a confirmar con el proveedor junto con el supuesto 3: [dato pendiente: listados que Discovery puede exportar]. Si no pudiera, los números del tablero (pedidos recibidos, producción cargada por día y diferencias de conteo) son pocos por semana y se pasan a mano: se pierde comodidad, no la propuesta.

**Lo que no integramos y por qué.** WhatsApp con Discovery: el pedido sigue entrando por chat y se carga a mano, porque conectarlos pediría una API que no existe y un CRM, que está fuera de alcance. SaaS de gestión, tienda online y portal del distribuidor: el SaaS se descartó en la sección 2, y la tienda y el portal no hacen falta para este problema ("later"). Costeo, listas de precios, insumos y packaging: no son parte de este problema (sección 1).

## Reglas de datos

Las reglas valen para los datos críticos: el stock físico, las reservas, los productos, los distribuidores y el stock mínimo. Son simples a propósito, porque las tiene que poder cumplir una empresa de 15 a 20 personas con la planta saturada. Tres principios las sostienen: La revisión de las reglas es parte de cada Go/No-Go (sección 8); si baja la exactitud de stock o los días con producción cargada, primero se revisan capacitación, carga de trabajo, incentivos y reglas, antes que el compromiso de la gente (sección 5).

1. **Un solo lugar por dato.** Cada dato de pedidos y stock vive en Discovery. La planilla de stock solo existe en el piloto, y solo para el producto del piloto. Dos datos viven afuera porque Discovery no los tiene: el registro semanal de recortes, en una hoja compartida simple que lleva Oficina, y las horas extras, que salen de la liquidación de sueldos.
2. **No se borra, se corrige.** Un error se arregla con un movimiento nuevo y un motivo escrito, que deja rastro. Nadie pisa un número.
3. **Lo que se cuenta manda sobre lo que se cargó.** Si el conteo físico y Discovery no coinciden, se corrige Discovery.

### Quién puede qué

Cada rol carga lo suyo y no toca lo ajeno. Oficina carga notas de pedido, reservas, facturas y distribuidores, pero no el stock físico ni los productos. Producción (el responsable de carga del turno y su suplente) carga los partes de producción y corrige los suyos el mismo día, pero no reservas ni facturas. Depósito deja la hoja de conteo y no toca los ajustes. El responsable de sistemas carga productos, stock mínimo, ajustes de stock, depuración de maestros y permisos, y no toca pedidos ni partes salvo para corregirlos. Dirección fija el stock mínimo y pide las altas de productos, pero no carga en Discovery. Si Discovery no permite separar los permisos así, la regla se sostiene por procedimiento y se revisa en el conteo semanal. Como varias tareas caen en el responsable de sistemas, el tiempo que puede dedicarle cada semana, que la sección 5 deja como dato pendiente, también decide si las reglas se sostienen.

### Alta, corrección y depuración

La corrección es siempre de quien cargó el dato, con motivo escrito. Los ajustes de stock físico son del responsable de sistemas, con una sola excepción: el parte de producción mal cargado, que corrige el mismo día quien lo cargó.

| Dato | Alta | Corrección | Depuración |
|---|---|---|---|
| **Producto** | Lo pide Dirección y lo da de alta el responsable de sistemas, con código único, nombre, presentación y stock mínimo. Hasta entonces Producción no puede cargarlo ni Oficina reservarlo. Empieza con stock cero y suma con el primer parte de producción o con un conteo | El responsable de sistemas | Los que ya no se fabrican se marcan inactivos: no admiten pedidos y se conserva el historial. Un duplicado deja un código activo y el otro inactivo; nunca se borra un código con movimientos |
| **Distribuidor** | Lo da de alta Oficina (administración) antes del primer pedido, con su zona; antes de crearlo se busca, para no duplicarlo | Oficina; los duplicados, el responsable de sistemas | Igual que el producto |
| **Stock mínimo** | Lo fijan el dueño y los hijos y lo carga el responsable de sistemas; se revisa cuando Dirección lo pide, no antes | El responsable de sistemas, a pedido de Dirección | – |
| **Stock inicial y conteo semanal** | El stock inicial sale del conteo físico inicial, no de la planilla del piloto ni de lo que se cree que hay (en el piloto, de un conteo de papas fritas) | Manda lo contado: Depósito deja la hoja de conteo y el responsable de sistemas carga un ajuste con motivo (rotura, error de carga, merma u otro), sin editar el stock directamente, y avisa a Producción si la diferencia viene de un parte. Si un producto difiere semana tras semana, se trata en la reunión diaria | – |
| **Nota de pedido y reserva** | La nota se carga una sola vez, al recibir el pedido; la reserva se crea al confirmarlo, nunca antes ni después. Si falta producto, se reserva lo que hay (esa parte se despacha solo si el distribuidor la acepta; si no, el pedido espera completo) y el resto queda pendiente, sin reserva, con la fecha que Producción confirmó, si la confirmó. Cómo se anota ese resto lo confirma Buenos Aires Software en la prueba técnica (supuesto 3) | Antes de facturar se corrige la nota y se rehace la reserva. Una factura emitida no se edita: se corrige con el procedimiento contable que ya usa administración y, si la mercadería quedó mal, por conteo. Una reserva que no corresponde la libera Oficina, que la creó, y deja el motivo | Oficina revisa cada semana las reservas abiertas, porque una sin facturar sigue restando del disponible y el stock parece más chico de lo que es. La que pasó el plazo estándar de su zona (en la Patagonia, hasta una semana) se confirma con el distribuidor y se factura o se libera; lo liberado se comenta en la reunión diaria |
| **Parte de producción** | Lo carga el responsable del turno al cerrarlo, con la cantidad realmente producida, no la planificada ni la estimada | Lo corrige el mismo día quien lo cargó, con una corrección que resta lo mal cargado y carga lo correcto. Si se descubre después, lo recoge el conteo | – |
| **Planilla del piloto y tablero** | – | – | La planilla se archiva en solo lectura al terminar las 2 semanas, para no tener dos fuentes del mismo dato. El tablero no es una fuente: si un número no coincide con Discovery, manda Discovery y el tablero se recalcula |

**Fuentes:** secciones 2 a 5 de esta parte; relevamiento del proceso; Parte 1 (Discovery, sus límites de integración y el canal).
