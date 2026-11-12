# Proceso actual y alternativas de solución

Describimos el proceso tal como funciona hoy, con los volúmenes y tiempos que relevamos en la empresa.

## Matriz de descubrimiento

| Campo | Contenido |
|---|---|
| **Nombre** | Atender pedido de distribuidor |
| **Empieza cuando** | Llega un pedido del distribuidor por WhatsApp o por teléfono |
| **Termina (camino feliz)** | El pedido queda facturado en Discovery y despachado |
| **Áreas involucradas** | Oficina, Depósito, Producción y Dirección (el dueño y los hijos) |
| **Actores externos** | El distribuidor, que inicia el proceso y recibe el resultado, y el transporte tercerizado si no hay flota propia |
| **Volumen y periodicidad** | ~25 pedidos por día y ~125 por semana, con una demanda estable durante todo el año |
| **Camino alternativo frecuente** | Falta producto: en la semana que registramos, 30 de ~125 pedidos salieron recortados o demorados (~24 %) |
| **Fuera de los límites** | Insumos y packaging, y la visibilidad de stock para el distribuidor (sección 1) |

## SIPOC

Son seis pasos; el cuarto, alternativo, ocurre todas las semanas.

| # | Proveedor | Entrada | Proceso | Salida | Cliente |
|---|---|---|---|---|---|
| 1 | Distribuidor (externo) | Pedido por WhatsApp o teléfono | Recibir pedido | Pedido anotado en papel o planilla | Oficina (paso 2) |
| 2 | Depósito y Producción | Pedido anotado; lo que se ve en el depósito; lo que contesta Producción | Verificar disponibilidad | Disponibilidad conocida y pedido pasado a la lista | Depósito (paso 3) |
| 3 | Oficina y Producción | Lista de pedidos y producto terminado | Preparar pedido | Pedido armado, completo o con faltante | Oficina (pasos 4 y 5) |
| 4 | Depósito y Producción | Faltante detectado al armar | Resolver faltante (solo si falta producto) | Aviso al distribuidor, o producción con o sin horas extras | Distribuidor y Oficina |
| 5 | Depósito | Pedido armado o completado | Facturar pedido | Pedido facturado en Discovery | Distribuidor y Depósito (paso 6) |
| 6 | Oficina | Pedido facturado | Despachar pedido | Pedido despachado | Distribuidor y transporte tercerizado |

## RECI

R es el responsable (uno solo por actividad), E el ejecutor, C el consultado e I el informado. En una pyme quien ejecuta suele responder, por eso todas las filas son R/E.

| Actividad | Oficina | Depósito | Producción | Dirección | Distribuidor (externo) | Transporte tercerizado (externo) |
|---|---|---|---|---|---|---|
| Anotar pedido en papel o planilla | R/E | – | – | – | – | – |
| Preguntar disponibilidad a producción | R/E | – | C | – | – | – |
| Mirar el stock a ojo | I | R/E | – | – | – | – |
| Pasar pedido a la lista | R/E | I | – | – | – | – |
| Preparar pedido | I | R/E | – | – | – | – |
| Avisar al distribuidor del faltante | R/E | C | – | – | I | – |
| Producir lo que falta | I | I | R/E | C* | – | – |
| Producir con horas extras | I | I | R/E | C* | – | – |
| Facturar en Discovery | R/E | C | – | – | I | – |
| Despachar con flota propia | I | R/E | – | – | I | – |
| Entregar a transporte tercerizado | I | R/E | – | – | I | I |
| Decidir producción | – | – | I | R/E | – | – |
| Producir lo decidido | – | – | R/E | I | – | – |
| Registrar producción de la semana | – | – | R/E | – | – | – |

\* Como el dueño o los hijos deciden la producción, entendemos que producir de más o con horas extras se consulta con Dirección.

"Decidir producción" no tiene a nadie consultado, ni Oficina ni Depósito, que conocen los pedidos, y Dirección tiene una sola R aunque decide el dueño o uno de los hijos, sin definir cuál. La compuerta "¿Qué se hace con el faltante?" tampoco tiene un responsable relevado: quién decide entre mandar incompleto, esperar producción o hacer horas extras, y quién autoriza estas últimas, lo vamos a definir con el dueño antes del piloto.

## Diagrama AS-IS

![Proceso AS-IS](bpmn/as-is.png)

El pedido nace en el mensaje del distribuidor. Oficina lo anota y, en paralelo, pregunta a Producción mientras Depósito mira el stock; con las dos respuestas pasa el pedido a la lista y Depósito lo prepara. "¿Falta producto?" viene después de preparar, porque la averiguación previa no alcanza para saberlo, y sus tres salidas (mandar incompleto avisando, esperar producción o producir con horas extras) se juntan antes de facturar y despachar. El diagrama completo se adjunta en formato BPMN.

En los carriles de abajo, el dueño o uno de los hijos decide cada semana qué producir según su criterio y sin mirar los pedidos, y Producción registra lo producido una sola vez por semana, es decir, el 20 % de los días hábiles, sin cruzarlo con las ventas. Buena parte del proceso se sostiene en la memoria de las personas: el pedido original vive en el chat o en la llamada y lo demás son copias a mano que nadie más ve.

| Aspecto | Hoy |
|---|---|
| Actores y pasos | Los 4 carriles y los 2 externos; 14 actividades (11 del pedido y 3 de producción) |
| Entradas y salidas | Entra el pedido; sale facturado y despachado, o con aviso de incompleto |
| Herramientas | WhatsApp, teléfono, papel o planilla y lista de pedidos; Discovery, solo para facturar; control de producción semanal |
| Dolores | Recortes y demoras todas las semanas; faltantes que aparecen al armar; horas extras; producción que no mira los pedidos |
| Costos | ~25 horas extras por mes, en parte para completar pedidos, y el margen perdido en los pedidos recortados |
| Indicadores y línea de base | Pedidos completos y a tiempo: 76 % (estimado sobre una semana). Días con producción cargada: 20 %. Horas extras: ~25 por mes. Exactitud de stock: no existe porque no hay stock registrado |
| Lo que no es el problema | El armado del pedido: es rápido y no se mide |

## Tres lentes

Miramos el diagrama AS-IS desde tres ángulos: las ineficiencias, las tareas manuales y el flujo de datos.

Hay ineficiencias en la disponibilidad, que se averigua dos veces, preguntando a Producción y mirando el depósito, y en el faltante, que obliga a esperar a producción o a hacer horas extras antes de facturar. Automatizar el flujo tal como está no lo arregla: hay que reservar el stock contra los pedidos antes de confirmarlos.

Las tareas manuales se repiten: el mismo pedido se anota tres veces (chat, papel o planilla y lista) y en cada copia puede equivocarse un producto o una cantidad. La intervención es cargarlo una sola vez y que de ahí salgan la reserva y la lista de armado.

En el flujo de datos, Producción, Depósito y ventas no comparten nada: no hay stock de producto terminado registrado y lo producido se carga una vez por semana en un control que no se cruza con los pedidos. Es el silo más grande; la intervención es un registro de stock cargado todos los días, con un solo criterio de stock disponible: stock físico menos lo reservado por pedidos confirmados sin facturar.

Como las tres lentes apuntan a la misma causa, ordenamos los pasos de una misma solución: primero la planilla del piloto, una mejora rápida, y después el stock en Discovery, una inversión de impacto alto.

## Alternativas

### Do Nothing: seguir igual

Sin inversión, pero con el costo de seguir igual: los recortes y demoras de todas las semanas, un margen perdido en los pedidos recortados y unas 25 horas extras por mes, de las cuales solo una parte sirve para completar pedidos; el resto responde a la capacidad de la planta, tema que queda fuera de alcance. La producción sigue decidiéndose a criterio del dueño y los hijos.

### A. Planilla compartida (incremental)

Una planilla compartida de stock de producto terminado: Producción carga lo producido al cierre de cada turno, Oficina reserva por pedido confirmado y ventas y Producción se reúnen unos 10 minutos por día. Cuesta casi nada, apenas tiempo de carga, de reunión y de conteo. Se probaría como piloto de 2 semanas con papas fritas, el producto con más faltantes.

Permite comprobar con poco riesgo que Producción y Oficina sostienen la carga diaria (supuesto 2 de la sección 4) y tener una primera lectura de si planificar contra pedidos baja los recortes (supuesto 1). Pero no se conecta con Discovery: al facturar hay que bajar el físico y descontar la reserva a mano, el pedido se carga dos veces y escala mal a todos los productos.

### B. Stock de Discovery (intermedia, recomendada)

Consiste en activar el módulo de stock de Discovery, que según el relevamiento está incluido en la licencia, permite pedidos y reserva, y la empresa nunca usó. Incluye un conteo físico inicial, la activación línea por línea (Salados, Dulces y Repostería) con el mismo criterio de stock disponible y la misma rutina que A (sección 3), un responsable de carga por turno con suplente y un conteo cíclico semanal. No hay licencia nueva: el costo está en el conteo, la capacitación, el tiempo de carga y lo que el proveedor cobre por soporte, repartido en los 6 meses del plazo.

Deja un solo registro de stock en la herramienta donde ya se factura, con el pedido cargado una vez y la reserva consumida por la factura, si el módulo funciona como esperamos (supuesto 3). No resuelve que la producción se decida mirando pedidos, que es un cambio de criterio de Dirección y no de herramienta, ni la saturación de la planta. Como riesgo, en la Parte 1 identificamos que Discovery está desactualizado y con errores, y no sabemos qué versión usa la empresa, qué soporte incluye, cuánto cuesta ni cuánto tarda activar el módulo; se lo vamos a preguntar al proveedor.

### C. SaaS de gestión (integral, evaluada y descartada)

Un sistema de gestión en la nube para pedidos y stock, que conviviría con Discovery o lo reemplazaría, con cuota mensual nueva, migración, capacitación y, si Discovery sigue para facturar, su costo también. No pedimos cotizaciones; la evaluamos como categoría. Tendría todo en un solo lugar y escalaría mejor, pero no resuelve la disciplina de carga. Como Discovery no se integra con otros sistemas, quedaría al lado con carga manual en los dos. Reemplazarlo está fuera de alcance (sección 1).

## Matriz multicriterio

Usamos diez criterios y comparamos las alternativas como solución para los 6 meses y todos los productos, no como piloto. La escala va de 1 a 5 y 5 es siempre lo más favorable para la empresa, es decir, lo más barato, rápido y simple.

| Criterio | Do Nothing | A. Planilla compartida | B. Stock de Discovery | C. SaaS |
|---|---|---|---|---|
| **1. Alineación al negocio** (¿ataca la causa?) | 1 – No toca la causa | 3 – Registra y reserva, pero no cambia cómo se decide producir | 4 – Registra, reserva y factura en un lugar; producir mirando pedidos sigue siendo otro cambio | 3 – Cubre pedido y stock, no la decisión de producir |
| **2. Costo** | 5 – No hay inversión | 5 – Casi nulo | 4 – Sin licencia nueva; conteo, capacitación y activación | 2 – Cuota, migración y capacitación, más Discovery |
| **3. Viabilidad operativa** | 3 – Es lo de hoy, con horas extras | 3 – Liviana con un producto; con todos, la doble carga pesa | 3 – Una carga, pero diaria y sobre un módulo que nadie usó | 2 – Migrar y capacitar con la planta al límite |
| **4. Tiempo** | 1 – No hay efecto nunca | 5 – Sin proveedor; piloto de 2 semanas | 3 – Activar con el proveedor y contar por línea | 2 – Elegir, contratar, migrar y capacitar |
| **5. Adopción** | 5 – No pide nada, y tampoco mejora | 3 – Formato familiar, pero doble carga | 3 – Una carga, en una herramienta que nadie usó para esto | 2 – Pantallas nuevas y doble carga |
| **6. Complejidad** | 5 – Ninguna | 3 – Simple, pero descontar a mano es propenso a errores | 3 – Configurar pedido, reserva y consumo; depende de la versión de Discovery | 1 – Dos sistemas que no se integran, más una migración |
| **7. Capacidad interna** | 5 – No hace falta nada | 4 – Lo arma el responsable de sistemas, según el tiempo que pueda dedicarle | 3 – Depende de Buenos Aires Software y del responsable de sistemas | 2 – Proveedor nuevo y dos sistemas |
| **8. Integración** | 1 – Nada se conecta | 2 – La planilla no habla con Discovery | 4 – Todo en Discovery, si la factura consume la reserva (supuesto 3) | 2 – Discovery no se integra: carga manual en los dos |
| **9. Flujo de caja** | 3 – No sale dinero nuevo, pero siguen las horas extras | 5 – Casi nada, y se puede cortar sin perder inversión | 4 – Sin cuota nueva; gasto puntual que el dueño evaluaría por su retorno | 2 – Cuota fija en una empresa que cobra de contado, a ~30 días o con cheques diferidos |
| **10. Continuidad operativa** | 2 – Sin registro, depende de las personas | 3 – No corta nada, pero es un archivo suelto | 4 – Una sola fuente, con suplente; riesgo: Discovery desactualizado | 2 – Suma un proveedor y una migración |
| **Total (suma simple, máximo 50)** | 31 | 36 | 35 | 20 |

C queda descartada: tiene la suma más baja y no es la mejor en ningún criterio. Do Nothing llega a 31 porque no pide inversión ni cambios y por eso puntúa 5 en costo, adopción, complejidad y capacidad interna, pero no resuelve el problema (alineación 1 e integración 1). Entre A y B hay un solo punto, una diferencia demasiado chica para decidir. Probamos también otros pesos, solo como referencia, porque A y B quedaron muy parejos: B supera a A si alineación, integración y continuidad operativa pesan más de 1,25 veces lo que el resto (empatan en 38); con más peso en costo, tiempo y flujo de caja solo crece la ventaja de A.

Decide el argumento cualitativo. Las notas bajas de A son estructurales (integración 2, alineación 3, continuidad 3) y no mejoran con la práctica, porque la planilla vive aparte de Discovery. Las medias de B son incógnitas, porque nadie usó ese módulo en Dulxelitos, y pueden subir o bajar cuando se sepa. Por eso A va primero, como paso 1 y MVP: el piloto, la prueba técnica y la activación por línea despejan las incógnitas de B, que es el destino.

## Recomendación

Recomendamos B, el stock de Discovery, con A, la planilla compartida, como piloto de 2 semanas sobre papas fritas. B es la solución del proceso nuevo y A sirve para probarla antes de gastar.

Si el equipo no sostiene la carga diaria en una planilla simple, tampoco la va a sostener en Discovery, y pagar la herramienta no resolvería el problema de carga. Además, cargar stock sin cambiar cómo se decide producir no baja los recortes (supuesto 5), por eso B va junto con el rediseño de la sección 3. El piloto prueba la carga diaria (supuesto 2) y da una primera lectura de si planificar contra pedidos baja los recortes (supuesto 1). El supuesto 3, que Discovery reserve y que la factura consuma la reserva, lo verifica la prueba técnica de la sección 7 antes del Go, salvo el paso de la factura si no hay ambiente de prueba; los umbrales y el Go/No-Go están en las secciones 7 y 8.

El dueño está dispuesto a invertir si se demuestra el retorno, y el ahorro principal de B se puede medir en la liquidación de sueldos. En lugar de un VAN usamos un punto de equilibrio, que la sección 4 retoma: B se paga si evita por mes tantas horas extras como resulte de dividir su costo mensual por el costo de la hora extra, repartiendo en los 6 meses lo que se paga una sola vez. Si el cociente da menos de unas 12 o 13 horas por mes, que es la meta de la sección 1, con solo cumplirla B se paga. No sumamos el margen de los pedidos que dejan de recortarse, así que la cuenta es conservadora. El punto de equilibrio compara B con no hacer nada y no con A: lo que B agrega es una sola carga que integra pedido, reserva y factura y escala a más de 25 combinaciones de producto y formato, como identificamos en la Parte 1. El plazo de recupero lo decide el dueño.
