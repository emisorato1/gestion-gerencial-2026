# Proceso actual y alternativas de solución

Esta sección describe cómo se atiende hoy un pedido de distribuidor en Dulxelitos, qué encuentran en ese proceso las tres lentes de la Clase 7 y qué alternativas hay para mejorarlo, incluida la de no hacer nada. Sigue el orden que vimos en clase: primero se descubre el proceso (matriz de descubrimiento, SIPOC y RECI), después se lo dibuja y recién entonces se comparan alternativas.

**Una corrección que sostiene todo lo que sigue.** Como dijimos en la sección 1, el relevamiento de esta parte corrige la Parte 1 en dos puntos que acá pesan mucho: el stock de producto terminado no se registra (ni en Discovery ni en ningún otro lado) y los recortes vienen de la mezcla y del momento de producción, no de la capacidad total de la planta. Por eso el proceso que describimos no tiene ningún paso de "consultar el stock": no hay dónde consultarlo.

**De dónde sale cada cosa.** El proceso, los datos de volumen y lo que dice la matriz de descubrimiento los relevamos con nuestro compañero que trabaja en Dulxelitos. El RECI, la lectura de las tres lentes y los puntajes de la matriz multicriterio son nuestros: razonados sobre ese relevamiento, no medidos. Lo que no sabemos queda como "dato pendiente".

**Adelantamos la conclusión.** Recomendamos activar el módulo de stock de Discovery (alternativa B), probado antes con una planilla compartida durante 2 semanas sobre papas fritas (alternativa A). En la matriz, A y B quedan casi empatadas, y lo decimos así. Elegimos B porque los puntos flojos de A son estructurales y los de B son incógnitas que el piloto ayuda a despejar. El retorno lo planteamos como punto de equilibrio y no como VAN, porque faltan dos datos de costo.

## Matriz de descubrimiento

La matriz de descubrimiento fija el ámbito del proceso antes de dibujarlo. Seguimos los campos de la clase: nombre con verbo y sustantivo, evento que lo inicia, evento que lo termina en el camino feliz, áreas, y volumen y periodicidad.

| Campo | Contenido |
|---|---|
| **Nombre** | Atender pedido de distribuidor |
| **Empieza cuando** | Llega un pedido del distribuidor por WhatsApp o por teléfono |
| **Termina (camino feliz)** | El pedido queda facturado en Discovery y despachado |
| **Áreas involucradas** | Oficina, depósito, producción y dirección (el dueño y los hijos) |
| **Actores externos** | El distribuidor, que inicia el proceso y recibe el resultado, y el transporte tercerizado, cuando no se despacha con flota propia |
| **Volumen y periodicidad** | ~25 pedidos por día, ~125 por semana (25 por 5 días hábiles). La demanda es pareja todo el año |
| **Camino alternativo frecuente** | Falta producto: en la semana que registramos, 30 de ~125 pedidos salieron recortados o demorados (~24 %) |
| **Fuera de los límites** | Insumos y packaging, y la visibilidad de stock para el distribuidor (sección 1) |

Empezamos por el camino feliz, como se hace al descubrir un proceso, pero el faltante no lo tratamos como una excepción rara: pasa todas las semanas, así que el diagrama lo dibuja completo.

Una aclaración sobre los límites. La decisión de qué producir (decidir, producir y registrar) no es parte de "Atender pedido de distribuidor": corre aparte, por semana. La dibujamos igual en el mismo diagrama porque esa falta de conexión con los pedidos es justamente parte del problema.

## SIPOC

El SIPOC resume el proceso en 4 a 6 pasos con quién provee, qué entra, qué sale y quién lo recibe. Tiene seis pasos: cinco del camino feliz y uno, el cuarto, que es alternativo pero en Dulxelitos ocurre todas las semanas.

| # | Proveedor | Entrada | Proceso | Salida | Cliente |
|---|---|---|---|---|---|
| 1 | Distribuidor (externo) | Pedido por WhatsApp o teléfono: productos, cantidades, zona | Recibir pedido | Pedido anotado en papel o planilla | Oficina (paso 2) |
| 2 | Depósito y Producción | Pedido anotado; lo que se ve a ojo en el depósito; lo que contesta producción | Verificar disponibilidad | Disponibilidad conocida y pedido pasado a la lista | Depósito (paso 3) |
| 3 | Oficina (la lista) y Producción (producto terminado) | Lista de pedidos y producto terminado | Preparar pedido | Pedido armado, completo o con faltante | Oficina (pasos 4 y 5) |
| 4 | Producción y Dirección | Faltante detectado al armar | Resolver faltante (solo si falta producto) | Aviso al distribuidor, o producto producido con o sin horas extras | Distribuidor y Oficina |
| 5 | Depósito | Pedido armado o ya completado | Facturar pedido | Pedido facturado en Discovery | Distribuidor y Depósito (paso 6) |
| 6 | Oficina | Pedido facturado | Despachar pedido | Pedido despachado | Distribuidor y transporte tercerizado (externo, si se terceriza) |

Dos cosas se ven en el SIPOC antes de dibujar nada. Primero, en el paso 2 el proveedor de la información son personas y no registros: lo que se sabe de la disponibilidad es lo que alguien ve o contesta en el momento. Segundo, en ningún paso hay una entrada que sea el stock registrado ni una salida que lo actualice: nada de lo que se produce entra a un registro que el resto del proceso pueda mirar.

## RECI

El RECI dice quién hace y quién responde por cada actividad. Usamos las letras de la clase: **R** es el responsable, el que responde por el resultado, y hay uno solo por actividad; **E** es el ejecutor; **C** es el consultado e **I** es el informado. Cuando el responsable es también quien lo hace, ponemos R/E. Las columnas son las lanes del diagrama más los dos actores externos, que nunca son R. Los nombres de las actividades son los del diagrama, y dejamos la herramienta en algunos nombres ("en papel o planilla", "en Discovery") porque es parte de lo que se relevó.

| Actividad | Oficina | Depósito | Producción | Dirección | Distribuidor (externo) | Transporte tercerizado (externo) |
|---|---|---|---|---|---|---|
| Anotar pedido en papel o planilla | R/E | – | – | – | – | – |
| Preguntar disponibilidad a producción | R/E | – | C | – | – | – |
| Mirar el stock a ojo | I | R/E | – | – | – | – |
| Pasar pedido a la lista | R/E | I | – | – | – | – |
| Preparar pedido | I | R/E | – | – | – | – |
| Avisar al distribuidor del faltante | R/E | C | – | – | I | – |
| Producir lo que falta | I | I | R/E | C* | – | – |
| Producir con horas extras | – | – | R/E | C* | – | – |
| Facturar en Discovery | R/E | C | – | – | I | – |
| Despachar con flota propia | I | R/E | – | – | I | – |
| Entregar a transporte tercerizado | I | R/E | – | – | I | I |
| Decidir producción | – | – | I | R/E | – | – |
| Producir lo decidido | – | – | R/E | I | – | – |
| Registrar producción de la semana | – | – | R/E | – | – | – |

\* Es supuesto nuestro: como la producción la deciden el dueño o los hijos, leemos que producir de más o con horas extras se consulta con Dirección. A confirmar con la empresa.

**Quién responde "Preguntar disponibilidad a producción".** Es una actividad de Oficina, que la ejecuta y responde por ella. La respuesta la da Producción, que figura como consultada (C). Es el único punto del proceso en que ventas y producción se tocan, y es una pregunta a una persona, no una consulta a un registro.

Qué muestra el RECI:

- **Cada actividad tiene un solo responsable, y todos son roles internos.** Oficina responde por cinco actividades, Depósito por cuatro, Producción por cuatro y Dirección por una. El distribuidor y el transporte aparecen solo como informados.
- **En "Decidir producción" no hay nadie consultado.** Ni Oficina ni Depósito, que son los que conocen los pedidos, figuran como C. La decisión se toma sin ellos, que es lo que nos dijo el relevamiento.
- **Falta un dueño para el faltante.** La compuerta "¿Qué se hace con el faltante?" del diagrama no es una actividad, así que no entra en el RECI, pero alguien tiene que decidir si se manda incompleto, se espera producción o se hacen horas extras. Eso no lo relevamos: [dato pendiente: quién decide qué se hace con el faltante y quién autoriza las horas extras].
- **Rol y persona no coinciden en Dirección.** El rol tiene una sola R, pero la decisión la toma el dueño o uno de los hijos, según el caso. En una empresa chica una persona cumple varios roles, y eso es normal; el problema es que no está definido quién responde por la decisión.

## Diagrama AS-IS

![Proceso AS-IS](bpmn/as-is.png)

### Cómo se lee

El pool Dulxelitos tiene cuatro lanes, las mismas del RECI: Oficina, Depósito, Producción y Dirección. El distribuidor y el transporte tercerizado son pools colapsados: solo intercambian mensajes con la empresa.

**El recorrido del pedido.** Empieza con el mensaje del distribuidor, por WhatsApp o teléfono. Oficina lo anota en papel o planilla y, a partir de ahí, averigua si hay mercadería de dos maneras al mismo tiempo: pregunta a producción y, en paralelo, depósito mira el stock a ojo. Cuando tiene las dos respuestas, Oficina pasa el pedido a una lista, y Depósito lo prepara. Si no falta nada, Oficina factura en Discovery, y Depósito despacha con flota propia o entrega al transporte tercerizado. Ahí termina el pedido.

**Cuando falta producto.** La pregunta "¿Falta producto?" está después de preparar el pedido: aunque ya se averiguó a ojo y preguntando, el faltante recién aparece al armar, porque esa averiguación no alcanza para saberlo. Desde ahí hay tres salidas: se manda incompleto avisando al distribuidor, se espera producción, o se produce con horas extras si hace falta. Las tres vuelven a juntarse antes de facturar. Esta rama no es un caso raro: se recorre todas las semanas, con unos 30 de ~125 pedidos recortados o demorados. Y el diagrama no dice quién decide cuál de las tres se usa.

**La producción corre aparte.** En el carril de abajo, cada semana el dueño o uno de los hijos deciden qué producir por criterio propio, sin mirar los pedidos. Producción produce lo decidido y registra la producción de la semana, una sola vez (el 20 % de los días hábiles). Ese registro no se cruza con las ventas. El único punto donde este recorrido toca al del pedido es el faltante, y recién después de que el pedido ya se aceptó.

**Lo que el diagrama no tiene.** Ningún paso de consultar o reservar stock registrado, y ninguna flecha que lleve los pedidos a la decisión de producción. Es el mapa de un proceso que acepta pedidos sin saber qué hay y produce sin saber qué se pidió.

### El estado actual, en una tabla

| Aspecto | Hoy |
|---|---|
| **Actores** | Oficina, depósito, producción y dirección (dueño e hijos); el distribuidor y el transporte tercerizado como externos |
| **Pasos** | 14 actividades: 11 del pedido y 3 de producción, que corre aparte |
| **Entradas** | Pedido por WhatsApp o teléfono; lo que se ve a ojo y lo que contesta producción; la decisión de producción del dueño o los hijos |
| **Salidas** | Pedido facturado y despachado; aviso de pedido incompleto; registro semanal de producción |
| **Herramientas** | WhatsApp y teléfono; papel o planilla; una lista de pedidos; Discovery, solo para facturar; el control propio de producción, que se carga una vez por semana |
| **Dolores** | Pedidos recortados o demorados todas las semanas; faltantes que se descubren al armar; horas extras; producción que no mira los pedidos; la misma información cargada varias veces |
| **Costos** | ~25 horas extras por mes, de las cuales parte se hace para completar pedidos. En pesos: [dato pendiente: costo por hora extra]. Margen perdido en pedidos recortados: [dato pendiente: margen o valor promedio de un pedido recortado] |
| **Indicadores y línea de base** | Pedidos completos y a tiempo: 76 % (cuenta nuestra sobre una semana). Días con producción cargada: 20 %. Horas extras: ~25 por mes. Exactitud de stock: no existe, porque no hay stock registrado; sale del primer conteo físico [dato pendiente: exactitud de stock en el conteo inicial] |
| **Lo que no es el problema** | El armado del pedido: según nuestro compañero es rápido y no se mide, así que no es la restricción |

### Dependencias informales

El proceso funciona porque la gente se acuerda de cosas que no están escritas en ningún lado. Las que relevamos:

- **WhatsApp y teléfono.** El pedido original vive en el chat o en la llamada. Lo que queda en papel o planilla y en la lista son copias hechas a mano.
- **Papel o planilla de quien atiende.** Es el único registro del pedido hasta que se factura, y no lo ve nadie más.
- **Preguntar a producción.** La disponibilidad depende de lo que sepa y conteste una persona en ese momento. No queda registro de la respuesta.
- **Mirar a ojo.** La disponibilidad depende de la vista de quien está en el depósito y de que el producto esté donde se espera.
- **El criterio del dueño y los hijos.** Qué producir se decide por experiencia, sin registro de pedidos ni de stock, y sin que quede dicho por qué.
- **Qué se hace con el faltante y quién autoriza las horas extras.** Funciona de hecho, y cómo se decide no lo tenemos relevado (ver el RECI).
- **El control propio de producción.** Se carga una vez por semana y no está vinculado a ventas, así que lo que sabe producción no le llega al resto.

## Tres lentes

Miramos el diagrama con las tres lentes de la Clase 7. Cada una da un hallazgo concreto.

### Lente 1: ineficiencias

**Hallazgo.** La disponibilidad se averigua dos veces: se pregunta a producción y se mira a ojo en el depósito. Las dos tareas corren en paralelo y las dos hacen falta, porque ninguna alcanza sola. Es una doble averiguación que existe porque no hay un stock registrado. Además hay un bucle de espera: cuando falta producto, el pedido espera producción o horas extras antes de facturarse.

**Qué hace falta.** No es un flujo de aprobaciones al que se le pueda poner un workflow. Es una pregunta que se contesta mirando un registro. La intervención es un rediseño: reservar el stock contra pedidos antes de confirmar.

### Lente 2: tareas manuales

**Hallazgo.** El mismo pedido se transcribe tres veces: queda en el chat, se copia al papel o planilla y se vuelve a copiar a la lista. Cada copia a mano es un punto donde se puede equivocar un producto o una cantidad.

**Qué hace falta.** Cargar el pedido una sola vez y que de ahí salgan la reserva y la lista de armado. Como con la lente anterior, no se trata solo de pasar a pantalla lo que hoy está en papel: se trata de que haya un único registro del pedido.

### Lente 3: flujo de datos

**Hallazgo.** Producción, depósito y ventas no comparten ningún dato. No existe un stock de producto terminado registrado, y lo producido se carga una vez por semana en un control propio que no se cruza con los pedidos. Es el silo más grande del proceso.

**Qué hace falta.** Un registro de stock cargado todos los días, con un solo criterio de stock disponible: stock físico menos lo reservado por pedidos confirmados sin facturar.

### Cuál va primero

Las tres lentes no dan tres proyectos: dan una sola causa vista desde tres lados. La doble averiguación existe porque no hay stock registrado; las tres transcripciones, porque el pedido no se carga en un lugar que lo reserve; y la producción ciega, porque no se cruzan datos. Por eso no ordenamos tres iniciativas con la matriz impacto-esfuerzo ni con RICE (que, como dijo la clase, no decide: fuerza la discusión). Lo que ordenamos son los pasos de una sola iniciativa: primero un quick win, la planilla del piloto, que cuesta poco y enseña mucho; detrás de él, la inversión de impacto alto, el stock en Discovery.

### La pregunta del proceso balde

La clase del 05-10 pidió una pregunta antes de mejorar nada: ¿este proceso aporta valor al cliente final, o solo contiene un error anterior? Es la paradoja de la gotera: se pone un balde debajo, después otro más grande, y nadie arregla la gotera.

"Atender pedido de distribuidor" como proceso sí aporta valor: empieza y termina en el distribuidor. Lo que tiene adentro son baldes. La gotera es doble: no se registra el stock y se produce sin mirar los pedidos. Los baldes son la doble averiguación, el aviso de faltante y las horas extras para completar pedidos. Mejorar los baldes sin tocar la gotera sería una solución balde: por ejemplo, que el aviso de faltante salga más rápido por WhatsApp, o armar un tablero de horas extras. Sería poner una herramienta a contener un problema que sigue ahí.

Una salvedad: una parte de las horas extras no es balde, porque tapa la saturación estructural de la planta. Eso no es una gotera nuestra, es capacidad, y está fuera de alcance.

## Alternativas

El enunciado pide comparar al menos dos alternativas, más no avanzar. Las organizamos así: **A** es la mejora incremental y de bajo costo, **B** es la intermedia (configurar una herramienta que la empresa ya tiene) y **C** es la integral, que el enunciado dice que se incluya solo si el caso la justifica. No la justifica, y la dejamos como evaluada y descartada.

### Do Nothing: seguir igual

- **Qué es.** Mantener el proceso como está.
- **Costo.** No hay inversión. El costo es el de seguir igual: las ~25 horas extras por mes (en parte), los pedidos recortados o demorados todas las semanas, y un margen perdido que hoy no podemos poner en pesos: [dato pendiente: margen o valor promedio de un pedido recortado]. La Parte 1 dijo que el costo de no actuar "no está bajo, está sin observar"; ahora sabemos por qué: ni el stock ni los recortes se registraban.
- **Qué resuelve.** Nada. Tampoco empeora nada que hoy ande bien.
- **Qué no resuelve.** Todo lo demás. Además la planta sigue dependiendo de la memoria del dueño, de los hijos y de quien mira a ojo.

### A. Planilla compartida (mejora incremental)

- **Qué es.** Una planilla compartida de stock de producto terminado. Producción carga lo producido al cierre de cada turno, Oficina reserva el stock por pedido confirmado, y hay una reunión corta diaria entre ventas y producción (~10 minutos). Usa el mismo criterio que B: el stock disponible es el stock físico menos lo reservado por pedidos confirmados sin facturar. Se prueba como piloto de 2 semanas con papas fritas, el producto que más falta.
- **Costo.** Casi cero en plata: la planilla y el tiempo de carga, de reunión y del conteo inicial.
- **Qué resuelve.** Hace visible un stock que hoy no existe, y permite probar con poco riesgo las dos cosas de las que depende todo: que producción y oficina sostengan la carga diaria (supuesto 2 de la sección 4) y que planificar contra pedidos baje los recortes (supuesto 1).
- **Qué no resuelve.** No se conecta con Discovery: al facturar, la reserva se libera a mano y el pedido se carga dos veces. Vive en un archivo suelto que depende de quien lo carga, escala mal a todos los productos y no cambia por sí sola cómo se decide qué producir.

### B. Stock de Discovery (alternativa intermedia, recomendada)

- **Qué es.** Activar el módulo de stock de Discovery, que según nuestro compañero está dentro de la licencia, permite pedidos y reserva, y la empresa todavía no usó. Se hace un conteo físico inicial y se activa línea de producto por línea de producto. Mismo criterio de stock disponible que en A, y la misma rutina: carga diaria al cierre de turno, un responsable de carga por turno con suplente, conteo cíclico semanal y reunión diaria.
- **Costo.** Sin licencia nueva. Cuesta el conteo inicial, la capacitación, el tiempo de carga, y [dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]. Los gastos que se pagan una sola vez se reparten en los 6 meses del plazo.
- **Qué resuelve.** Un solo registro de stock en la herramienta donde ya se factura, con el pedido cargado una vez y la reserva consumida por la factura (si el módulo funciona como esperamos: supuesto 3). Es lo que ataca la causa común de las tres lentes.
- **Qué no resuelve.** Que la producción se decida mirando pedidos: es un cambio de criterio de Dirección, no de herramienta. Tampoco toca la saturación de la planta, los insumos y el packaging, ni la visibilidad de stock para el distribuidor, que queda para "later". Y tiene un riesgo propio: la Parte 1 describió a Discovery como desactualizado y con errores, y la versión y el soporte incluidos son [dato pendiente: versión de Discovery y soporte incluido].

### C. SaaS de gestión (integral, evaluada y descartada)

- **Qué es.** Contratar un sistema de gestión en la nube para pedidos y stock, que convivía con Discovery o lo reemplazaba.
- **Costo.** Cuota mensual nueva, migración y capacitación, y seguir pagando Discovery si se lo mantiene para facturar. No pedimos cotizaciones: la evaluamos como categoría, no con proveedores concretos. Los otros motivos alcanzan para descartarla.
- **Qué resuelve.** En teoría, pedido y stock en un solo lugar y mejor escala.
- **Qué no resuelve.** La disciplina de carga: si el equipo no sostiene una carga diaria en una planilla simple, tampoco la va a sostener en un sistema más grande. Según la Parte 1, Discovery no se integra con otros sistemas, así que el SaaS quedaría al lado con carga manual en los dos. Reemplazar Discovery está fuera de alcance (sección 1).

## Matriz multicriterio

La matriz usa los diez criterios del enunciado. Comparamos cada alternativa como **solución para los 6 meses y para todos los productos**, no como piloto: el piloto lo tratamos aparte en la recomendación.

**Escala.** De 1 a 5, donde **5 siempre es lo más favorable para la empresa**. Para costo, tiempo y complejidad, 5 quiere decir lo más barato, lo más rápido y lo más simple, no lo más caro. Los puntajes son nuestro juicio sobre lo que relevamos y sobre los supuestos de la sección 4; ninguno sale de una medición. Donde hay un dato pendiente que movería el puntaje, está marcado.

| Criterio (qué miramos) | Do Nothing | A. Planilla compartida | B. Stock de Discovery | C. SaaS |
|---|---|---|---|---|
| **1. Alineación al negocio** (¿ataca la causa: pedidos aceptados sin saber qué hay y producción sin mirar pedidos?) | **1.** No toca la causa: los recortes siguen cada semana | **3.** Registra y reserva, pero la reserva se libera a mano al facturar y no cambia sola cómo se decide producir | **4.** Registra, reserva y factura en el mismo lugar. No llega a 5: producir mirando pedidos es un cambio de criterio, no de herramienta | **3.** Cubre pedido y stock, pero no la disciplina de carga ni la decisión de producir, y suma un sistema al lado de Discovery |
| **2. Costo** (inversión y gasto recurrente; 5 es lo más barato) | **5.** No hay inversión; el costo de seguir igual se mide aparte | **5.** Casi cero: la planilla y el tiempo de carga y de conteo | **4.** Sin licencia nueva. Cuesta conteo, capacitación y [dato pendiente: costo de activar el módulo] | **2.** Cuota nueva, migración y capacitación, y se sigue pagando Discovery para facturar |
| **3. Viabilidad operativa** (¿se puede hacer con una planta saturada, sin frenarla?) | **3.** Se puede y es lo que se hace hoy, pero sostenido con horas extras | **3.** Es chica con un producto. Con todos, la carga doble (planilla y Discovery) pesa sobre una planta al límite | **3.** Una sola carga, pero exige carga diaria y reserva con la gente que hay, sobre un módulo que nadie usó en Dulxelitos | **2.** Migrar datos y capacitar a tres áreas con la planta al límite |
| **4. Tiempo** (rapidez hasta el primer efecto) | **1.** No hay efecto nunca | **5.** Se arma sin proveedor ni instalación; el piloto dura 2 semanas | **3.** Hay que activar con el proveedor y hacer el conteo inicial, línea por línea: [dato pendiente: plazo de activación del módulo] | **2.** Elegir producto, contratar, migrar y capacitar antes del primer efecto |
| **5. Adopción** (¿lo usan quienes tienen que usarlo?) | **5.** No le pide nada a nadie. Por eso no hay resistencia, y tampoco mejora | **3.** El formato es familiar, pero es trabajo nuevo para producción y oficina y se carga dos veces | **3.** La misma carga diaria, una sola vez, en una herramienta que la Parte 1 describió vieja y que nadie usó para esto | **2.** Herramienta y pantallas nuevas, y doble carga con Discovery |
| **6. Complejidad** (5 es lo más simple) | **5.** Ninguna | **3.** Simple de armar, pero reservar y liberar a mano se presta a errores cuando suben los productos | **3.** Hay que configurar pedido, reserva y consumo por factura. Depende de la versión: [dato pendiente: versión de Discovery] | **1.** Dos sistemas que no se integran, más una migración |
| **7. Capacidad interna** (¿lo puede hacer la gente de la empresa?) | **5.** No hace falta nada | **4.** Lo arma el responsable de sistemas, sin proveedor. Baja porque se suma a un rol cuyo tiempo disponible no conocemos | **3.** Depende de Buenos Aires Software para activar y configurar, y del tiempo del responsable de sistemas | **2.** Proveedor nuevo y dos sistemas para sostener con el equipo de hoy |
| **8. Integración** (¿conecta pedido, stock y facturación?) | **1.** Nada se conecta | **2.** La planilla no habla con Discovery: al facturar se libera la reserva a mano | **4.** Pedido, reserva, stock y factura en Discovery. Falta confirmar que la factura consume la reserva (supuesto 3) | **2.** Según la Parte 1, Discovery no se integra con otros sistemas: carga manual entre los dos |
| **9. Flujo de caja** (cuánto sale y cuándo; 5 es poco y sin cuotas fijas nuevas) | **3.** No sale plata nueva, pero siguen saliendo las horas extras y se pierde margen en los pedidos recortados | **5.** Casi nada, y se puede cortar sin perder inversión | **4.** Sin cuota nueva. El gasto es puntual y el dueño acepta invertir si se demuestra el retorno | **2.** Cuota fija mensual en una empresa que cobra de contado, a ~30 días o con cheques diferidos (Parte 1) |
| **10. Continuidad operativa** (¿protege ventas y producción durante y después del cambio?) | **2.** Depende de la memoria del dueño, los hijos y quien mira a ojo; si faltan, no hay registro | **3.** No corta nada y se revierte, pero es un archivo suelto que depende de quien lo carga | **4.** Una sola fuente en la herramienta de facturación, con carga por turno y suplente. Riesgo: Discovery está desactualizado y con errores (Parte 1) | **2.** Suma un proveedor más para algo de uso diario y una migración encima de la operación |
| **Total (suma simple, máximo 50)** | **31** | **36** | **35** | **20** |

### Cómo leer la matriz

**C queda descartada.** Tiene la suma más baja por mucho y no es la mejor en ningún criterio. Pesan en contra el costo recurrente, una migración sobre una planta saturada y un segundo sistema que no se integra con Discovery.

**Do Nothing no se descarta por la suma.** Con 31 no queda tan abajo, y es porque la suma premia lo fácil: no hacer nada es barato, simple y no le pide nada a nadie. La descartamos por lo que no hace: tiene 1 en alineación y 1 en integración, es decir, no resuelve el problema.

**A y B quedan casi empatadas: 36 contra 35.** Un punto de diferencia entre puntajes de juicio no es una diferencia. Para ver cuánto depende de lo que pese cada criterio, probamos dos ponderaciones. Son nuestras, no de la cátedra, y las mostramos para que se vea el efecto, no para dar por cerrada la discusión.

| Ponderación (nuestro criterio) | Do Nothing | A | B | C |
|---|---|---|---|---|
| Suma simple | 31 | 36 | 35 | 20 |
| Doble peso a lo que dice si resuelve el problema de forma durable: alineación, integración y continuidad | 35 | 44 | 47 | 27 |
| Doble peso a lo barato y rápido: costo, tiempo y flujo de caja | 40 | 51 | 46 | 26 |

Si lo único que importara fuera gastar poco y arrancar ya, ganaría A. Si importa que el problema quede resuelto de manera durable, gana B. Elegimos mirar lo segundo porque el dueño aceptó invertir más si se demuestra el retorno: el costo no es el límite, así que no tiene sentido que mande en la decisión.

**Dónde están los puntos flojos de cada una.** Acá está lo que decide entre las dos. Las notas bajas de A son estructurales: integración 2, alineación 3 y continuidad 3 salen de que la planilla vive aparte de Discovery, y no mejoran con el tiempo ni con la práctica. Las notas medias de B son incógnitas: viabilidad, tiempo, adopción, complejidad y capacidad interna valen 3 porque nadie usó ese módulo en Dulxelitos. Un 3 por no saber puede subir o bajar cuando se sepa; un 2 porque la planilla no habla con Discovery no cambia. Y los supuestos que más inciden en esos 3, la carga diaria sostenida y el módulo que funciona como esperamos, son justamente los que el piloto con A y la activación por línea de producto sirven para despejar.

## Recomendación

**Recomendamos B, el stock de Discovery, con A, la planilla compartida, como piloto de 2 semanas sobre papas fritas.** B es la solución, la que queda en el proceso nuevo. A es el experimento que la prueba antes de gastar.

### Por qué en ese orden

La lógica es la misma que usó la clase para el MVP: antes de construir, probar con el experimento mínimo. Si el equipo no sostiene la carga diaria en una planilla simple, tampoco la va a sostener en Discovery, y habríamos gastado en una herramienta para un problema que es de disciplina y no de tecnología. El ejemplo de la clase del 19-10 va en la misma dirección: la firma digital de planos no acortó el tiempo de ciclo, lo acortó juntar a los decisores una vez por semana. Acá también: cargar stock en Discovery sin que la producción se decida mirando pedidos no baja los recortes (supuesto 5 de la sección 4). Por eso la recomendación incluye el rediseño de la sección 3, no solo la herramienta.

La hipótesis del piloto, con la plantilla de la Clase 7: creemos que una planilla compartida con el stock de papas fritas, la carga diaria de producción y la reserva por pedido confirmado resolverá los recortes de ese producto para oficina y producción, y sabremos que funciona cuando la carga se sostenga todos los días y los pedidos completos y a tiempo de papas fritas mejoren. Es un MVP funcional, en pequeño. Nos falta la línea de base de ese producto: [dato pendiente: pedidos de papas fritas recortados o demorados en la semana de registro]. Si no se consigue, se mide una semana antes de arrancar.

### Qué decide el Go/No-Go

El piloto contesta dos preguntas. Una, si producción y oficina sostienen la carga y la reserva con la planta saturada (supuesto 2). Otra, y es la que decide si el proyecto vale la pena, si planificar contra pedidos baja los recortes que atribuimos a mezcla y momento (supuesto 1). Si la respuesta es no, B no se gasta: el problema es de organización o de capacidad, y una herramienta mejor no lo arregla. Los umbrales y el criterio de decisión están en la sección 7, y el lugar de la decisión en el roadmap de la sección 8.

### Qué tipo de inversión es

Según la clase del 19-10, una inversión puede ser obligatoria, de beneficio medible o estratégica. B no es obligatoria: ninguna ley ni ningún cliente la exigen. Tampoco la tratamos como estratégica: no abre un negocio nuevo. Es de **beneficio medible**: el ahorro principal se puede ver en la liquidación de sueldos, que ya existe. Por eso corresponde pedirle retorno, y el dueño ya dijo que lo acepta si se demuestra.

### El retorno, como punto de equilibrio

Para un VAN o una TIR faltan cifras que no tenemos, y no las inventamos. Hacemos la cuenta de la sección 4, con dos variables. **B se paga si evita, por mes, al menos tantas horas extras como dé este cociente:** [dato pendiente: costo mensual de la alternativa B] dividido [dato pendiente: costo por hora extra]. Los gastos que se pagan una sola vez, como el conteo inicial y la capacitación, se reparten en los 6 meses del plazo y se suman al costo mensual.

Cómo se lee, para que sirva cuando estén los datos:

- **El tope son las ~25 horas extras por mes de hoy**, y la meta de la sección 1 es la mitad, que vale solo si se cumple el supuesto 7. Si ese cociente, dividido por las ~25 horas, da menos de la mitad, B se paga aun con la meta de la sección 1.
- **No contamos el margen de los pedidos que dejan de recortarse.** Falta [dato pendiente: margen o valor promedio de un pedido recortado]. La prueba es conservadora: si B se paga solo con horas extras, se paga con más razón sumando ese margen.
- **A casi no tiene costo en plata**, así que no necesita punto de equilibrio. Su costo es tiempo de carga, y el piloto lo va a medir. Es un quick win en el sentido de la clase: bajo esfuerzo y aprende rápido.
- **Do Nothing es la base de la comparación.** Lo que B evita es el costo de seguir igual.
- **Qué recupero es aceptable lo decide el dueño.**

### Qué podría cambiar la recomendación

- **Si el módulo de Discovery no funciona como esperamos** (supuesto 3: reserva, factura que la consume, versión), la solución sigue siendo A, con sus controles, antes que pasar a C. Es peor en integración, pero es lo que ya se probó.
- **Si el piloto no baja los recortes**, la causa es más de capacidad que de mezcla, y la meta de la sección 1 se revisa. Lo que quedaría es un problema de planta, fuera de alcance.
- **Si la carga no se sostiene en el piloto**, se frena antes de gastar en B. Es un problema del cambio de trabajo, no de la herramienta.

**Fuentes:** relevamiento del proceso con nuestro compañero que trabaja en Dulxelitos; Parte 1 (madurez, VPC y canvas) y secciones 1 y 4 de esta parte; clases del 05-10 (descubrimiento de procesos, SIPOC, RECI y proceso balde), Clase 6 (modelado BPMN), Clase 7 y clase del 19-10 (tres lentes, priorización, MVP y tipos de inversión). Las cifras son las de la sección 1: 30 de ~125 pedidos por semana, 76 % completos y a tiempo como cuenta nuestra, ~25 horas extras por mes y carga de producción en el 20 % de los días. Los puntajes y las ponderaciones son nuestro juicio. Lo que no se sabe queda marcado como "dato pendiente".
