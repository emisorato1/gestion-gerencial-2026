# Arquitectura conceptual y flujo de datos

La alternativa B, el stock en Discovery probado antes con una planilla compartida, no pide una arquitectura complicada. Para una pyme de 15 a 20 personas alcanza con un flujo simple de un solo sistema, y ese sistema la empresa ya lo tiene: Discovery, que hoy usa para facturar. A eso se suman una planilla compartida, solo durante el piloto de 2 semanas, y un tablero con cuatro indicadores. No hay sistema nuevo que comprar, ni integración automática, ni canal nuevo.

## Diagrama

![Arquitectura y flujo de datos](diagramas/arquitectura.png)

El flujo también se adjunta en una versión interactiva.

### Qué muestra el diagrama

- Oficina carga pedidos y reservas, Producción lo producido y Depósito la hoja del conteo semanal, que el responsable de sistemas carga como ajuste. Todo entra a Discovery, de donde sale la lista de armado de cada pedido confirmado.
- La planilla de stock va punteada porque es solo del piloto: dura 2 semanas, con papas fritas, el producto con más faltantes, y usa la misma regla de stock disponible que Discovery (sección 3).
- El distribuidor sigue pidiendo por WhatsApp o teléfono y recibe el aviso si falta algo, pero no ve el stock, algo que queda para más adelante (sección 1).

El diagrama supone que el módulo de stock de Discovery permite pedidos y reserva, incluso de una parte del pedido, y que la factura consume la reserva. Según lo relevado, el módulo existe dentro de la licencia actual pero nunca se usó en Dulxelitos (supuesto 3 de la sección 4). Si no fuera así, el flujo se sostiene con la planilla (alternativa A) y solo cambia dónde está el registro.

## Datos

Los responsables son roles (sección 3); el asterisco (*) marca los que falta acordar con cada área.

### Datos maestros

| Dato | Origen | Destino | Uso | Responsable |
|---|---|---|---|---|
| **Productos** (código, nombre, presentación) | Discovery, donde ya existen | Discovery y planilla del piloto | Que pedido, parte y conteo usen el mismo producto; falta revisar la lista contra lo que se produce | Responsable de sistemas; Dirección pide las altas |
| **Distribuidores** (57 en 7 provincias) | Discovery, donde ya son clientes | Discovery | Identificar al que pide y su zona, que define el plazo estándar de entrega (en la Patagonia, hasta una semana); falta ver dónde se registra la zona | Oficina (administración) |
| **Stock mínimo por producto** | Dirección (dueño e hijos) | Discovery, si el módulo tiene el campo; si no, una lista del responsable de sistemas | Planificar la producción semanal; el valor de cada producto sale del primer conteo y se revisa cuando Dirección lo pide | Dirección fija el valor; responsable de sistemas lo carga |

### Datos transaccionales

| Dato | Origen | Destino | Uso | Responsable |
|---|---|---|---|---|
| **Notas de pedido** (distribuidor, productos, cantidades) | WhatsApp o teléfono, recibido por Oficina | Discovery | Confirmar, armar, facturar y contar pedidos; reemplaza las tres anotaciones del mismo pedido | Oficina |
| **Reservas** (por pedido confirmado sin facturar) | La nota de pedido, al confirmarla | Discovery | Calcular el stock disponible; la factura la consume | Oficina |
| **Partes de producción** (cantidad producida por producto en el día) | Producción, al cierre del turno | Discovery (suma al stock físico) | Stock físico al día y planificación; reemplaza el control semanal propio de Producción | Responsable de carga del turno, con suplente |
| **Conteos físicos** (producto, cantidad, fecha) | Depósito, hoja del conteo semanal | Discovery, como ajuste con motivo | Ajustar el stock y medir la exactitud | Depósito deja la hoja; responsable de sistemas carga el ajuste |
| **Lista de armado** (por pedido confirmado) | Discovery, desde la nota confirmada | Depósito, impresa o en pantalla | Armar desde un solo registro | Oficina, al confirmar |
| **Facturas** | La nota confirmada, cuando Oficina factura | Discovery | Cobrar y cerrar el pedido; baja el stock y consume la reserva (supuesto 3) | Oficina (facturación) |
| **Registro semanal de pedidos recortados o demorados** | Oficina, en una hoja compartida simple | Tablero | Indicador de pedidos completos y a tiempo; dio la semana base | Oficina* |
| **Horas extras del mes** | Liquidación de sueldos | Tablero | Indicador de horas extras; la liquidación no separa planificadas de no planificadas | Oficina (administración)* |

El registro semanal lleva una línea por pedido: fecha, distribuidor, producto que faltó, qué pasó (recortado, demorado, rechazado o reprogramado de entrada, o cancelado tras el aviso) y motivo. Oficina anota además el total semanal de pedidos recibidos, incluidos los que no llegan a nota de pedido, que es el denominador del indicador 1 de la sección 8.

Algunos datos no los carga nadie. El stock disponible, que es el stock físico menos lo reservado por pedidos confirmados sin facturar (sección 3), lo calcula Discovery, o la planilla en el piloto, y es la cifra con la que Oficina contesta al distribuidor. Los cuatro indicadores del tablero salen de las fórmulas de la sección 8.

## Integraciones

No hay integraciones automáticas. En la Parte 1 vimos que Discovery está desactualizado, tiene errores y no se puede integrar con otros sistemas, así que no hay API a la que conectarse. Tampoco haría falta: se mueven pocas cargas por día y hoy lo que falta es el dato. Todo es carga manual controlada y exportación CSV.

| Flujo | Cómo | Cuándo | Quién | Cómo se controla |
|---|---|---|---|---|
| Pedido del distribuidor → Discovery | Carga manual, una sola vez; reserva al confirmar | Al recibir el pedido | Oficina | Producto y distribuidor salen de los maestros; no se confirma sin ver el disponible |
| Producción → Discovery | Carga manual del parte | Todos los días, al cierre del turno | Responsable de carga del turno, con suplente | Una carga por producto; si un día falta, lo muestra el indicador de días con producción cargada |
| Discovery → Depósito | Lista de armado impresa o en pantalla (qué listado emite Discovery, a confirmar con el proveedor) | Al confirmar el pedido | Oficina confirma; Depósito arma | Solo se arma desde pedidos confirmados, que ya tienen reserva |
| Depósito → Discovery | Hoja de conteo y ajuste a mano | Una vez por semana | Depósito deja la hoja; responsable de sistemas carga el ajuste | Se compara contra Discovery antes de ajustar; la diferencia queda registrada y es la exactitud de stock |
| Discovery (y planilla, en el piloto) → tablero | Exportación CSV; en el piloto, CSV o carga manual desde la planilla, con el mismo criterio de stock disponible | Cada semana* | Responsable de sistemas | Los totales se recalculan desde el CSV; el tablero no es una fuente, así que si no coincide con Discovery, manda Discovery y se recalcula |
| Registro de recortes → tablero | Carga manual | Cada semana* | Oficina* | Un pedido por línea, con el motivo |
| Liquidación de sueldos → tablero | Carga manual del total de horas extras | Una vez por mes | Oficina (administración)* | Se carga el total que figura en la liquidación |

Damos por hecho que Discovery exporta listados a CSV o a planilla de cálculo (supuesto 3). Si no pudiera, los números del tablero son pocos por semana y se pasan a mano, con menos comodidad pero sin cambiar la propuesta.

WhatsApp no se integra con Discovery: conectarlos pediría una API que no existe y un CRM, que está fuera de alcance, así que el pedido sigue entrando por chat y se carga a mano. El SaaS de gestión se descartó en la sección 2; la tienda online y el portal del distribuidor quedan para más adelante, y costeo, precios, insumos y packaging no son parte del problema (sección 1).

## Reglas de datos

Las reglas valen para los datos críticos (stock físico, reservas, productos, distribuidores y stock mínimo) y son simples a propósito, porque las tiene que poder cumplir una empresa de 15 a 20 personas con la carga de trabajo que ya tiene la planta. Se apoyan en tres principios.

1. Un solo lugar por dato. Todo lo de pedidos y stock vive en Discovery; la planilla existe solo en el piloto y solo para su producto, y se archiva en solo lectura al terminar las 2 semanas para no tener dos fuentes del mismo dato. Fuera de Discovery quedan solo el registro semanal de recortes y las horas extras, que Discovery no maneja, y el stock mínimo si el módulo no tiene ese campo.
2. Nada se borra. Un error se arregla con un movimiento nuevo y un motivo escrito; nadie pisa un número.
3. Manda lo contado. Si el conteo físico y Discovery no coinciden, se ajusta Discovery.

La revisión de las reglas es parte de cada Go/No-Go (sección 8).

### Quién puede qué

Cada rol carga lo suyo. Oficina, las notas de pedido, reservas, facturas y distribuidores, pero no el stock físico ni los productos. Producción, los partes, que arregla el mismo día, sin tocar reservas ni facturas. Depósito deja la hoja de conteo y no toca los ajustes. El responsable de sistemas carga productos, stock mínimo, ajustes, depuración de maestros y permisos, y no toca pedidos ni partes salvo para arreglarlos. Dirección fija el stock mínimo y pide las altas de productos, pero no carga en Discovery. Si Discovery no permite separar así los permisos, la regla se sostiene por procedimiento y se revisa en el conteo semanal. Como varias tareas caen en el responsable de sistemas, el tiempo semanal que pueda dedicarle también decide si las reglas se sostienen (sección 5).

### Alta, modificación y depuración

Quien cargó un dato es quien lo arregla, y deja el motivo escrito; los ajustes de stock físico son del responsable de sistemas.

| Dato | Alta | Modificación | Depuración |
|---|---|---|---|
| **Producto** | Lo pide Dirección y lo da de alta el responsable de sistemas, con código único, nombre, presentación y stock mínimo; hasta entonces no se puede cargar ni reservar. Empieza en cero y suma con el primer parte o con un conteo | Responsable de sistemas | Los que ya no se fabrican quedan inactivos (sin pedidos, con historial). Un duplicado deja un código activo y el otro inactivo; nunca se borra un código con movimientos |
| **Distribuidor** | Oficina (administración), antes del primer pedido y con su zona; antes de crearlo se busca, para no duplicarlo | Oficina; los duplicados, el responsable de sistemas | Igual que el producto |
| **Stock inicial y conteo semanal** | Sale del conteo físico inicial, no de la planilla ni de lo que se cree que hay (en el piloto, de un conteo de papas fritas) | Manda lo contado: el responsable de sistemas carga un ajuste con motivo (rotura, error de carga, merma u otro), sin editar el stock, y avisa a Producción si la diferencia viene de un parte. Si un producto difiere semana tras semana, se trata en la reunión diaria | – |
| **Nota de pedido y reserva** | Una sola carga, al recibir el pedido; la reserva se crea al confirmar, ni antes ni después. Si falta producto, se reserva lo que hay (se despacha solo si el distribuidor lo acepta; si no, el pedido espera completo) y el resto queda pendiente, sin reserva, con la fecha de Producción. Cómo se anota ese resto depende de lo que permita el módulo (supuesto 3) | Antes de facturar se arregla la nota y se rehace la reserva. La factura emitida no se edita: se rectifica por el procedimiento contable de administración y, si la mercadería quedó mal, por conteo. La reserva que no corresponde la libera Oficina, con el motivo | Oficina revisa cada semana las reservas abiertas, que siguen restando del disponible mientras no se facturen. La que pasó el plazo estándar de su zona (en la Patagonia, hasta una semana) se confirma con el distribuidor y se factura o se libera; lo liberado se comenta en la reunión diaria |
| **Parte de producción** | Lo carga el responsable del turno al cerrarlo, con lo realmente producido | Lo arregla el mismo día quien lo cargó, con un movimiento que resta lo mal cargado y carga lo correcto; si se descubre después, lo recoge el conteo | – |
