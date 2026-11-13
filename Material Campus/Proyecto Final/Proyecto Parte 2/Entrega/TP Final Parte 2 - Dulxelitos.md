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

---

# Introducción

Este trabajo es la segunda parte del proyecto integrador de Gestión Gerencial. En la primera hicimos un diagnóstico gerencial de Dulxelitos, una empresa familiar de San Rafael que fabrica, fracciona y distribuye snacks desde 1973. En esta pasamos de diagnosticar a proponer: a partir de ese diagnóstico definimos el problema gerencial priorizado, mapeamos el proceso actual y el futuro, comparamos alternativas y armamos el plan para llevar la mejora a la práctica y medir si funciona.

Uno de los integrantes del grupo trabaja en la empresa, y con él relevamos en detalle el proceso de atención de pedidos de distribuidores. Ese relevamiento aportó más precisión sobre tres puntos: el stock de producto terminado no se registra en ningún lado, los pedidos recortados o demorados se repiten todas las semanas y, según creemos, tienen más que ver con qué se produce y cuándo que con la capacidad de la planta. Sobre esa base armamos la propuesta.

La sección 1 plantea el problema, los objetivos y el alcance; la 2 y la 3 describen el proceso actual y el futuro, con las alternativas que evaluamos; la 4, la 5 y la 6 revisan el modelo de negocio, los actores involucrados y la arquitectura de datos, y la 7 y la 8 explican cómo validar la propuesta con un piloto y cómo medirla. Las cifras de partida salen del relevamiento; las metas, los umbrales y los responsables que proponemos son estimaciones del grupo que habría que acordar con el dueño antes de empezar.

---

# 1. Problema gerencial, objetivos y alcance

A partir del diagnóstico de la Parte 1 definimos el problema gerencial priorizado, sobre la base de un relevamiento más detallado del proceso de atención de pedidos de distribuidores.

## 1.1 Lo que encontramos en el relevamiento

La facturación está en Discovery, pero el stock de producto terminado no se registra en ningún lado. Para saber si hay mercadería se mira en el depósito y se le pregunta a Producción, que lleva su propio control y lo carga una vez por semana, sin relacionarlo con las ventas. El módulo de stock de Discovery está incluido en la licencia y no se usa.

Los pedidos recortados o demorados ocurren todas las semanas: en la semana que registramos fueron 30 de unos 125, de modo que los completos y a tiempo rondaron el 76 %. Falta confirmar con la empresa si esa semana incluyó también los pedidos rechazados de entrada.

La planta está saturada y parte de las horas extras compensa esa carga. Aun así, creemos que los recortes vienen sobre todo de la mezcla y el momento de producción, más que de la capacidad total (supuesto 1): el dueño o los hijos deciden qué producir por criterio propio, sin mirar los pedidos pendientes. Es el supuesto más importante del trabajo y el piloto nos va a dar una primera lectura.

## 1.2 Problema gerencial

> Dulxelitos recorta o demora 30 de unos 125 pedidos semanales porque los acepta sin conocer el stock de producto terminado, que no se registra, y produce sin mirar las ventas. Genera faltantes y parte de las horas extras (unas 25 mensuales) sobre una planta saturada. Éxito: pedidos completos y a tiempo del 76 % al 90 % en 6 meses.

La causa raíz es en parte técnica, porque no hay registro del stock, y en parte de organización, porque ventas y producción no se miran entre sí. "A tiempo" quiere decir dentro del plazo estándar de cada zona (en la Patagonia, hasta una semana), y un pedido rechazado o reprogramado de entrada no cuenta como completo.

La meta del 90 % la fijamos nosotros: en una pyme con la planta al límite siempre va a haber roturas e imprevistos. Si el piloto muestra que la planificación explica menos de lo que suponemos, la revisamos.

## 1.3 Objetivo general

Que cada pedido de distribuidor se confirme sabiendo qué hay en stock y que la producción se planifique contra los pedidos pendientes, para llevar los pedidos completos y a tiempo del 76 % al 90 % en 6 meses. Abarca el proceso "Atender pedido de distribuidor", de la recepción al despacho, y la planificación semanal de producción.

## 1.4 Objetivos específicos

| Objetivo | Métrica | Línea de base | Meta a 6 meses |
|---|---|---|---|
| 1. Confirmar los pedidos sabiendo qué hay en stock | Pedidos completos y a tiempo sobre recibidos, por semana | 76 % | 90 % |
| 2. Cargar la producción todos los días | Días hábiles con producción cargada | 20 % (hoy, una vez por semana) | 100 % |
| 3. Bajar las horas extras | Horas extras por mes, según la liquidación | Unas 25 horas | Unas 12 o 13 horas |

La meta de horas extras supone que al menos la mitad de esas horas se hace para completar pedidos que faltaron (supuesto 7). Las que responden a la falta de capacidad no van a bajar, y como la liquidación no distingue unas de otras, lo vamos a ver recién con los primeros meses de medición. Para pasarlo a pesos falta el costo de la hora extra, que vamos a pedir a liquidación de sueldos.

Hay además un indicador de soporte, la exactitud de stock: si lo cargado no coincide con el conteo físico, ninguno de los otros se sostiene. Su línea de base sale del primer conteo, y las fichas de los cuatro indicadores están en la sección 8.

## 1.5 Alcance

El proceso empieza cuando llega el pedido por WhatsApp o teléfono y termina con el pedido facturado en Discovery y despachado. Incluye también la planificación semanal de producción y el seguimiento con indicadores.

Participan Oficina, Depósito, Producción y Dirección (el dueño y los hijos). El dueño es el sponsor y el responsable de sistemas lidera el proyecto; el diagnóstico de la Parte 1 había marcado la gobernanza digital como una debilidad y la propuesta se la asigna a él. Los distribuidores y el transporte siguen trabajando igual: piden por WhatsApp o teléfono y, si falta algo, se les avisa en el momento.

Los cambios de trabajo son pocos. Producción carga lo producido al cierre de cada turno (falta relevar cuántos turnos tiene la planta), Oficina consulta y reserva el stock antes de confirmar, Dirección planifica la semana mirando los pedidos pendientes y un stock mínimo, y se suman una reunión diaria corta entre ventas y producción y un conteo semanal. Hacen falta disciplina de carga, un responsable de carga por turno con suplente y algunos datos que hoy no existen o están dispersos: el stock físico, las reservas, los pedidos pendientes, el stock mínimo y las horas extras. Todo se apoya en una sola definición:

**stock disponible = stock físico menos lo reservado por pedidos confirmados sin facturar.**

Las herramientas son Discovery, que la empresa ya tiene, y una planilla compartida solo para el piloto (sección 2).

## 1.6 Fuera de alcance

Quedan afuera insumos y packaging, la visibilidad de stock para el distribuidor (para más adelante, junto con la tienda online), la ampliación de la planta, el reemplazo de Discovery por otro sistema, el CRM y el costeo y las listas de precios. También se mantienen manuales a propósito el armado del pedido, que es rápido y no es la restricción, el conteo físico y la decisión de qué producir, que sigue siendo del dueño y los hijos aunque ahora con pedidos y stock a la vista.

---

# 2. Proceso actual y alternativas de solución

Describimos el proceso como funciona hoy, con los volúmenes que relevamos en la empresa.

## 2.1 Matriz de descubrimiento

| Campo | Contenido |
|---|---|
| **Proceso** | Atender pedido de distribuidor |
| **Inicio y fin** | Llega un pedido por WhatsApp o teléfono; termina facturado en Discovery y despachado |
| **Áreas** | Oficina, Depósito, Producción y Dirección (el dueño y los hijos) |
| **Externos** | El distribuidor y, si no hay flota propia, el transporte tercerizado |
| **Volumen** | ~25 pedidos por día, ~125 por semana, con una demanda estable en el año |
| **Camino alternativo frecuente** | Falta producto: 30 de ~125 pedidos recortados o demorados en la semana registrada |
| **Fuera de los límites** | Insumos y packaging, y la visibilidad de stock para el distribuidor |

## 2.2 SIPOC

| Proveedor | Entrada | Proceso | Salida | Cliente |
|---|---|---|---|---|
| Distribuidor | Pedido por WhatsApp o teléfono | Recibir pedido | Pedido anotado | Oficina |
| Depósito y Producción | Pedido anotado, lo que se ve en el depósito y lo que dice Producción | Verificar disponibilidad | Pedido pasado a la lista | Depósito |
| Oficina y Producción | Lista de pedidos y producto terminado | Preparar pedido | Pedido armado, completo o con faltante | Oficina |
| Depósito y Producción | Faltante detectado al armar | Resolver faltante (si falta) | Aviso al distribuidor o producción extra | Distribuidor y Oficina |
| Depósito | Pedido armado | Facturar | Pedido facturado en Discovery | Distribuidor y Depósito |
| Oficina | Pedido facturado | Despachar | Pedido despachado | Distribuidor y transporte |

## 2.3 RECI

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

## 2.4 Diagrama AS-IS

![Proceso AS-IS](../bpmn/as-is.png)

El pedido nace en el mensaje del distribuidor. Oficina lo anota y le pregunta a Producción mientras Depósito mira el stock; con eso pasa el pedido a la lista y Depósito lo prepara. Recién al preparar se sabe si falta algo, y en ese caso el pedido sale incompleto, espera producción o se completa con horas extras. Por otro lado, el dueño o uno de los hijos decide cada semana qué producir sin mirar los pedidos, y Producción registra lo producido una vez por semana. Buena parte del proceso depende de la memoria de las personas. El diagrama completo se adjunta en formato BPMN.

| Aspecto | Hoy |
|---|---|
| Herramientas | WhatsApp, teléfono, papel o planilla, una lista de pedidos, Discovery solo para facturar y el control semanal de Producción |
| Dependencias informales | El pedido vive en el chat o la llamada, la disponibilidad se averigua de palabra y las horas extras se autorizan de forma verbal |
| Dolores y costos | Recortes y demoras todas las semanas, faltantes que aparecen al armar y ~25 horas extras por mes, en parte para completar pedidos |
| Indicadores | Pedidos completos y a tiempo: 76 %. Días con producción cargada: 20 %. Exactitud de stock: no se puede medir, porque no hay stock registrado |

El armado del pedido, en cambio, es rápido y no es el problema.

## 2.5 Tres lentes

Miramos el diagrama desde tres ángulos. En ineficiencias, la disponibilidad se averigua dos veces y el faltante obliga a esperar o a hacer horas extras antes de facturar. En tareas manuales, el mismo pedido se anota tres veces (chat, papel o planilla y lista), con riesgo de error en cada copia. En flujo de datos, Producción, Depósito y ventas no comparten nada: no hay stock registrado y la producción se carga una vez por semana sin cruzarse con los pedidos.

Las tres apuntan a la misma causa, así que más que elegir entre varias oportunidades ordenamos los pasos de una sola solución: un registro de stock cargado todos los días, con una sola regla de stock disponible, primero en una planilla de prueba y después en Discovery.

## 2.6 Alternativas

### Do Nothing: seguir igual

No requiere inversión, pero siguen los recortes semanales, el margen que se pierde en ellos y las horas extras, y la producción se sigue decidiendo a criterio del dueño y los hijos.

### A. Planilla compartida (incremental)

Una planilla de stock de producto terminado donde Producción carga lo producido al cierre de cada turno y Oficina reserva por pedido confirmado, con una reunión diaria corta entre ventas y producción. Cuesta casi nada y se puede probar en 2 semanas con papas fritas, el producto con más faltantes. Sirve para ver si la carga diaria se sostiene, pero no se conecta con Discovery: al facturar hay que descontar a mano y escala mal a todo el catálogo.

### B. Stock de Discovery (intermedia, recomendada)

Activar el módulo de stock de Discovery, que según el relevamiento ya está en la licencia y permite pedidos y reserva, aunque la empresa nunca lo usó. Incluye un conteo inicial, la activación por línea de producto (Salados, Dulces y Repostería), un responsable de carga por turno y un conteo semanal. No hay licencia nueva: el costo está en el conteo, la capacitación, el tiempo de carga y lo que cobre el proveedor por soporte.

Deja un solo registro donde ya se factura, si el módulo funciona como esperamos (supuesto 3), aunque por sí solo no cambia cómo se decide la producción. Como riesgo, en la Parte 1 vimos que Discovery está desactualizado, y todavía no sabemos qué versión usa la empresa, qué soporte incluye ni cuánto cuesta y tarda la activación; se lo vamos a consultar al proveedor.

### C. SaaS de gestión (integral, evaluada y descartada)

Un sistema en la nube para pedidos y stock, con cuota mensual, migración y capacitación. Tendría todo junto y escalaría mejor, pero como Discovery no se integra con otros sistemas habría que cargar en los dos, y tampoco resuelve la disciplina de carga. Reemplazar Discovery está fuera de alcance.

## 2.7 Matriz multicriterio

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

## 2.8 Recomendación

Recomendamos B, con A como piloto de 2 semanas sobre papas fritas: B es la solución de fondo y A sirve para probarla antes de gastar. Si el equipo no sostiene la carga diaria en una planilla simple, tampoco la va a sostener en Discovery. Además, registrar stock sin cambiar cómo se decide producir no baja los recortes (supuesto 5), por eso B va junto con el rediseño de la sección 3. El piloto prueba la carga diaria y da una primera lectura sobre los recortes, y el funcionamiento del módulo lo verifica una prueba técnica (sección 7).

El dueño está dispuesto a invertir si se demuestra el retorno. Como todavía no tenemos los costos para un VAN, usamos un punto de equilibrio: B se paga si las horas extras que evita por mes, al costo de la hora, cubren lo que cuesta por mes. Si para eso alcanza con la meta de unas 12 o 13 horas, cumplirla es suficiente. La cuenta es conservadora, porque no suma el margen de los pedidos que dejan de recortarse.

---

# 3. Proceso futuro (TO-BE)

Así se atendería un pedido con la alternativa recomendada, el stock en Discovery, que antes se prueba durante 2 semanas en una planilla con la misma regla. Respecto de hoy cambia el orden, porque primero se mira qué hay y después se confirma, y la producción pasa a mirar los pedidos.

## 3.1 Diagrama TO-BE

![Proceso TO-BE](../bpmn/to-be.png)

Usa los mismos carriles que el AS-IS, y el ícono de persona marca los pasos que se hacen en Discovery. El diagrama completo se adjunta en formato BPMN.

Oficina carga la nota de pedido una sola vez y consulta el stock disponible. Si hay, reserva y confirma, Depósito arma con la lista que sale de Discovery y la factura consume la reserva. Si no hay, Oficina avisa en el momento con la fecha que Producción confirma en la reunión diaria, y el pedido queda pendiente; si alcanza solo para una parte, esa parte se despacha únicamente si el distribuidor lo acepta. Cada semana Dirección planifica la producción con los pedidos pendientes y un stock mínimo, Producción carga lo producido al cierre del turno y Depósito hace un conteo que, si encuentra diferencias, se ajusta en Discovery.

El diagrama da por ciertas tres cosas que todavía no probamos: que Discovery reserva y la factura consume la reserva (supuesto 3), que la fecha estimada se cumple (supuesto 4) y que la producción se planifica mirando los pedidos (supuesto 5).

## 3.2 Qué cambia

| Paso | Hoy | Con la propuesta |
|---|---|---|
| Registrar el pedido | Se anota tres veces (chat, papel o planilla y lista) | Una sola vez, como nota de pedido en Discovery |
| Saber si hay | Se mira el depósito y se pregunta a Producción; el faltante aparece al armar | Se consulta el stock disponible antes de confirmar |
| Resolver el faltante | Sale incompleto, espera producción o se hacen horas extras | Aviso en el momento, con fecha, y pedido pendiente a la vista |
| Qué se produce | Lo decide el dueño o un hijo sin mirar pedidos | Plan semanal contra pedidos y stock mínimo |
| Cargar lo producido | Una vez por semana | Todos los días, al cierre del turno |
| Horas extras | Una salida habitual del faltante | Excepción del plan semanal, con motivo |

El ingreso por WhatsApp o teléfono, el armado y el despacho siguen igual.

### La regla del stock disponible

Es la misma en la planilla y en Discovery:

**stock disponible = stock físico − reservado por pedidos confirmados sin facturar**

El disponible sube cuando Producción carga lo producido o se libera una reserva, y baja cuando Oficina reserva al confirmar. Al facturar baja el físico pero no el disponible, porque la factura consume la reserva. El conteo semanal ajusta el físico a lo contado.

## 3.3 Responsables y decisiones

| Actividad | Oficina | Depósito | Producción | Dirección | Resp. de sistemas | Distribuidor (externo) |
|---|---|---|---|---|---|---|
| Cargar pedido, consultar y reservar | R/E | – | – | – | – | – |
| Confirmar o avisar faltante con fecha | R/E | I | C | – | – | I |
| Preparar pedido | I | R/E | – | – | – | – |
| Facturar | R/E | C | – | – | – | I |
| Planificar producción de la semana | C | – | C | R/E | – | – |
| Producir y cargar lo producido | I | I | R/E | I | – | – |
| Contar stock | – | R/E | I | – | I | – |
| Ajustar diferencias de conteo | I | C | I | – | R/E | – |
| Reunión diaria ventas–producción | C | – | C | R/E | – | – |
| Actualizar el tablero | C | – | I | I | R/E | – |

El responsable de sistemas no tiene carril en el diagrama porque es un rol, no un área. A diferencia de hoy, el faltante tiene responsables: Oficina avisa, Producción confirma la fecha y Dirección decide si hacen falta horas extras. Oficina no confirma sin mirar el stock, salvo algún día en que el dato no esté al día, y no promete fechas que Producción no confirmó. Dirección sigue decidiendo qué producir, pero primero va lo pedido que no hay y después lo que está bajo el mínimo.

Antes del piloto hay que acordar con el dueño quién responde por el plan semanal, quién hace los conteos (en principio, Depósito), quiénes son los responsables de carga de cada turno y quién convoca la reunión diaria.

## 3.4 Datos y controles

En el proceso nuevo el stock se genera en cinco momentos, todos en Discovery: la nota de pedido, la reserva, el parte de producción, la factura y el ajuste del conteo. Las reglas de datos están en la sección 6.

| Riesgo | Control | Cómo se ve si falla |
|---|---|---|
| Confirmar sin saber qué hay | Consultar el disponible antes de confirmar | Días en que se confirmó sin el dato |
| Producir sin mirar los pedidos | Plan semanal y reunión diaria | Pedidos completos que no suben |
| Stock cargado distinto del real | Conteo semanal; manda lo contado | Exactitud de stock |
| Carga que se corta | Responsable por turno, con suplente | Días con producción cargada |
| Reservas viejas | Revisión semanal de reservas abiertas | Reservas vencidas |
| Horas extras habituales | Solo como excepción del plan | Horas extras por mes |

El seguimiento es un tablero simple de cuatro indicadores que el responsable de sistemas actualiza cada semana (sección 8). Para que la rutina no dependa de la memoria, cada momento tiene una lista corta: al cerrar el turno, cargar lo realmente producido; antes de confirmar, consultar y reservar; y una vez por semana, contar, ajustar con motivo, revisar las reservas y actualizar el tablero. El control más importante es la carga diaria, porque sin ella no hay stock confiable, y por eso su tiempo se reserva dentro del turno.

---

# 4. Modelo de negocio y propuesta de valor

La propuesta cambia sobre todo cómo trabaja la empresa por dentro: la promesa al distribuidor es la misma y lo que mejora es la manera de cumplirla.

## 4.1 Cambios en el BMC

Partimos del canvas de la Parte 1. Las cinco primeras filas son lo que ve el distribuidor (frontstage) y las cuatro últimas, lo interno (backstage).

| Bloque | Hoy | Con la propuesta | ¿Cambia? |
|---|---|---|---|
| Segmentos | Distribuidores mayoristas, sobre todo patagónicos, y Aiello | Los mismos | No |
| Propuesta de valor | Precio y logística para el canal, y aviso cuando falta algo | La misma, mejor cumplida: pedidos completos y un aviso que llega antes | Se refuerza |
| Canales | WhatsApp y teléfono; la tienda web sigue vacía desde 2020 | Iguales; mostrar el stock o terminar la tienda queda para más adelante | No |
| Relación con clientes | El faltante se descubre al armar el pedido | Oficina confirma sabiendo qué hay y avisa en el momento, con fecha | Sí, acotado |
| Fuentes de ingreso | Venta mayorista, a Aiello y de fraccionado | Igual; un pedido recortado es una venta parcial o tardía | No |
| Actividades clave | Se produce por criterio propio y se confirma mirando el depósito | Carga diaria, reserva antes de confirmar, plan semanal contra pedidos, reunión diaria y conteo semanal | Sí, el principal |
| Recursos clave | La planta al límite y el conocimiento de los dueños; el stock no se registra | Un recurso nuevo: el registro de stock de producto terminado | Sí |
| Socios clave | Proveedor de film, materia prima, transporte, distribuidores y Aiello | Se suma el proveedor de Discovery para activar el módulo | Casi no |
| Estructura de costos | Materia prima, packaging, mano de obra (con ~25 horas extras por mes), logística y energía | Sin licencia nueva; se suman tiempo de carga, conteo y capacitación, y se ahorra en horas extras | Sí, poco |

No hay un modelo de negocio nuevo. Cambian a fondo las actividades y los recursos, y en menor medida la relación con clientes y los costos. La capacidad de la planta y los ingresos no se tocan; cuánto margen se pierde por cada pedido recortado queda por calcular.

## 4.2 VPC TO-BE

El segmento es el mismo de la Parte 1, el distribuidor mayorista, sobre todo el patagónico. El relevamiento muestra que los faltantes se repiten todas las semanas, y las papas fritas son el producto que más falta.

| | Del lado del distribuidor | Qué hace la propuesta | Efecto |
|---|---|---|---|
| Dolor | Faltantes | Planificar contra pedidos ataca la causa más probable (supuesto 1) y, si falta algo, se avisa al confirmar | Lo alivia |
| Dolor | No saber si hay stock sin llamar | Oficina responde con el stock registrado | En parte |
| Dolor | Horario acotado y paquetes rotos | Nada, quedan fuera de alcance | No los toca |
| Ganancia | Que le avisen cuando falta algo | El aviso llega en el momento, con fecha | Mejora |
| Ganancia | Entrega previsible y compromiso | Confirmar pasa a significar que hay mercadería o una fecha | Mejora |
| Ganancia | Precio, exclusividad y catálogo | Ninguna acción | Sin cambio |

El único beneficio nuevo es saber cuándo llega lo que falta. Es una promesa nueva sobre una planta saturada y, si no se cumple, el aviso pierde valor (supuesto 4). Como la relación con los distribuidores hoy es buena, el cambio beneficia sobre todo a la empresa.

## 4.3 Supuestos clave

Son lo que damos por cierto sin haberlo probado, agrupado en deseabilidad (si lo van a usar), factibilidad (si se puede hacer) y viabilidad (si se paga).

| # | Supuesto | Tipo | Si es falso |
|---|---|---|---|
| 1 | La mezcla y el momento de producción, más que la capacidad, explican la mayoría de los recortes | Factibilidad (crítico) | Planificar no baja los recortes |
| 2 | Producción carga todos los días y Oficina reserva antes de confirmar, aun con la planta saturada | Factibilidad | No hay stock confiable y se vuelve a mirar el depósito |
| 3 | El módulo de Discovery permite pedidos y reserva, y la factura consume la reserva | Factibilidad | Más costo con el proveedor, o seguir con la planilla |
| 4 | La fecha estimada que se le da al distribuidor se cumple | Factibilidad | El aviso deja de ser confiable |
| 5 | El dueño y los hijos planifican mirando pedidos y stock mínimo | Deseabilidad | Se registra el stock pero se decide igual |
| 6 | Al distribuidor no le molesta más una fecha estimada que un pedido recortado | Deseabilidad | Se resiente una relación que hoy está bien |
| 7 | Al menos la mitad de las horas extras se hace para completar pedidos que faltaron | Viabilidad | La meta de horas extras queda larga |
| 8 | El ahorro en horas extras justifica el costo del cambio | Viabilidad | La inversión no se recupera |
| 9 | La semana registrada (30 de ~125) es representativa | Viabilidad | El problema tiene otro tamaño |

El supuesto 1 decide si la propuesta vale la pena, y el 5 es el cambio más difícil, porque toca cómo decide la dirección. Para el 8 usamos el punto de equilibrio de la sección 2. Cómo se valida cada uno está en la sección 7.

---

# 5. Stakeholders del proyecto de mejora

El dueño aprueba el presupuesto y decide el Go/No-Go, pero el cambio lo sostienen todos los días Producción, Oficina y quienes deciden qué producir. Las resistencias que esperamos surgen del relevamiento.

## 5.1 Mapa de actores

| Actor y rol | Qué hace en el proceso nuevo |
|---|---|
| **Dueño**: sponsor y, con los hijos, decisor de la producción | Aprueba el presupuesto y el Go/No-Go; planifica con pedidos y stock mínimo |
| **Hijos** (dos): decisores de la producción | Planifican la semana con los pedidos pendientes |
| **Responsable de sistemas**: líder | Coordina con el proveedor, capacita, carga los ajustes y sigue los indicadores |
| **Oficina** (4 personas): usuarios clave | Cargan el pedido y reservan antes de confirmar; avisan los faltantes |
| **Producción** (7 personas): usuarios clave | Cargan lo producido al cierre de cada turno |
| **Depósito**: usuarios afectados | Arma como hasta ahora y, en principio, hace el conteo |
| **Buenos Aires Software** (proveedor de Discovery) | Activa el módulo de stock |
| **Distribuidores** (57, de los cuales 35 en la Patagonia): afectados indirectos | Siguen pidiendo igual y reciben el aviso con fecha |

El transporte queda afuera porque no cambia su trabajo. La propuesta le asigna al responsable de sistemas la gobernanza digital, que en el diagnóstico de la Parte 1 aparecía como una debilidad, con un tiempo semanal a acordar con el dueño.

## 5.2 Matriz poder/interés

El poder es cuánto puede un actor ayudar o frenar el proyecto, y el interés, cuánto le importa y le toca el cambio.

| | **Interés bajo** | **Interés alto** |
|---|---|---|
| **Poder alto** | **Mantener satisfecho:** Dueño como sponsor, Buenos Aires Software | **Gestionar de cerca:** Dueño como decisor, Hijos, Responsable de sistemas, Oficina, Producción |
| **Poder bajo** | **Mantener informado:** Distribuidores | **Monitorear y dar voz:** Depósito |

Oficina y Producción tienen poder de hecho, porque cualquiera de las dos frena el proyecto con solo no usarlo. Producción además suma legitimidad y urgencia, así que, en términos de saliencia, es la parte que hay que atender primero.

## 5.3 Estrategias de involucramiento

| Actor | Poder / interés / impacto | Resistencia esperada | Estrategia |
|---|---|---|---|
| **Dueño** | Alto / bajo como sponsor y alto como decisor / medio | Baja como sponsor; como decisor, puede sentir que pierde su criterio | Informes cortos y Go/No-Go acordado de antemano |
| **Hijos** | Alto / alto / alto | Posible: perder peso en la decisión | Siguen decidiendo, con más información, y fijan el stock mínimo |
| **Responsable de sistemas** | Alto (delegado) / alto / alto | Sobrecarga | Asignación formal con tiempo reservado |
| **Oficina** | Alto de hecho / alto / alto | Esperada: suma un paso | Mostrar qué pasos reemplaza y darle un guion para avisar faltantes |
| **Producción** | Alto de hecho / alto / alto | Esperada: poco margen, y las horas extras pueden ser un ingreso | Escucharlos antes de pedir el cambio y reservar el tiempo de carga dentro del turno |
| **Depósito** | Bajo / alto / medio | Baja | Que valide el primer conteo |
| **Buenos Aires Software** | Alto sobre la viabilidad / bajo / bajo | Baja; el riesgo es que el módulo no funcione o el soporte tarde | Probar el módulo con un producto antes de escalar |
| **Distribuidores** | Bajo / bajo / bajo | No relevada (supuesto 6) | Informar que el aviso llega al confirmar, con fecha |

La parte técnica del cambio (qué se carga, cuándo y en qué pantalla) se resuelve con capacitación. La parte adaptativa, en términos de Heifetz, es otra cosa: que Producción haga lugar a una tarea nueva en una planta sin margen, que Oficina aprenda a decir "hay en tal fecha" y, sobre todo, que el dueño y los hijos pasen de decidir por experiencia a decidir con información. Ese último es el cambio de fondo (supuesto 5), y por eso el piloto empieza con un solo producto.

Para acompañar a cada grupo usamos FUD (miedo, incertidumbre y duda) y ADKAR. En Producción el miedo es tener más trabajo y que el dato se use para señalar a alguien, así que acordamos con el dueño que sirve para planificar y no para evaluar personas. En Oficina el miedo es que el aviso enoje al distribuidor; el guion y la fecha confirmada en la reunión diaria ayudan. En la dirección el punto débil es la conciencia del problema: perciben los pedidos incompletos como algo poco frecuente, pero en la semana relevada fueron 30 de alrededor de 125. El refuerzo lo da el tablero a la vista.

La negociación busca un intercambio con cada uno: Producción reemplaza su control semanal por la carga diaria, Oficina hace una consulta en lugar de dos y carga el pedido una sola vez, y los hijos miran pedidos a cambio de que la decisión siga siendo suya.

## 5.4 Cómo cambia por fase

La matriz se revisa en cada Go/No-Go, porque algunos actores cambian de cuadrante según la fase del roadmap (sección 8). En la tabla, Cerca, Satisfecho y Voz abrevian los cuadrantes de la matriz.

| Actor | Preparación | Piloto | Go/No-Go | Activación por línea | Estabilización |
|---|---|---|---|---|---|
| Dueño como sponsor | Cerca | Satisfecho | Cerca | Satisfecho | Satisfecho |
| Decisores y responsable de sistemas | Cerca | Cerca | Cerca | Cerca | Cerca |
| Oficina y Producción | Voz | Cerca | Cerca | Cerca | Satisfecho |
| Buenos Aires Software | Satisfecho | Satisfecho | Satisfecho | Cerca | Satisfecho |

En la estabilización Oficina y Producción pierden interés por la rutina, pero conservan el poder de dejar de cargar; si baja la carga diaria, vuelven a gestionarse de cerca. Depósito y los distribuidores no cambian de lugar en ninguna fase.

---

# 6. Arquitectura conceptual y flujo de datos

Para una pyme de 15 a 20 personas alcanza con un flujo simple sobre un solo sistema, y la empresa ya lo tiene: Discovery. Se suman una planilla compartida, solo durante el piloto, y un tablero de cuatro indicadores. No hay sistema nuevo, ni integraciones automáticas, ni canal nuevo.

## 6.1 Diagrama

![Arquitectura y flujo de datos](../diagramas/arquitectura.png)

Oficina carga pedidos y reservas, Producción lo producido y Depósito la hoja del conteo, que el responsable de sistemas carga como ajuste. Todo entra a Discovery, de donde sale la lista de armado. La planilla va punteada porque solo existe en el piloto, y el distribuidor sigue pidiendo por WhatsApp o teléfono sin ver el stock. El flujo también se adjunta en una versión interactiva.

El diagrama supone que el módulo de stock de Discovery permite pedidos y reserva y que la factura consume la reserva (supuesto 3). Si no fuera así, el mismo flujo funciona con la planilla.

## 6.2 Datos

| Dato | Tipo | Origen y destino | Uso | Responsable |
|---|---|---|---|---|
| **Productos** | Maestro | Ya están en Discovery | Que pedido, parte y conteo hablen del mismo producto | Responsable de sistemas, a pedido de Dirección |
| **Distribuidores** y su zona | Maestro | Ya están en Discovery; falta ver dónde queda la zona | Saber quién pide y qué plazo de entrega le corresponde | Oficina |
| **Stock mínimo por producto** | Maestro | De Dirección a Discovery, o a una lista aparte si el módulo no lo admite | Planificar la producción | Dirección y responsable de sistemas |
| **Notas de pedido** | Transaccional | Del WhatsApp o el teléfono a Discovery | Confirmar, armar y facturar | Oficina |
| **Reservas** | Transaccional | De la nota confirmada | Calcular el disponible | Oficina |
| **Partes de producción** | Transaccional | De Producción a Discovery, al cierre del turno | Tener el stock físico al día | Responsable de carga del turno |
| **Conteos físicos** | Transaccional | De la hoja de Depósito a un ajuste en Discovery | Ajustar el stock y medir la exactitud | Depósito y responsable de sistemas |
| **Facturas** | Transaccional | De la nota confirmada | Cobrar y consumir la reserva | Oficina |
| **Registro semanal de recortes** | Seguimiento | De Oficina al tablero | Indicador de pedidos completos | Oficina |
| **Horas extras del mes** | Seguimiento | De la liquidación de sueldos al tablero | Indicador de horas extras | Oficina (administración) |

El registro de recortes lleva una línea por pedido con el producto que faltó, qué pasó y el motivo, e incluye los pedidos que ni siquiera llegan a cargarse, porque forman parte del total. El stock disponible no lo carga nadie: lo calcula Discovery, o la planilla en el piloto, con la regla de la sección 3.

## 6.3 Integraciones

No hay integraciones automáticas. Discovery no se puede integrar con otros sistemas, y tampoco hace falta: son pocas cargas por día y lo que falta es el dato, no la conexión. Todo es carga manual controlada y una exportación a CSV para el tablero.

| Flujo | Cómo y cuándo | Control |
|---|---|---|
| Pedido → Discovery | Carga manual al recibirlo; reserva al confirmar | No se confirma sin ver el disponible |
| Producción → Discovery | Parte diario al cierre del turno | Lo muestra el indicador de días con producción cargada |
| Discovery → Depósito | Lista de armado al confirmar | Solo se arma lo confirmado |
| Depósito → Discovery | Hoja de conteo y ajuste, una vez por semana | La diferencia queda registrada y da la exactitud |
| Discovery → tablero | Exportación CSV semanal (en el piloto, desde la planilla) | Si no coincide, manda Discovery |
| Recortes y horas extras → tablero | Carga manual, semanal y mensual | Un pedido por línea; el total de la liquidación |

Damos por hecho que Discovery exporta a CSV; si no pudiera, los números del tablero son pocos y se pasan a mano. WhatsApp tampoco se integra, porque pediría una API que no existe y un CRM que está fuera de alcance.

## 6.4 Reglas de datos

Las reglas cubren los datos críticos (stock, reservas, productos, distribuidores y stock mínimo) y son simples a propósito, para que una empresa de este tamaño las pueda cumplir.

1. Un solo lugar por dato. Pedidos y stock viven en Discovery; la planilla existe solo en el piloto y después se archiva, para no tener dos fuentes.
2. Nada se borra. Un error se arregla con un movimiento nuevo y un motivo escrito.
3. Manda lo contado. Si el conteo y Discovery no coinciden, se ajusta Discovery.

Cada rol carga lo suyo: Oficina los pedidos, las reservas, las facturas y los distribuidores; Producción los partes; Depósito la hoja de conteo; y el responsable de sistemas los productos, el stock mínimo, los ajustes y los permisos. Los productos nuevos los da de alta el responsable de sistemas a pedido de Dirección, y los distribuidores, Oficina, buscando antes que no estén ya cargados. Quien carga un dato es quien lo arregla, en lo posible el mismo día. Los productos y distribuidores que dejan de usarse quedan inactivos, y nunca se borra un código con movimientos. Oficina revisa cada semana las reservas abiertas: las que pasaron el plazo de su zona se confirman con el distribuidor y se facturan o se liberan. Si Discovery no permite separar los permisos de esta forma, las reglas se sostienen por procedimiento y se revisan en cada Go/No-Go.

---

# 7. Validación de supuestos

Antes de invertir en el módulo de stock hacemos dos pruebas baratas: un piloto de 2 semanas con papas fritas sobre una planilla compartida y una prueba técnica del módulo con ese mismo producto. Lo primero que queremos saber es si los recortes vienen de la mezcla y el momento de producción (supuesto 1).

## 7.1 Supuestos críticos

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

## 7.2 Piloto

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

## 7.3 Criterio de decisión

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

---

# 8. Roadmap, OKR e indicadores

El cambio se hace en cinco fases a lo largo de 6 meses, con una decisión principal al terminar el piloto y después una línea de producto por vez.

## 8.1 Roadmap

| Fase | Hito y entregables | Responsable y recursos | Semanas | Depende de | Go/No-Go |
|---|---|---|---|---|---|
| 1. Preparación | Umbrales acordados, papas fritas contadas, planilla y tablero armados, semana 0 medida y prueba técnica hecha | Responsable de sistemas, con Oficina y Depósito | 1 a 3 | Respaldo del dueño | El dueño confirma que todo está listo |
| 2. Piloto | 10 días con carga diaria, reserva y reunión diaria; primer tablero | Responsable de sistemas; Producción y Oficina | 4 y 5 | Fase 1 | Se puede cortar en cualquier momento |
| 3. Go/No-Go | Hoja de decisión con el piloto, la prueba técnica y el punto de equilibrio | Decide el dueño | 6 | Costos del proveedor y de la hora extra | Go, Go con ajustes, No-Go o no se concluye |
| 4. Activación por línea | Salados primero y después Dulces y Repostería, cada una con conteo, carga y capacitación | Responsable de sistemas y proveedor; tiempo de las áreas | 7 a 22 | Go de la fase 3 y plazo del proveedor | Las medidas del piloto, línea por línea |
| 5. Estabilización | Rutina sin apoyo del proyecto, lectura del OKR y cierre | Responsable de sistemas | 23 a 26 | Líneas activadas | El dueño decide si sigue, revisa las metas o frena |

La fase 4 es la más incierta, porque depende de cuánto tarden el proveedor y cada línea: si no alcanza el tiempo, se activan menos líneas sin acortar el seguimiento, y la meta del 90 % se revisa en el cierre. Si el piloto se repite, todo se corre 2 semanas. El orden de Dulces y Repostería y el plazo de entrega de las zonas fuera de la Patagonia los define el dueño durante la preparación.

Visto como ahora, próximo y más adelante: ahora son las fases 1 a 3; lo próximo, la activación y la estabilización, que dependen del Go/No-Go; y más adelante, sin fecha, la visibilidad de stock para el distribuidor y la tienda online, cuando la exactitud se sostenga.

En cada Go/No-Go decide el dueño, con los umbrales de la sección 7 acordados de antemano. Si al cierre se llegó a las metas, el OKR termina y los indicadores siguen como KPI permanentes. Si no, se busca la causa, y la meta se revisa si los recortes no se explicaban por qué se produce y cuándo (supuesto 1) o si las horas extras eran sobre todo por falta de capacidad (supuesto 7).

Para la implementación, el dueño presenta el proyecto al equipo al empezar el piloto y la activación, la capacitación se hace en el puesto con pedidos reales y cada línea nueva repite el mismo procedimiento de una hoja. La evaluación se hace en cada Go/No-Go y el escalamiento es de a una línea por vez.

## 8.2 Cómo se protege la operación

La prioridad es seguir despachando: si cargar o contar choca con la operación, se corre una fecha. No se suma una tarea sin sacar otra, ya que la carga diaria reemplaza el control semanal de Producción y Oficina pasa a hacer una consulta en lugar de dos. Los conteos iniciales se hacen en fin de semana y sus horas no se cuentan en el indicador de horas extras. Cada turno tiene un responsable de carga con suplente y Oficina una segunda persona que sepa reservar; el responsable de sistemas, que concentra muchas tareas, también necesita un suplente. Si un día el dato no está al día, Oficina confirma como siempre, y si una línea falla, solo esa vuelve atrás. La atención a los distribuidores y la cobranza no cambian en ninguna fase. La línea siguiente se frena si las horas extras superan las de hoy o si el tablero muestra dos semanas seguidas de baja en la carga o en la exactitud.

## 8.3 OKR

El OKR dura los 6 meses y se lee en cada Go/No-Go. Sus resultados clave son los objetivos específicos de la sección 1 y miden el resultado del cambio, no la actividad.

**Objetivo:** que cada pedido se confirme sabiendo qué hay.

| Resultado clave | Hoy | Meta a 6 meses |
|---|---|---|
| Pedidos completos y a tiempo | 76 % | 90 % |
| Días con producción cargada | 20 % | 100 % |
| Horas extras por mes | ~25 horas | ~12 o 13 horas |

La exactitud de stock queda fuera del OKR porque es una condición permanente y su base sale del primer conteo, pero sigue en el tablero.

## 8.4 Indicadores

Cada indicador tiene un contrapeso, es decir, un segundo número que empeora si alguien fuerza el primero (ley de Goodhart).

### 1. Pedidos completos y a tiempo

| Elemento | Contenido |
|---|---|
| **Fórmula** | Pedidos completos y a tiempo ÷ pedidos recibidos en la semana × 100. No cuentan como completos los recortados, los demorados ni los rechazados, reprogramados o cancelados |
| **Fuente y frecuencia** | Registro de Oficina; se anota a diario y se informa por semana |
| **Responsable** | El dueño, con los hijos; Oficina lleva el registro |
| **Meta** | 90 % en 6 meses |

- **Línea de base:** 76 % (30 recortados o demorados de alrededor de 125 en una semana).
- **Tipo:** de resultado; lo anticipan la carga diaria y la exactitud.
- **Contrapeso:** el porcentaje de rechazados, reprogramados o cancelados, para ver si la mejora es real o se acomoda la entrada.

### 2. Exactitud de stock

| Elemento | Contenido |
|---|---|
| **Fórmula** | Productos contados sin diferencia mayor a la tolerancia ÷ productos contados × 100 |
| **Fuente y frecuencia** | Hoja de conteo de Depósito contra Discovery (o la planilla); semanal |
| **Responsable** | El responsable de sistemas |
| **Meta** | Al menos 9 de cada 10 productos dentro de la tolerancia en 6 meses |

- **Línea de base:** sale del primer conteo físico, antes del piloto.
- **Tipo:** de avance; avisa antes de que un error de stock llegue al distribuidor.
- **Contrapeso:** la cobertura del conteo, para que no se cuenten solo los productos fáciles.

### 3. Días con producción cargada

| Elemento | Contenido |
|---|---|
| **Fórmula** | Días hábiles en que todos los turnos cargaron lo producido ÷ días hábiles × 100 |
| **Fuente y frecuencia** | Partes de producción en Discovery (o la planilla); se ve en la reunión diaria y se informa por semana |
| **Responsable** | Producción, con el responsable de carga de cada turno |
| **Meta** | 100 % de los días hábiles en 6 meses |

- **Línea de base:** 20 %; hoy se carga una vez por semana.
- **Tipo:** de avance; es lo primero que muestra si el cambio se adopta.
- **Contrapeso:** la exactitud de stock, porque cargar lo planificado en vez de lo producido aparece en el conteo. El indicador se usa para planificar, no para evaluar personas.

### 4. Horas extras por mes

| Elemento | Contenido |
|---|---|
| **Fórmula** | Total de horas extras del mes, sin las de los conteos iniciales |
| **Fuente y frecuencia** | Liquidación de sueldos, mensual |
| **Responsable** | El dueño; Oficina las carga en el tablero |
| **Meta** | Unas 12 o 13 horas por mes en 6 meses |

- **Línea de base:** unas 25 horas por mes, sin separar causas. El costo de la hora extra se pide a liquidación de sueldos.
- **Tipo:** de resultado y el más lento; en 2 semanas de piloto dice poco.
- **Contrapeso:** pedidos completos y a tiempo, que caería si se dejan de hacer las horas que completaban pedidos.

### Cómo se mira el tablero

El tablero es una hoja simple con una fila por semana y una columna por indicador y contrapeso, con el valor, la línea de base, la meta y un color: verde si va en camino y rojo si empeora dos semanas seguidas. Queda a la vista de Oficina, Producción y Depósito, porque ver el efecto de lo que se carga ayuda a sostener el hábito. Si algo se pone en rojo, primero se miran las causas anotadas y si la rutina se está cumpliendo; en el caso de la carga diaria, se revisan la capacitación, la carga de trabajo, los incentivos y las reglas antes que el compromiso de la gente.

---

# 9. Bibliografía

**Herramientas de análisis**

- Doerr, J. (2018). *Measure What Matters*. Portfolio / Penguin.
- Freund, J. y Rücker, B. (2019). *Real-Life BPMN* (4.ª ed.). Camunda.
- Goodhart, C. A. E. (1975). Problems of monetary management: the U.K. experience. *Papers in Monetary Economics*, 1. Reserve Bank of Australia.
- Heifetz, R. A., Grashow, A. y Linsky, M. (2009). *The Practice of Adaptive Leadership*. Harvard Business Press.
- Heifetz, R. A. y Laurie, D. L. (1997). The work of leadership. *Harvard Business Review*, 75(1), 124-134.
- Hiatt, J. M. (2006). *ADKAR: A Model for Change in Business, Government and Our Community*. Prosci.
- Mendelow, A. L. (1981). Environmental scanning: the impact of the stakeholder concept. *Proceedings of the Second International Conference on Information Systems*, 407-418.
- Mitchell, R. K., Agle, B. R. y Wood, D. J. (1997). Toward a theory of stakeholder identification and salience: defining the principle of who and what really counts. *Academy of Management Review*, 22(4), 853-886.
- Osterwalder, A. y Pigneur, Y. (2010). *Business Model Generation*. John Wiley & Sons.
- Osterwalder, A., Pigneur, Y., Bernarda, G. y Smith, A. (2014). *Value Proposition Design*. John Wiley & Sons.
- Rogers, D. L. (2023). *The Digital Transformation Roadmap: Rebuild Your Organization for Continuous Change*. Columbia Business School Publishing.
- Savoia, A. (2019). *The Right It*. HarperOne.

**Fuentes primarias del caso**

- Lepez, J., Geyer, J. J., Lopez, J. y Sorato, E. (2026). *Trabajo Práctico Final - Parte 1: diagnóstico gerencial de Dulxelitos*.
- Relevamiento del proceso de atención de pedidos con un integrante del equipo que trabaja en Dulxelitos (2026), y entrevistas y observación directa del equipo en la organización (Parte 1).
