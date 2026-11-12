# Modelo de negocio y propuesta de valor

La solución recomendada es activar el módulo de stock de Discovery (alternativa B), que antes se prueba con una planilla compartida (alternativa A). Casi todo el cambio es interno: la promesa al distribuidor es la misma y lo que se modifica es la manera de cumplirla.

## Cambios en el BMC

Partimos del canvas de la Parte 1, con lo que encontramos al relevar el proceso con más detalle, y separamos el frontstage (lo que ve el distribuidor) del backstage.

### Frontstage

| Bloque | AS-IS | TO-BE | ¿Cambia? |
|---|---|---|---|
| Segmentos de clientes | Distribuidores mayoristas, con foco en la Patagonia, y Aiello | Los mismos | No |
| Propuesta de valor | Precio y logística para el canal. Lo más importante es que la empresa avisa cuando falta algo y no manda lo que no hay | La misma promesa, mejor cumplida: pedidos completos y a tiempo, y un aviso que llega antes | Se refuerza |
| Canales | Pedidos por WhatsApp y teléfono. La tienda del sitio sigue con el catálogo vacío desde 2020 | Iguales; mostrar el stock al distribuidor o terminar la tienda queda para más adelante, porque hoy no hay un stock confiable que mostrar | No |
| Relación con clientes | Se acepta el pedido sin mirar si hay mercadería; si falta, el distribuidor lo sabe al armarlo y recibe un envío incompleto o espera producción | Oficina confirma sabiendo qué hay y, si falta, avisa en el momento, con una fecha estimada si Producción ya la confirmó | Sí, acotado |
| Fuentes de ingreso | Venta mayorista, venta a Aiello y producto fraccionado. Cobran de contado, a ~30 días o con cheques diferidos | Misma estructura. Un pedido recortado es una venta parcial o tardía; cuánto margen se pierde por cada uno queda por calcular | No |

### Backstage

| Bloque | AS-IS | TO-BE | ¿Cambia? |
|---|---|---|---|
| Actividades clave | El dueño o los hijos deciden qué producir por criterio propio. El pedido se confirma mirando el depósito y preguntando a Producción. La administración se reparte entre planillas y un sistema de gestión desconectados | Producción carga lo producido todos los días, al cierre de turno. Oficina consulta y reserva el stock antes de confirmar. Dirección planifica la semana con los pedidos pendientes y un stock mínimo por producto. Reunión diaria de ~10 minutos entre ventas y producción y conteo cíclico semanal | Sí, el principal |
| Recursos clave | La línea de producción al límite y el conocimiento concentrado en los dueños. El stock de producto terminado no existe como recurso porque no se registra | Un recurso nuevo: el registro de stock de producto terminado, con un solo criterio de stock disponible (sección 3), cargado en el módulo de Discovery por una persona en cada turno, con suplente | Sí |
| Socios clave | Proveedor único de packaging y film, proveedores de materia prima, transportistas, distribuidores y Aiello | Los mismos; el proveedor de Discovery pasa a contar, porque hay que activar un módulo que hoy no se usa | Casi no |
| Estructura de costos | Materia prima, packaging, mano de obra, logística, energía y costo financiero. Las ~25 horas extras por mes están dentro de la mano de obra | Sin licencia nueva: según el relevamiento, el módulo ya está incluido en la licencia. Se suman tiempo de carga y de reunión, conteo inicial y capacitación. El ahorro está en las horas extras, valoradas al costo de la hora | Sí, poco |

De los nueve bloques, cuatro cambian: actividades y recursos a fondo, y relación con clientes y costos de forma acotada. Dos cambian apenas, propuesta de valor y socios, y tres quedan igual: segmentos, canales e ingresos. No hay un modelo de negocio nuevo: la capacidad de la planta no se toca, porque la propuesta se ocupa de qué se produce y cuándo. Los ingresos tampoco cambian, y por eso no los usamos para calcular el retorno.

## VPC TO-BE

El segmento es el mismo de la Parte 1: el distribuidor mayorista, sobre todo el patagónico. El relevamiento muestra que los faltantes de papas fritas se repiten todas las semanas y que, en la semana registrada, 30 de unos 125 pedidos, de cualquier producto, salieron recortados o demorados. Las papas fritas son el producto con más faltantes.

### Dolores

| Dolor del distribuidor (Parte 1) | Qué hace la propuesta | Efecto |
|---|---|---|
| Faltantes | Planificar contra pedidos pendientes y un stock mínimo ataca la causa más probable, qué se produce y cuándo (supuesto 1). Si falta algo, se avisa al confirmar | Lo alivia; es el dolor central |
| No poder saber si hay stock sin llamar o ir al depósito | El distribuidor sigue llamando, pero Oficina responde con el stock disponible registrado | En parte: mejora la respuesta, aunque no hay autoservicio |
| Horario acotado de atención y paquetes rotos en el viaje | Nada: quedan fuera de alcance | No los toca |

### Ganancias

| Lo que el distribuidor espera (Parte 1) | Qué hace la propuesta | Efecto |
|---|---|---|
| Que le avisen cuando falta algo | Hoy lo hace la empresa, pero recién al armar el pedido. Pasa a avisarse en el momento, con fecha estimada | Se mantiene y mejora |
| Entrega previsible (en la Patagonia, hasta una semana) y compromiso | Confirmar un pedido pasa a significar que hay mercadería o una fecha para completarlo, y que se cumple completo y dentro del plazo estándar de la zona. Es el indicador principal: del 76 % a la meta de la sección 1 | Mejora |
| Precio, exclusividad territorial, catálogo amplio y formatos de reventa | Ninguna acción | Sin cambio |

### Qué beneficio nuevo aparece

Uno solo, menor: saber con una fecha estimada cuándo llega lo que falta. Hoy el distribuidor se entera de que falta algo pero no hasta cuándo; con la producción planificada contra los pedidos, la empresa puede darle una fecha. Es una promesa nueva sobre una planta saturada y, si no se cumple, el aviso pierde el valor que hoy tiene (supuesto 4). No hay beneficio digital nuevo porque no hay canal nuevo. Como hoy la relación con los distribuidores es buena, el cambio beneficia sobre todo a la empresa.

## Supuestos clave

Son cosas que damos por ciertas sin haberlas probado, agrupadas en deseabilidad (si lo van a querer y usar), factibilidad (si se puede hacer en esta empresa) y viabilidad (si se paga).

| # | Supuesto | Tipo | Riesgo si es falso |
|---|---|---|---|
| 1 | La mezcla y el momento de producción, y no la capacidad total de la planta, explican la mayoría de los recortes. | Factibilidad (crítico) | Planificar contra pedidos no baja los recortes porque lo que falta es capacidad |
| 2 | Producción carga lo producido todos los días y Oficina consulta y reserva antes de confirmar, aun con la planta saturada y sin gente de más. | Factibilidad | Sin carga diaria no hay stock confiable y se vuelve a mirar el depósito. Es la resistencia que esperamos |
| 3 | El módulo de stock de Discovery permite pedidos, reserva stock y la factura consume la reserva, con el mismo criterio de stock disponible que la planilla del piloto. | Factibilidad | Nadie lo usó en la empresa. Si no funciona así, hay que sumar costo y tiempo con el proveedor o seguir con la planilla (alternativa A) |
| 4 | La fecha estimada que se le da al distribuidor cuando falta algo se cumple, con la planta al límite de su capacidad. | Factibilidad | El aviso deja de ser confiable y se empeora lo que hoy funciona bien |
| 5 | El dueño y los hijos deciden la producción de la semana mirando pedidos pendientes y stock mínimo, además de su criterio. | Deseabilidad | Se registra el stock pero se decide igual que antes y los recortes siguen. Es el cambio adaptativo del proyecto |
| 6 | Al distribuidor no le molesta más oír una fecha estimada al confirmar que recibir el pedido recortado, como hoy. | Deseabilidad | Se pierden pedidos o se resiente una relación que hoy está bien; no hay señal previa de que quiera este cambio |
| 7 | Al menos la mitad de las ~25 horas extras por mes se hace para completar pedidos que faltaron por mezcla y momento de producción. | Viabilidad | Es la base de la meta de horas extras de la sección 1. Si la mayoría responde a la capacidad limitada de la planta, la meta queda larga y el ahorro es menor |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo de implementar y sostener el cambio, que esperamos bajo. | Viabilidad | La inversión no se recupera |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa. | Viabilidad | El tamaño del problema es otro. Se apoya en que la demanda se mantiene estable durante el año, pero hay una sola semana de registro |

El supuesto 1 decide si la propuesta vale la pena. La planta está saturada y eso no cambia; creemos que los recortes vienen sobre todo de producir sin mirar los pedidos, y el piloto va a dar una primera lectura. Si el problema persistiera con la producción bien planificada, habría que revisar la meta.

En lugar de un VAN usamos el punto de equilibrio de la sección 2: B se paga si las horas extras que evita por mes, al costo de la hora, cubren su costo mensual. El tope es de unas 25 horas por mes, las de hoy, y que se llegue a la mitad depende del supuesto 7. El dueño estaría dispuesto a una inversión mayor si el retorno se demuestra. La validación de cada supuesto está en la sección 7.
