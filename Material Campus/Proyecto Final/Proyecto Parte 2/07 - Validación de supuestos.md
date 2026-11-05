# Validación de supuestos

Esta sección dice qué hay que aprender antes de invertir, cómo aprenderlo barato y qué resultado hace avanzar o frenar. Parte de los nueve supuestos de la sección 4 y de la corrección de la sección 1: el stock de producto terminado no se registra, y los recortes vienen de la mezcla y el momento de producción, no de la capacidad total. Esto último es una hipótesis razonada, no un dato, y es lo primero que hay que probar.

Adelantamos la conclusión: **antes de gastar en el stock de Discovery hacemos dos pruebas baratas.** Un piloto de 2 semanas con papas fritas en una planilla compartida, que muestra si la rutina se sostiene y si planificar contra pedidos baja los recortes, y una prueba técnica de Discovery sobre un solo producto. Los umbrales de decisión son una propuesta nuestra, no un dato de la empresa, y el dueño tiene que acordarlos antes de arrancar. Lo que el piloto no puede probar queda para el Go/No-Go posterior a la activación (sección 8).

## Supuestos críticos

Son los nueve de la sección 4, con su número. **Probabilidad** es la de que el supuesto resulte falso e **impacto** lo que le pasa a la propuesta si lo es; son juicio nuestro (alta, media o baja), no mediciones. La **etapa** es la principal de las cuatro de validación de la Clase 7 (Rogers): problema, solución, producto y negocio, que son iterativas y se superponen.

### El riesgo de cada supuesto

| # | Supuesto | Tipo y etapa | Prob. de ser falso | Impacto si es falso | Señal temprana |
|---|---|---|---|---|---|
| 1 | La mezcla y el momento de producción, y no la capacidad total, explican la mayoría de los recortes | Factibilidad (crítico) · Problema | Media | Alto | En la semana 0, la mayoría de los recortes se anota como "no alcanzaba la planta" |
| 2 | Producción carga todos los días, y oficina consulta y reserva antes de confirmar, aun con la planta saturada | Factibilidad · Producto | Alta | Alto | Días sin carga al cierre de turno; la planilla no coincide con lo que se ve a ojo |
| 3 | El módulo de stock de Discovery permite pedidos y reserva, y la factura consume la reserva, con el mismo criterio de disponible | Factibilidad · Producto | Media | Medio | El proveedor no lo confirma por escrito, o un paso de la prueba falla |
| 4 | La fecha estimada que se da al distribuidor se cumple, con la planta saturada | Factibilidad · Producto | Media | Alto | Producción no confirma la fecha en la reunión diaria, o una fecha se pasa |
| 5 | Dueño e hijos deciden la producción mirando pedidos pendientes y stock mínimo, y no solo por criterio propio | Deseabilidad · Solución | Media | Alto | La reunión diaria no cambia lo que se produce con pedidos sin cubrir |
| 6 | Al distribuidor no le resulta peor una fecha estimada al confirmar que recibir el pedido recortado | Deseabilidad · Solución | Baja | Medio | El distribuidor cancela, reprograma o reclama cuando oye la fecha |
| 7 | Al menos la mitad de las ~25 horas extras por mes es por pedidos que faltaron por mezcla y momento | Viabilidad · Negocio | Media | Medio | El motivo de las horas extras es sobre todo "saturación"; no bajan aunque los recortes sí |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo de implementar y sostener el cambio | Viabilidad · Negocio | Media | Alto | El punto de equilibrio pide evitar más horas extras que las ~25 de hoy |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa | Viabilidad · Problema | Media | Medio | El total semanal de la semana 0 o del piloto se aleja del registrado |

El 2 es alta porque hoy producción carga 1 de cada 5 días (20 %) y esperamos resistencia. El 6 es baja porque el distribuidor ya recibe avisos y pedidos incompletos sin quejarse.

### Cómo se valida cada uno

| # | Mecanismo de validación ágil | Qué se anota | Se contesta en |
|---|---|---|---|
| 1 | Anotar la causa de cada recorte de papas fritas en la semana 0 y ver si bajan al planificar contra pedidos | Mezcla y momento, capacidad u otra | Semana 0 y piloto |
| 2 | Contar los días con carga y las diferencias de conteo | Los días en que la planilla falló y se confirmó como hoy | Piloto |
| 3 | Probar un producto de punta a punta y consultar por escrito a Buenos Aires Software | Cada paso y las respuestas del proveedor | Prueba técnica |
| 4 | Producción confirma la fecha en la reunión diaria | Cada aviso con su fecha y si se cumplió | Piloto |
| 5 | Pedirle al dueño y a los hijos que fijen el stock mínimo | Si la reunión cambió lo que se produjo de papas fritas | Piloto, señal inicial |
| 6 | Observar cómo reacciona el distribuidor a cada aviso | Acepta, espera, cancela o reclama | Piloto |
| 7 | Registrar el motivo de cada hora extra | Completar un pedido que faltó, saturación u otro | Piloto como señal; después, la liquidación de sueldos |
| 8 | Completar el punto de equilibrio de la sección 4 | El tiempo de carga, reserva y reunión (costo en horas) | Datos de costo y consulta al proveedor |
| 9 | Repetir el registro semanal de todos los productos, con el mismo criterio | El total de la semana | Semana 0 y piloto |

El piloto contesta, al menos en parte, siete de los nueve. El 3 tiene su prueba técnica y el 8 depende de dos datos que faltan: [dato pendiente: costo mensual de la alternativa B] y [dato pendiente: costo por hora extra]. Van primero los de impacto alto y probabilidad media o alta (1, 2, 4, 5 y 8).

## Piloto

Según la Clase 7, un MVP no es una versión beta ni una versión light del producto final: es el experimento mínimo necesario para validar una hipótesis, y el nuestro es **funcional** (funciona, en pequeño). Tiene espíritu de pretotipo, que busca construir lo correcto antes de construirlo bien (Savoia), y la prueba técnica de Discovery cumple el papel del prototipo; van en paralelo, no una después de la otra.

### Hipótesis en una hoja

Plantilla de la Clase 7, que afina la hipótesis de la sección 2 con los umbrales de "Qué se mide".

| Elemento | Contenido |
|---|---|
| **Problema** | Dulxelitos recorta o demora unos 30 de ~125 pedidos por semana, de cualquier producto, porque confirma sin saber qué hay y produce sin mirar los pedidos. Las papas fritas son lo que más falta |
| **Hipótesis de solución** | Creemos que una planilla compartida con el stock de papas fritas, la carga diaria de lo producido, la reserva por pedido confirmado y una reunión diaria de ~10 minutos resolverá los recortes y demoras de papas fritas para oficina, producción y quienes deciden qué producir, y sabremos que funciona cuando se cumplan los cuatro umbrales de "Qué se mide": carga en 8 de los 10 días hábiles, recortes a la mitad o menos que en la semana 0, conteos dentro de la tolerancia y fechas cumplidas |
| **Tipo de MVP** | Funcional |
| **Experimento mínimo** | Dos semanas con papas fritas solamente y la rutina de "Cómo se corre". Los demás productos siguen como hoy |
| **Etapa de validación** | **Producto**: ¿podemos entregar una solución que se use? Toca también **Problema** (¿la causa es la que creemos?) y, en parte, **Solución** (¿el distribuidor ve valor en un aviso con fecha?). No toca **Negocio**: espera a los datos de costo y a la activación |

### Cómo se corre

- **Cuándo y qué.** Una semana 0 para medir la línea de base y después 2 semanas (10 días hábiles), solo con papas fritas, el producto que más falta según el relevamiento. Un solo producto protege la operación y alcanza para aprender. Puede empezar cuando se quiera, con el conteo inicial hecho el fin de semana anterior.
- **La regla.** Stock disponible es el stock físico menos lo reservado por pedidos confirmados sin facturar, la misma que se usaría en Discovery.
- **La rutina.** Producción carga lo producido al cierre de turno, con un responsable y un suplente. Oficina consulta y reserva antes de confirmar un pedido con papas fritas; si no alcanza, avisa con una fecha que producción confirmó. Al facturar, baja el stock físico y se libera la reserva, a mano porque la planilla no habla con Discovery. Hay un conteo físico al arrancar y uno por semana, y una reunión diaria de ~10 minutos entre ventas y producción para mirar el disponible, los pedidos y los avisos, y decidir qué producir.
- **Vuelta atrás.** Si un día la planilla no está al día, oficina confirma como hoy, a ojo y preguntando a producción, y se anota el día. El piloto se corta cuando se quiera: no toca Discovery ni el armado de pedidos.
- **Quién.** El dueño, como sponsor, acuerda los umbrales y respalda el arranque. El responsable de sistemas, como líder, arma la planilla y junta las medidas. Producción carga; oficina reserva y avisa. Conteo físico: [dato pendiente: quién lo hace].

### Qué se mide

Cuenta como **recortado o demorado** un pedido con papas fritas que sale con menos cantidad de la pedida o después del plazo estándar de su zona. Como en la sección 1, uno rechazado o reprogramado de entrada, o cancelado después del aviso, también cuenta: si no, el número mejoraría empujando pedidos afuera. El criterio es el mismo en la semana 0 y en el piloto.

| Medida | Cómo se mide | Línea de base | Umbral para un Go | Por qué ese umbral |
|---|---|---|---|---|
| **Días con producción de papas fritas cargada** | Días con carga al cierre de turno sobre los 10 días hábiles | 20 % de los días: hoy se carga 1 vez por semana [dato pendiente: si el control de producción separa por producto] | 8 de los 10 días o más | La meta de la sección 1 es todos los días; en un primer intento dejamos 2 días de margen |
| **Pedidos de papas fritas recortados o demorados** | Promedio por semana de las 2 del piloto, del registro semanal | Se mide en la semana 0: [dato pendiente: pedidos de papas fritas recortados o demorados en la semana 0]. Los 30 de ~125 son de todos los productos y no sirven de base para uno | La mitad o menos que en la semana 0, y que los rechazados, reprogramados de entrada o cancelados tras el aviso, que cuentan en el total, no suban | La meta de la sección 1 lleva los pedidos completos y a tiempo del 76 % al 90 %: queda 1 recortado de cada 10 (100 menos 90), menos de la mitad de los ~24 % de hoy. Pedimos la mitad como señal del rumbo, por ser un producto y 2 semanas |
| **Diferencias de conteo** | Conteo físico de papas fritas contra la planilla, al arrancar y al final de cada semana | [dato pendiente: diferencia en el conteo inicial] | En los conteos semanales, una diferencia de hasta una décima parte de lo contado | La meta de exactitud se fija con el primer conteo (sección 1): esta tolerancia es provisional |
| **Fecha estimada cumplida** | Cada aviso con fecha: si el pedido se completó ese día | No existe hoy: el aviso no trae fecha | 4 de cada 5 avisos o más; si hubo pocos, se revisan uno por uno | Es una promesa nueva: si falla más de 1 vez de cada 5, el aviso pierde su valor. No pedimos todas por la planta saturada |

Lo demás que se anota está en la tabla de mecanismos. Como control, se compara con los demás productos en las mismas semanas: si los recortes bajan en todos por igual, la mejora no es del piloto. Si la semana 0 casi no tiene recortes de papas fritas, la comparación no distingue mejora de azar: se mide otra semana, como adelantó la sección 2.

### Prueba técnica de Discovery

Es la prueba del supuesto 3: nuestro compañero que trabaja en la empresa sabe que Discovery permite pedidos y reserva, pero nadie lo usó en Dulxelitos. La lleva el responsable de sistemas con Buenos Aires Software, en la preparación y en paralelo con la semana 0, y su resultado entra al Go/No-Go junto con el del piloto. Se prueba **un solo producto**, el mismo del piloto, en cinco pasos:

| Paso | Qué se verifica | Resultado esperado |
|---|---|---|
| 1. Ingreso de stock | Cargar el stock inicial | Queda registrado el stock físico |
| 2. Pedido y reserva | Cargar una nota de pedido y reservar | La reserva aparece contra el pedido |
| 3. Disponible | Consultar cuánto hay | Es el stock físico menos lo reservado, como en la planilla |
| 4. Factura | Facturar el pedido | La factura baja el stock físico y consume la reserva |
| 5. Corrección | Anular o modificar el pedido | La reserva se libera |

Por escrito se le pregunta a Buenos Aires Software qué versión es y qué soporte incluye ([dato pendiente: versión de Discovery y soporte incluido]), cuánto cuesta activar y capacitar ([dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]), en cuánto tiempo ([dato pendiente: plazo de activación del módulo]) y si hay ambiente de prueba, que importa por el paso 4: una factura de prueba en el sistema real puede quedar como una factura verdadera. Sin ambiente de prueba, ese paso se verifica con el primer pedido real de la activación.

**La prueba pasa** si los cinco pasos funcionan. Si algo falla, se pregunta al proveedor si se configura y cuánto cuesta; si no se puede, se sigue con la alternativa A.

## Criterio de decisión

Las reglas se acuerdan con el dueño **antes de arrancar**: él decide el Go/No-Go, y fijar el criterio después del resultado invita a leerlo a favor. Los umbrales son una propuesta nuestra, sin dato de la empresa que los respalde, y se ajustan con el dueño y con la semana 0.

| Qué pasó | Qué significa | Decisión |
|---|---|---|
| Se cumplen los cuatro umbrales (incluido que los rechazados no suban) y la prueba técnica pasa | Rutina sostenida, mezcla como causa y módulo que funciona | **Go.** Activar Discovery por línea de producto, con la misma rutina, si además el punto de equilibrio de la sección 4 cierra con los datos de costo |
| Se cumplen la carga y los recortes, pero fallan el conteo o la fecha | La rutina anda; el dato o la promesa necesitan ajuste | **Go con ajustes.** Corregir capacitación, responsable o regla de fecha y repetir una sola vez |
| La carga no llega a 8 de los 10 días | La rutina no se sostiene | **No-Go.** B no se gasta: una herramienta mejor no arregla un problema de disciplina. Se revisan capacitación, carga de trabajo, incentivos y reglas, no el compromiso de la gente (sección 5) |
| La carga anda, los recortes no bajan a la mitad y las causas anotadas son sobre todo de capacidad | El supuesto 1 cae | **No-Go** de B para este problema; se revisa la meta de la sección 1, porque lo que queda es un problema de planta, fuera de alcance. Si hubo pocos recortes para concluir, se repite una sola vez |
| La carga anda, los recortes no bajan, pero las causas anotadas son sobre todo mezcla y momento | Algo falla en cómo se usa el dato (supuesto 5) | **No se concluye.** Revisar si la producción cambió con lo que se vio en la reunión y repetir una sola vez |
| La prueba técnica falla y el proveedor no lo resuelve | El supuesto 3 cae | Se sigue con A, la planilla, con sus controles, antes que pasar a C (sección 2) |

**Repetir una sola vez** es otra vuelta de 2 semanas con el mismo producto. Si en la segunda tampoco se cumple, la decisión es No-Go: seguir probando sin criterio es no decidir.

### Qué valida el piloto y qué queda para después de activar

Dos semanas con un producto dan una señal, no una demostración. El piloto valida la factibilidad y la deseabilidad de la rutina (supuesto 2, con una primera lectura de los 4, 5 y 6) y si la causa de los recortes de papas fritas es la mezcla y el momento (supuesto 1). No valida lo siguiente, que se mira en el Go/No-Go de la sección 8 con las mismas medidas sobre más productos y más tiempo:

- **El efecto en todo el catálogo.** Cada línea que se suma se activa con las medidas del piloto antes de pasar a la siguiente. La meta es llevar los pedidos completos y a tiempo del 76 % a la de la sección 1 en 6 meses (supuesto 1); el registro semanal sigue acumulando semanas para saber si los 30 de ~125 eran típicos (supuesto 9).
- **La baja de las horas extras a la mitad**, con la liquidación de sueldos de varios meses (supuesto 7). En 2 semanas hay pocas horas.
- **La carga sostenida y la exactitud de stock**: el riesgo mayor aparece cuando ya es rutina y nadie nota que se dejó de cargar (sección 5).
- **El retorno**, con los costos reales: se completa el punto de equilibrio y el dueño decide si es aceptable (supuesto 8).

La ficha de los indicadores y el calendario de las decisiones están en la sección 8.

**Fuentes:** secciones 2, 4 y 5 de esta parte; relevamiento con nuestro compañero que trabaja en Dulxelitos; Clase 7 (etapas de Rogers, MVP, pretotipo de Savoia, hipótesis en una hoja). Las cifras son las de la sección 1 (el 76 % es cuenta nuestra). Probabilidades, impactos y umbrales son supuestos declarados, no datos. Lo que no se sabe queda como "dato pendiente".
