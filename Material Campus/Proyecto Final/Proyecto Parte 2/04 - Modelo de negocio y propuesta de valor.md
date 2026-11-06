# Modelo de negocio y propuesta de valor

Esta sección mira la propuesta desde afuera del proceso: qué cambia en el modelo de negocio que diagnosticamos en la Parte 1, qué le llega distinto al distribuidor y qué tenemos que creer para que esto funcione. Parte del canvas y del VPC de la Parte 1, y evalúa la solución recomendada, el stock de Discovery, probada antes con una planilla compartida. Para no prometer de más, **el cambio es casi todo backstage**: lo que el distribuidor ve cambia poco, y lo que cambia es la forma de cumplir lo que ya prometía. Es coherente con la Parte 1, que encontró los problemas de Dulxelitos puertas adentro.

## Cambios en el BMC

Los bloques son los del canvas AS-IS de la Parte 1. Los separamos en lo que ve el distribuidor (frontstage) y lo que pasa puertas adentro (backstage), que es como lo pide el enunciado.

### Frontstage: lo que ve el distribuidor

| Bloque | AS-IS (Parte 1, con la corrección) | TO-BE | ¿Cambia? |
|---|---|---|---|
| **Segmentos de clientes** | Distribuidores mayoristas, con foco en la Patagonia, y Aiello | Los mismos. El cambio no toca a quién se le vende | No |
| **Propuesta de valor** | Precio y logística para el canal. Lo más fuerte que tiene la empresa es que avisa cuando falta algo y no manda lo que no hay | La misma promesa, mejor cumplida: pedidos completos y a tiempo, y un aviso que llega antes | Se refuerza, no cambia |
| **Canales** | Los pedidos entran por WhatsApp y teléfono. La tienda del sitio sigue con el catálogo vacío desde 2020 | Iguales. Ver el stock desde afuera, o terminar la tienda, queda para "later" (explicación abajo) | No |
| **Relación con clientes** | El pedido se acepta sin mirar si hay mercadería. Si falta algo, el distribuidor se entera cuando se arma el pedido, y se le manda incompleto o se espera producción | Oficina confirma sabiendo qué hay y, si falta, avisa en el momento, con una fecha estimada si Producción ya la confirmó. El distribuidor sigue hablando con la misma gente por los mismos medios | **Sí, acotado** |
| **Fuentes de ingreso** | Venta mayorista, venta a Aiello y producto fraccionado. Cobran de contado, a ~30 días o con cheques diferidos | Misma estructura. Un pedido recortado o demorado es una venta parcial o tardía; cuánto vale eso es [dato pendiente: margen o valor promedio de un pedido recortado] | No |

**Por qué la tienda y el stock visible quedan para "later".** En la Parte 1 dijimos que terminar la tienda para que el distribuidor consulte stock era la iniciativa más barata. Lo seguimos creyendo, pero hoy no hay un stock que mostrar: primero hay que tener un stock en el que se pueda confiar, y recién después enseñárselo a un cliente. Por eso la visibilidad para el distribuidor queda fuera de alcance y va al roadmap como "later": la ponemos después de la mejora que la hace posible.

### Backstage: lo que pasa puertas adentro

| Bloque | AS-IS (Parte 1, con la corrección) | TO-BE | ¿Cambia? |
|---|---|---|---|
| **Actividades clave** | El dueño o los hijos deciden qué producir por criterio propio. El pedido se anota en papel o planilla y se confirma mirando a ojo y preguntando a producción. La administración está repartida entre planillas y un sistema de gestión que no se hablan | Producción carga lo producido todos los días, al cierre de turno. Oficina consulta y reserva el stock antes de confirmar. Dirección planifica la semana con los pedidos pendientes y un stock mínimo por producto. Hay una reunión diaria corta entre ventas y producción (~10 minutos) y un conteo cíclico semanal. El armado y el despacho quedan como están | **Sí, es el cambio principal** |
| **Recursos clave** | La línea de producción al límite y el conocimiento concentrado en los dueños. El stock de producto terminado no existe como recurso, porque no se registra | Aparece un recurso nuevo: el registro del stock de producto terminado, con un solo criterio de stock disponible (stock físico menos lo reservado por pedidos confirmados sin facturar) y una persona responsable de cargarlo en cada turno, con suplente. Se usa el módulo de stock de Discovery, que ya está dentro de la licencia. La planta sigue saturada | **Sí** |
| **Socios clave** | Proveedor único de packaging y film, proveedores de materia prima, transportistas, distribuidores y Aiello. El proveedor del sistema de gestión no figura | Los mismos. Con un detalle: el proveedor de Discovery pasa a contar, porque hay que activar y configurar un módulo que hoy no se usa. Insumos y packaging siguen fuera de alcance | Casi no |
| **Estructura de costos** | Materia prima, packaging, mano de obra, logística, energía y costo financiero. Las ~25 horas extras por mes están dentro de la mano de obra | Sin licencia nueva: el módulo de stock ya está en la licencia que se paga, según nuestro compañero que trabaja en la empresa, y la planilla del piloto cuesta casi nada. Costos nuevos: tiempo de carga y de reunión, el conteo inicial y la capacitación, más [dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]. Ahorro buscado: menos horas extras; llevarlo a pesos necesita [dato pendiente: costo por hora extra] | **Sí, poco** |

### Cómo se lee el conjunto

De los nueve bloques, **cuatro cambian** (actividades y recursos a fondo; relación con clientes y costos de manera acotada), **dos cambian apenas** (la propuesta de valor, que se cumple mejor, y los socios, por el proveedor de Discovery) y **tres quedan igual** (segmentos, canales e ingresos). Solo uno de los cuatro que cambian lo ve el cliente, y lo ve de una manera modesta: un aviso a tiempo.

Tres cosas conviene decir con claridad:

- **No hay un modelo de negocio nuevo.** Dulxelitos sigue siendo una empresa de volumen que le vende al canal, compite por precio y logística y depende de una planta saturada; cambia que sabe qué tiene y qué le falta antes de comprometerse.
- **La saturación de la planta no se toca.** La propuesta ataca la mezcla y el momento de producción, no la capacidad, que está fuera de alcance; hasta que el piloto lo mida, no sabemos cuánto de los recortes es una cosa y cuánto la otra.
- **Los ingresos no suben por diseño.** No prometemos vender más, solo cumplir mejor lo que ya se vende. Cuánto vale eso queda pendiente hasta tener los datos de costo y margen.

## VPC TO-BE

El segmento es el mismo de la Parte 1: el distribuidor mayorista, mirando sobre todo al patagónico. Volvemos a la tabla de dolores y de lo que el distribuidor espera de esa parte, y vemos qué hace la propuesta con cada uno y qué no hace.

**Una corrección al VPC.** La Parte 1 ubicaba los faltantes de papas fritas "en algunas temporadas", con un peso alto cuando pasan pero de corta duración. Esta parte lo corrige: los faltantes pasan todas las semanas, y en la semana que registramos 30 de ~125 pedidos, de cualquier producto, salieron recortados o demorados. Las papas fritas siguen siendo lo que más falta, pero no lo único.

### Dolores

| Dolor del distribuidor (Parte 1) | Qué hace la propuesta | Efecto |
|---|---|---|
| **Faltantes** (en la Parte 1, sobre todo de papas fritas) | Planificar la producción contra pedidos pendientes y un stock mínimo ataca la causa que suponemos, la mezcla y el momento (supuesto 1). Si falta algo, se avisa al confirmar | **Lo alivia**, y es el dolor central. Depende del supuesto crítico de más abajo |
| **No poder saber si hay stock sin llamar o ir al depósito** | El distribuidor sigue llamando o escribiendo, pero la respuesta se apoya en el stock registrado: oficina consulta el stock disponible antes de contestar | **En parte.** Mejora la respuesta, no el autoservicio, que queda para "later" |
| **Horario acotado de atención** | Nada: no se amplía el horario ni se abre un canal fuera de él | **No lo toca** |
| **Paquetes rotos en el viaje** | Nada: es un problema de embalaje y transporte, que está fuera de alcance | **No lo toca** |

### Ganancias

| Lo que el distribuidor espera (Parte 1) | Qué hace la propuesta | Efecto |
|---|---|---|
| **Que le avisen cuando falta algo** | Hoy lo hace la empresa y es su punto más fuerte, pero se entera al armar el pedido. Pasa a avisarse en el momento, con una fecha estimada | **Se mantiene y mejora**: el aviso llega antes y trae una fecha |
| **Entrega previsible** (en la Patagonia, hasta una semana) | Un pedido confirmado se cumple completo y dentro del plazo estándar de la zona. Es el indicador principal: del 76 % a la meta de la sección 1 | **Mejora**, medida por pedidos completos y a tiempo |
| **Compromiso** | Confirmar un pedido pasa a significar que hay mercadería o una fecha estimada para completarlo | **Mejora** |
| **Precio, exclusividad territorial, catálogo amplio y formatos de reventa** | Nada: no se toca ninguno | Sin cambio |

### Qué beneficio nuevo aparece

Uno solo, y es chico: **saber con una fecha estimada cuándo llega lo que falta.** Hoy el distribuidor se entera de que falta algo y no sabe hasta cuándo; con producción planificada contra pedidos, la empresa puede darle una fecha. Es una promesa nueva de cara al cliente y sobre una planta saturada: si la fecha no se cumple, el aviso pierde el valor que hoy tiene (supuesto 4). No hay ningún beneficio digital nuevo, porque no hay canal nuevo.

### Quién gana más

La Parte 1 encontró algo raro en el canal: el distribuidor está conforme y no se queja, y el que sufre es Dulxelitos. Lo mismo vale acá: el distribuidor gana un aviso más temprano y pedidos más completos, pero **el que más gana es la empresa** (menos reprogramaciones, menos horas extras para completar pedidos y un proceso que se puede medir). Un cambio que nadie pide desde afuera exige cuidado para no empeorar lo único que hoy anda bien, la relación con el canal.

## Supuestos clave

Son las cosas que damos por ciertas y no hemos probado. Las ordenamos por tipo, como pide el enunciado: **deseabilidad** (¿lo quiere y lo va a usar quien tiene que usarlo?), **factibilidad** (¿se puede hacer en esta empresa?) y **viabilidad** (¿se paga?). El primero de la lista es el que más pesa.

| # | Supuesto | Tipo | Riesgo si es falso |
|---|---|---|---|
| 1 | **La mezcla y el momento de producción, y no la capacidad total de la planta, explican la mayoría de los recortes.** | **Factibilidad (crítico)** | Planificar contra pedidos no baja los recortes porque lo que falta es capacidad. La meta no se cumple, las horas extras siguen y la propuesta ataca el problema equivocado |
| 2 | Producción carga lo producido todos los días, y oficina consulta y reserva antes de confirmar, aun con la planta saturada y sin gente de más. | Factibilidad | Sin carga diaria no hay stock en el que confiar: la exactitud cae y se vuelve a mirar a ojo. Es la resistencia que esperamos en producción y en oficina |
| 3 | El módulo de stock de Discovery funciona como esperamos: permite pedidos, reserva el stock y la facturación consume la reserva, con el mismo criterio de stock disponible que la planilla del piloto. | Factibilidad | El relevamiento indica que Discovery permite pedidos y reserva, pero nadie lo usó en Dulxelitos. Si no funciona así, hay que sumar costo y tiempo con el proveedor o seguir con la planilla compartida, que es la alternativa A |
| 4 | La fecha estimada que se le da al distribuidor cuando falta algo se cumple, con la planta saturada. | Factibilidad | Es una promesa nueva de cara al cliente. Si la fecha falla, el aviso deja de ser confiable, y ese aviso es lo más fuerte que hoy tiene la empresa: se empeora justo lo que anda bien |
| 5 | El dueño y los hijos van a decidir la producción de la semana mirando pedidos pendientes y stock mínimo, y no solo por criterio propio. | Deseabilidad | Se registra el stock pero la decisión no cambia: se digitaliza sin rediseñar y los recortes siguen. Es el cambio adaptativo del proyecto, no el técnico |
| 6 | Al distribuidor no le resulta peor oír una fecha estimada al confirmar que recibir el pedido recortado, como hoy. | Deseabilidad | Se pierden pedidos o se resiente una relación que hoy está bien. Hoy el distribuidor no se queja, así que no tenemos una señal previa de que quiera este cambio |
| 7 | Al menos la mitad de las ~25 horas extras por mes se hace para completar pedidos que faltaron por mezcla y momento de producción. | Viabilidad | Es la base de la meta de horas extras de la sección 1. La liquidación de sueldos no distingue una hora de otra. Si la mayoría de las horas es por saturación estructural de la planta, que esta propuesta no toca, la meta queda larga y el ahorro es menor |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo de implementar y sostener el cambio, que esperamos bajo y se confirma cuando estén los datos de costo. | Viabilidad | La inversión no se recupera. Hoy no hay ninguna cifra de costo, así que "bajo" es una expectativa y no un dato: el módulo ya está en la licencia y la planilla del piloto cuesta casi nada, pero falta el costo de activarlo y de la carga diaria |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa. | Viabilidad | El tamaño del problema, y de lo que se gana, es otro. Se apoya en que la demanda es pareja todo el año, pero es una sola semana |

**El supuesto 1 es el que decide si la propuesta vale la pena.** La planta está saturada, y eso lo dijo la Parte 1 y no lo corregimos. Lo que matizamos es que los recortes semanales vendrían sobre todo de otra cosa: se produce lo que no hace falta y falta lo que se pide, porque la producción se decide sin mirar los pedidos. Es la hipótesis del grupo, razonada sobre cómo funciona el proceso y no medida. Si la mayoría de los recortes se daría igual con la mezcla ideal, la meta se revisa y la propuesta no alcanza por sí sola. El piloto de 2 semanas con papas fritas está pensado, entre otras cosas, para ver cuántos recortes se evitan al planificar contra pedidos.

**Cómo se prueba el retorno, sin inventar cifras.** Todavía no tenemos el costo de la hora extra ni lo que cuesta activar el módulo, así que no hay VAN sino un punto de equilibrio (sección 2): B se paga si evita por mes al menos [dato pendiente: costo mensual de la alternativa B] sobre [dato pendiente: costo por hora extra] horas extras. Los costos que se pagan una sola vez, como el conteo inicial y la capacitación, se reparten en los 6 meses del plazo y se suman al costo mensual. El margen de los pedidos que dejan de recortarse no se cuenta (falta [dato pendiente: margen o valor promedio de un pedido recortado]), así que la prueba es conservadora. El tope de lo que se puede evitar son las ~25 horas de hoy, y la meta de la mitad vale solo si se cumple el supuesto 7. Se compara B con no hacer nada, no con A. El dueño ya dijo que acepta una inversión mayor si se demuestra el retorno.

Cómo se valida cada supuesto, con su probabilidad, su impacto y su señal temprana, se desarrolla en la sección 7.

**Fuentes:** canvas AS-IS y VPC de la Parte 1; relevamiento del proceso; secciones 1 y 2 de esta parte.
