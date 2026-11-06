---
lang: es
---
<div class="portada">

<p class="p-titulo">Trabajo Práctico Final - Parte 2</p>
<p class="p-sub">Propuesta de transformación de Dulxelitos</p>
<p class="p-materia">Gestión Gerencial</p>
<p class="p-carrera">Ingeniería en Sistemas de Información</p>
<p class="p-equipo">Integrantes: Lepez Joaquín, Geyer Juan José, Lopez Juan, Olivares Manuel, Sorato Emiliano</p>
<p class="p-docente">Docentes: Ing. Jeremías Pino, Ing. Martín Noguerol</p>

</div>

---

# Índice

- Introducción
- 1\. Problema gerencial, objetivos y alcance
- 2\. Proceso actual y alternativas de solución
- 3\. Proceso futuro (TO-BE)
- 4\. Modelo de negocio y propuesta de valor
- 5\. Stakeholders del proyecto de mejora
- 6\. Arquitectura conceptual y flujo de datos
- 7\. Validación de supuestos
- 8\. Roadmap, OKR e indicadores
- 9\. Bibliografía
- 10\. Anexos

---

# Introducción

Este trabajo es la segunda parte del proyecto integrador de Gestión Gerencial. En la primera hicimos un diagnóstico gerencial de Dulxelitos, una empresa familiar de San Rafael que fabrica, fracciona y distribuye snacks desde 1973. En esta pasamos de diagnosticar a proponer: definimos el problema gerencial que la Parte 1 había dejado pendiente, mapeamos el proceso actual y el futuro, comparamos alternativas y armamos el plan para llevar la mejora a la práctica y medir si funciona.

Seguimos sobre el mismo caso, pero al relevar de nuevo el proceso de atender un pedido encontramos que tres cosas de la Parte 1 estaban mal o incompletas: el stock de producto terminado no se registra, los pedidos recortados son semanales y esos recortes vendrían de la mezcla y el momento de producción más que de la capacidad total de la planta. La corrección está al comienzo de la sección 1, y lo que sigue se apoya en la versión corregida.

El documento va del problema a la forma de medirlo: la sección 1 plantea el problema, los objetivos y el alcance; la 2 y la 3 describen el proceso actual y el futuro, con las alternativas y la recomendación; la 4, la 5 y la 6 revisan el modelo de negocio, a las personas y la arquitectura de datos; y la 7 y la 8 explican cómo se valida con un piloto y cómo se mide con el roadmap, el OKR y los indicadores. Lo que no sabemos queda marcado como «dato pendiente» y se junta en el Anexo I.

---

# 1. Problema gerencial, objetivos y alcance

Esta sección cierra dos pendientes de la Parte 1: el problema gerencial priorizado, que dijimos que íbamos a presentar por separado, y una corrección, porque al relevar el proceso para esta parte encontramos que varias cosas del diagnóstico no eran del todo ciertas. Empezamos por la corrección, porque lo que sigue se apoya en la versión corregida.

## 1.1 Lo que corrige el relevamiento

Para la Parte 2 relevamos de nuevo el proceso de atender un pedido de distribuidor con nuestro compañero que trabaja en Dulxelitos, y eso corrige tres cosas de la Parte 1. Nos pasó lo mismo que con el catálogo web de la Parte 1, pero esta vez lo que se corrige es el diagnóstico nuestro.

**El stock de producto terminado no se registra.** En la sección 5.2 de la Parte 1 pusimos "Facturación y stock sí" como proceso digitalizado y "Facturación, stock y cuentas corrientes en el sistema" como nivel de automatización; la 5.4 lo repite. La facturación sí está en Discovery y eso se mantiene. El stock de producto terminado no: no se lleva ni en Discovery ni en ningún otro registro. Para saber si hay mercadería se mira a ojo en el depósito y se le pregunta a producción, que lleva su propio control, lo carga una vez por semana y no se relaciona con las ventas. El módulo de stock de Discovery está dentro de la licencia y no se usa.

**Los pedidos recortados no son raros, pasan todas las semanas.** En la sección 5.5 escribimos que los pedidos incompletos "son poco frecuentes y se resuelven fácil". En una semana de registro, 30 de los ~125 pedidos (25 por día durante 5 días) salieron recortados o demorados: un ~24 %, o un ~76 % de pedidos completos y a tiempo, cuenta nuestra sobre una sola semana y no un promedio anual. Esa semana contó pedidos recortados o demorados; si incluyó rechazados de entrada, no se registró: [dato pendiente: si la semana base incluyó rechazados de entrada].

**Los recortes vendrían de la mezcla y el momento más que de la capacidad total de la planta.** En la sección 2.1 atribuimos los faltantes de papas fritas a "la capacidad de planta". La planta sigue saturada y eso no se corrige: las horas extras que la tapan siguen ahí, al menos en parte. Pero los recortes semanales vendrían sobre todo de la mezcla y el momento (supuesto 1): se produce lo que no hace falta y falta lo que se pide, porque la producción la deciden el dueño o los hijos por criterio propio, sin mirar los pedidos. Es un supuesto crítico y lo vamos a medir en el piloto, no lo damos por probado.

Las tres correcciones no cambian el diagnóstico de fondo, lo refuerzan (el costo de no actuar "no está bajo, está sin observar": ni el stock ni los recortes se registraban). Lo que sí toca son dos puntajes de la Parte 1: automatización (sección 5.2, Tecnología y Datos) y digitalización de los procesos clave (Procesos y Operaciones) tienen un 3 apoyado en parte en la afirmación equivocada del stock, y la 5.4 la repite. Con la corrección esos dos ítems saldrían más bajos, pero el nivel global seguiría siendo Inicial (1.0 a 1.9; el nuestro era 1.79). No volvemos a puntuar la encuesta: dejamos la Parte 1 como se entregó y marcamos los dos ítems sobreestimados.

## 1.2 Problema gerencial

Es la sección 6 de la Parte 1, que quedó pendiente. Sigue la plantilla de la Clase 3: dolor, causa raíz, magnitud y métrica de éxito, en no más de 60 palabras y sin nombrar ninguna herramienta, porque la solución se elige recién en la sección 2 de esta parte.

> Dulxelitos recorta o demora 30 de ~125 pedidos semanales porque los acepta sin conocer el stock de producto terminado, que no se registra, y decide la producción sin mirar las ventas. Genera faltantes y parte de las ~25 horas extras mensuales sobre una planta saturada. Éxito: pedidos completos y a tiempo del 76 % al 90 % en 6 meses.

Dos aclaraciones sobre el bloque. La causa raíz es técnica y de organización a la vez: no hay un registro del stock de producto terminado (lo técnico), y los pedidos se aceptan y la producción se decide sin mirarse entre sí, con el criterio del dueño o de los hijos (lo social). "A tiempo" quiere decir dentro del plazo estándar de cada zona (en la Patagonia, hasta una semana), y un pedido que se rechaza o se reprograma de entrada para que el número cierre no cuenta como completo.

**Por qué 90 % y no 100 %.** La meta es nuestra, no un dato de la empresa. Si la mezcla y el momento de producción son la causa principal, planificar contra pedidos ataca esa causa y justifica prometer una baja real; pero es una pyme con la planta saturada y siempre va a haber roturas e imprevistos. Un 90 % deja un 10 % de margen (100 menos 90) y es una meta que el equipo puede sostener. Si el piloto muestra que la mezcla explica menos de lo que suponemos, la meta se revisa.

## 1.3 Objetivo general

Que cada pedido de distribuidor se confirme sabiendo qué hay en stock de producto terminado, y que la producción se planifique contra los pedidos pendientes, para llevar los pedidos completos y a tiempo del 76 % al 90 % en un plazo de 6 meses.

Según lo que pide el enunciado:

- **Problema abordado:** recortes y demoras semanales por aceptar pedidos sin conocer el stock y producir sin mirar las ventas.
- **Resultado esperado:** pedidos completos y a tiempo del 76 % al 90 %.
- **Proceso y capacidad alcanzados:** el proceso "Atender pedido de distribuidor", de la recepción al despacho, y la planificación semanal de producción. La capacidad nueva es saber qué hay y qué falta antes de comprometer un pedido.
- **Plazo:** 6 meses. Se puede arrancar en cualquier momento, porque la demanda es pareja todo el año.

## 1.4 Objetivos específicos

Son tres. Cada uno tiene una métrica que la empresa puede obtener, una línea de base, una meta y un plazo. Las líneas de base salen de los datos del relevamiento; no inventamos ninguna.

**1. Que los pedidos se confirmen sabiendo qué hay en stock.**

- **Métrica:** pedidos completos y a tiempo sobre pedidos recibidos, por semana.
- **Línea de base:** 76 % (30 recortados o demorados de ~125, en una semana de registro; cuenta nuestra).
- **Meta:** 90 %.
- **Plazo:** 6 meses.

**2. Que la producción se cargue todos los días.**

- **Métrica:** días hábiles con producción cargada sobre días hábiles.
- **Línea de base:** 20 % (hoy se carga 1 vez por semana, o sea 1 de 5 días hábiles).
- **Meta:** 100 % de los días hábiles.
- **Plazo:** dentro de los 6 meses. La primera prueba es un piloto de 2 semanas con papas fritas (de la línea Salados), el producto que más falta.

**3. Que bajen las horas extras.**

- **Métrica:** horas extras totales por mes, de la liquidación de sueldos.
- **Línea de base:** ~25 horas por mes.
- **Meta:** la mitad, unas 12 o 13 horas por mes (25 dividido 2). Es un supuesto de meta nuestro, a confirmar con el dueño, y se apoya en otro: que al menos la mitad de las ~25 horas se hace para completar pedidos que faltaron por mezcla y momento de producción; la parte que cubre la saturación estructural no baja. La liquidación no distingue una de otra, así que la meta puede quedar corta o larga hasta que el piloto lo muestre.
- **Plazo:** 6 meses.
- **De dónde sale:** de la liquidación de sueldos, que la empresa ya tiene. Falta el costo de la hora extra para llevarlo a pesos: [dato pendiente: costo por hora extra].

Hay un cuarto indicador, la **exactitud de stock**, que no es un objetivo sino la condición de los otros tres: si lo cargado no coincide con el conteo físico semanal, ninguno se sostiene. Su línea de base sale del primer conteo físico: [dato pendiente: exactitud de stock en el conteo inicial]. La meta provisional es que al menos 9 de cada 10 productos queden sin diferencia mayor a la tolerancia de la sección 7, en 6 meses (propuesta nuestra, a confirmar con ese conteo). Las fichas de los cuatro indicadores están en la sección 8.

## 1.5 Alcance

**Proceso.** "Atender pedido de distribuidor": empieza cuando llega el pedido por WhatsApp o teléfono y termina con el pedido facturado en Discovery y despachado. Incluye además la planificación semanal de producción contra pedidos, y los indicadores con su rutina de seguimiento.

**Áreas y actores.** Oficina, depósito, producción y dirección (el dueño y los hijos). El dueño es el sponsor, que aprueba el presupuesto y los Go/No-Go; el líder es el responsable de sistemas, a quien la propuesta le asigna formalmente la gobernanza que en la Parte 1 le faltaba. Los distribuidores y el transporte tercerizado no cambian su trabajo: siguen pidiendo por WhatsApp o teléfono y, si falta algo, se les avisa en el momento, con fecha estimada si Producción ya la confirmó. Los pedidos de Aiello, del viajante y de retiro en fábrica entran por Oficina y se cargan con reserva como cualquier nota de pedido; cómo llegan hoy no lo relevamos: [dato pendiente: cómo entran hoy los pedidos de Aiello y del viajante].

**Cambios de trabajo incluidos.** Producción carga lo producido todos los días, al cierre de cada turno ([dato pendiente: cuántos turnos tiene la planta]); Oficina consulta el stock y lo reserva antes de confirmar un pedido; Dirección planifica la producción de la semana mirando los pedidos pendientes y un stock mínimo por producto; y hay una reunión corta diaria entre ventas y producción (~10 minutos) y un conteo cíclico semanal.

**Capacidades, datos y herramientas requeridas.**

- **Capacidades:** disciplina de carga diaria, un responsable de carga por turno con suplente y un criterio único de stock disponible.
- **Datos:** stock físico de producto terminado, reservas por pedido confirmado sin facturar, pedidos pendientes, stock mínimo y horas extras, con un solo criterio: **stock disponible = stock físico menos lo reservado por pedidos confirmados sin facturar.**
- **Herramientas:** Discovery, que ya tiene la empresa, para facturar y para el módulo de stock, pedidos y reserva que hoy no se usa; y una planilla compartida para el piloto de 2 semanas. Cuál va como solución y cuál como prueba se fundamenta en la sección 2.

## 1.6 Fuera de alcance

Dejamos afuera lo que no es necesario para el problema, y decimos por qué.

- **Insumos y packaging.** También tienen problemas, pero son otro problema. Quedan declarados como deuda; el proveedor único de film ya figura como riesgo en la Parte 1.
- **Visibilidad de stock para el distribuidor.** Por ahora el stock es solo interno. Va al roadmap como "later", junto con la tienda online de 2020.
- **Ampliación de planta.** La saturación sigue. Lo que atacamos es la mezcla y el momento de producción, no la capacidad total.
- **Cambiar Discovery por otro sistema.** Un SaaS de gestión lo evaluamos y lo descartamos en la sección 2 de esta parte.
- **CRM.** Es un problema real de la Parte 1 (Clientes y Canales), pero no es este.
- **Costeo y listas de precios.** Tampoco se tocan en esta propuesta.

**Se queda manual a propósito.** No todo conviene digitalizarlo ahora. El armado del pedido en el depósito se queda como está: según el relevamiento es rápido y no se mide, así que no es la restricción. El conteo físico sigue siendo a mano. Y la decisión de qué producir sigue siendo del dueño y de los hijos, que ahora la toman mirando pedidos y stock. Digitalizar sin rediseñar no mejora el tiempo de ciclo.

---

# 2. Proceso actual y alternativas de solución

Esta sección describe cómo se atiende hoy un pedido de distribuidor, qué encuentran en él las tres lentes de la Clase 7 y qué alternativas hay, incluida la de no hacer nada. El proceso, los volúmenes y los datos salen del relevamiento con nuestro compañero que trabaja en Dulxelitos; el RECI, las lentes y los puntajes son nuestro juicio, y lo que no sabemos queda como "dato pendiente".

## 2.1 Matriz de descubrimiento

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

Mapeamos el camino feliz, pero dibujamos el faltante completo porque pasa todas las semanas. La decisión de qué producir corre aparte; la dibujamos igual porque su desconexión de los pedidos es parte del problema.

## 2.2 SIPOC

Tiene seis pasos: cinco del camino feliz y el cuarto, alternativo, que en Dulxelitos ocurre todas las semanas.

| # | Proveedor | Entrada | Proceso | Salida | Cliente |
|---|---|---|---|---|---|
| 1 | Distribuidor (externo) | Pedido por WhatsApp o teléfono: productos, cantidades, zona | Recibir pedido | Pedido anotado en papel o planilla | Oficina (paso 2) |
| 2 | Depósito y Producción | Pedido anotado; lo que se ve a ojo en el depósito; lo que contesta producción | Verificar disponibilidad | Disponibilidad conocida y pedido pasado a la lista | Depósito (paso 3) |
| 3 | Oficina (la lista) y Producción (producto terminado) | Lista de pedidos y producto terminado | Preparar pedido | Pedido armado, completo o con faltante | Oficina (pasos 4 y 5) |
| 4 | Depósito y Producción | Faltante detectado al armar | Resolver faltante (solo si falta producto) | Aviso al distribuidor, o producto producido con o sin horas extras | Distribuidor y Oficina |
| 5 | Depósito | Pedido armado o ya completado | Facturar pedido | Pedido facturado en Discovery | Distribuidor y Depósito (paso 6) |
| 6 | Oficina | Pedido facturado | Despachar pedido | Pedido despachado | Distribuidor y transporte tercerizado (externo, si se terceriza) |

En el paso 2 la información viene de personas y no de registros, y ningún paso lee ni actualiza un stock registrado.

## 2.3 RECI

**R** es el responsable, el que responde por el resultado (uno solo por actividad); **E**, el ejecutor; **C**, el consultado; **I**, el informado. En una pyme quien ejecuta suele ser quien responde, por eso todas las filas son R/E. Las columnas son las lanes del diagrama y dos actores externos, que solo aparecen como informados.

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

\* Supuesto nuestro, a confirmar: como la producción la deciden el dueño o los hijos, leemos que producir de más o con horas extras se consulta con Dirección.

- **"Preguntar disponibilidad a producción".** Oficina la ejecuta y responde por ella; Producción es la consultada (C), y es una pregunta a una persona, no a un registro.
- **"Decidir producción" no tiene a nadie consultado.** Ni Oficina ni Depósito, que son los que conocen los pedidos.
- **El faltante no tiene un dueño relevado.** La compuerta "¿Qué se hace con el faltante?" no es una actividad: alguien decide entre mandar incompleto, esperar producción o hacer horas extras. El diagrama la dibuja en Oficina, pero no relevamos quién decide ni quién autoriza las horas extras: [dato pendiente: quién decide qué se hace con el faltante y quién autoriza las horas extras].
- **Rol y persona no coinciden en Dirección.** Hay una sola R, pero decide el dueño o uno de los hijos y no está definido cuál responde.

## 2.4 Diagrama AS-IS

![Proceso AS-IS](../bpmn/as-is.png)

**Cómo se lee.** El pedido nace en el mensaje del distribuidor. Oficina lo anota y, en paralelo, pregunta a producción mientras depósito mira el stock a ojo; con las dos respuestas pasa el pedido a la lista y Depósito lo prepara. Si no falta nada, se factura en Discovery y se despacha con flota propia o con transporte tercerizado. "¿Falta producto?" viene después de preparar el pedido, porque la averiguación previa no alcanza para saberlo; hay tres salidas (mandar incompleto avisando, esperar producción o producir con horas extras) que se juntan antes de facturar, y la compuerta está dibujada en Oficina, donde se avisa al distribuidor. El archivo `Proceso AS-IS - Dulxelitos.bpmn` se entrega aparte y abre en Bizagi o Camunda.

En los carriles de abajo, cada semana el dueño o uno de los hijos decide qué producir por criterio propio, sin mirar los pedidos, y Producción produce y registra la semana una sola vez (el 20 % de los días hábiles) sin cruzarla con las ventas. No hay ningún paso de consultar o reservar un stock registrado: es el proceso de quien acepta pedidos sin saber qué hay y produce sin saber qué se pidió.

| Aspecto | Hoy |
|---|---|
| **Actores y pasos** | Las 4 lanes y los 2 externos; 14 actividades: 11 del pedido y 3 de producción, que corre aparte |
| **Entradas** | Pedido por WhatsApp o teléfono; lo que se ve a ojo y lo que contesta producción; la decisión de producción del dueño o los hijos |
| **Salidas** | Pedido facturado y despachado; aviso de pedido incompleto; registro semanal de producción |
| **Herramientas** | WhatsApp y teléfono; papel o planilla; una lista de pedidos; Discovery, solo para facturar; el control propio de producción, que se carga una vez por semana |
| **Dolores** | Pedidos recortados o demorados todas las semanas; faltantes que aparecen al armar; horas extras; producción que no mira los pedidos |
| **Costos** | ~25 horas extras por mes, en parte para completar pedidos. En pesos: [dato pendiente: costo por hora extra]. Margen perdido en pedidos recortados: [dato pendiente: margen o valor promedio de un pedido recortado] |
| **Indicadores y línea de base** | Pedidos completos y a tiempo: 76 % (cuenta nuestra sobre una semana). Días con producción cargada: 20 %. Horas extras: ~25 por mes. Exactitud de stock: no existe porque no hay stock registrado; sale del primer conteo [dato pendiente: exactitud de stock en el conteo inicial] |
| **Lo que no es el problema** | El armado del pedido: según el relevamiento es rápido y no se mide, así que no es la restricción |

**Dependencias informales.** El proceso funciona porque la gente se acuerda de cosas que no están escritas:

- **WhatsApp, teléfono y papel.** El pedido original vive en el chat o en la llamada; lo que queda en el papel, la planilla de quien atiende y la lista son copias a mano que nadie más ve.
- **Preguntar a producción y mirar a ojo.** La disponibilidad depende de lo que sepa y conteste una persona y de la vista de quien está en el depósito; no queda registro.
- **El criterio del dueño y los hijos.** Qué producir se decide por experiencia, sin pedidos ni stock a la vista.
- **El faltante y las horas extras.** Funciona de hecho; cómo se decide no está relevado (ver RECI).
- **El control propio de producción.** Se carga una vez por semana y no está vinculado a ventas.

## 2.5 Tres lentes

**Lente 1: ineficiencias.** La disponibilidad se averigua dos veces, preguntando a producción y mirando a ojo, porque ninguna alcanza sola; además, cuando falta producto el pedido espera producción u horas extras antes de facturarse. No se arregla con un workflow: la intervención es un rediseño, reservar el stock contra pedidos antes de confirmar.

**Lente 2: tareas manuales.** El mismo pedido se transcribe tres veces: queda en el chat, se copia al papel o planilla y se vuelve a copiar a la lista, y cada copia a mano es un punto donde se puede equivocar un producto o una cantidad. La intervención es cargar el pedido una sola vez y que de ahí salgan la reserva y la lista de armado: un único registro, no el mismo papel en pantalla.

**Lente 3: flujo de datos.** Producción, depósito y ventas no comparten ningún dato: no hay stock de producto terminado registrado y lo producido se carga una vez por semana en un control propio que no se cruza con los pedidos. Es el silo más grande. La intervención es un registro de stock cargado todos los días, con un solo criterio de stock disponible: stock físico menos lo reservado por pedidos confirmados sin facturar.

**Cuál va primero.** Las tres lentes no dan tres proyectos sino una sola causa vista desde tres lados, así que no ordenamos iniciativas con impacto-esfuerzo ni con RICE (que, como dijo la clase, no decide: fuerza la discusión): ordenamos los pasos de una, primero un quick win (la planilla del piloto) y después la inversión de impacto alto (el stock en Discovery).

**La pregunta del proceso balde.** La clase del 05-10 pidió preguntar, antes de mejorar, si el proceso aporta valor al cliente final o solo contiene un error anterior (la paradoja de la gotera). "Atender pedido de distribuidor" sí aporta valor, pero tiene baldes adentro. La gotera es doble: no se registra el stock y se produce sin mirar los pedidos. Los baldes son la doble averiguación, el aviso de faltante y las horas extras para completar pedidos; la parte de las horas extras que tapa la saturación de la planta no es balde sino capacidad, y está fuera de alcance.

## 2.6 Alternativas

El enunciado pide una mejora incremental y de bajo costo (A), una intermedia que configure una herramienta existente (B) y una integral solo si el caso la justifica (C). No la justifica: queda como evaluada y descartada.

**Do Nothing: seguir igual.**

- **Costo y alcance.** No hay inversión; el costo es seguir igual: las ~25 horas extras por mes (en parte), los pedidos recortados o demorados todas las semanas y un margen perdido que hoy no podemos poner en pesos. La Parte 1 dijo que el costo de no actuar "no está bajo, está sin observar"; ahora sabemos por qué (corrección de la sección 1): ni el stock ni los recortes se registraban. No resuelve nada, y la planta sigue dependiendo de la memoria del dueño, de los hijos y de quien mira a ojo.

**A. Planilla compartida (incremental).**

- **Qué es y costo.** Una planilla compartida de stock de producto terminado: Producción carga lo producido al cierre de cada turno, Oficina reserva por pedido confirmado y hay una reunión diaria corta entre ventas y producción (~10 minutos), con el mismo criterio de stock disponible que B (sección 3). Casi cero en plata: la planilla y el tiempo de carga, de reunión y del conteo inicial. Se prueba como piloto de 2 semanas con papas fritas, el producto que más falta.
- **Qué resuelve.** Hace visible un stock que hoy no existe y permite probar con poco riesgo que producción y oficina sostienen la carga diaria (supuesto 2 de la sección 4) y que planificar contra pedidos baja los recortes (supuesto 1).
- **Qué no resuelve.** No se conecta con Discovery: al facturar se baja el físico y se descuenta la reserva a mano, y el pedido se carga dos veces. Vive en un archivo suelto que depende de quien lo carga, escala mal a todos los productos y no cambia por sí sola cómo se decide qué producir.

**B. Stock de Discovery (intermedia, recomendada).**

- **Qué es y costo.** Activar el módulo de stock de Discovery, que según el relevamiento está dentro de la licencia, permite pedidos y reserva, y la empresa no usó. Conteo físico inicial y activación línea por línea (Salados, Dulces y Repostería), con el mismo criterio y la misma rutina que A, más un responsable de carga por turno con suplente y conteo cíclico semanal. Sin licencia nueva: cuesta el conteo inicial, la capacitación, el tiempo de carga y [dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación], repartido en los 6 meses del plazo.
- **Qué resuelve.** Un solo registro de stock en la herramienta donde ya se factura, con el pedido cargado una vez y la reserva consumida por la factura (si el módulo funciona como esperamos: supuesto 3). Ataca la causa común de las tres lentes.
- **Qué no resuelve.** Que la producción se decida mirando pedidos (es un cambio de criterio de Dirección, no de herramienta), la saturación de la planta, los insumos y packaging, ni la visibilidad para el distribuidor ("later"). Tiene además un riesgo propio: la Parte 1 describió a Discovery como desactualizado y con errores, y la versión y el soporte incluidos son [dato pendiente: versión de Discovery y soporte incluido].

**C. SaaS de gestión (integral, evaluada y descartada).**

- **Qué es y costo.** Un sistema de gestión en la nube para pedidos y stock, que conviviera con Discovery o lo reemplazara: cuota mensual nueva, migración, capacitación y, si Discovery sigue para facturar, su costo también. No pedimos cotizaciones: la evaluamos como categoría, y los otros motivos alcanzan para descartarla.
- **Qué resuelve y qué no.** En teoría, pedido y stock en un solo lugar y mejor escala. No resuelve la disciplina de carga: si el equipo no sostiene una carga diaria en una planilla simple, tampoco la sostendrá en un sistema más grande. Según la Parte 1, Discovery no se integra con otros sistemas, así que el SaaS quedaría al lado con carga manual en los dos. Reemplazar Discovery está fuera de alcance (sección 1).

## 2.7 Matriz multicriterio

Usa los diez criterios del enunciado y compara cada alternativa como **solución para los 6 meses y para todos los productos**, no como piloto. La escala va de 1 a 5 y **5 siempre es lo más favorable para la empresa** (en costo, tiempo y complejidad, lo más barato, rápido y simple). Los puntajes son nuestro juicio, no una medición.

| Criterio (qué miramos) | Do Nothing | A. Planilla compartida | B. Stock de Discovery | C. SaaS |
|---|---|---|---|---|
| **1. Alineación al negocio** (¿ataca la causa: pedidos aceptados sin saber qué hay y producción sin mirar pedidos?) | **1.** No toca la causa | **3.** Registra y reserva, pero al facturar se descuenta a mano y no cambia cómo se decide producir | **4.** Registra, reserva y factura en el mismo lugar; no llega a 5 porque producir mirando pedidos es un cambio de criterio | **3.** Cubre pedido y stock, pero no la disciplina de carga ni la decisión de producir |
| **2. Costo** (inversión y gasto recurrente; 5 es lo más barato) | **5.** No hay inversión | **5.** Casi cero: planilla y tiempo de carga y conteo | **4.** Sin licencia nueva; cuesta conteo, capacitación y [dato pendiente: costo de activar el módulo] | **2.** Cuota nueva, migración y capacitación, y se sigue pagando Discovery |
| **3. Viabilidad operativa** (¿se puede con una planta saturada, sin frenarla?) | **3.** Es lo de hoy, sostenido con horas extras | **3.** Chica con un producto; con todos, la carga doble pesa sobre una planta al límite | **3.** Una sola carga, pero exige carga diaria y reserva con la gente que hay, sobre un módulo que nadie usó | **2.** Migrar datos y capacitar a tres áreas con la planta al límite |
| **4. Tiempo** (rapidez hasta el primer efecto) | **1.** No hay efecto nunca | **5.** Se arma sin proveedor; el piloto dura 2 semanas | **3.** Hay que activar con el proveedor y contar línea por línea: [dato pendiente: plazo de activación del módulo] | **2.** Elegir, contratar, migrar y capacitar antes del primer efecto |
| **5. Adopción** (¿lo usan quienes tienen que usarlo?) | **5.** No le pide nada a nadie, y tampoco mejora | **3.** Formato familiar, pero trabajo nuevo y doble carga | **3.** La misma carga, una sola vez, en una herramienta vieja que nadie usó para esto | **2.** Pantallas nuevas y doble carga con Discovery |
| **6. Complejidad** (5 es lo más simple) | **5.** Ninguna | **3.** Simple de armar, pero reservar y descontar a mano se presta a errores | **3.** Hay que configurar pedido, reserva y consumo por factura; depende de la versión: [dato pendiente: versión de Discovery] | **1.** Dos sistemas que no se integran, más una migración |
| **7. Capacidad interna** (¿lo puede hacer la gente de la empresa?) | **5.** No hace falta nada | **4.** Lo arma el responsable de sistemas, sin proveedor; baja porque no conocemos su tiempo disponible | **3.** Depende de Buenos Aires Software y del tiempo del responsable de sistemas | **2.** Proveedor nuevo y dos sistemas para sostener |
| **8. Integración** (¿conecta pedido, stock y facturación?) | **1.** Nada se conecta | **2.** La planilla no habla con Discovery | **4.** Todo en Discovery; falta confirmar que la factura consume la reserva (supuesto 3) | **2.** Según la Parte 1, Discovery no se integra: carga manual entre los dos |
| **9. Flujo de caja** (cuánto sale y cuándo; 5 es poco y sin cuotas fijas nuevas) | **3.** No sale plata nueva, pero siguen las horas extras y se pierde margen | **5.** Casi nada, y se puede cortar sin perder inversión | **4.** Sin cuota nueva; gasto puntual, y el dueño acepta invertir si se demuestra el retorno | **2.** Cuota fija mensual en una empresa que cobra de contado, a ~30 días o con cheques diferidos (Parte 1) |
| **10. Continuidad operativa** (¿protege ventas y producción durante y después del cambio?) | **2.** Depende de la memoria del dueño, los hijos y quien mira a ojo | **3.** No corta nada y se revierte, pero es un archivo suelto | **4.** Una sola fuente en la herramienta de facturación, con suplente; riesgo: Discovery desactualizado (Parte 1) | **2.** Suma un proveedor y una migración sobre la operación |
| **Total (suma simple, máximo 50)** | **31** | **36** | **35** | **20** |

**Cómo leer la matriz.** C se descarta: tiene la suma más baja y no es la mejor en ningún criterio. Do Nothing suma 31 porque la suma premia lo fácil; se descarta por alineación 1 e integración 1, es decir, porque no resuelve el problema. A y B quedan casi empatadas, 36 contra 35, y un punto entre puntajes de juicio no es una diferencia.

Probamos pesos distintos después de ver el empate, así que no prueban nada (son post hoc): con alineación, integración y continuidad operativa más de ~1,25 veces más pesadas, B supera a A (empatan en 38); con más peso en costo, tiempo y flujo de caja, solo crece la ventaja de A. El empate es fino hacia los dos lados y la matriz no decide.

Decide el argumento cualitativo. Las notas bajas de A son estructurales: integración 2, alineación 3 y continuidad 3 salen de que la planilla vive aparte de Discovery, y no mejoran con la práctica. Las medias de B son incógnitas: viabilidad, tiempo, adopción, complejidad y capacidad interna valen 3 porque nadie usó ese módulo en Dulxelitos, y pueden subir o bajar cuando se sepa. Además el dueño aceptó invertir más si se demuestra el retorno, y por eso el costo pesa menos. Por eso A va primero, como paso 1 y MVP: el piloto con A, la prueba técnica y la activación por línea despejan las incógnitas de B, que es el destino.

## 2.8 Recomendación

**Recomendamos B, el stock de Discovery, con A, la planilla compartida, como piloto de 2 semanas sobre papas fritas.** B es la solución del proceso nuevo; A es el experimento que la prueba antes de gastar.

**Por qué en ese orden.** Si el equipo no sostiene la carga diaria en una planilla simple, tampoco la va a sostener en Discovery, y habríamos pagado una herramienta por un problema de disciplina. Y digitalizar sin rediseñar no acorta el tiempo de ciclo (la firma digital de planos de la clase del 19-10): cargar stock sin que la producción se decida mirando pedidos no baja los recortes (supuesto 5), por eso va con el rediseño de la sección 3. El piloto con A prueba la carga diaria y si planificar contra pedidos baja los recortes (supuestos 1 y 2); el supuesto 3 (que Discovery reserve y que la factura consuma la reserva) lo verifica la prueba técnica de la sección 7 antes del Go, salvo el paso de la factura si no hay ambiente de prueba, que queda para el primer pedido real de la activación. La hipótesis del piloto, sus umbrales y el Go/No-Go están en las secciones 7 y 8.

**Retorno.** B es una inversión de beneficio medible (clase del 19-10): el ahorro principal se ve en la liquidación de sueldos, y por eso se le pide retorno. Sin VAN porque faltan cifras (la sección 4 lo retoma): B se paga si evita por mes al menos [dato pendiente: costo mensual de la alternativa B] dividido [dato pendiente: costo por hora extra] horas extras, repartiendo lo que se paga una sola vez en los 6 meses. Si el cociente es menor a ~12,5 horas por mes (25 dividido 2, la meta de la sección 1), se paga con la meta. No contamos el margen de los pedidos que dejan de recortarse [dato pendiente: margen o valor promedio de un pedido recortado], así que la cuenta es conservadora. El punto de equilibrio compara B con no hacer nada, no con A: lo que B agrega sobre A es una sola carga que integra pedido, reserva y factura, y que escala a más de 25 combinaciones de producto y formato (Parte 1). Qué plazo de recupero es aceptable lo decide el dueño.

**Fuentes:** relevamiento del proceso; Parte 1; secciones 1 y 4 de esta parte; clases del 05-10, 19-10 y Clases 6 y 7. Los puntajes son nuestro juicio.

---

# 3. Proceso futuro (TO-BE)

Esta sección diseña cómo se atiende un pedido de distribuidor cuando la propuesta está andando: el proceso de la alternativa recomendada en la sección 2 (el stock de Discovery), probado antes con una planilla compartida en un piloto de 2 semanas con papas fritas, que corre este mismo flujo con la misma regla de stock; solo cambia dónde vive el registro. El proceso nuevo cambia el orden (primero se mira qué hay, después se confirma) y conecta la producción con los pedidos. Responsables, criterios y rutinas son propuesta nuestra, a acordar con cada área antes del piloto (sección 5).

## 3.1 Diagrama TO-BE

![Proceso TO-BE](../bpmn/to-be.png)

**Cómo se lee.** Usa los mismos carriles y actores externos que el AS-IS de la sección 2, para comparar de un vistazo; el muñequito marca los pasos que se hacen en Discovery. El archivo `Proceso TO-BE - Dulxelitos.bpmn` se entrega aparte y abre en Bizagi o Camunda. Los tres objetos "Stock en Discovery" son el mismo registro, repetido para no cruzar carriles (la flecha en la tarea es una lectura; en el objeto, una escritura). Cuatro cosas arrancan por su cuenta: el pedido, con el mensaje del distribuidor; la semana de producción, con el reloj de Dirección; la carga del día, con el cierre del turno; y el conteo, con el reloj de Depósito.

- **El pedido.** Oficina carga la nota de pedido una sola vez en Discovery y consulta el stock disponible antes de confirmar. Si hay, reserva (la reserva se escribe en el stock), confirma al distribuidor y Depósito arma desde la lista de armado que Discovery da para ese pedido confirmado (sección 6). Después Oficina factura en Discovery, y la factura consume la reserva. El despacho es como hoy.
- **Si no hay.** Oficina avisa en el momento, con una fecha estimada que Producción confirma en la reunión diaria; si todavía no la confirmó, avisa del faltante sin prometer fecha y se la da después de la próxima reunión. El pedido queda pendiente, sin reserva, y cuando llega la fecha Oficina vuelve a consultar. "Hay" quiere decir que alcanza para el pedido completo; si alcanza solo para una parte, se reserva esa parte y se despacha solo si el distribuidor lo acepta, y si no el pedido espera completo (sección 6). Si el distribuidor cancela después del aviso, el pedido cuenta como recortado (sección 7).
- **La producción.** Cada semana Dirección planifica leyendo los pedidos pendientes (los avisados con faltante entre ellos), el stock mínimo y el tablero, y Producción produce lo planificado. La carga es otra rutina, que arranca todos los días con el cierre del turno: Producción carga lo producido y eso sube el stock físico en Discovery (hoy se carga una vez por semana). En Repostería, que es producto de terceros que Dulxelitos solo envasa, lo que se carga es lo envasado.
- **El conteo.** Una vez por semana Depósito cuenta el stock; quién lo hace queda a confirmar ([dato pendiente: responsable del conteo inicial y del semanal]). Si hay diferencias, manda lo contado y el responsable de sistemas, que es un rol y no un área, carga el ajuste con motivo; por eso aparece en la nota del diagrama y no como un paso con carril propio.
- **Las notas.** La reunión diaria de ~10 minutos entre ventas y producción, el tablero de 4 indicadores (sección 8) y las horas extras como excepción decidida en el plan semanal.

**Lo que el diagrama da por cierto y no está probado.** Que Discovery reserva, que permite reservar solo una parte de un pedido y que la factura consume la reserva (supuesto 3 de la sección 4, que verifica la prueba técnica de la sección 7); que la fecha estimada se cumple (supuesto 4); y que el dueño y los hijos planifican mirando pedidos y stock mínimo (supuesto 5). En el piloto con planilla, al facturar se baja el físico y se descuenta la reserva a mano.

## 3.2 Qué cambia

| Paso | Hoy (AS-IS) | Futuro (TO-BE) |
|---|---|---|
| **Registrar el pedido** | Se anota en papel o planilla y se pasa a una lista: tres transcripciones del mismo pedido | Se carga una sola vez, como nota de pedido en Discovery, y de ahí sale la lista de armado |
| **Saber si hay, y cuándo aparece el faltante** | Se mira a ojo en el depósito y se pregunta a producción; el faltante aparece al armar el pedido, con el pedido ya aceptado | Una sola consulta del stock disponible en Discovery, antes de confirmar, en la compuerta "¿Hay stock disponible?" |
| **Qué se le dice al distribuidor y cómo se resuelve el faltante** | Se acepta con una averiguación que no alcanza; si falta, tres salidas: mandar incompleto avisando, esperar producción u horas extras | Se confirma lo que hay, con reserva; si falta, aviso en el momento, con la fecha que confirmó Producción (sin fecha si todavía no la confirmó), y el pedido queda pendiente hasta esa fecha, a la vista de Dirección en el plan semanal |
| **Qué se produce** | Lo decide el dueño o uno de los hijos por criterio propio, sin mirar los pedidos | Plan semanal contra pedidos pendientes y stock mínimo por producto; sigue decidiendo Dirección |
| **Cargar lo producido** | Una vez por semana (20 % de los días), en un control propio sin relación con ventas | Todos los días, al cierre del turno, en Discovery, con un responsable de carga por turno y suplente |
| **Horas extras** | Una de las tres salidas del faltante (~25 horas por mes) | Excepción que se decide en el plan semanal, con el motivo anotado |

**Lo que no cambia, a propósito.** El pedido sigue entrando por WhatsApp o teléfono; el armado en el depósito sigue siendo manual (según el relevamiento es rápido y no es la restricción); el despacho, con flota propia o transporte tercerizado, queda igual; qué producir lo sigue decidiendo el dueño o uno de los hijos, ahora con pedidos y stock a la vista; y el distribuidor no ve el stock: eso queda para "later" (sección 1).

### La regla del stock disponible

Es la misma en Discovery y en la planilla del piloto, y es la cifra con la que Oficina contesta al distribuidor:

**stock disponible = stock físico − reservado por pedidos confirmados sin facturar**

| Qué pasa | Stock físico | Reservado | Disponible |
|---|---|---|---|
| Producción carga lo producido al cierre del turno | Sube | Igual | Sube |
| Oficina reserva al confirmar un pedido | Igual | Sube | Baja |
| Oficina factura el pedido (consume la reserva) | Baja | Baja | Igual |
| Se libera una reserva (cancelación o pedido rehecho) | Igual | Baja | Sube |
| El conteo encuentra una diferencia | Se corrige a lo contado | Igual | Cambia con el físico |

Confirmar un pedido baja lo que se puede prometer sin tocar lo que hay, y recién la factura baja lo que hay; por eso el disponible no se mueve al facturar, ya se había descontado al reservar. Las reglas para cargar, corregir y depurar estos datos están en la sección 6.

## 3.3 Responsables y decisiones

Usamos el criterio del RECI de la sección 2: una sola R por actividad y, como en una pyme quien ejecuta suele ser quien responde, casi todas las filas son R/E. Agregamos al responsable de sistemas, que ejecuta dos pasos (los ajustes de stock y el tablero) y no tiene carril. Los asteriscos marcan propuestas nuestras que todavía no hablamos con cada área.

| Actividad | Oficina | Depósito | Producción | Dirección | Resp. de sistemas | Distribuidor (externo) |
|---|---|---|---|---|---|---|
| Cargar nota de pedido en Discovery | R/E | – | – | – | – | – |
| Consultar stock disponible | R/E | – | – | – | – | – |
| Reservar stock | R/E | – | – | – | – | – |
| Confirmar pedido al distribuidor | R/E | I | – | – | – | I |
| Avisar faltante con fecha estimada | R/E | – | C | – | – | I |
| Preparar pedido | I | R/E | – | – | – | – |
| Facturar en Discovery | R/E | C | – | – | – | I |
| Planificar producción de la semana | C* | – | C* | R/E | – | – |
| Producir lo planificado | I | I | R/E | I | – | – |
| Cargar producción del día | I | I | R/E | – | – | – |
| Contar stock | – | R/E (a confirmar) | I | – | I | – |
| Ajustar diferencias de conteo (nota del diagrama) | I | C | I | – | R/E | – |
| Reunión diaria ventas–producción* | C | – | C | R/E | – | – |
| Actualizar el tablero* | C | – | I | I | R/E | – |

Qué cambia en las responsabilidades respecto del AS-IS:

- **El faltante tiene dueño.** La sección 2 no relevó quién decide qué se hace con el faltante ni quién autoriza las horas extras. La propuesta: si el disponible no alcanza, Oficina avisa; la fecha la confirma Producción; las horas extras las decide Dirección en el plan semanal. Falta acordarlo con el dueño.
- **"Planificar" tiene consultados.** El AS-IS no tenía a nadie consultado en "Decidir producción"; ahora Oficina aporta los pedidos pendientes y Producción dice qué puede producir.
- **Hay cuatro cosas sin definir.** Cuál de los decisores responde por el plan semanal [dato pendiente: cuál responde por el plan semanal]; quién cuenta, porque proponemos a Depósito pero no relevamos quién lo haría, ni en el conteo inicial ni en el semanal [dato pendiente: responsable del conteo inicial y del semanal]; quién es el responsable de carga de cada turno y su suplente, porque una carga que depende de alguien que falta se corta [dato pendiente: quién es el responsable de carga de cada turno y su suplente]; y quién convoca la reunión diaria, que proponemos que sea Dirección [dato pendiente: quién convoca la reunión diaria y si participa el dueño o un hijo todos los días].

### Quién decide qué, y con qué dato

| Decisión | Quién | Con qué dato | Criterio |
|---|---|---|---|
| ¿Se confirma el pedido? | Oficina | Stock disponible, de Discovery | Si alcanza, se reserva y se confirma; si no, no se confirma sin avisar. No se confirma a ojo, salvo el día en que el dato no está al día (vuelta atrás, sección 7) |
| ¿Qué fecha se da? | Producción la confirma; Oficina la comunica | Plan semanal y producción en curso, vistos en la reunión diaria | Oficina no la inventa: si Producción todavía no la confirmó, avisa del faltante sin fecha y la da después de la próxima reunión diaria |
| ¿Qué se produce esta semana? | Dirección (dueño o hijos) | Pedidos pendientes, stock disponible frente al stock mínimo de cada producto, y el tablero | Primero lo pedido que no hay; después lo que está por debajo del mínimo. El criterio propio sigue contando, pero ya no es el único dato |
| ¿Cómo se corrige una diferencia de conteo? | Manda lo contado; el responsable de sistemas carga el ajuste | La hoja de conteo de Depósito | Se ajusta Discovery, con motivo, sin editar el stock a mano. Si un producto difiere semana tras semana, se trata en la reunión diaria |
| ¿Se libera una reserva? | Oficina, que la creó | Plazo estándar de la zona del distribuidor y su confirmación | La que pasó el plazo sin facturarse se confirma con el distribuidor y se factura o se libera |

## 3.4 Datos y controles

Hoy el dato del stock no se genera nunca. En el proceso nuevo se genera en cinco momentos, todos en Discovery: al recibir el pedido (la nota de pedido), al confirmarlo (la reserva), al cierre de cada turno (el parte de producción), al facturar (que baja el físico y consume la reserva) y en el conteo semanal (el ajuste). Quién carga cada dato y sus reglas de alta, corrección y depuración están en la sección 6.

### Controles

Cada control corresponde a un error que hoy no se detecta:

| Error de hoy | Control en el proceso nuevo | Cómo se ve si falla |
|---|---|---|
| Confirmar sin saber qué hay | Consultar el disponible es un paso del flujo, antes de confirmar | Días en que se confirmó a ojo porque el dato no estaba al día, que el piloto anota (sección 7) |
| Producir sin mirar los pedidos | Plan semanal con pedidos pendientes y stock mínimo, y reunión diaria | La reunión no cambia lo que se produce con pedidos sin cubrir (supuesto 5, sección 7) y el indicador de pedidos completos no sube |
| Stock cargado que no coincide con el real | Conteo cíclico semanal; manda lo contado | Exactitud de stock |
| Carga que se corta | Responsable de carga por turno con suplente, y carga al cierre del turno | Días con producción cargada |
| Reservas viejas que bajan el disponible sin motivo | Oficina revisa cada semana las reservas abiertas | Reservas abiertas en la revisión semanal (sección 6) |
| Horas extras como arreglo habitual | Excepción decidida en el plan semanal, con el motivo anotado | Horas extras por mes |

### Seguimiento simple

Son los cuatro instrumentos que pide la consigna, y caben en una pyme sin sumar un sistema.

**Tablero de 4 indicadores.** Una hoja simple que actualiza el responsable de sistemas cada semana, con la exportación de Discovery y dos cargas manuales (sección 6). La ficha, la fórmula y la meta de cada indicador, quién lo ve y cómo se lee están en la sección 8.

**Checklist.** Tres listas cortas, una por rutina:

*Cierre de turno (responsable de carga o suplente)*

- [ ] Cargué la cantidad realmente producida de cada producto, no la planificada ni la estimada.
- [ ] Si me equivoqué en una carga de hoy, la corregí el mismo día, con su motivo.
- [ ] Si no pude cargar, lo avisé para anotarlo en la reunión.

*Antes de confirmar un pedido (Oficina)*

- [ ] El pedido está cargado una sola vez, con el producto y el distribuidor elegidos de la lista.
- [ ] Consulté el stock disponible.
- [ ] Si alcanza, reservé antes de confirmar. Si no, avisé del faltante, con la fecha que confirmó Producción o, si todavía no la confirmó, sin fecha.

*Cada semana, un día fijo a acordar con Depósito (Depósito, Oficina y responsable de sistemas)*

- [ ] Depósito contó el stock y dejó la hoja de conteo. [dato pendiente: responsable del conteo inicial y del semanal]
- [ ] El responsable de sistemas cargó los ajustes, cada uno con su motivo.
- [ ] Oficina revisó las reservas abiertas: las que pasaron el plazo de su zona se confirmaron o se liberaron.
- [ ] Se actualizó el tablero.

**Responsable de carga.** Una persona por turno, con suplente, que responde porque lo producido llegue a Discovery al cierre. Es el control más importante: sin carga diaria no hay stock en el que confiar, y es trabajo nuevo para Producción (sección 5). El tiempo de carga se reserva dentro del turno.

**Reunión diaria ventas–producción.** Dura ~10 minutos y tiene tres preguntas: ¿qué hay y qué está pendiente?, ¿qué avisos hay abiertos y qué fecha confirma Producción?, ¿hay que mover lo que se produce? Termina con la fecha y la decisión de producción anotadas, y es el lugar donde se tratan las diferencias de conteo que se repiten y las reservas liberadas.

**Fuentes:** relevamiento del proceso y secciones 1, 2, 4, 5, 6 y 7 de esta parte. Los responsables, los criterios de decisión y las rutinas son propuesta nuestra, no datos de la empresa.

---

# 4. Modelo de negocio y propuesta de valor

Esta sección mira la propuesta desde afuera del proceso: qué cambia en el modelo de negocio de la Parte 1, qué le llega distinto al distribuidor y qué tenemos que creer para que funcione. Evalúa la solución recomendada, el stock de Discovery, probada antes con una planilla compartida. **El cambio es casi todo backstage:** lo que el distribuidor ve cambia poco, y lo que cambia es la forma de cumplir lo que ya prometía, coherente con la Parte 1, que encontró los problemas puertas adentro.

## 4.1 Cambios en el BMC

Los bloques son los del canvas AS-IS de la Parte 1. Los separamos en lo que ve el distribuidor (frontstage) y lo que pasa puertas adentro (backstage), que es como lo pide el enunciado.

### Frontstage: lo que ve el distribuidor

| Bloque | AS-IS (Parte 1, con la corrección) | TO-BE | ¿Cambia? |
|---|---|---|---|
| **Segmentos de clientes** | Distribuidores mayoristas, con foco en la Patagonia, y Aiello | Los mismos. El cambio no toca a quién se le vende | No |
| **Propuesta de valor** | Precio y logística para el canal. Lo más fuerte que tiene la empresa es que avisa cuando falta algo y no manda lo que no hay | La misma promesa, mejor cumplida: pedidos completos y a tiempo, y un aviso que llega antes | Se refuerza, no cambia |
| **Canales** | Los pedidos entran por WhatsApp y teléfono. La tienda del sitio sigue con el catálogo vacío desde 2020 | Iguales. Ver el stock desde afuera, o terminar la tienda, queda para "later" (explicación abajo) | No |
| **Relación con clientes** | El pedido se acepta sin mirar si hay mercadería. Si falta algo, el distribuidor se entera cuando se arma el pedido, y se le manda incompleto o se espera producción | Oficina confirma sabiendo qué hay y, si falta, avisa en el momento, con una fecha estimada si Producción ya la confirmó. El distribuidor sigue hablando con la misma gente por los mismos medios | **Sí, acotado** |
| **Fuentes de ingreso** | Venta mayorista, venta a Aiello y producto fraccionado. Cobran de contado, a ~30 días o con cheques diferidos | Misma estructura. Un pedido recortado o demorado es una venta parcial o tardía; cuánto vale eso es [dato pendiente: margen o valor promedio de un pedido recortado] | No |

**Por qué la tienda y el stock visible quedan para "later".** La Parte 1 dijo que terminar la tienda para que el distribuidor consulte stock era la iniciativa más barata, pero hoy no hay un stock confiable que mostrar: primero se mejora el registro y recién después se le enseña a un cliente.

### Backstage: lo que pasa puertas adentro

| Bloque | AS-IS (Parte 1, con la corrección) | TO-BE | ¿Cambia? |
|---|---|---|---|
| **Actividades clave** | El dueño o los hijos deciden qué producir por criterio propio. El pedido se anota en papel o planilla y se confirma mirando a ojo y preguntando a producción. La administración está repartida entre planillas y un sistema de gestión que no se hablan | Producción carga lo producido todos los días, al cierre de turno. Oficina consulta y reserva el stock antes de confirmar. Dirección planifica la semana con los pedidos pendientes y un stock mínimo por producto. Hay una reunión diaria de ~10 minutos entre ventas y producción y un conteo cíclico semanal. El armado y el despacho quedan como están | **Sí, es el cambio principal** |
| **Recursos clave** | La línea de producción al límite y el conocimiento concentrado en los dueños. El stock de producto terminado no existe como recurso, porque no se registra | Aparece un recurso nuevo: el registro del stock de producto terminado, con un solo criterio de stock disponible (sección 3) y una persona responsable de cargarlo en cada turno, con suplente. Usa el módulo de stock de Discovery, que ya está en la licencia. La planta sigue saturada | **Sí** |
| **Socios clave** | Proveedor único de packaging y film, proveedores de materia prima, transportistas, distribuidores y Aiello. El proveedor del sistema de gestión no figura | Los mismos. Con un detalle: el proveedor de Discovery pasa a contar, porque hay que activar y configurar un módulo que hoy no se usa. Insumos y packaging siguen fuera de alcance | Casi no |
| **Estructura de costos** | Materia prima, packaging, mano de obra, logística, energía y costo financiero. Las ~25 horas extras por mes están dentro de la mano de obra | Sin licencia nueva: el módulo ya está en la licencia que se paga, según nuestro compañero que trabaja en la empresa, y la planilla del piloto cuesta casi nada. Costos nuevos: tiempo de carga y de reunión, conteo inicial y capacitación, más [dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]. Ahorro buscado: menos horas extras; llevarlo a pesos necesita [dato pendiente: costo por hora extra] | **Sí, poco** |

### Cómo se lee el conjunto

De los nueve bloques, **cuatro cambian** (actividades y recursos a fondo; relación con clientes y costos de manera acotada), **dos cambian apenas** (la propuesta de valor, que se cumple mejor, y los socios, por el proveedor de Discovery) y **tres quedan igual** (segmentos, canales e ingresos). Solo uno de los cuatro que cambian lo ve el cliente, y de manera modesta: un aviso a tiempo.

No hay un modelo de negocio nuevo: Dulxelitos sigue siendo una empresa de volumen que vende al canal; cambia que sabe qué tiene y qué le falta antes de comprometerse. La saturación de la planta no se toca (la propuesta ataca la mezcla y el momento de producción, no la capacidad) y los ingresos no suben por diseño: solo se cumple mejor lo que ya se vende.

## 4.2 VPC TO-BE

El segmento es el mismo de la Parte 1: el distribuidor mayorista, mirando sobre todo al patagónico. Para cada dolor y cada ganancia de esa parte, qué hace la propuesta y qué no.

**Una corrección al VPC.** La Parte 1 ubicaba los faltantes de papas fritas "en algunas temporadas". Esta parte lo corrige: pasan todas las semanas, y en la semana registrada 30 de ~125 pedidos, de cualquier producto, salieron recortados o demorados. Las papas fritas siguen siendo lo que más falta, pero no lo único.

### Dolores

| Dolor del distribuidor (Parte 1) | Qué hace la propuesta | Efecto |
|---|---|---|
| **Faltantes** (en la Parte 1, sobre todo de papas fritas) | Planificar la producción contra pedidos pendientes y un stock mínimo ataca la causa que suponemos, la mezcla y el momento (supuesto 1). Si falta algo, se avisa al confirmar | **Lo alivia**, y es el dolor central. Depende del supuesto crítico de más abajo |
| **No poder saber si hay stock sin llamar o ir al depósito** | El distribuidor sigue llamando o escribiendo, pero la respuesta se apoya en el stock registrado: oficina consulta el stock disponible antes de contestar | **En parte.** Mejora la respuesta, no el autoservicio, que queda para "later" |
| **Horario acotado de atención** y **paquetes rotos en el viaje** | Nada: no se amplía el horario ni se abre un canal fuera de él, y el embalaje y el transporte están fuera de alcance | **No los toca** |

### Ganancias

| Lo que el distribuidor espera (Parte 1) | Qué hace la propuesta | Efecto |
|---|---|---|
| **Que le avisen cuando falta algo** | Hoy lo hace la empresa y es su punto más fuerte, pero se entera al armar el pedido. Pasa a avisarse en el momento, con una fecha estimada | **Se mantiene y mejora**: el aviso llega antes y trae una fecha |
| **Entrega previsible** (en la Patagonia, hasta una semana) | Un pedido confirmado se cumple completo y dentro del plazo estándar de la zona. Es el indicador principal: del 76 % a la meta de la sección 1 | **Mejora**, medida por pedidos completos y a tiempo |
| **Compromiso** | Confirmar un pedido pasa a significar que hay mercadería o una fecha estimada para completarlo | **Mejora** |
| **Precio, exclusividad territorial, catálogo amplio y formatos de reventa** | Nada: no se toca ninguno | Sin cambio |

### Qué beneficio nuevo aparece

Uno solo, y es chico: **saber con una fecha estimada cuándo llega lo que falta.** Hoy el distribuidor se entera de que falta algo y no sabe hasta cuándo; con producción planificada contra pedidos, la empresa puede darle una fecha. Es una promesa nueva sobre una planta saturada: si no se cumple, el aviso pierde el valor que hoy tiene (supuesto 4). No hay ningún beneficio digital nuevo, porque no hay canal nuevo. Como el distribuidor está conforme y no se queja (Parte 1), quien más gana es la empresa (menos reprogramaciones y horas extras, y un proceso que se puede medir), y hay que cuidar la relación con el canal, lo único que hoy anda bien.

## 4.3 Supuestos clave

Son las cosas que damos por ciertas y no hemos probado. Las ordenamos por tipo, como pide el enunciado: **deseabilidad** (¿lo quiere y lo va a usar quien tiene que usarlo?), **factibilidad** (¿se puede hacer en esta empresa?) y **viabilidad** (¿se paga?). El primero de la lista es el que más pesa.

| # | Supuesto | Tipo | Riesgo si es falso |
|---|---|---|---|
| 1 | **La mezcla y el momento de producción, y no la capacidad total de la planta, explican la mayoría de los recortes.** | **Factibilidad (crítico)** | Planificar contra pedidos no baja los recortes porque lo que falta es capacidad: la propuesta ataca el problema equivocado y la meta no se cumple |
| 2 | Producción carga lo producido todos los días, y oficina consulta y reserva antes de confirmar, aun con la planta saturada y sin gente de más. | Factibilidad | Sin carga diaria no hay stock en el que confiar: la exactitud cae y se vuelve a mirar a ojo. Es la resistencia que esperamos en producción y en oficina |
| 3 | El módulo de stock de Discovery funciona como esperamos: permite pedidos, reserva el stock (también una parte de un pedido) y la facturación consume la reserva, con el mismo criterio de stock disponible que la planilla del piloto. | Factibilidad | Nadie lo usó en Dulxelitos. Si no funciona así, hay que sumar costo y tiempo con el proveedor o seguir con la planilla compartida (alternativa A) |
| 4 | La fecha estimada que se le da al distribuidor cuando falta algo se cumple, con la planta saturada. | Factibilidad | Es una promesa nueva de cara al cliente: si la fecha falla, el aviso deja de ser confiable y se empeora justo lo que hoy anda bien |
| 5 | El dueño y los hijos van a decidir la producción de la semana mirando pedidos pendientes y stock mínimo, y no solo por criterio propio. | Deseabilidad | Se registra el stock pero la decisión no cambia: se digitaliza sin rediseñar y los recortes siguen. Es el cambio adaptativo del proyecto, no el técnico |
| 6 | Al distribuidor no le resulta peor oír una fecha estimada al confirmar que recibir el pedido recortado, como hoy. | Deseabilidad | Se pierden pedidos o se resiente una relación que hoy está bien; hoy el distribuidor no se queja, así que no hay señal previa de que quiera este cambio |
| 7 | Al menos la mitad de las ~25 horas extras por mes se hace para completar pedidos que faltaron por mezcla y momento de producción. | Viabilidad | Es la base de la meta de horas extras (sección 1). La liquidación no distingue una hora de otra: si la mayoría es por saturación estructural, que esta propuesta no toca, la meta queda larga y el ahorro es menor |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo de implementar y sostener el cambio, que esperamos bajo y se confirma cuando estén los datos de costo. | Viabilidad | La inversión no se recupera. Hoy no hay ninguna cifra de costo, así que "bajo" es una expectativa y no un dato |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa. | Viabilidad | El tamaño del problema, y de lo que se gana, es otro. Se apoya en que la demanda es pareja todo el año, pero es una sola semana |

**El supuesto 1 es el que decide si la propuesta vale la pena.** La planta está saturada (lo dijo la Parte 1 y no lo corregimos); lo que matizamos es que los recortes vendrían sobre todo de la mezcla y el momento: se produce lo que no hace falta y falta lo que se pide, porque la producción se decide sin mirar los pedidos. Es una hipótesis razonada, no medida; si se diera igual con la mezcla ideal, la meta se revisa y la propuesta no alcanza por sí sola. El piloto está pensado, entre otras cosas, para verlo.

**Cómo se prueba el retorno, sin inventar cifras.** No tenemos el costo de la hora extra ni lo que cuesta activar el módulo, así que no hay VAN sino el punto de equilibrio de la sección 2: B se paga si evita por mes al menos [dato pendiente: costo mensual de la alternativa B] sobre [dato pendiente: costo por hora extra] horas extras. El tope son las ~25 horas de hoy, y la meta de la mitad vale solo si se cumple el supuesto 7. El dueño acepta una inversión mayor si se demuestra el retorno.

Cómo se valida cada supuesto, con su probabilidad, su impacto y su señal temprana, se desarrolla en la sección 7.

**Fuentes:** canvas AS-IS y VPC de la Parte 1; relevamiento del proceso; secciones 1 y 2 de esta parte.

---

# 5. Stakeholders del proyecto de mejora

Esta sección mira a quienes hacen que la propuesta funcione o no. Usamos la matriz poder/interés de Mendelow, que es la que pide la consigna y la que se explicó en la clase del 23-10 (la lámina de la Clase 4 usa influencia e impacto, otra lectura).

**Quien aprueba el proyecto no es quien lo hace andar.** El dueño aprueba el presupuesto y el Go/No-Go, pero que el cambio funcione depende de lo que hagan todos los días Producción, Oficina y quienes deciden qué producir. Las resistencias de Producción y de Oficina las anticipamos con nuestro compañero que trabaja en la empresa. Lo demás (poder, interés, impacto y lo que decimos de los hijos) es lectura nuestra, no un dato medido: la vamos a contrastar con cada grupo antes del piloto.

## 5.1 Mapa de actores

Son ocho actores. El dueño tiene dos roles distintos: sponsor y, junto con los hijos, decisor de la producción.

| Actor | Rol en el proyecto | Qué hace en el proceso nuevo |
|---|---|---|
| **Dueño** | **Sponsor** y, con los hijos, **decisor de la producción** | Como sponsor, aprueba el presupuesto y el Go/No-Go, y acepta invertir más si se demuestra el retorno. Como decisor, planifica la producción mirando pedidos y stock mínimo |
| **Hijos** (dos) | Decisores de la producción | Planifican la producción de la semana mirando los pedidos pendientes y un stock mínimo por producto |
| **Responsable de sistemas** | **Líder del proyecto** | Coordina con el proveedor, capacita, sigue los indicadores, carga los ajustes de stock, mantiene los maestros y exporta el tablero |
| **Oficina** (4 personas: administración, facturación, cobranza) | Usuarios clave | Cargan la nota de pedido y reservan el stock antes de confirmar. Si falta algo, avisan con una fecha estimada |
| **Producción** (7 personas) | Usuarios clave: aportan el dato | Cargan lo producido todos los días, al cierre de turno, con un responsable por turno |
| **Depósito** (pedidos, embalaje, envíos) | Usuarios afectados | Arma desde el pedido confirmado, como hasta ahora. Conteo físico: [dato pendiente: responsable del conteo inicial y del semanal] |
| **Buenos Aires Software** (proveedor de Discovery) | Proveedor de tecnología | Activa el módulo de stock, pedidos y reserva. Licencia: [dato pendiente: versión de Discovery y soporte incluido] |
| **Distribuidores** (57 en 7 provincias, 35 en la Patagonia) | Afectados indirectos | Siguen pidiendo por WhatsApp o teléfono. Si falta algo, reciben el aviso al confirmar, con una fecha |

Queda afuera el transporte tercerizado, que no cambia su trabajo (sección 1). Sobre el líder: la Parte 1 le puso 1 punto a la gobernanza digital porque el responsable de sistemas no la tiene asignada. La propuesta se la asigna, pero un liderazgo sin tiempo es un agregado: [dato pendiente: tiempo semanal que el responsable de sistemas puede dedicar al proyecto].

## 5.2 Matriz poder/interés

Poder es cuánto puede ayudar o frenar el proyecto; interés, cuánto le importa y cuánto le toca. La matriz muestra la posición típica durante la ejecución, con las excepciones entre paréntesis. Las etiquetas siguen a la clase del 23-10 (en el Mendelow original las dos celdas de bajo poder se nombran al revés).

| | **Interés bajo** | **Interés alto** |
|---|---|---|
| **Poder alto** | **Mantener satisfecho:** Dueño como sponsor (cerca al arrancar el piloto y la activación), Buenos Aires Software (cerca en la activación) | **Gestionar de cerca:** Dueño como decisor de la producción, Hijos, Responsable de sistemas, Oficina, Producción |
| **Poder bajo** | **Mantener informado:** Distribuidores | **Monitorear y dar voz:** Depósito |

En las tablas siguientes los cuadrantes se abrevian: Cerca, Satisfecho, Voz e Informado.

El poder de Oficina y de Producción es de hecho, no formal: ninguno tiene autoridad sobre el proyecto, pero cualquiera lo frena con solo no usarlo. Por saliencia (poder, legitimidad, urgencia), Producción es una parte definitiva: tiene poder de hecho, la legitimidad de una planta saturada y la urgencia de las primeras semanas de carga, y se la atiende primero.

## 5.3 Estrategias de involucramiento

La ficha junta, por actor, su lugar en la matriz, su resistencia y su estrategia. Los que más cambian su trabajo se trabajan además con Heifetz, FUD, ADKAR y la negociación del 23-10.

| Actor | Poder | Interés | Impacto | Resistencia | Estrategia | Cuadrante |
|---|---|---|---|---|---|---|
| **Dueño** | **Alto**: aprueba presupuesto y Go/No-Go; con los hijos, decide la producción | Bajo como sponsor; alto como decisor | Medio como sponsor; alto como decisor | **Baja como sponsor** (el riesgo es que no mire); **posible como decisor**: perder el criterio propio | Sponsor: informe corto y regular, Go/No-Go acordado antes. Decisor: igual que los hijos | Satisfecho; Cerca como decisor |
| **Hijos** | **Alto**: deciden qué producir | **Alto** | Alto | **Posible, no relevada** (hipótesis nuestra): perder el criterio propio | Siguen decidiendo, con más información, y fijan el stock mínimo | Cerca |
| **Responsable de sistemas** | **Alto**, delegado por el dueño | **Alto** | Alto | Sobrecarga | Asignación formal con tiempo reservado | Cerca |
| **Oficina** | **Alto de hecho**: sin carga ni reserva no hay stock confiable | **Alto** | Alto: cambia cómo se confirma un pedido | **Esperada**: suma un paso | Mostrar qué pasos reemplaza el nuevo; guion de aviso | Cerca |
| **Producción** | **Alto de hecho**: sin carga diaria no hay stock | **Alto** | Alto: trabajo nuevo con la planta saturada | **Esperada**: es trabajo nuevo sin holgura | Escucharlos antes de pedirles nada | Cerca |
| **Depósito** | **Bajo**; sube si le toca el conteo | **Alto**: sabe cuánto hay | Medio | Baja | Dar voz: que valide el primer conteo | Voz |
| **Buenos Aires Software** | **Alto** sobre la viabilidad: si el módulo no anda, la alternativa B no se puede | **Bajo** | Bajo | Baja; el riesgo es que el módulo no ande o el soporte tarde | Pedirle por escrito qué incluye la licencia; probar el módulo en un producto antes de escalar (sección 7) | Satisfecho |
| **Distribuidores** | **Bajo** sobre el proyecto, aunque sean el negocio | **Bajo** | Bajo: cambia lo que reciben | No relevada; ver el supuesto 6 de la sección 4 | Informar que el aviso llega al confirmar, con una fecha | Informado |

### Técnico o adaptativo (Heifetz)

Un desafío técnico se resuelve con procedimientos que ya existen; uno adaptativo exige aprender y cambiar prácticas o relaciones. Una transformación suele combinar los dos (Clase 4).

| Cambio | Componente técnico | Componente adaptativo | Predomina |
|---|---|---|---|
| **Cargar lo producido todos los días** (Producción) | Qué se carga, cuándo y quién; capacitación en Discovery | Trabajo nuevo en una planta sin holgura: hay que decidir qué se deja de hacer | **Técnico**, con un borde adaptativo |
| **Reservar stock antes de confirmar** (Oficina) | Un paso en Discovery con una sola regla de stock disponible | Aprender a decir "hay en tal fecha estimada" en vez de confirmar siempre | **Mixto** |
| **Planificar la producción contra pedidos y stock mínimo** (dueño e hijos) | Definir el mínimo por producto y mirar los pedidos pendientes | Cambiar el criterio propio por uno informado y compartir la decisión | **Adaptativo** |

Lo técnico se resuelve con procedimiento y capacitación; lo adaptativo pide conversar, acotar el cambio, ofrecer soporte y reservar tiempo (Clase 4). El de fondo es la última fila (supuesto 5 de la sección 4), y por eso el piloto es de un solo producto. Si la carga diaria se cae, primero se revisan capacitación, carga de trabajo, incentivos y reglas, no el compromiso de la gente (Clase 4).

### Qué siente cada grupo y dónde se traba (FUD y ADKAR)

Dos guías para conversar, no diagnósticos: son hipótesis nuestras. FUD es miedo, incertidumbre y duda; ADKAR, las cinco condiciones para adoptar un cambio (conciencia, disposición, conocimiento, capacidad y refuerzo). La Clase 4 recuerda que capacitar da conocimiento, pero la capacidad pide además práctica, tiempo y soporte; el refuerzo lo da el tablero a la vista (sección 8).

| Grupo | FUD: qué puede sentir | ADKAR: dónde se traba | Qué hacemos |
|---|---|---|---|
| **Producción** | Más trabajo en una planta al límite; que el dato señale a alguien; no saber quién suple; duda de que sirva, porque hoy lo que cargan no se cruza con ventas | **Capacidad** (tiempo y práctica) y **disposición**, si no ven qué ganan | Acordar con el dueño que el dato planifica y no evalúa; procedimiento de una hoja; capacitar en el puesto con el tiempo de carga dentro del turno; mostrar en la reunión diaria que ventas usa el dato |
| **Oficina** | Que avisar "hoy no hay" enoje al distribuidor; qué fecha dar si producción no la confirmó; duda de que el stock cargado sea confiable | **Disposición** (miedo a perder el pedido) y **conocimiento** (qué fecha dar, cómo usar la reserva) | Guion de aviso con fecha y respaldo del dueño; fecha confirmada en la reunión diaria (supuesto 4); conteo y exactitud a la vista; práctica con pedidos reales del piloto |
| **Dueño e hijos** | Perder el criterio propio; cuánto de la decisión sigue siendo suya; que un número capture lo que saben y, en el dueño, que haya retorno | **Conciencia**: la Parte 1 decía que los pedidos incompletos eran poco frecuentes y el relevamiento lo corrige (30 de ~125 en una semana) | Siguen decidiendo ellos, con una regla clara de qué se mira y quién fija el mínimo; mostrar el dato y después el resultado del piloto (supuesto 1) |

### Cómo negociamos

La clase del 23-10 da cuatro consejos; los aplicamos en tres puntos, propuestas nuestras a acordar con cada parte.

- **Toma y daca, sabiendo qué se negocia; nunca un sí o un no.** Producción: la carga diaria reemplaza a su control semanal propio en vez de sumarse (falta confirmar qué contiene); lo que se negocia es el tiempo de planta. Oficina: reservar antes de confirmar a cambio de una sola consulta en lugar de dos y una nota que se carga una vez, no tres; no quiere quedar mal con el distribuidor. Los hijos: mirar pedidos y stock mínimo a cambio de que la decisión siga siendo de ellos; lo que se negocia es quién la controla. Vale preguntar cómo ve cada uno las horas extras: para quien las hace pueden ser también un ingreso.
- **Información simétrica.** Todos ven los mismos números (los 30 de ~125 pedidos, las horas extras, el tablero) y la misma regla de stock disponible: quien siente que no sabe lo que otros saben, se retrae.
- **Pocos en el punto de dolor.** Si Producción y Oficina se echan la culpa y van juntas ante el dueño, se vuelven una sola parte con poder, legitimidad y urgencia: se habla primero con cada una por separado.

## 5.4 Cómo cambia por fase

En clase se dijo que la matriz no es una foto fija: el jefe de finanzas, sin presupuesto aprobado, se gestiona de cerca, y una vez aprobado pasa a otro cuadrante. Las fases son las del roadmap de la sección 8.

| Actor | Preparación y conteo inicial | Piloto (2 semanas, papas fritas) | Go/No-Go | Activar Discovery por línea | Estabilización |
|---|---|---|---|---|---|
| Dueño como sponsor | Cerca | Satisfecho (Cerca al arrancar) | Cerca | Satisfecho (Cerca al arrancar) | Satisfecho |
| Dueño e hijos como decisores | Cerca | Cerca | Cerca | Cerca | Cerca |
| Responsable de sistemas | Cerca | Cerca | Cerca | Cerca | Cerca |
| Oficina | Voz | Cerca | Cerca | Cerca | Satisfecho |
| Producción | Voz | Cerca | Cerca | Cerca | Satisfecho |
| Depósito | Voz | Voz | Voz | Voz | Voz |
| Buenos Aires Software | Satisfecho | Satisfecho | Satisfecho | Cerca | Satisfecho |
| Distribuidores | Informado | Informado | Informado | Informado | Informado |

- **El dueño como sponsor sube y baja.** Cerca al aprobar el presupuesto y al decidir el Go/No-Go; entre medio basta mantenerlo satisfecho, pero su respaldo tiene que verse delante del equipo al arrancar el piloto y la activación, porque ahí se le pide trabajo nuevo a Producción y a Oficina.
- **Oficina y Producción activan su poder con el uso.** En la estabilización el interés baja porque ya es rutina, pero el poder queda: es el momento de más riesgo silencioso, porque pueden dejar de cargar y nadie lo nota hasta que cae la exactitud. Si baja el indicador de días con producción cargada, vuelven a Cerca (sección 8).
- **El responsable de sistemas está en Cerca todo el proyecto**, porque la propuesta le delega el poder desde el arranque. **Buenos Aires Software importa dos veces:** al principio, para saber si el módulo funciona, y en la activación, por su soporte.
- **Dueño e hijos no se mueven, y esa es la señal:** la decisión de producción es el cambio adaptativo y el que más tarda en consolidarse. Depósito y distribuidores casi no se mueven, salvo que a Depósito le toque el conteo o se junten quejas por los avisos (son 57 distribuidores).

La matriz se revisa en cada Go/No-Go.

---

# 6. Arquitectura conceptual y flujo de datos

Esta sección dibuja la alternativa recomendada (la B: el stock de Discovery, probado antes con una planilla compartida) como cajas y flechas, y dice qué datos se mueven, quién los carga, cómo pasan de un lugar a otro y qué reglas los mantienen limpios.

La guía de la cátedra pregunta si una empresa chica necesita un diagrama de la NASA o un flujo simple. Para una pyme de 15 a 20 personas la respuesta es el flujo simple: **un solo sistema, y ya lo tienen.** Es Discovery, que hoy usan para facturar, más una planilla compartida que existe solo durante el piloto de 2 semanas y un tablero con cuatro indicadores. No hay sistema nuevo que comprar (el costo de activar el módulo de stock está pendiente, sección 4), ni integración automática, ni canal nuevo: las áreas aportan sus datos a un solo lugar, y de ahí salen la lista para armar cada pedido y los números del tablero.

## 6.1 Diagrama

![Arquitectura y flujo de datos](../diagramas/arquitectura.png)

Para la exposición hay además una versión interactiva del flujo de datos, el archivo `Flujo de datos interactivo - Dulxelitos.html` de la carpeta de entrega, que se abre en el navegador.

### Cómo se lee

- **Tres áreas aportan, un solo lugar guarda.** Oficina carga la nota de pedido y reserva el stock antes de confirmar; Producción carga lo producido al cierre del turno; Depósito deja la hoja del conteo semanal, que el responsable de sistemas carga como ajuste (quién cuenta: [dato pendiente: responsable del conteo inicial y del semanal]). Los tres aportes entran juntos a Discovery y de ahí sale, para cada pedido confirmado, la lista de armado que usa Depósito: lo que se gana por cargar el pedido una sola vez.
- **La planilla de stock es solo del piloto.** Va punteada en el diagrama porque dura 2 semanas, con papas fritas, el producto que más falta. Recibe los mismos tres aportes (por eso el diagrama los muestra juntos antes de bifurcar), usa la misma regla de stock disponible que Discovery (sección 3) y, después del Go/No-Go, se archiva.
- **El tablero no guarda nada propio.** Se alimenta de la exportación CSV de Discovery, el registro semanal de Oficina y las horas extras de la liquidación; qué muestra y cómo se mira, en la sección 8.
- **El distribuidor queda afuera de los datos.** Sigue pidiendo por WhatsApp o teléfono y recibe el aviso si falta algo, pero no ve el stock: esa visibilidad queda para "later" (sección 1).

**Lo que el diagrama da por cierto y no está probado.** Supone que el módulo de stock de Discovery permite pedidos y reserva (también reservar solo una parte de un pedido), que la factura consume la reserva y que el módulo está dentro de la licencia que ya pagan. Lo sabe nuestro compañero que trabaja en la empresa, pero nadie lo usó en Dulxelitos: falta confirmarlo por escrito con Buenos Aires Software (supuesto 3 de la sección 4). Los datos no dependen de la herramienta: si Discovery no se comporta así, el flujo sigue en pie con la planilla (alternativa A) y solo cambia dónde está el registro.

## 6.2 Datos

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

## 6.3 Integraciones

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

## 6.4 Reglas de datos

Las reglas valen para los datos críticos: el stock físico, las reservas, los productos, los distribuidores y el stock mínimo. Son simples a propósito, porque las tiene que poder cumplir una empresa de 15 a 20 personas con la planta saturada. Tres principios las sostienen:

1. **Un solo lugar por dato.** Cada dato de pedidos y stock vive en Discovery. La planilla de stock solo existe en el piloto, y solo para el producto del piloto. Dos datos viven afuera porque Discovery no los tiene: el registro semanal de recortes, en una hoja compartida simple que lleva Oficina, y las horas extras, que salen de la liquidación de sueldos.
2. **No se borra, se corrige.** Un error se arregla con un movimiento nuevo y un motivo escrito, que deja rastro. Nadie pisa un número.
3. **Lo que se cuenta manda sobre lo que se cargó.** Si el conteo físico y Discovery no coinciden, se corrige Discovery.

La revisión de las reglas es parte de cada Go/No-Go (sección 8). Si baja la exactitud de stock o los días con producción cargada, primero se revisan capacitación, carga de trabajo, incentivos y reglas, antes que el compromiso de la gente (sección 5).

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

---

# 7. Validación de supuestos

Esta sección dice qué hay que aprender antes de invertir, cómo aprenderlo barato y qué resultado hace avanzar o frenar, a partir de los nueve supuestos de la sección 4. **Antes de gastar en el stock de Discovery hacemos dos pruebas baratas:** un piloto de 2 semanas con papas fritas en una planilla compartida y una prueba técnica de Discovery sobre un solo producto. Lo primero que hay que probar es el supuesto 1, que los recortes vendrían de la mezcla y el momento: una hipótesis razonada, no un dato. Los umbrales de decisión son propuesta nuestra y el dueño los acuerda antes de arrancar.

## 7.1 Supuestos críticos

Son los nueve de la sección 4, con su número. **Probabilidad** es la de que el supuesto resulte falso e **impacto** lo que le pasa a la propuesta si lo es; son juicio nuestro (alta, media o baja), no mediciones. La **etapa** es la principal de las cuatro de validación de la Clase 7 (Rogers): problema, solución, producto y negocio, que son iterativas y se superponen.

### El riesgo de cada supuesto

| # | Supuesto | Tipo y etapa | Prob. de ser falso | Impacto si es falso | Señal temprana |
|---|---|---|---|---|---|
| 1 | La mezcla y el momento de producción, y no la capacidad total, explican la mayoría de los recortes | Factibilidad (crítico) · Problema | Media | Alto | En la semana 0, la mayoría de los recortes se anota como "no alcanzaba la planta" |
| 2 | Producción carga todos los días, y oficina consulta y reserva antes de confirmar, aun con la planta saturada | Factibilidad · Producto | Alta | Alto | Días sin carga al cierre de turno; la planilla no coincide con lo que se ve a ojo |
| 3 | El módulo de stock de Discovery permite pedidos y reserva (también una parte de un pedido), y la factura consume la reserva, con el mismo criterio de disponible | Factibilidad · Producto | Media | Medio | El proveedor no lo confirma por escrito, o un paso de la prueba falla |
| 4 | La fecha estimada que se da al distribuidor se cumple, con la planta saturada | Factibilidad · Producto | Media | Alto | Producción no confirma la fecha en la reunión diaria, o una fecha se pasa |
| 5 | Dueño e hijos deciden la producción mirando pedidos pendientes y stock mínimo, y no solo por criterio propio | Deseabilidad · Solución | Media | Alto | La reunión diaria no cambia lo que se produce con pedidos sin cubrir |
| 6 | Al distribuidor no le resulta peor una fecha estimada al confirmar que recibir el pedido recortado | Deseabilidad · Solución | Baja | Medio | El distribuidor cancela, reprograma o reclama cuando oye la fecha |
| 7 | Al menos la mitad de las ~25 horas extras por mes es por pedidos que faltaron por mezcla y momento | Viabilidad · Negocio | Media | Medio | El motivo de las horas extras es sobre todo "saturación"; no bajan aunque los recortes sí |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo de implementar y sostener el cambio | Viabilidad · Negocio | Media | Alto | El punto de equilibrio pide evitar más horas extras que las ~25 de hoy |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa | Viabilidad · Problema | Media | Medio | El total semanal de la semana 0 o del piloto se aleja del registrado |

El 2 es alta porque hoy producción carga 1 de cada 5 días (20 %) y esperamos resistencia; el 6 es baja porque el distribuidor ya recibe avisos y pedidos incompletos sin quejarse.

### Cómo se valida cada uno

| # | Mecanismo de validación ágil y qué se anota | Se contesta en |
|---|---|---|
| 1 | Anotar la causa de cada recorte de papas fritas en la semana 0 (mezcla y momento, capacidad u otra) y ver si bajan al planificar contra pedidos | Semana 0 y piloto |
| 2 | Contar los días con carga y las diferencias de conteo, y anotar los días en que la planilla falló y se confirmó como hoy | Piloto |
| 3 | Probar un producto de punta a punta, anotando cada paso, y consultar por escrito a Buenos Aires Software | Prueba técnica |
| 4 | Producción confirma la fecha en la reunión diaria; se anota cada aviso con su fecha y si se cumplió | Piloto |
| 5 | Pedirle al dueño y a los hijos que fijen el stock mínimo y anotar si la reunión cambió lo que se produjo de papas fritas | Piloto, señal inicial |
| 6 | Observar cómo reacciona el distribuidor a cada aviso (acepta, espera, cancela o reclama) | Piloto |
| 7 | Registrar el motivo de cada hora extra (completar un pedido que faltó, saturación u otro) | Piloto como señal; después, la liquidación de sueldos |
| 8 | Completar el punto de equilibrio de la sección 2 con el tiempo de carga, reserva y reunión (costo en horas) | Datos de costo y consulta al proveedor |
| 9 | Repetir el registro semanal de todos los productos, con el mismo criterio, y anotar el total de la semana | Semana 0 y piloto |

El piloto contesta, al menos en parte, siete de los nueve. El 3 tiene su prueba técnica y el 8 depende de dos datos que faltan: [dato pendiente: costo mensual de la alternativa B] y [dato pendiente: costo por hora extra]. Van primero los de impacto alto y probabilidad media o alta (1, 2, 4, 5 y 8).

## 7.2 Piloto

Según la Clase 7, un MVP no es una versión beta ni una versión light del producto final sino el experimento mínimo necesario para validar una hipótesis; el nuestro es **funcional** (funciona, en pequeño). Tiene espíritu de pretotipo (construir lo correcto antes de construirlo bien, Savoia), y la prueba técnica de Discovery cumple el papel del prototipo: van en paralelo.

### Hipótesis en una hoja

Plantilla de la Clase 7. Los umbrales están en "Qué se mide" y la rutina, en "Cómo se corre".

| Elemento | Contenido |
|---|---|
| **Problema** | Unos 30 de ~125 pedidos por semana salen recortados o demorados porque se confirma sin saber qué hay y se produce sin mirar los pedidos (sección 1) |
| **Hipótesis de solución** | Creemos que una planilla compartida con el stock de papas fritas, la carga diaria, la reserva por pedido confirmado y una reunión diaria de ~10 minutos resolverá los recortes y demoras de papas fritas, y sabremos que funciona cuando se cumplan los cuatro umbrales de "Qué se mide" |
| **Tipo de MVP y experimento mínimo** | Funcional: dos semanas con papas fritas solamente; los demás productos siguen como hoy |
| **Etapa de validación** | **Producto**: ¿podemos entregar una solución que se use? Toca también **Problema** (¿la causa es la que creemos?) y, en parte, **Solución** (¿el distribuidor ve valor en un aviso con fecha?). No toca **Negocio**: espera a los datos de costo y a la activación |

### Cómo se corre

- **Cuándo y qué.** Una semana 0 para medir la línea de base y después 2 semanas (10 días hábiles), solo con papas fritas, el producto que más falta según el relevamiento. Un solo producto protege la operación y alcanza para aprender. Puede empezar cuando se quiera, con el conteo inicial hecho el fin de semana anterior.
- **La rutina.** Con la regla de stock disponible de la sección 3, la misma que se usaría en Discovery: Producción carga lo producido al cierre de turno, con un responsable y un suplente; Oficina consulta y reserva antes de confirmar un pedido con papas fritas y, si no alcanza, avisa con una fecha que producción confirmó. Al facturar se baja el físico y se descuenta la reserva, a mano porque la planilla no habla con Discovery. Hay un conteo físico al arrancar y uno por semana, y una reunión diaria de ~10 minutos entre ventas y producción para mirar el disponible, los pedidos y los avisos, y decidir qué producir.
- **Vuelta atrás.** Si un día la planilla no está al día, oficina confirma como hoy, a ojo y preguntando a producción, y se anota el día. El piloto se corta cuando se quiera: no toca Discovery ni el armado de pedidos.
- **Quién.** El dueño, como sponsor, acuerda los umbrales y respalda el arranque. El responsable de sistemas, como líder, arma la planilla y junta las medidas. Producción carga; oficina reserva y avisa. Conteo físico: [dato pendiente: responsable del conteo inicial y del semanal].

### Qué se mide

Cuenta como **recortado o demorado** un pedido con papas fritas que sale con menos cantidad de la pedida o después del plazo estándar de su zona. Como en las secciones 1 y 3, uno rechazado o reprogramado de entrada, o cancelado después del aviso, también cuenta: si no, el número mejoraría empujando pedidos afuera. El criterio es el mismo en la semana 0 y en el piloto.

| Medida | Cómo se mide | Línea de base | Umbral para un Go | Por qué ese umbral |
|---|---|---|---|---|
| **Días con producción de papas fritas cargada** | Días con carga al cierre de turno sobre los 10 días hábiles | 20 % de los días: hoy se carga 1 vez por semana [dato pendiente: si el control de producción separa por producto] | 8 de los 10 días o más | La meta de la sección 1 es todos los días; en un primer intento dejamos 2 días de margen |
| **Pedidos de papas fritas recortados o demorados** | Promedio por semana de las 2 del piloto, del registro semanal | Se mide en la semana 0: [dato pendiente: pedidos de papas fritas recortados o demorados en la semana 0]. Los 30 de ~125 son de todos los productos y no sirven de base para uno | La mitad o menos que en la semana 0, y que los rechazados, reprogramados de entrada o cancelados tras el aviso, que cuentan en el total, no suban | La meta de la sección 1 lleva los pedidos completos y a tiempo del 76 % al 90 %: queda 1 recortado de cada 10 (100 menos 90), menos de la mitad de los ~24 % de hoy. Pedimos la mitad como señal del rumbo, por ser un producto y 2 semanas |
| **Diferencias de conteo** | Conteo físico de papas fritas contra la planilla, al arrancar y al final de cada semana | [dato pendiente: diferencia en el conteo inicial] | En los conteos semanales, una diferencia de hasta una décima parte de lo contado | La meta de exactitud (al menos 9 de cada 10 productos dentro de la tolerancia, sección 8) y esta tolerancia son provisionales: se ajustan con el primer conteo |
| **Fecha estimada cumplida** | Cada aviso con fecha: si el pedido se completó ese día | No existe hoy: el aviso no trae fecha | 4 de cada 5 avisos o más; si hubo pocos, se revisan uno por uno | Es una promesa nueva: si falla más de 1 vez de cada 5, el aviso pierde su valor. No pedimos todas por la planta saturada |

Lo demás que se anota está en la tabla de mecanismos. Como control, se compara con los demás productos en las mismas semanas: si los recortes bajan en todos por igual, la mejora no es del piloto. Si la semana 0 casi no tiene recortes de papas fritas, la comparación no distingue mejora de azar: se mide otra semana.

### Prueba técnica de Discovery

Es la prueba del supuesto 3: nuestro compañero que trabaja en la empresa sabe que Discovery permite pedidos y reserva, pero nadie lo usó en Dulxelitos. La lleva el responsable de sistemas con Buenos Aires Software, en la preparación y en paralelo con la semana 0, y su resultado entra al Go/No-Go junto con el del piloto. Se prueba **un solo producto**, el mismo del piloto, en cinco pasos:

| Paso | Qué se verifica | Resultado esperado |
|---|---|---|
| 1. Ingreso de stock | Cargar el stock inicial | Queda registrado el stock físico |
| 2. Pedido y reserva | Cargar una nota de pedido y reservar; con otro pedido mayor al stock, reservar solo la parte que hay y dejar el resto pendiente | La reserva aparece contra el pedido, y el proveedor confirma cómo se anota el resto pendiente |
| 3. Disponible | Consultar cuánto hay | Es el stock físico menos lo reservado, como en la planilla |
| 4. Factura | Facturar el pedido | La factura baja el stock físico y consume la reserva |
| 5. Corrección | Anular o modificar el pedido | La reserva se libera |

Por escrito se le pregunta a Buenos Aires Software qué versión es y qué soporte incluye ([dato pendiente: versión de Discovery y soporte incluido]), cuánto cuesta activar y capacitar ([dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]), en cuánto tiempo ([dato pendiente: plazo de activación del módulo]) y si hay ambiente de prueba, que importa por el paso 4: una factura de prueba en el sistema real puede quedar como una factura verdadera.

**La prueba pasa** si funcionan los pasos que se pueden probar. Sin ambiente de prueba, el paso 4 (la factura) queda para el primer pedido real de la activación y no bloquea el Go. Si algo falla, se pregunta al proveedor si se configura y cuánto cuesta; si no se puede, se sigue con la alternativa A.

## 7.3 Criterio de decisión

Las reglas se acuerdan con el dueño **antes de arrancar**: él decide el Go/No-Go, y fijar el criterio después del resultado invita a leerlo a favor. Los umbrales son una propuesta nuestra, sin dato de la empresa que los respalde, y se ajustan con el dueño y con la semana 0.

| Qué pasó | Qué significa | Decisión |
|---|---|---|
| Se cumplen los cuatro umbrales (incluido que los rechazados no suban) y la prueba técnica pasa (con el paso de la factura pendiente si no hay ambiente de prueba) | Rutina sostenida, mezcla como causa y módulo que funciona | **Go.** Activar Discovery por línea de producto, con la misma rutina, si además el punto de equilibrio de la sección 2 cierra con los datos de costo |
| Se cumplen la carga y los recortes, pero fallan el conteo o la fecha | La rutina anda; el dato o la promesa necesitan ajuste | **Go con ajustes.** Corregir capacitación, responsable o regla de fecha y repetir una sola vez |
| La carga no llega a 8 de los 10 días | La rutina no se sostiene | **No-Go.** B no se gasta: una herramienta mejor no arregla un problema de disciplina. Se revisan capacitación, carga de trabajo, incentivos y reglas, no el compromiso de la gente (sección 5) |
| La carga anda, los recortes no bajan a la mitad y las causas anotadas son sobre todo de capacidad | El supuesto 1 cae | **No-Go** de B para este problema; se revisa la meta de la sección 1, porque lo que queda es un problema de planta, fuera de alcance. Si hubo pocos recortes para concluir, se repite una sola vez |
| La carga anda, los recortes no bajan, pero las causas anotadas son sobre todo mezcla y momento | Algo falla en cómo se usa el dato (supuesto 5) | **No se concluye.** Revisar si la producción cambió con lo que se vio en la reunión y repetir una sola vez |
| La prueba técnica falla y el proveedor no lo resuelve | El supuesto 3 cae | Se sigue con A, la planilla, con sus controles, antes que pasar a C (sección 2) |

**Repetir una sola vez** es otra vuelta de 2 semanas con el mismo producto. Si en la segunda tampoco se cumple, la decisión es No-Go: seguir probando sin criterio es no decidir.

### Qué valida el piloto y qué queda para después de activar

Dos semanas con un producto dan una señal, no una demostración. El piloto valida la factibilidad y la deseabilidad de la rutina (supuesto 2, con una primera lectura de los 4, 5 y 6) y si la causa de los recortes de papas fritas es la mezcla y el momento (supuesto 1). Con las mismas medidas sobre más productos y más tiempo, el Go/No-Go de la sección 8 mira lo que el piloto no puede: el efecto en todo el catálogo (supuestos 1 y 9), la baja de las horas extras (supuesto 7), la carga y la exactitud sostenidas cuando ya son rutina y el retorno con los costos reales (supuesto 8).

**Fuentes:** secciones 2, 4 y 5 de esta parte; relevamiento del proceso; Clase 7 (etapas de Rogers, MVP, pretotipo de Savoia, hipótesis en una hoja). Probabilidades, impactos y umbrales son supuestos declarados, no datos.

---

# 8. Roadmap, OKR e indicadores

Esta sección dice en qué orden se hace el cambio, cómo se cuida la operación y cómo sabremos si funcionó, apoyándose en el piloto y los criterios de la sección 7, que acá se ubican en el calendario. **El roadmap tiene una decisión grande, el Go/No-Go al terminar el piloto, y después se avanza de a una línea de producto con las mismas medidas.** Los indicadores miden el efecto y avisan si la carga diaria se cae.

## 8.1 Roadmap

Es un roadmap y no un Gantt (23-10): detalla lo próximo y deja abierto lo lejano, porque la activación depende de lo que muestre el piloto. La demanda es pareja todo el año, así que se arranca cuando el dueño apruebe, sin temporada alta que esquivar. Las fases son las que usa la sección 5.

### Las cinco fases en 6 meses

| Fase | Hito | Entregable | Responsable | Duración (propuesta nuestra) | Recursos | Dependencias | Go/No-Go |
|---|---|---|---|---|---|---|---|
| **1. Preparación y conteo inicial** | Umbrales acordados, papas fritas contadas y semana 0 medida | Umbrales por escrito; registro de la semana 0 con la causa de cada recorte; stock inicial y mínimo de papas fritas; planilla, tablero simple y procedimiento de una hoja; prueba técnica y respuestas de Buenos Aires Software | Responsable de sistemas | 3 semanas (1 a 3) | Responsable de sistemas ([dato pendiente: tiempo semanal que el responsable de sistemas puede dedicar al proyecto]); Oficina y Depósito; planilla | Respaldo del dueño; [dato pendiente: responsable del conteo inicial y del semanal] | **Antes del piloto:** el dueño confirma umbrales, carga con suplente y conteo hecho |
| **2. Piloto, 2 semanas con papas fritas** | 10 días hábiles con carga, reserva y reunión diaria | Las medidas de la sección 7 y el primer tablero, con la planilla y el registro de Oficina | Responsable de sistemas | 2 semanas (4 y 5) | Planilla; carga de Producción; reserva y aviso de Oficina; reunión de ~10 minutos | Fase 1 terminada | Ninguno; se corta cuando se quiera |
| **3. Go/No-Go** | Decisión del dueño sobre activar Discovery | Hoja de decisión con las medidas del piloto, la prueba técnica y el punto de equilibrio | Dueño (decide); responsable de sistemas (prepara) | 1 semana (6) | Reunión con el dueño | Piloto y prueba técnica cerrados; costos del punto de equilibrio: [dato pendiente: costo mensual de la alternativa B] y [dato pendiente: costo por hora extra] | **Go, Go con ajustes, No-Go o no se concluye** (tabla de la sección 7) |
| **4. Activar Discovery por línea de producto** | Primero Salados, porque arranca con papas fritas, ya probada en el piloto; después Dulces y Repostería, una línea por vez | Por línea: conteo inicial, stock cargado, capacitación y carga con suplente. El tablero suma el CSV de Discovery | Responsable de sistemas, con Buenos Aires Software | Hasta 16 semanas (7 a 22) | Buenos Aires Software ([dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]); tiempo de las áreas | Go de la fase 3; [dato pendiente: plazo de activación del módulo]; [dato pendiente: en qué orden se activan Dulces y Repostería] | **Después de cada línea:** las medidas del piloto sobre esa línea |
| **5. Estabilización** | Rutina sin apoyo del proyecto y cierre | Tablero a la vista, lectura del OKR y propuesta de lo que sigue | Responsable de sistemas | 4 semanas (23 a 26) | Reunión diaria y conteo semanal en rutina; reunión de cierre | Líneas activadas en la fase 4; liquidaciones de varios meses | **De cierre:** el dueño lee el OKR y decide si sigue, revisa las metas o frena |

Las duraciones suman los 6 meses. La semana 0 es la tercera de la fase 1, con la prueba técnica en paralelo (sección 7); si casi no hay recortes de papas fritas, se mide otra y el resto se corre una semana. Si el piloto se repite una vez (sección 7), todo lo que sigue corre 2 semanas.

**La fase 4 es la más incierta**: depende del plazo de activación y de cuánto tarde cada una de las tres líneas (Salados, Dulces y Repostería), que no sabemos. Si las 16 semanas no alcanzan, se activan menos líneas dentro de los 6 meses: Salados va primero y, después, la que más recortes tenga (el registro anota qué producto faltó, ver el indicador 1); el seguimiento de cada línea no se acorta. Por eso la meta de 90 % vale solo si esas líneas están activas antes del cierre; si no, se revisa en el Go/No-Go de cierre.

### Ahora, próximo y más adelante

Con la lógica de la clase del 23-10 (detalle en lo próximo, alternativas abiertas en lo que sigue y lo estratégico anotado, sin planificar): **ahora** son las fases 1 a 3, hasta la semana 6, ya detalladas arriba y en las secciones 5 a 7. **Próximo** son las fases 4 y 5: se activa por línea, pero antes hay que resolver cuatro cosas: si el Go/No-Go confirma B o se sigue con la planilla (A); en qué orden se activan Dulces y Repostería (Salados va primero, con el piloto de papas fritas); cuánto tarda y cuesta activar el módulo; y el stock mínimo de cada línea, que fijan el dueño y los hijos. **Más adelante** quedan, anotadas y sin planificar, la visibilidad de stock para el distribuidor y la tienda online de 2020, cuando la exactitud se sostenga y el dueño lo decida (secciones 1 y 4); insumos y packaging quedan como deuda declarada.

### Decisiones de avance (Go/No-Go)

Las toma el dueño en los cuatro momentos de la última columna de la tabla, con el criterio acordado antes para no leer el resultado a favor: al terminar el piloto valen los umbrales y la tabla de la sección 7, y cada línea nueva se activa con los mismos umbrales. En el cierre, si se llegó a las metas, el OKR termina y los indicadores pasan a vigilarse como KPI permanentes. Si no, se mira primero la causa y no a la gente: si la mezcla y el momento no explicaban los recortes (supuesto 1) o menos de la mitad de las horas extras era por pedidos que faltaron (supuesto 7), se revisa la meta; si la rutina no se sostuvo, se revisan capacitación, carga de trabajo, incentivos y reglas. Cada Go/No-Go revisa también las reglas de datos (sección 6) y la matriz de la sección 5.

### Comunicación, proceso, capacitación, piloto, evaluación y escalamiento

| Línea | Qué se hace | Fases |
|---|---|---|
| **Comunicación** | El dueño presenta el proyecto delante del equipo al arrancar el piloto y la activación (sección 5). Todos ven los mismos números (los 30 de ~125 pedidos, las horas extras, el tablero) y el dueño recibe un informe corto y regular. A los distribuidores se les avisa que, si falta algo, lo sabrán al confirmar, con una fecha | 1, 2 y 4 |
| **Proceso** | Procedimiento de una hoja (quién carga, cuándo y quién suple), regla de stock disponible, guion de aviso y reunión diaria de ~10 minutos (sección 3) | 1, con ajustes en 2 y 4 |
| **Capacitación** | En el puesto, con pedidos reales y el tiempo de carga dentro del turno: capacitar da conocimiento, pero la capacidad pide además práctica, tiempo y soporte (Clase 4). Se repite en cada línea | 2 y 4 |
| **Piloto, evaluación y escalamiento** | Piloto con papas fritas en planilla, 2 semanas y vuelta atrás (sección 7); tablero simple desde la fase 1, informe al dueño y Go/No-Go; después, una línea por vez con las medidas del piloto | 1 a 5 |

## 8.2 Cómo se protege la operación

La regla de fondo es que **ninguna fecha del roadmap vale más que despachar los pedidos**: si cargar o contar choca con la operación, se corre el calendario. Cuatro cuidados.

- **Cargas de trabajo.** No se suma una tarea sin sacar otra: la carga diaria de Producción reemplaza a su control semanal propio (falta confirmar qué contiene, secciones 5 y 6), y Oficina hace una consulta en lugar de dos y carga la nota una vez en lugar de tres. Se cambia un producto por vez y la carga se hace al cierre, dentro del turno, sin cortar la producción ni generar horas extras; el tiempo que lleva se mide en el piloto (sección 7).
- **Momentos de menor actividad.** El conteo inicial de cada línea se hace en fin de semana, para no frenar ventas ni producción (a confirmar con Depósito); cuenta [dato pendiente: responsable del conteo inicial y del semanal]. Esas horas no engordan el indicador 4: se compensan con franco o, si se pagan, se anotan con el motivo "conteo inicial" y se restan del total antes de compararlo con la línea de base y con la regla de freno. El conteo semanal va al final de la semana, sin horas extras, y la reunión diaria a una hora que acuerden Producción y Oficina, fuera de sus momentos de más trabajo.
- **Suplentes.** Un responsable de carga por turno, con suplente; una segunda persona de Oficina que sepa consultar y reservar; un suplente para el conteo. El caso más delicado es el responsable de sistemas, que lidera, arma la planilla, prueba Discovery, carga los ajustes y exporta el tablero: si falta, el proyecto se frena, y hay que definir quién lo suple.
- **Continuidad de ventas, producción, atención y cobranza.** Ventas: si un día la planilla o Discovery no está al día, Oficina confirma como hoy y se anota el día (vuelta atrás, sección 7). Producción: el dueño y los hijos siguen decidiendo qué producir, con más información, y el piloto no toca Discovery ni el armado de pedidos. Atención: a los distribuidores los atiende Oficina como hoy. Facturación y cobranza: no se tocan en el piloto, la cobranza no cambia en ninguna fase y, en la activación, sin ambiente de prueba, facturar se verifica con el primer pedido real (sección 7). Si una línea falla, solo esa vuelve a confirmarse como hoy.

**Cuándo se frena.** Si durante la activación las horas extras del mes (sin las del conteo inicial) superan las ~25 horas de hoy, o dos lecturas seguidas del tablero muestran que baja la carga diaria o la exactitud, se frena la línea siguiente hasta entender por qué.

## 8.3 OKR

Un OKR (Clase 5) es un objetivo en palabras y unos pocos resultados clave que miden un efecto, no una tarea: armar la planilla, activar el módulo o capacitar son entregables (output) y los resultados clave son lo que cambia gracias a ellos (outcome, 23-10). Dura los 6 meses y se lee en cada Go/No-Go. Los tres resultados clave son los objetivos específicos de la sección 1, con las mismas líneas de base y metas.

**Objetivo: que cada pedido se confirme sabiendo qué hay.**

| Resultado clave | Hoy | Meta | Plazo |
|---|---|---|---|
| Pedidos completos y a tiempo (indicador 1) | 76 % | 90 % | 6 meses |
| Días con producción cargada (indicador 3) | 20 % | 100 % de los días hábiles | 6 meses |
| Horas extras por mes (indicador 4) | ~25 horas | ~12 o 13 horas | 6 meses |

- **Por qué estos tres.** Los pedidos son el efecto sobre el distribuidor; la carga diaria, el hábito que hace posible a los demás; las horas extras, el efecto sobre el costo. Si los pedidos mejoran y las horas no bajan, cae el supuesto 7.
- **Por qué la exactitud de stock (indicador 2) no es un resultado clave.** Su línea de base todavía no existe (sale del conteo inicial) y no es un cambio que busquemos sino una condición que tiene que estar siempre bien. Es un KPI: sigue en el tablero cuando el OKR termina.

## 8.4 Indicadores

Son cuatro, dentro de los tres a cinco que pide la consigna: resultado y experiencia (indicador 1), calidad de datos (2), adopción (3) y eficiencia (4). Cada uno tiene la ficha de ocho elementos de la Clase 5, dice si es de resultado (informa cuando ya pasó) o de avance (informa mientras se puede corregir) y trae su contrapeso, el segundo número que empeora si alguien fuerza el primero (ley de Goodhart). Se encadenan: la carga diaria (3) avisa antes que la exactitud (2), y la exactitud antes que los pedidos (1). Los dueños son roles; falta conversarlos con cada área (sección 6).

### 1. Pedidos completos y a tiempo

| Elemento | Contenido |
|---|---|
| **Título** | Pedidos completos y a tiempo |
| **Propósito** | Que cada pedido de distribuidor salga entero y dentro del plazo: el resultado del objetivo general de la sección 1 |
| **Unidad** | Porcentaje (%) de los pedidos recibidos en la semana |
| **Fórmula** | (pedidos recibidos − pedidos no completos) ÷ pedidos recibidos × 100. No es completo el pedido recortado (sale con menos cantidad de la pedida), el demorado (sale después del plazo estándar de su zona: en la Patagonia, hasta una semana; [dato pendiente: plazo estándar de las zonas fuera de la Patagonia]) ni el rechazado o reprogramado de entrada o cancelado tras el aviso, aunque no llegue a nota de pedido (secciones 1 y 7) |
| **Fuente** | Registro semanal de Oficina (hoja compartida simple), un pedido por línea, con la causa y las columnas de la sección 6. El denominador es el total semanal de pedidos recibidos que Oficina anota en ese registro, incluidos los que no llegan a nota de pedido (rechazados o reprogramados de entrada); el CSV de Discovery solo verifica el resto de los recibidos a medida que se activan las líneas |
| **Frecuencia** | Se anota todos los días; se calcula y se informa por semana |
| **Dueño** | El dueño, que con los hijos decide la producción; Oficina lleva el registro |
| **Meta** | De 76 % a 90 % en 6 meses |

**Meta en una oración** (acción, métrica, valor actual, objetivo y plazo, como en la Clase 5): subir los pedidos completos y a tiempo de 76 % a 90 % en 6 meses.

- **Línea de base:** 76 % (30 recortados o demorados de ~125 en una semana de registro; cuenta nuestra, no un promedio anual). Esa semana contó recortados o demorados: [dato pendiente: si la semana base incluyó rechazados de entrada].
- **Tipo:** de resultado: informa cuando el pedido ya salió. Lo anticipan la carga diaria y la exactitud.
- **Contrapeso:** los pedidos rechazados, reprogramados de entrada o cancelados tras el aviso, como porcentaje de los recibidos. Ya cuentan como no completos, pero verlos aparte muestra si el 90 % es real o si se acomoda la entrada de pedidos. Se mide desde la semana 0.

### 2. Exactitud de stock

| Elemento | Contenido |
|---|---|
| **Título** | Exactitud de stock de producto terminado |
| **Propósito** | Que lo cargado coincida con lo que hay, para confirmar sabiendo qué hay: es la condición de los otros tres indicadores (sección 1) |
| **Unidad** | Porcentaje (%) de los productos contados |
| **Fórmula** | En cada conteo semanal: productos contados cuya diferencia con el stock físico cargado está dentro de la tolerancia ÷ productos contados × 100. La tolerancia provisional es una décima parte de lo contado (sección 7) y se corrige con el conteo inicial. Los productos a contar salen de los activos en Discovery |
| **Fuente** | Hoja de conteo de Depósito contra el stock físico de Discovery (contra la planilla, en el piloto). La diferencia de cada producto queda registrada con su motivo al cargar el ajuste (sección 6) |
| **Frecuencia** | Se calcula y se informa por semana, con el conteo cíclico |
| **Dueño** | El responsable de sistemas, que carga los ajustes. Depósito cuenta (quién, a confirmar) |
| **Meta** | Al menos 9 de cada 10 productos sin diferencia mayor a la tolerancia, en 6 meses (propuesta nuestra, a confirmar con el conteo inicial y con el dueño) |

- **Línea de base:** [dato pendiente: exactitud de stock en el conteo inicial]. Hoy no hay stock cargado contra el cual comparar, así que en el conteo inicial Depósito anota antes de contar cuánto cree que hay de cada producto (a ojo, como hoy), y esa diferencia es la base (propuesta nuestra).
- **Tipo:** de avance: si baja, avisa antes de que un stock equivocado llegue al distribuidor como un pedido recortado.
- **Contrapeso:** la cobertura del conteo, es decir, productos contados sobre productos activos. Si se cuentan solo los productos fáciles, la exactitud sube y la cobertura baja.

### 3. Días con producción cargada

| Elemento | Contenido |
|---|---|
| **Título** | Días con producción cargada |
| **Propósito** | Saber si el dato diario existe: sin carga diaria no hay stock en el que confiar, y es lo primero que avisa si el cambio se adopta |
| **Unidad** | Porcentaje (%) de los días hábiles |
| **Fórmula** | Días hábiles en que todos los turnos que produjeron cargaron su parte (producto y cantidad realmente producida) ese mismo día, al cierre ÷ días hábiles del período × 100. En el piloto, solo papas fritas sobre los 10 días hábiles; en la activación, cada línea activa cuenta por separado |
| **Fuente** | Partes de producción de Discovery, con la fecha de carga (la planilla, en el piloto). Hoy sale del control propio de Producción, que se carga una vez por semana |
| **Frecuencia** | Se ve cada día en la reunión diaria; se calcula y se informa por semana |
| **Dueño** | Producción, por medio del responsable de carga de cada turno. El responsable de sistemas lo calcula |
| **Meta** | De 20 % a 100 % de los días hábiles en 6 meses |

- **Línea de base:** 20 % (hoy se carga 1 vez por semana, o sea 1 de 5 días hábiles).
- **Tipo:** de avance. Avisa mientras hay tiempo: si hoy se cargó poco, mañana el stock será dudoso. El umbral del piloto está en la sección 7.
- **Contrapeso:** la exactitud de stock: si se carga lo planificado o lo estimado solo para completar el día, el conteo lo muestra. El indicador sirve para planificar y dar apoyo, no para evaluar personas (acuerdo con el dueño, sección 5).

### 4. Horas extras por mes

| Elemento | Contenido |
|---|---|
| **Título** | Horas extras por mes (totales) |
| **Propósito** | Medir cuánto cuesta en horas tapar los pedidos que faltaron y la saturación de la planta: el efecto sobre el costo |
| **Unidad** | Horas por mes |
| **Fórmula** | Suma de las horas extras de todo el personal en el mes, sin las del conteo inicial si se pagaron (ver "Cómo se protege la operación"). Son totales: la liquidación no distingue las planificadas de las no planificadas, ni las que tapan la saturación de las que completan pedidos |
| **Fuente** | Liquidación de sueldos del mes, que la empresa ya tiene. En el piloto y la activación se anota además el motivo de cada hora extra (sección 7); el conteo inicial lleva el suyo |
| **Frecuencia** | Mensual, cuando cierra la liquidación |
| **Dueño** | El dueño. Oficina (administración) carga el total en el tablero |
| **Meta** | De ~25 a ~12 o 13 horas por mes en 6 meses |

- **Línea de base:** ~25 horas por mes, dato del relevamiento, sin separar causas.
- **La meta es un supuesto:** la mitad (25 dividido 2), a confirmar con el dueño. Se apoya en el supuesto 7 (al menos la mitad de esas horas es para completar pedidos que faltaron por mezcla y momento); la parte que cubre la saturación no baja, y si el motivo anotado es sobre todo saturación, la meta se revisa.
- **Tipo:** de resultado, y el que llega más tarde: se conoce al cerrar el mes, y en 2 semanas de piloto hay pocas horas para concluir algo.
- **Contrapeso:** pedidos completos y a tiempo (indicador 1): si las horas bajan porque se dejan de hacer las que completaban pedidos, ese indicador baja. Para quien las hace pueden ser además un ingreso (sección 5).

### Cómo se mira el tablero

El tablero es una hoja simple con una fila por semana y una columna por indicador y por contrapeso (sección 6). Arranca en la fase 1, con la semana 0; durante el piloto lo alimentan la planilla y el registro de Oficina, y desde la fase 4 suma el CSV de Discovery. Se actualiza cada semana, y las horas extras cada mes con la liquidación. Cada indicador muestra valor actual, línea de base y meta, con un color: verde si va en camino y rojo si empeora en dos lecturas seguidas. Queda a la vista de Oficina, Producción y Depósito, porque ver el efecto de lo que se carga refuerza el hábito (ADKAR, sección 5); Dirección lo mira al planificar la semana, la reunión diaria mira solo la carga y el disponible, y los cuatro indicadores se leen en el informe al dueño y en cada Go/No-Go.

| Si está en rojo | Se mira primero |
|---|---|
| 1. Pedidos completos y a tiempo | La causa anotada de cada recorte (mezcla y momento, o capacidad) y si la producción cambió con lo visto en la reunión diaria (supuestos 1 y 5) |
| 2. Exactitud de stock | Qué producto difiere semana tras semana, si bajó la carga diaria y si hay reservas viejas sin facturar (sección 6) |
| 3. Días con producción cargada | Capacitación, carga de trabajo, incentivos y reglas, no el compromiso de la gente. Producción y Oficina vuelven a "gestionar de cerca" (sección 5) |
| 4. Horas extras por mes | El motivo anotado. Si bajan los recortes pero no las horas, se revisa el supuesto 7 |

**Fuentes y qué es propuesta nuestra:** secciones 1, 4, 5, 6 y 7 de esta parte; Clase 5, clase del 23-10 y guía de la cátedra. Del grupo vienen además el plazo de 6 meses, las 2 semanas del piloto y la carga diaria como meta. Son propuesta nuestra, a acordar con el dueño: las otras duraciones, los umbrales, las metas, los dueños de cada indicador, el color del tablero y las reglas de freno y de cierre.

---

# 9. Bibliografía

**Herramientas de análisis**

- Doerr, J. (2018). *Measure What Matters*. Portfolio / Penguin.
- Freund, J. y Rücker, B. (2019). *Real-Life BPMN* (4.ª ed.). Camunda.
- Heifetz, R. A. y Laurie, D. L. (1997). The work of leadership. *Harvard Business Review*, 75(1), 124-134.
- Heifetz, R., Grashow, A. y Linsky, M. (2009). *The Practice of Adaptive Leadership*. Harvard Business Press.
- Hiatt, J. M. (2006). *ADKAR: A Model for Change in Business, Government and Our Community*. Prosci.
- Mendelow, A. L. (1981). Environmental scanning: the impact of the stakeholder concept. *Proceedings of the Second International Conference on Information Systems*, 407-418.
- Osterwalder, A. y Pigneur, Y. (2010). *Business Model Generation*. John Wiley & Sons.
- Osterwalder, A., Pigneur, Y., Bernarda, G. y Smith, A. (2014). *Value Proposition Design*. John Wiley & Sons.
- Rogers, D. L. (2023). *davidrogers.digital* [sitio web]. Citado en la Clase 7.
- Savoia, A. (2019). *The Right It*. HarperOne.

**Material de cátedra (UTN FRSR)**

- Cátedra de Gestión Gerencial (2026). Clase 3: Transformación Digital, Madurez Tecnológica y Cartera de Oportunidades.
- Cátedra de Gestión Gerencial (2026). Clase 4: gestión del cambio y liderazgo adaptativo.
- Cátedra de Gestión Gerencial (2026). Clase 5: medir la estrategia (objetivos, OKR, KPI y tablero).
- Cátedra de Gestión Gerencial (2026). Clase 6: modelado de procesos con BPMN.
- Cátedra de Gestión Gerencial (2026). Clase 7: de procesos a estrategia digital.
- Cátedra de Gestión Gerencial (2026). Clase del 05-10: línea de base y procesos balde.
- Cátedra de Gestión Gerencial (2026). Clase del 19-10: evaluación de tecnologías.
- Cátedra de Gestión Gerencial (2026). Clase del 23-10: partes interesadas y roadmap.
- Cátedra de Gestión Gerencial (2026). Trabajo Práctico Final, Parte 2: consigna y guía de ejemplo.

**Fuentes primarias del caso**

- Lepez, J., Geyer, J. J., Lopez, J. y Sorato, E. (2026). *Trabajo Práctico Final - Parte 1: diagnóstico gerencial de Dulxelitos*.
- Relevamiento del proceso de atención de pedidos con un integrante del equipo que trabaja en Dulxelitos (2026), y entrevistas y observación directa del equipo en la organización (Parte 1).

---

# 10. Anexos

## Anexo I: datos pendientes

Lo dejamos escrito en vez de inventar una cifra. Cada uno de estos datos aparece en el texto marcado como «dato pendiente» y acá se juntan sin repetir los que figuran en más de una sección. Algunos salen del primer conteo físico, otros se le preguntan al proveedor o se sacan de la liquidación de sueldos de la empresa.

| Dato | Sección |
|------------------------------------------------------------|----------|
| Si la semana base incluyó rechazados de entrada | 1 y 8 |
| Costo por hora extra | 1, 2, 4, 7 y 8 |
| Exactitud de stock en el conteo inicial | 1, 2 y 8 |
| Cómo entran hoy los pedidos de Aiello y del viajante | 1 |
| Cuántos turnos tiene la planta | 1 |
| Quién decide qué se hace con el faltante y quién autoriza las horas extras | 2 |
| Margen o valor promedio de un pedido recortado | 2 y 4 |
| Costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación | 2, 4, 7 y 8 |
| Versión de Discovery y soporte incluido | 2, 5 y 7 |
| Plazo de activación del módulo | 2, 7 y 8 |
| Costo mensual de la alternativa B | 2, 4, 7 y 8 |
| Responsable del conteo inicial y del semanal | 3, 5, 6, 7 y 8 |
| Cuál responde por el plan semanal | 3 |
| Quién es el responsable de carga de cada turno y su suplente | 3 |
| Quién convoca la reunión diaria y si participa el dueño o un hijo todos los días | 3 |
| Tiempo semanal que el responsable de sistemas puede dedicar al proyecto | 5 y 8 |
| Dónde queda registrada la zona de cada distribuidor | 6 |
| Stock mínimo de cada producto, a fijar con el primer conteo | 6 |
| Qué listado de armado emite Discovery | 6 |
| Listados que Discovery puede exportar | 6 |
| Si el control de producción separa por producto | 7 |
| Pedidos de papas fritas recortados o demorados en la semana 0 | 7 |
| Diferencia en el conteo inicial | 7 |
| En qué orden se activan Dulces y Repostería | 8 |
| Plazo estándar de las zonas fuera de la Patagonia | 8 |
