# Validación de supuestos

Antes de invertir en el módulo de stock de Discovery hacemos dos pruebas de bajo costo: un piloto de 2 semanas con papas fritas en una planilla compartida y una prueba técnica del módulo sobre un solo producto. Lo primero que queremos saber es si los recortes vienen de la mezcla y el momento de producción (supuesto 1), que por ahora es una hipótesis razonada.

## Supuestos críticos

Son los nueve supuestos de la sección 4. La probabilidad de que resulte falso y el impacto que tendría sobre la propuesta se califican en alta, media o baja. La etapa es la principal de las cuatro de validación de Rogers: problema, solución, producto y negocio.

| # | Supuesto | Tipo y etapa | Prob. de ser falso | Impacto si es falso | Qué se anota y señal temprana |
|---|---|---|---|---|---|
| 1 | La mezcla y el momento de producción, y no la capacidad, explican la mayoría de los recortes | Factibilidad (crítico) · Problema | Media | Alto | La causa de cada recorte de papas fritas en la semana 0; alerta si es sobre todo capacidad |
| 2 | Producción carga todos los días y Oficina reserva antes de confirmar, aun con la planta saturada | Factibilidad · Producto | Alta | Alto | Días con carga y días en que la planilla falló; alerta si hay días sin carga o la planilla no coincide con la planta |
| 3 | Discovery permite pedidos y reserva (también parcial) y la factura consume la reserva | Factibilidad · Producto | Media | Medio | Un producto probado de punta a punta; alerta si el proveedor no lo confirma por escrito o falla un paso |
| 4 | La fecha estimada que se da al distribuidor se cumple, con la planta saturada | Factibilidad · Producto | Media | Alto | Cada aviso con su fecha y si se cumplió; alerta si Producción no la confirma o se pasa |
| 5 | Dueño e hijos deciden qué producir mirando pedidos pendientes y stock mínimo | Deseabilidad · Solución | Media | Alto | El stock mínimo que fijan; alerta si la reunión diaria no cambia lo que se produce |
| 6 | Al distribuidor no le resulta peor una fecha estimada que recibir el pedido recortado | Deseabilidad · Solución | Baja | Medio | Su reacción a cada aviso; alerta si cancela, reprograma o reclama |
| 7 | Al menos la mitad de las ~25 horas extras por mes es por pedidos que faltaron por lo que se produjo y cuándo | Viabilidad · Negocio | Media | Medio | El motivo de cada hora extra; alerta si es sobre todo falta de capacidad y no bajan aunque los recortes sí |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo del cambio | Viabilidad · Negocio | Media | Alto | El punto de equilibrio de la sección 2, con el tiempo de carga, reserva y reunión; alerta si pide evitar más de las ~25 horas de hoy |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa | Viabilidad · Problema | Media | Medio | El registro semanal de todos los productos, con el mismo criterio; alerta si el total del piloto se aleja del registrado |

El piloto responde el supuesto 2 y da una primera lectura de los supuestos 1, 4, 5 y 6. El 3 lo resuelve la prueba técnica; el 7, el 8 y el 9 se miden más adelante, con los meses de operación, y el 8 depende además de los costos reales de la alternativa B y de la hora extra. Entre todos, los que más atención piden son los de impacto alto y probabilidad media o alta: el 1, el 2, el 4, el 5 y el 8.

## Piloto

El piloto es nuestro MVP, el experimento mínimo para validar una hipótesis: creemos que una planilla compartida con el stock de papas fritas, la carga diaria, la reserva por pedido confirmado y una reunión diaria de unos 10 minutos va a reducir los recortes y demoras de ese producto, y lo sabremos si se cumplen los cuatro umbrales de "Qué se mide". Es funcional, con la rutina en uso real pero en pequeño, y sigue el espíritu del pretotipo de Savoia, que busca comprobar que la idea funciona antes de invertir en construirla. La prueba técnica de Discovery hace de prototipo, en paralelo.

### Cómo se corre

- Cuándo y qué. Una semana 0 para medir la línea de base y después 2 semanas (10 días hábiles) solo con papas fritas, el producto con más faltantes según el relevamiento. Puede comenzar cuando se acuerde, con el conteo inicial hecho el fin de semana anterior.
- La rutina. Con la regla de stock disponible de la sección 3, Producción carga al cierre de turno, con un responsable y un suplente. Oficina consulta y reserva antes de confirmar un pedido con papas fritas y, si no alcanza, avisa con una fecha que Producción confirmó. Al facturar se baja el stock físico y se descuenta la reserva a mano, porque la planilla no se conecta con Discovery. Hay un conteo físico al comenzar y otro por semana, y una reunión diaria de unos 10 minutos entre ventas y producción para decidir qué producir.
- Vuelta atrás. Si un día la planilla no está al día, Oficina confirma como hoy, consultando a Producción, y se anota el día. El piloto puede cortarse en cualquier momento, porque no toca Discovery ni el armado de pedidos.
- Quién. El dueño, como sponsor, acuerda los umbrales y respalda el inicio; el responsable de sistemas, como líder, arma la planilla y junta las medidas. Los conteos físicos los hace el responsable del conteo.

### Qué se mide

Cuenta como recortado o demorado, con el mismo criterio en la semana 0 y en el piloto, un pedido con papas fritas que sale con menos cantidad de la pedida o después del plazo estándar de su zona. También cuentan el rechazado o reprogramado de entrada y el cancelado tras el aviso, porque, si no, el número mejoraría rechazando o postergando pedidos.

| Medida | Línea de base | Umbral para un Go | Por qué ese umbral |
|---|---|---|---|
| Días con producción de papas fritas cargada al cierre de turno, sobre 10 días hábiles | 20 % de los días: hoy se carga 1 vez por semana. En la semana 0 vemos si el control de producción separa por producto | 8 de los 10 días o más | La meta de la sección 1 es todos los días; dejamos 2 días de margen |
| Pedidos de papas fritas recortados o demorados, promedio semanal de las 2 semanas | Se mide en la semana 0; los 30 de ~125 son de todos los productos y no sirven de base | La mitad o menos que en la semana 0, sin que suban los rechazados, reprogramados de entrada o cancelados tras el aviso | La meta de la sección 1, del 76 % al 90 %, deja 1 recortado de cada 10, menos de la mitad del ~24 % de hoy; pedimos la mitad por ser un producto y 2 semanas |
| Diferencias entre el conteo físico y la planilla, al comenzar y cada semana | Sale del primer conteo | Hasta una décima parte de lo contado en los conteos semanales | La meta de exactitud de la sección 8, al menos 9 de cada 10 productos dentro de la tolerancia, y la tolerancia son provisionales; se ajustan con el primer conteo |
| Fecha estimada cumplida, por aviso | No existe hoy: el aviso no trae fecha | 4 de cada 5 avisos o más; si hubo pocos, se revisan uno por uno | Es una promesa nueva y si falla más de 1 vez de cada 5 pierde valor; no pedimos todas porque la planta tiene poco margen |

Como control se compara con los demás productos en las mismas semanas, porque si los recortes bajan en todos por igual la mejora no es del piloto. Si la semana 0 casi no tiene recortes de papas fritas, se mide otra semana.

### Prueba técnica de Discovery

Verifica el supuesto 3: según el relevamiento, Discovery permite pedidos y reserva, pero nunca se usó en Dulxelitos. La lleva el responsable de sistemas con Buenos Aires Software, en paralelo con la semana 0, y su resultado entra al Go/No-Go junto con el del piloto. Se prueba un solo producto, el mismo del piloto, en cinco pasos:

| Paso | Qué se verifica | Resultado esperado |
|---|---|---|
| 1. Ingreso de stock | Cargar el stock inicial | Queda registrado el stock físico |
| 2. Pedido y reserva | Cargar un pedido y reservar; con otro mayor al stock, reservar solo lo que hay y dejar el resto pendiente | La reserva aparece contra el pedido; el proveedor confirma cómo se anota el resto |
| 3. Disponible | Consultar cuánto hay | Stock físico menos lo reservado, como en la planilla |
| 4. Factura | Facturar el pedido | Baja el stock físico y consume la reserva |
| 5. Anulación o cambio | Anular o modificar el pedido | La reserva se libera |

A Buenos Aires Software le vamos a consultar por escrito la versión de Discovery y el soporte, cuánto cuesta y cuánto tarda activar el módulo, y si hay ambiente de prueba, porque en el paso 4 una factura de prueba en el sistema real puede quedar como verdadera. La prueba pasa si funcionan los pasos que se pueden probar; sin ambiente de prueba, el paso 4 queda para el primer pedido real de la activación y no bloquea el Go. Si algo falla, se pregunta si se puede configurar y cuánto cuesta, y, si no, se sigue con la alternativa A.

## Criterio de decisión

Las reglas se acuerdan con el dueño antes de comenzar. El Go/No-Go lo decide él. Si el criterio se fijara después de ver el resultado, sería fácil leerlo a favor. Como la empresa no tiene datos previos para fijar los umbrales, se ajustan con el dueño y con la semana 0.

| Qué pasó | Decisión |
|---|---|
| Se cumplen los cuatro umbrales y la prueba técnica pasa, con el paso 4 pendiente si no hay ambiente de prueba | Go. Activar Discovery por línea de producto, con la misma rutina, si con los costos reales se alcanza el punto de equilibrio de la sección 2 |
| Se cumplen la carga y los recortes, pero fallan el conteo o la fecha | Go con ajustes. Ajustar capacitación, responsable o regla de fecha y repetir una sola vez |
| La carga no llega a 8 de los 10 días | No-Go. No se invierte en B; se revisa por qué no se carga (sección 5) |
| La carga funciona, los recortes no bajan a la mitad y las causas son sobre todo de capacidad | Cae el supuesto 1. No-Go de B para este problema; se revisa la meta de la sección 1, porque queda un problema de planta, fuera de alcance. Con pocos recortes para concluir, se repite una sola vez |
| La carga funciona, los recortes no bajan y las causas son sobre todo qué se produce y cuándo | Algo falla en cómo se usa el dato (supuesto 5). No se concluye. Se revisa si la producción cambió con lo que se vio en la reunión y se repite una sola vez |
| La prueba técnica falla y el proveedor no lo resuelve | Cae el supuesto 3. Se sigue con A, la planilla, con sus controles, antes que pasar a C (sección 2) |

Repetir una sola vez significa otra vuelta de 2 semanas con el mismo producto; si en la segunda tampoco se cumple, la decisión es No-Go.

### Qué valida el piloto y qué queda para después de activar

Con dos semanas y un producto, el piloto da una señal temprana, sobre todo en la etapa de producto: muestra si la carga diaria se sostiene y cuál es la causa de los recortes de papas fritas. Lo que necesita más productos y meses de operación se mide en los Go/No-Go de la sección 8: el efecto en todo el catálogo, las horas extras, el retorno con los costos reales y que la carga y la exactitud se mantengan en el tiempo.
