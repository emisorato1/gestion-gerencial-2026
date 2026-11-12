# Problema gerencial, objetivos y alcance

A partir del diagnóstico de la Parte 1 definimos el problema gerencial priorizado. Lo presentamos acá con los objetivos y el alcance, sobre la base de un relevamiento más detallado del proceso de atender un pedido de distribuidor.

## Lo que encontramos en el relevamiento

Del relevamiento surgieron tres cosas que definen el problema.

La facturación está en Discovery, pero el stock de producto terminado no se lleva ahí ni en ningún otro registro. Para saber si hay mercadería se mira en el depósito y se le pregunta a Producción, que mantiene su propio control, lo carga una vez por semana y no lo relaciona con las ventas. El módulo de stock de Discovery está incluido en la licencia y no se usa.

Los pedidos recortados ocurren todas las semanas. En la semana que registramos, 30 de unos 125 pedidos salieron recortados o demorados, cerca del 24 %, de modo que los completos y a tiempo fueron cerca del 76 %. Es el resultado de una sola semana. Esa semana se contaron los pedidos recortados o demorados; si se incluyeron también los rechazados de entrada, lo vamos a confirmar con la empresa.

La planta sigue saturada y las horas extras compensan esa carga al menos en parte. Pero los recortes de cada semana vendrían sobre todo de la mezcla y el momento de producción más que de la capacidad total (supuesto 1): el dueño o los hijos deciden qué producir por criterio propio, sin mirar los pedidos pendientes. Es un supuesto crítico y el piloto nos va a dar una primera lectura.

## Problema gerencial

> Dulxelitos recorta o demora 30 de unos 125 pedidos semanales porque los acepta sin conocer el stock de producto terminado, que no se registra, y produce sin mirar las ventas. Genera faltantes y parte de las horas extras (unas 25 mensuales) sobre una planta saturada. Éxito: pedidos completos y a tiempo del 76 % al 90 % en 6 meses.

La causa raíz es en parte técnica, porque no hay registro del stock de producto terminado, y en parte de organización: los pedidos se aceptan y la producción se decide sin mirarse entre sí. Entendemos "a tiempo" como dentro del plazo estándar de cada zona, que en la Patagonia es de hasta una semana, y un pedido rechazado o reprogramado de entrada para mejorar el número no cuenta como completo.

La meta del 90 % la fijamos nosotros: en una pyme con la planta al límite siempre va a haber roturas e imprevistos. Si el piloto muestra que la planificación de la producción explica menos de lo que suponemos, la revisamos.

## Objetivo general

Que cada pedido de distribuidor se confirme sabiendo qué hay en stock de producto terminado, y que la producción se planifique contra los pedidos pendientes, para llevar los pedidos completos y a tiempo del 76 % al 90 % en un plazo de 6 meses.

Abarca el proceso "Atender pedido de distribuidor", de la recepción al despacho, y la planificación semanal de producción. Puede comenzar en cualquier momento del año, porque la demanda se mantiene estable.

## Objetivos específicos

Son tres, cada uno con una métrica que la empresa puede obtener, una línea de base y una meta con plazo.

### 1. Que los pedidos se confirmen sabiendo qué hay en stock

- Métrica: pedidos completos y a tiempo sobre pedidos recibidos, por semana.
- Línea de base: 76 % (30 recortados o demorados de unos 125, en una semana de registro).
- Meta: 90 % en 6 meses.

### 2. Que la producción se cargue todos los días

- Métrica: días hábiles con producción cargada sobre días hábiles.
- Línea de base: 20 %, porque hoy se carga una vez por semana.
- Meta: 100 % de los días hábiles dentro de los 6 meses. La primera prueba es un piloto de 2 semanas con papas fritas (línea Salados), el producto con más faltantes.

### 3. Que bajen las horas extras

- Métrica: horas extras totales por mes, de la liquidación de sueldos.
- Línea de base: unas 25 horas por mes.
- Meta: la mitad, unas 12 o 13 horas por mes, en 6 meses. Depende de que al menos la mitad de esas horas se haga para completar pedidos que faltaron por la mezcla y el momento de producción; lo que responde a la falta de capacidad no baja. La liquidación no distingue una causa de la otra, así que si la meta queda corta o larga se va a ver con los primeros meses de medición.
- Costo: para llevarlo a pesos falta el costo de la hora extra, que vamos a pedir a liquidación de sueldos.

Hay además otro indicador, la exactitud de stock, que funciona como condición de los otros tres: si lo cargado no coincide con el conteo físico semanal, ninguno se sostiene. Su línea de base sale del primer conteo físico, y la meta provisional es que al menos 9 de cada 10 productos queden sin diferencia mayor a la tolerancia de la sección 7 en 6 meses. Las fichas de los cuatro indicadores están en la sección 8.

## Alcance

El proceso es "Atender pedido de distribuidor": empieza cuando llega el pedido por WhatsApp o teléfono y termina con el pedido facturado en Discovery y despachado. Incluye la planificación semanal de producción contra pedidos y los indicadores, con su rutina de seguimiento.

Participan Oficina, Depósito, Producción y Dirección (el dueño y los hijos). El dueño es el sponsor y aprueba el presupuesto y los Go/No-Go. El líder es el responsable de sistemas: el diagnóstico de la Parte 1 marcó la gobernanza digital como una debilidad y la propuesta se la asigna a él. Los distribuidores y el transporte tercerizado no cambian su trabajo: siguen pidiendo por WhatsApp o teléfono y, si falta algo, se les avisa en el momento, con fecha estimada si Producción ya la confirmó.

En el trabajo diario, Producción carga lo producido todos los días, al cierre de cada turno, aunque falta relevar cuántos turnos tiene la planta. Oficina consulta el stock y lo reserva antes de confirmar un pedido. Dirección planifica la producción de la semana mirando los pedidos pendientes y un stock mínimo por producto. Se suman una reunión diaria corta entre ventas y producción, de unos 10 minutos, y un conteo cíclico semanal.

Hacen falta disciplina de carga diaria, un responsable de carga por turno con suplente y un criterio único de stock disponible. Los datos son el stock físico de producto terminado, las reservas por pedido confirmado sin facturar, los pedidos pendientes, el stock mínimo y las horas extras, con una sola definición: **stock disponible = stock físico menos lo reservado por pedidos confirmados sin facturar.** Las herramientas son Discovery, que la empresa ya tiene, para facturar y para el módulo de stock, pedidos y reserva que hoy no se usa, y una planilla compartida para el piloto de 2 semanas; cuál va como solución y cuál como prueba se justifica en la sección 2.

## Fuera de alcance

- Insumos y packaging: también tienen problemas, que exceden este proyecto. Quedan declarados como deuda, y el proveedor único de film ya figura como riesgo en la Parte 1.
- Visibilidad de stock para el distribuidor: por ahora el stock es solo interno. Queda en el roadmap para más adelante, junto con la tienda online de 2020.
- Ampliación de planta: la capacidad total no cambia, y el proyecto apunta a qué se produce y cuándo.
- Cambiar Discovery por otro sistema: evaluamos un SaaS de gestión y lo descartamos en la sección 2.
- CRM: es un problema real identificado en la Parte 1 (Clientes y Canales) que se deja para una etapa posterior.
- Costeo y listas de precios: tampoco se tocan.

Algunas tareas se mantienen manuales a propósito: el armado del pedido en el depósito, que según el relevamiento es rápido y no se mide, así que no es la restricción; el conteo físico; y la decisión de qué producir, que sigue siendo del dueño y de los hijos aunque ahora la toman mirando pedidos y stock.
