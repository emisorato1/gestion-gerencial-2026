# Validación de supuestos

Antes de invertir en el módulo de stock hacemos dos pruebas baratas: un piloto de 2 semanas con papas fritas sobre una planilla compartida y una prueba técnica del módulo con ese mismo producto. Lo primero que queremos saber es si los recortes vienen de la mezcla y el momento de producción (supuesto 1).

## Supuestos críticos

Calificamos los nueve supuestos de la sección 4 según su tipo de riesgo, la probabilidad de que sean falsos y el impacto que tendría.

| # | Supuesto (resumido) | Tipo | Prob. de ser falso | Impacto | Señal temprana | Cómo se valida |
|---|---|---|---|---|---|---|
| 1 | Los recortes vienen de la mezcla y el momento, más que de la capacidad | Factibilidad | Media | Alto | Causas anotadas que son sobre todo de capacidad | Piloto |
| 2 | Producción carga todos los días y Oficina reserva | Factibilidad | Alta | Alto | Días sin carga | Piloto |
| 3 | Discovery reserva y la factura consume la reserva | Factibilidad | Media | Medio | Un paso que falla | Prueba técnica |
| 4 | La fecha estimada se cumple | Factibilidad | Media | Alto | Fechas que se pasan | Piloto |
| 5 | La dirección planifica mirando pedidos | Deseabilidad | Media | Alto | Una reunión diaria que no cambia lo que se produce | Piloto |
| 6 | Al distribuidor no le molesta la fecha estimada | Deseabilidad | Baja | Medio | Cancelaciones o reclamos | Piloto |
| 7 | La mitad de las horas extras es por pedidos que faltaron | Viabilidad | Media | Medio | Horas que no bajan aunque bajen los recortes | Operación |
| 8 | El ahorro justifica el costo | Viabilidad | Media | Alto | Un punto de equilibrio por encima de las horas actuales | Operación |
| 9 | La semana registrada es representativa | Viabilidad | Media | Medio | Un registro que se aleja mucho de esa semana | Operación |

El piloto confirma o no el supuesto 2 y da una primera lectura del 1, el 4, el 5 y el 6. El 3 lo resuelve la prueba técnica, y el 7, el 8 y el 9 necesitan más productos y meses de operación. Los que más atención piden son los de impacto alto y probabilidad media o alta. En términos de las etapas de validación de Rogers (problema, solución, producto y negocio), el piloto cubre sobre todo la de producto.

## Piloto

El piloto es nuestro MVP: creemos que una planilla con el stock de papas fritas, la carga diaria, la reserva por pedido y una reunión diaria corta van a reducir los recortes de ese producto, y lo vamos a saber con los umbrales de la tabla de abajo. Siguiendo la idea del pretotipo de Savoia, buscamos comprobar que la idea funciona antes de invertir en construirla.

Primero hay una semana 0 para medir la línea de base y después 2 semanas (10 días hábiles) solo con papas fritas, el producto con más faltantes, con un conteo inicial el fin de semana anterior. Producción carga al cierre de cada turno, y Oficina consulta y reserva antes de confirmar y, si no alcanza, avisa con la fecha que da Producción. Si un día la planilla no está al día, Oficina confirma como siempre y se anota. Como no toca Discovery, el piloto se puede cortar en cualquier momento. El dueño acuerda los umbrales y respalda el inicio, y el responsable de sistemas arma la planilla y junta las medidas.

Cuenta como recortado o demorado el pedido que sale con menos de lo pedido o fuera del plazo de su zona, y también el que se rechaza, se reprograma o se cancela tras el aviso, para que el número no mejore rechazando pedidos.

| Medida | Línea de base | Umbral para un Go |
|---|---|---|
| Días con producción cargada | 20 % (una vez por semana) | 8 de los 10 días o más |
| Pedidos de papas fritas recortados o demorados | Se mide en la semana 0 | La mitad o menos, sin que suban los rechazados |
| Diferencias entre conteo y planilla | Sale del primer conteo | Hasta una décima parte de lo contado |
| Fechas estimadas cumplidas | Hoy el aviso no trae fecha | 4 de cada 5 o más |

Los umbrales piden menos que la meta de la sección 1 porque se trata de un solo producto y dos semanas. Como control, comparamos los recortes con los de los demás productos: si bajan en todos por igual, la mejora no es del piloto.

### Prueba técnica de Discovery

En paralelo con la semana 0, el responsable de sistemas prueba con Buenos Aires Software, sobre el mismo producto, que el módulo haga lo que necesitamos: cargar el stock inicial, cargar un pedido y reservarlo (también en parte, si no alcanza), consultar el disponible, facturar y ver que la reserva se consume, y anular un pedido para que la reserva se libere. Al proveedor le vamos a consultar por escrito la versión, el soporte, el costo y el plazo de activación, y si hay ambiente de prueba. Si no lo hay, la parte de la factura queda para el primer pedido real y no frena la decisión.

## Criterio de decisión

Las reglas se acuerdan con el dueño antes de empezar, porque fijarlas después de ver el resultado haría fácil leerlo a favor. El Go/No-Go lo decide él.

| Qué pasó | Decisión |
|---|---|
| Se cumplen los umbrales y la prueba técnica pasa | Go: activar Discovery por línea, si con los costos reales se alcanza el punto de equilibrio |
| Se cumplen la carga y los recortes, pero fallan el conteo o la fecha | Go con ajustes: se ajusta lo que falló y se repite una vez |
| La carga no llega a 8 de 10 días | No-Go: no se invierte en B y se revisa por qué no se carga |
| La carga funciona pero los recortes no bajan, por falta de capacidad | Cae el supuesto 1: B no resuelve este problema y se revisa la meta |
| La carga funciona pero los recortes no bajan y la producción no cambió | Falla el uso del dato (supuesto 5): se revisa la reunión diaria y se repite una vez |
| La prueba técnica falla y el proveedor no lo resuelve | Cae el supuesto 3: se sigue con la planilla |

Repetir significa otras 2 semanas con el mismo producto; si tampoco se cumple, la decisión es No-Go.
