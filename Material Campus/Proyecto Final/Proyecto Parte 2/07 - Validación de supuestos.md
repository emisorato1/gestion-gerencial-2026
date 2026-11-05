# Validación de supuestos

Esta sección dice qué tenemos que aprender antes de invertir, cómo aprenderlo gastando lo menos posible y qué resultado nos hace avanzar o frenar. Parte de los nueve supuestos de la sección 4 y de la corrección de la sección 1: el stock de producto terminado no se registra, y los recortes vienen de la mezcla y el momento de producción, no de la capacidad total. Esa segunda afirmación es una hipótesis razonada y no un dato medido, y por eso es lo primero que hay que probar.

Adelantamos la conclusión: **antes de gastar en el stock de Discovery hacemos dos pruebas baratas.** Un piloto de 2 semanas con papas fritas en una planilla compartida, que muestra si la rutina se sostiene y si planificar contra pedidos baja los recortes. Y una prueba técnica de Discovery sobre un solo producto, que muestra si el módulo hace lo que esperamos. Los números de decisión (los umbrales) son una propuesta nuestra y no un dato de la empresa: el dueño tiene que acordarlos antes de arrancar. Lo que el piloto no puede probar, como el efecto sobre todo el catálogo o la baja de las horas extras sostenida durante meses, queda para el Go/No-Go posterior a la activación (sección 8).

## Supuestos críticos

Son los nueve de la sección 4, con su número. Para cada uno damos el tipo de riesgo, la probabilidad, el impacto, la señal temprana y el mecanismo para validarlo rápido, como pide el enunciado.

Cómo se leen las columnas. **Probabilidad** es la de que el supuesto resulte falso e **impacto** es lo que le pasa a la propuesta si lo es. Las dos son juicio nuestro (alta, media o baja), no mediciones. El **tipo** es el de la sección 4. La **etapa** es la principal de las cuatro de validación de la Clase 7 (Rogers): problema (¿es real?), solución (¿el cliente ve valor?), producto (¿podemos entregar algo que se use?) y negocio (¿capturamos valor?). En clase se aclaró que las etapas son iterativas y se superponen: acá le asignamos a cada supuesto una sola, la principal, aunque otras también lo toquen.

### El riesgo de cada supuesto

| # | Supuesto | Tipo y etapa | Prob. de ser falso | Impacto si es falso | Señal temprana |
|---|---|---|---|---|---|
| 1 | La mezcla y el momento de producción, y no la capacidad total, explican la mayoría de los recortes | Factibilidad (crítico) · Problema | Media | Alto | Al anotar la causa de cada recorte en la semana 0, la mayoría queda como "no alcanzaba aun produciendo solo eso" |
| 2 | Producción carga todos los días, y oficina consulta y reserva antes de confirmar, aun con la planta saturada | Factibilidad · Producto | Alta | Alto | Días sin carga al cierre de turno; el disponible de la planilla no coincide con lo que se ve a ojo; pedidos confirmados sin consultar |
| 3 | El módulo de stock de Discovery permite pedidos y reserva, y la factura consume la reserva, con el mismo criterio de disponible | Factibilidad · Producto | Media | Medio | El proveedor no lo confirma por escrito, o un paso de la prueba sobre un producto falla |
| 4 | La fecha estimada que se da al distribuidor se cumple, con la planta saturada | Factibilidad · Producto | Media | Alto | Producción no confirma la fecha en la reunión diaria, o una fecha se pasa |
| 5 | Dueño e hijos deciden la producción mirando pedidos pendientes y stock mínimo, y no solo por criterio propio | Deseabilidad · Solución | Media | Alto | La reunión diaria no cambia lo que se produce de papas fritas aun con pedidos sin cubrir; nadie fija el mínimo |
| 6 | Al distribuidor no le resulta peor una fecha estimada al confirmar que recibir el pedido recortado | Deseabilidad · Solución | Baja | Medio | El distribuidor cancela, reprograma o reclama a oficina cuando oye la fecha |
| 7 | Al menos la mitad de las ~25 horas extras por mes es por pedidos que faltaron por mezcla y momento | Viabilidad · Negocio | Media | Medio | El motivo anotado de las horas extras del piloto es en su mayoría "saturación"; las horas no bajan aunque los recortes sí |
| 8 | El ahorro en horas extras y reprogramaciones justifica el costo de implementar y sostener el cambio | Viabilidad · Negocio | Media | Alto | El punto de equilibrio pide evitar más horas extras que las ~25 de hoy, o el proveedor cobra activación o soporte |
| 9 | La semana de registro (30 recortados o demorados de ~125) es representativa | Viabilidad · Problema | Media | Medio | El total semanal de recortes de la semana 0 o del piloto se aleja del de la semana registrada |

Sobre las probabilidades que no son obvias. El 2 es alta porque hoy producción carga en 1 de 5 días (20 %) y la resistencia de producción y oficina es la que esperamos. El 6 es baja porque hoy el distribuidor ya recibe avisos y pedidos incompletos sin quejarse, pero sigue siendo una apuesta: no tenemos una señal previa de que quiera este cambio. El 3 tiene impacto medio y no alto porque, si el módulo no anda, queda la alternativa A, que ya se habría probado.

### Cómo se valida cada uno

| # | Mecanismo de validación ágil | Se contesta en |
|---|---|---|
| 1 | En la semana 0, sin cambiar nada, anotar la causa de cada recorte o demora de papas fritas (mezcla y momento, capacidad u otra). Después ver si bajan cuando se planifica contra pedidos | Semana 0 y piloto, solo papas fritas |
| 2 | Contar los días con carga y las diferencias de conteo. Anotar los días en que la planilla falló y se volvió a mirar a ojo | Piloto |
| 3 | Probar un producto de punta a punta en Discovery y preguntarle por escrito a Buenos Aires Software qué incluye la licencia, qué soporte tiene y cuánto cuesta activar | Prueba técnica, antes del Go/No-Go |
| 4 | Anotar cada aviso con fecha y si se cumplió. Producción confirma la fecha en la reunión diaria | Piloto |
| 5 | En la reunión diaria, anotar si la producción de papas fritas cambió por lo que se vio. Pedirle al dueño y a los hijos que fijen el stock mínimo de ese producto | Piloto, como señal inicial |
| 6 | Oficina anota cómo reaccionó el distribuidor a cada aviso: acepta, espera, cancela o reclama | Piloto, solo pedidos con papas fritas |
| 7 | Anotar el motivo de cada hora extra durante el piloto: completar un pedido que faltó, saturación u otra | Piloto, como señal; después, la liquidación de sueldos |
| 8 | Completar el punto de equilibrio de la sección 4 con el costo mensual de B (consulta al proveedor) y el costo por hora extra (liquidación de sueldos) | Consulta y datos de costo, antes del Go/No-Go |
| 9 | Repetir el registro semanal de recortes de todos los productos, con el mismo criterio, en la semana 0 y en las del piloto | Semana 0 y piloto |

El piloto contesta, al menos en parte, siete de los nueve. Los otros dos tienen su propia prueba: el 3 con la prueba técnica y el 8 con los datos de costo, que hoy son [dato pendiente: costo mensual de la alternativa B] y [dato pendiente: costo por hora extra]. Empezamos por los de impacto alto y probabilidad media o alta, que son el 1, el 2, el 4, el 5 y el 8, porque son los que más pueden tirar abajo la propuesta.

## Piloto

Según la Clase 7, un MVP no es una versión beta ni una versión light del producto final: es el experimento mínimo necesario para validar una hipótesis. Puede ser ilustrativo (no funciona, comunica la idea) o funcional (funciona, en pequeño). Nuestro piloto es un **MVP funcional**: no arma una Discovery en chiquito, hace lo mínimo para ver si la rutina de cargar, reservar y reunirse se sostiene. Es además lo que la clase llamó pretotipo, que prueba si algo se va a usar con el menor esfuerzo posible antes de construirlo. Savoia lo dice así: asegurarse de que se está construyendo la cosa correcta antes de construirla bien. La prueba técnica de Discovery es el paso siguiente, el prototipo, que mira si el módulo funciona. En la clase del 19-10 se dijo lo mismo con otra imagen: no conviene tirarle con un cañón a un mosquito cuando una solución analógica alcanza.

### Hipótesis en una hoja

Es la plantilla de la Clase 7, completada con el piloto. Afina la hipótesis que dejamos en la sección 2 con los umbrales de este documento.

| Elemento | Contenido |
|---|---|
| **Problema** | Dulxelitos recorta o demora unos 30 de ~125 pedidos por semana, de cualquier producto, porque confirma sin saber qué hay y produce sin mirar los pedidos (sección 1). Las papas fritas son lo que más falta |
| **Hipótesis de solución** | Creemos que una planilla compartida con el stock de papas fritas, la carga diaria de lo producido, la reserva por pedido confirmado y una reunión diaria de ~10 minutos resolverá los recortes y demoras de papas fritas para oficina, producción y quienes deciden qué producir, y sabremos que funciona cuando la producción se cargue en 8 de los 10 días hábiles y los pedidos de papas fritas recortados o demorados por semana bajen a la mitad o menos de lo medido en la semana 0 |
| **Tipo de MVP** | Funcional: funciona, en pequeño |
| **Experimento mínimo** | Dos semanas con papas fritas solamente, con la misma regla de stock disponible que tendría Discovery, carga al cierre de turno, consulta y reserva de oficina antes de confirmar y reunión diaria entre ventas y producción. Los demás productos siguen como hoy |
| **Etapa de validación** | **Producto**: ¿podemos entregar una solución que se use? Toca también **Problema** (¿la causa es la que creemos?) y, en parte, **Solución** (¿el distribuidor ve valor en un aviso con fecha?). No toca **Negocio**: eso espera a los datos de costo y a la activación |

### Cómo se corre

- **Cuándo.** Una semana 0, para medir la línea de base, y después 2 semanas, que son 10 días hábiles. La demanda es pareja todo el año, así que puede empezar en cualquier momento. Conviene arrancar un lunes, con el conteo inicial hecho el fin de semana anterior.
- **Qué producto.** Papas fritas, que según el relevamiento es el que más falta. Un solo producto protege la operación y alcanza para aprender.
- **La regla.** Stock disponible es el stock físico menos lo reservado por pedidos confirmados sin facturar. Es la misma que se usaría en Discovery, para que lo aprendido valga cuando se pase.
- **La rutina.** Producción carga lo producido de papas fritas al cierre de turno, con una persona responsable y un suplente. Oficina consulta la planilla y reserva antes de confirmar un pedido que lleva papas fritas; si no alcanza, avisa con una fecha estimada que producción confirmó. Al facturar, oficina libera la reserva a mano, porque la planilla no habla con Discovery. Hay un conteo físico de papas fritas al arrancar y uno por semana. Y una reunión diaria de ~10 minutos entre ventas y producción, donde se mira el disponible, los pedidos pendientes y los avisos, y se decide qué producir.
- **Vuelta atrás.** Si un día la planilla no está al día, oficina confirma como hoy, a ojo y preguntando a producción, y se anota el día. El piloto se corta cuando se quiera sin perder nada: no toca Discovery ni el armado de pedidos.
- **Quién.** El dueño, como sponsor, acuerda los umbrales antes y respalda el arranque delante del equipo. El responsable de sistemas, como líder, arma la planilla y junta las medidas. Producción carga, oficina reserva y avisa, y el conteo físico lo hace depósito: [dato pendiente: responsable del conteo inicial y del conteo semanal].

### Qué se mide

Primero, qué es un recorte. Cuenta como **recortado o demorado** un pedido con papas fritas que sale con menos cantidad de la pedida o después del plazo estándar de su zona. Es el mismo criterio de la sección 1 y se aplica igual en la semana 0 y en el piloto.

**Las cuatro medidas que deciden.** Los umbrales son una propuesta nuestra, y la sección Criterio de decisión explica por qué elegimos cada uno.

| Medida | Cómo se mide | Línea de base | Umbral para un Go (propuesta nuestra) |
|---|---|---|---|
| **Días con producción de papas fritas cargada** | Días con carga al cierre de turno sobre los 10 días hábiles | 20 % de los días (1 de 5), medido en el control de producción, que no separa por producto | 8 de los 10 días hábiles o más |
| **Pedidos de papas fritas recortados o demorados** | Del registro semanal, solo los pedidos con papas fritas; promedio por semana de las 2 del piloto | Se mide en la semana 0: [dato pendiente: pedidos de papas fritas recortados o demorados en la semana 0]. Los 30 de ~125 son de todos los productos y no sirven de base para uno solo | La mitad o menos que en la semana 0 |
| **Diferencias de conteo** | Conteo físico de papas fritas contra la planilla, al arrancar y al final de cada semana | [dato pendiente: diferencia en el conteo inicial] | En los conteos semanales, una diferencia de hasta una décima parte de lo contado |
| **Fecha estimada cumplida** | Cada aviso con fecha: si el pedido se completó en ese día | No existe hoy: el aviso no trae fecha | 4 de cada 5 avisos o más. Si hubo pocos avisos, se revisan uno por uno |

**Los registros de apoyo.** Informan la decisión pero no tienen umbral. Cuestan una columna más en la planilla.

- La causa de cada recorte o demora: mezcla y momento, capacidad u otra (supuesto 1). Sin esto, que los recortes bajen o no bajen no explica nada.
- El motivo de cada hora extra: completar un pedido que faltó, saturación u otra (supuesto 7).
- La reacción del distribuidor al aviso con fecha (supuesto 6).
- Si la reunión diaria cambió lo que se produjo de papas fritas (supuesto 5).
- El tiempo que lleva cargar, reservar y reunirse, que es el costo en horas del cambio (supuesto 8).
- Los días en que la planilla falló y se confirmó como hoy (supuesto 2).

La causa de cada recorte la anota quien lo vive, producción y oficina, así que es un juicio y no una medición. Lo que la contrasta es la otra medida: si los recortes bajan cuando la producción se dirige con los pedidos a la vista, la mezcla importa, se la haya clasificado bien o mal.

### Prueba técnica de Discovery

Es la prueba del supuesto 3. Nuestro compañero que trabaja en la empresa sabe que Discovery permite pedidos y reserva, pero nadie lo usó en Dulxelitos, y la Parte 1 describió a Discovery como desactualizado y con errores. Se hace durante la preparación, en paralelo con la semana 0, porque el piloto con planilla no la necesita. El resultado entra al Go/No-Go junto con el del piloto. La lleva el responsable de sistemas, con Buenos Aires Software.

Se prueba **un solo producto**, el mismo del piloto para poder comparar, con cinco pasos:

| Paso | Qué se verifica | Resultado esperado |
|---|---|---|
| 1. Ingreso de stock | Cargar el stock inicial del producto | Queda registrado el stock físico |
| 2. Pedido y reserva | Cargar una nota de pedido y reservar | La reserva aparece contra el pedido |
| 3. Disponible | Consultar cuánto hay | El disponible es el stock físico menos lo reservado, igual que en la planilla |
| 4. Factura | Facturar el pedido | La factura consume la reserva y baja el stock físico |
| 5. Corrección | Anular o modificar el pedido | La reserva se libera |

Además se le pregunta por escrito a Buenos Aires Software: la versión de Discovery y qué incluye la licencia para stock, pedidos y reserva ([dato pendiente: versión de Discovery y soporte incluido]), cuánto cuesta activar el módulo y capacitar ([dato pendiente: costo de activar el módulo de stock, si el proveedor cobra soporte o capacitación]), en cuánto tiempo se activa ([dato pendiente: plazo de activación del módulo]) y si hay un ambiente de prueba. Esto último importa por el paso 4: una factura de prueba en el sistema real puede quedar como una factura verdadera. Si no hay ambiente de prueba, ese paso se verifica con el primer pedido real de la activación, y el resto con pedidos que se pueden anular.

**La prueba pasa** si los cinco pasos funcionan y el criterio de disponible coincide con el de la planilla. Si algo falla, se le pregunta al proveedor si se configura y cuánto cuesta, y si no se puede, se sigue con la alternativa A.

### Qué valida el piloto y qué no

Dos semanas con un producto no demuestran un efecto: dan una señal. Hay que leerlo así.

| El piloto sí puede decir | El piloto no puede decir |
|---|---|
| Si producción y oficina sostienen la carga y la reserva con la planta saturada (supuesto 2) | Que el efecto sea el mismo en todo el catálogo: otros productos pueden tener otras causas de recorte (supuesto 1) |
| Si la mezcla y el momento explican los recortes de papas fritas (supuesto 1) | Que las horas extras bajen a la mitad: en 2 semanas hay pocas horas, y lo dirá la liquidación de sueldos de varios meses (supuesto 7) |
| Una primera lectura de la fecha, de la decisión de producción y del distribuidor (supuestos 4, 5 y 6) | Que la carga se sostenga con los meses: el riesgo mayor es cuando ya es rutina y nadie nota que se dejó de cargar |
| Que la regla de stock disponible funciona en la práctica | Si Discovery funciona (supuesto 3) ni si el cambio se paga (supuesto 8): tienen su prueba aparte |
| Si el recorte es del tamaño que creemos, repitiendo el registro (supuesto 9), aunque con pocas semanas | Que el 76 % pase a la meta de la sección 1: eso es de 6 meses y de todos los productos |

Lo que el piloto no puede decir se contesta después de activar, en el Go/No-Go de la sección 8.

## Criterio de decisión

Las reglas se acuerdan con el dueño **antes de arrancar**. Es quien decide el Go/No-Go, y fijar el criterio después de ver el resultado invita a leerlo a favor. Lo que sigue es una propuesta nuestra: ninguno de estos umbrales sale de un dato de la empresa ni de la cátedra, y los declaramos como supuestos para ajustarlos con el dueño y con lo que mida la semana 0.

### Por qué esos umbrales

- **Carga, 8 de los 10 días.** La meta de la sección 1 es que se cargue todos los días. En un primer intento, con la planta saturada y sin gente de más, pedimos una mayoría clara y dejamos 2 días de margen para aprender, no la perfección. Contra el 20 % de hoy es un salto grande. Si se pierden más de 2 días, la rutina no está sostenida.
- **Recortes, la mitad o menos.** La meta de la sección 1 (pasar del 76 % a la meta) deja los recortes en 1 de cada 10 pedidos, menos de la mitad de los ~24 % de hoy. En el piloto pedimos solo la mitad, como señal de que el rumbo es el correcto, porque es un producto y 2 semanas.
- **Conteo, una décima parte.** La meta de exactitud se fija con el primer conteo, como dice la sección 1. Para el piloto usamos esta tolerancia provisional, que se corrige con el conteo inicial.
- **Fecha, 4 de cada 5.** Una fecha estimada es una promesa nueva y, si falla más de 1 vez de cada 5, el aviso pierde el valor que hoy tiene. No pedimos todas porque la planta está saturada.

Con pocos datos hay que tener cuidado. Si la semana 0 casi no tiene recortes de papas fritas, la comparación no distingue una mejora del azar: se mide otra semana antes de arrancar, como ya adelantó la sección 2. Y si hubo pocos avisos con fecha, se miran uno por uno en vez de sacar un porcentaje.

### Qué se decide al terminar el piloto

Las dos semanas terminan en una reunión con el dueño. Se lee el piloto y la prueba técnica juntos.

| Qué pasó | Qué significa | Decisión |
|---|---|---|
| Se cumplen los cuatro umbrales y la prueba técnica pasa | La rutina se sostiene, la mezcla parece ser la causa y el módulo funciona | **Go.** Activar Discovery por línea de producto, con la misma rutina. El Go sobre B tiene además una condición que el piloto no mide: que el punto de equilibrio de la sección 4 cierre con los datos de costo |
| Se cumplen la carga y los recortes, pero fallan el conteo o la fecha | La rutina anda, pero el dato o la promesa necesitan ajuste | **Go con ajustes.** Corregir capacitación, responsable o regla de fecha y repetir el piloto una sola vez |
| La carga no llega a 8 de los 10 días | La rutina no se sostiene | **No-Go.** B no se gasta: una herramienta mejor no arregla un problema de disciplina. Primero se revisan capacitación, carga de trabajo, incentivos y reglas, no el compromiso de la gente (sección 5) |
| La carga anda, los recortes no bajan a la mitad y las causas anotadas son sobre todo de capacidad | La causa no es la que suponíamos: el supuesto 1 cae | **No-Go** de B para este problema. Se revisa la meta de la sección 1, y lo que queda es un problema de planta, fuera de alcance |
| La carga anda, los recortes no bajan, pero las causas anotadas son sobre todo mezcla y momento | Algo falla en cómo se usa el dato: puede ser el supuesto 5 | **No se concluye.** Revisar si la producción cambió con lo visto en la reunión y repetir una sola vez |
| La prueba técnica falla y el proveedor no lo resuelve | El supuesto 3 cae | Se sigue con A, la planilla, con sus controles, antes que pasar a C (sección 2) |

**Repetir una sola vez** quiere decir otra vuelta de 2 semanas con el mismo producto. Si en esa segunda vuelta tampoco se cumple, la decisión es No-Go. No hay tercera: seguir probando sin criterio es otra forma de no decidir.

### Lo que queda para después de activar

Todo lo que el piloto no puede decir se mira en el Go/No-Go de la sección 8, con las mismas medidas pero sobre más productos y más tiempo.

- **Cada línea que se suma** se activa con las mismas medidas que el piloto (recortes de esa línea, carga y conteo) antes de pasar a la siguiente. Es un Go/No-Go más chico por línea.
- **Los pedidos completos y a tiempo de todo el catálogo**, del 76 % a la meta de la sección 1 en 6 meses (supuestos 1 y 9). Mientras tanto, el registro semanal sigue acumulando semanas para saber si el 30 de ~125 era un caso típico.
- **Las horas extras**, con la liquidación de sueldos de varios meses y el motivo anotado (supuesto 7). La meta es la mitad y vale solo si se cumple ese supuesto.
- **La carga sostenida y la exactitud de stock**, que es donde el riesgo mayor aparece cuando ya es rutina. Si baja el indicador de días con producción cargada, producción y oficina vuelven a "gestionar de cerca" (sección 5).
- **El retorno**, con los costos reales: se completa el punto de equilibrio y el dueño decide si el recupero es aceptable (supuesto 8).

La ficha de los indicadores y el lugar de cada decisión en el calendario están en la sección 8.

**Fuentes:** supuestos de la sección 4; piloto, alternativas y recomendación de la sección 2; stakeholders de la sección 5; relevamiento del proceso con nuestro compañero que trabaja en Dulxelitos; Clase 7 (etapas de validación de Rogers, MVP, pretotipo de Savoia y plantilla de hipótesis en una hoja) y clase del 19-10. Las cifras son las de la sección 1 (30 de ~125 pedidos por semana, 76 % completos y a tiempo como cuenta nuestra, ~25 horas extras por mes y carga en el 20 % de los días). Los umbrales, las probabilidades y los impactos son juicio y propuesta nuestros, no datos. Lo que no se sabe queda marcado como "dato pendiente".
