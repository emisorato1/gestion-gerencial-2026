# Proceso actual y alternativas de solución

Describimos el proceso como funciona hoy, con los volúmenes que relevamos en la empresa.

## Matriz de descubrimiento

| Campo | Contenido |
|---|---|
| **Proceso** | Atender pedido de distribuidor |
| **Inicio y fin** | Llega un pedido por WhatsApp o teléfono; termina facturado en Discovery y despachado |
| **Áreas** | Oficina, Depósito, Producción y Dirección (el dueño y los hijos) |
| **Externos** | El distribuidor y, si no hay flota propia, el transporte tercerizado |
| **Volumen** | ~25 pedidos por día, ~125 por semana, con una demanda estable en el año |
| **Camino alternativo frecuente** | Falta producto: 30 de ~125 pedidos recortados o demorados en la semana registrada |
| **Fuera de los límites** | Insumos y packaging, y la visibilidad de stock para el distribuidor |

## SIPOC

| Proveedor | Entrada | Proceso | Salida | Cliente |
|---|---|---|---|---|
| Distribuidor | Pedido por WhatsApp o teléfono | Recibir pedido | Pedido anotado | Oficina |
| Depósito y Producción | Pedido anotado, lo que se ve en el depósito y lo que dice Producción | Verificar disponibilidad | Pedido pasado a la lista | Depósito |
| Oficina y Producción | Lista de pedidos y producto terminado | Preparar pedido | Pedido armado, completo o con faltante | Oficina |
| Depósito y Producción | Faltante detectado al armar | Resolver faltante (si falta) | Aviso al distribuidor o producción extra | Distribuidor y Oficina |
| Depósito | Pedido armado | Facturar | Pedido facturado en Discovery | Distribuidor y Depósito |
| Oficina | Pedido facturado | Despachar | Pedido despachado | Distribuidor y transporte |

## RECI

R es el responsable (uno por actividad), E el ejecutor, C el consultado e I el informado. En una pyme quien ejecuta suele ser quien responde, por eso casi todo es R/E.

| Actividad | Oficina | Depósito | Producción | Dirección | Distribuidor (externo) | Transporte tercerizado (externo) |
|---|---|---|---|---|---|---|
| Anotar pedido | R/E | – | – | – | – | – |
| Preguntar disponibilidad a producción | R/E | – | C | – | – | – |
| Mirar el stock a ojo | I | R/E | – | – | – | – |
| Pasar pedido a la lista | R/E | I | – | – | – | – |
| Preparar pedido | I | R/E | – | – | – | – |
| Avisar faltante al distribuidor | R/E | C | – | – | I | – |
| Producir lo que falta, con o sin horas extras | I | I | R/E | C | – | – |
| Facturar en Discovery | R/E | C | – | – | I | – |
| Despachar (flota propia o tercerizado) | I | R/E | – | – | I | I |
| Decidir producción | – | – | I | R/E | – | – |
| Producir y registrar la producción de la semana | – | – | R/E | I | – | – |

Se ven dos huecos. "Decidir producción" no tiene consultados, aunque Oficina es la que conoce los pedidos. Y el faltante no tiene un responsable claro: quién elige entre mandar incompleto, esperar o hacer horas extras es algo que hay que definir con el dueño.

## Diagrama AS-IS

![Proceso AS-IS](bpmn/as-is.png)

El pedido nace en el mensaje del distribuidor. Oficina lo anota y le pregunta a Producción mientras Depósito mira el stock; con eso pasa el pedido a la lista y Depósito lo prepara. Recién al preparar se sabe si falta algo, y en ese caso el pedido sale incompleto, espera producción o se completa con horas extras. Por otro lado, el dueño o uno de los hijos decide cada semana qué producir sin mirar los pedidos, y Producción registra lo producido una vez por semana. Buena parte del proceso depende de la memoria de las personas. El diagrama completo se adjunta en formato BPMN.

| Aspecto | Hoy |
|---|---|
| Herramientas | WhatsApp, teléfono, papel o planilla, una lista de pedidos, Discovery solo para facturar y el control semanal de Producción |
| Dependencias informales | El pedido vive en el chat o la llamada, la disponibilidad se averigua de palabra y las horas extras se autorizan de forma verbal |
| Dolores y costos | Recortes y demoras todas las semanas, faltantes que aparecen al armar y ~25 horas extras por mes, en parte para completar pedidos |
| Indicadores | Pedidos completos y a tiempo: 76 %. Días con producción cargada: 20 %. Exactitud de stock: no se puede medir, porque no hay stock registrado |

El armado del pedido, en cambio, es rápido y no es el problema.

## Tres lentes

Miramos el diagrama desde tres ángulos. En ineficiencias, la disponibilidad se averigua dos veces y el faltante obliga a esperar o a hacer horas extras antes de facturar. En tareas manuales, el mismo pedido se anota tres veces (chat, papel o planilla y lista), con riesgo de error en cada copia. En flujo de datos, Producción, Depósito y ventas no comparten nada: no hay stock registrado y la producción se carga una vez por semana sin cruzarse con los pedidos.

Las tres apuntan a la misma causa, así que más que elegir entre varias oportunidades ordenamos los pasos de una sola solución: un registro de stock cargado todos los días, con una sola regla de stock disponible, primero en una planilla de prueba y después en Discovery.

## Alternativas

### Do Nothing: seguir igual

No requiere inversión, pero siguen los recortes semanales, el margen que se pierde en ellos y las horas extras, y la producción se sigue decidiendo a criterio del dueño y los hijos.

### A. Planilla compartida (incremental)

Una planilla de stock de producto terminado donde Producción carga lo producido al cierre de cada turno y Oficina reserva por pedido confirmado, con una reunión diaria corta entre ventas y producción. Cuesta casi nada y se puede probar en 2 semanas con papas fritas, el producto con más faltantes. Sirve para ver si la carga diaria se sostiene, pero no se conecta con Discovery: al facturar hay que descontar a mano y escala mal a todo el catálogo.

### B. Stock de Discovery (intermedia, recomendada)

Activar el módulo de stock de Discovery, que según el relevamiento ya está en la licencia y permite pedidos y reserva, aunque la empresa nunca lo usó. Incluye un conteo inicial, la activación por línea de producto (Salados, Dulces y Repostería), un responsable de carga por turno y un conteo semanal. No hay licencia nueva: el costo está en el conteo, la capacitación, el tiempo de carga y lo que cobre el proveedor por soporte.

Deja un solo registro donde ya se factura, si el módulo funciona como esperamos (supuesto 3), aunque por sí solo no cambia cómo se decide la producción. Como riesgo, en la Parte 1 vimos que Discovery está desactualizado, y todavía no sabemos qué versión usa la empresa, qué soporte incluye ni cuánto cuesta y tarda la activación; se lo vamos a consultar al proveedor.

### C. SaaS de gestión (integral, evaluada y descartada)

Un sistema en la nube para pedidos y stock, con cuota mensual, migración y capacitación. Tendría todo junto y escalaría mejor, pero como Discovery no se integra con otros sistemas habría que cargar en los dos, y tampoco resuelve la disciplina de carga. Reemplazar Discovery está fuera de alcance.

## Matriz multicriterio

Puntuamos de 1 a 5 cada alternativa como solución para los 6 meses y todos los productos, donde 5 es siempre lo más favorable para la empresa.

| Criterio | Do Nothing | A. Planilla | B. Discovery | C. SaaS |
|---|---|---|---|---|
| Alineación (¿ataca la causa?) | 1 | 3 | 4 | 3 |
| Costo | 5 | 5 | 4 | 2 |
| Viabilidad operativa | 3 | 3 | 3 | 2 |
| Tiempo | 1 | 5 | 3 | 2 |
| Adopción | 5 | 3 | 3 | 2 |
| Complejidad | 5 | 3 | 3 | 1 |
| Capacidad interna | 5 | 4 | 3 | 2 |
| Integración | 1 | 2 | 4 | 2 |
| Flujo de caja | 3 | 5 | 4 | 2 |
| Continuidad operativa | 2 | 3 | 4 | 2 |
| **Total (máximo 50)** | **31** | **36** | **35** | **20** |

C queda descartada. Do Nothing suma bastante porque no pide nada, pero no ataca la causa. Entre A y B hay un solo punto, una diferencia muy chica para decidir, y basta con darles algo más de peso a la alineación, la integración y la continuidad para que B pase adelante. Lo que termina de definir es que las notas bajas de A son estructurales, porque la planilla vive aparte de Discovery, mientras que las de B son incógnitas que el piloto y una prueba técnica pueden despejar.

## Recomendación

Recomendamos B, con A como piloto de 2 semanas sobre papas fritas: B es la solución de fondo y A sirve para probarla antes de gastar. Si el equipo no sostiene la carga diaria en una planilla simple, tampoco la va a sostener en Discovery. Además, registrar stock sin cambiar cómo se decide producir no baja los recortes (supuesto 5), por eso B va junto con el rediseño de la sección 3. El piloto prueba la carga diaria y da una primera lectura sobre los recortes, y el funcionamiento del módulo lo verifica una prueba técnica (sección 7).

El dueño está dispuesto a invertir si se demuestra el retorno. Como todavía no tenemos los costos para un VAN, usamos un punto de equilibrio: B se paga si las horas extras que evita por mes, al costo de la hora, cubren lo que cuesta por mes. Si para eso alcanza con la meta de unas 12 o 13 horas, cumplirla es suficiente. La cuenta es conservadora, porque no suma el margen de los pedidos que dejan de recortarse.
