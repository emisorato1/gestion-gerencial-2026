# Stakeholders del proyecto de mejora

Esta sección mira a las personas y organizaciones de las que depende que la propuesta funcione. Usamos la matriz poder/interés de Mendelow, que es la que pide la consigna y la que se explicó en la clase del 23-10. La lámina de la Clase 4 sobre influencia e impacto es otra lectura del mismo problema: la usamos de apoyo para pensar a quién le toca cargar con el cambio, pero la matriz es la de Mendelow.

Adelantamos la conclusión: **quien aprueba el proyecto no es quien lo hace andar.** El dueño aprueba el presupuesto y el Go/No-Go, pero que el cambio funcione depende de lo que hagan todos los días Producción, Oficina y quienes deciden qué producir. Por eso la matriz pone el esfuerzo en ellos y no en el sponsor.

Una aclaración sobre de dónde sale cada cosa. Las resistencias de Producción y de Oficina las anticipamos con nuestro compañero que trabaja en la empresa. Las demás lecturas (poder, interés, impacto, y lo que decimos de los hijos) son nuestras, razonadas sobre cómo funciona el proceso. No son un dato medido: las vamos a contrastar conversando con cada grupo antes del piloto.

## Mapa de actores

Son ocho actores directamente vinculados al proyecto: el sponsor, el líder, los usuarios del proceso nuevo, el proveedor de tecnología y los afectados indirectos.

| Actor | Quién es | Rol en el proyecto | Qué hace en el proceso nuevo |
|---|---|---|---|
| **Dueño** | Dirección. Toma las decisiones importantes (Parte 1) | **Sponsor** | Aprueba el presupuesto y el Go/No-Go. Acepta una inversión mayor si se demuestra el retorno |
| **Hijos** (dos) | Dirección. Resuelven el día a día: reposición, compras, cuentas de clientes. Con el dueño, deciden qué producir | Decisores de la producción | Planifican la producción de la semana mirando los pedidos pendientes y un stock mínimo por producto |
| **Responsable de sistemas** | Rol que ya existe en la empresa, sin gobernanza asignada (Parte 1) | **Líder del proyecto** | Coordina la activación del módulo con el proveedor, capacita, y sigue los indicadores |
| **Oficina** (4 personas) | Administración, facturación y cobranza. Reciben los pedidos | Usuarios clave | Cargan la nota de pedido y reservan el stock antes de confirmar. Si falta algo, avisan al distribuidor en el momento con una fecha estimada |
| **Producción** (7 personas) | La fábrica | Usuarios clave: aportan el dato | Cargan lo producido todos los días, al cierre de turno. Hay un responsable de carga por turno, con suplente |
| **Depósito** | Pedidos, embalaje, fraccionamiento y envíos | Usuarios afectados | Arma desde el pedido confirmado, como hasta ahora. La facturación consume la reserva. El conteo físico inicial y el semanal los tiene que hacer quien conozca la mercadería: [dato pendiente: responsable del conteo inicial y del conteo semanal] |
| **Buenos Aires Software** | Proveedor de Discovery | Proveedor de tecnología | Activa y deja funcionando el módulo de stock, pedidos y reserva, y da soporte en la carga inicial. Lo que incluye la licencia es [dato pendiente: versión de Discovery y soporte incluido] |
| **Distribuidores** | 57 en 7 provincias, 35 de ellos en la Patagonia | Afectados indirectos | Siguen pidiendo por WhatsApp o teléfono. Si falta algo, reciben el aviso al confirmar, con una fecha |

Dejamos afuera al transporte tercerizado: participa del proceso pero no cambia su trabajo (sección 1).

Una nota sobre el líder. La Parte 1 le puso 1 punto a la gobernanza de los procesos digitales porque el responsable de sistemas no la tiene asignada, y en Liderazgo marcó que falta alguien que tenga el cambio como responsabilidad y no como un agregado. La propuesta le asigna formalmente el liderazgo, pero un liderazgo sin tiempo vuelve a ser un agregado: [dato pendiente: tiempo semanal que el responsable de sistemas puede dedicar al proyecto].

## Matriz poder/interés

El eje vertical es el poder: cuánto puede ayudar o frenar el proyecto. El eje horizontal es el interés: cuánto le importa y cuánto le toca. La foto es del momento en que más actores están en juego, el piloto y la activación de Discovery, porque ahí Producción y Oficina empiezan a usar lo nuevo. Cómo se mueve cada actor entre fases está en la última parte. Las etiquetas de cada cuadrante son las de la clase del 23-10.

| | **Interés bajo** | **Interés alto** |
|---|---|---|
| **Poder alto** | **Mantener satisfecho:** Dueño (entre decisiones), Buenos Aires Software | **Gestionar de cerca:** Hijos, Responsable de sistemas, Oficina, Producción |
| **Poder bajo** | **Mantener informado:** Distribuidores | **Monitorear y dar voz:** Depósito |

Cada actor, con el criterio que usamos:

| Actor | Poder | Interés | Impacto | Cuadrante |
|---|---|---|---|---|
| Dueño | **Alto**: aprueba el presupuesto y el Go/No-Go | **Bajo en el día a día**, alto en las decisiones | Medio: decide con un tablero que hoy no existe | Mantener satisfecho |
| Hijos | **Alto**: deciden qué producir | **Alto**: se les toca el criterio con el que deciden | Alto | Gestionar de cerca |
| Responsable de sistemas | **Alto, pero delegado por el dueño**. Sin asignación formal sería bajo | **Alto** | Alto: lidera, capacita y sigue los indicadores | Gestionar de cerca |
| Oficina | **Alto de hecho**: si no carga los pedidos ni reserva, no hay stock disponible confiable | **Alto** | Alto: cambia cómo se toma y se confirma un pedido | Gestionar de cerca |
| Producción | **Alto de hecho**: si no carga todos los días, no hay stock | **Alto** | Alto: trabajo nuevo con la planta saturada | Gestionar de cerca |
| Depósito | **Bajo**. Sube si le toca el conteo | **Alto**: sabe cuánto hay de verdad | Medio: cambia cómo le llega el pedido, el armado queda igual | Monitorear y dar voz |
| Buenos Aires Software | **Alto sobre la viabilidad técnica**: si el módulo no anda como esperamos, la alternativa B no se puede | **Bajo**: un cliente más, activando algo que ya estaba en su licencia | Bajo | Mantener satisfecho |
| Distribuidores | **Bajo sobre el proyecto**, aunque sean el negocio | **Bajo**: siguen pidiendo igual | Bajo: cambia lo que reciben, no lo que hacen | Mantener informado |

Cuatro lecturas que no son obvias:

- **El poder de Oficina y Producción es de hecho, no formal.** Ninguno tiene autoridad sobre el proyecto, pero cualquiera de los dos lo frena con solo no usarlo. En clase se ubicó así: el cliente interno y los usuarios de lo que se implementa tienen alto poder y alto interés.
- **El sponsor aprueba pero no ejecuta.** Para el dueño alcanza con mantenerlo satisfecho, salvo en las decisiones. La regla de clase es que un actor de alto poder mal informado es un riesgo latente: puede activar su veto, parar las tareas o sacar gente del proyecto. Por eso no se lo deja de informar, aunque no esté en el día a día.
- **Los hijos son el actor menos obvio.** El grupo no los marcó como resistencia, y lo decimos como hipótesis nuestra: la decisión de qué producir se toma hoy por criterio propio, y la propuesta les pide tomarla mirando pedidos y stock. Es el cambio que la sección 4 llama adaptativo (supuesto 4).
- **El poder del líder es prestado.** Sin respaldo explícito del dueño, el responsable de sistemas no tiene cómo pedirle a Producción que cargue ni a Oficina que reserve.

**Complemento: saliencia.** El modelo de saliencia (poder, legitimidad y urgencia) ayuda a ver cuándo una resistencia se vuelve peligrosa. Producción tiene poder de hecho, tiene legitimidad (la planta saturada es real, y la Parte 1 ya decía que se tapa con horas extras) y va a tener urgencia en las primeras semanas de carga, que es cuando el trabajo nuevo más se nota. Si las tres coinciden, es una parte interesada definitiva y hay que atenderla antes que a las demás. Oficina se parece: su legitimidad viene de que un aviso mal dado puede enojar al distribuidor. La conducta que se desprende es la misma: no dejar que las dos se junten en una sola queja ante el dueño (más abajo, en la negociación).

## Estrategias de involucramiento

Cada cuadrante tiene una conducta por defecto: al de alto poder y alto interés se lo gestiona de cerca, al de alto poder y bajo interés se lo mantiene satisfecho sin saturarlo, al de bajo poder y alto interés se lo escucha y se lo monitorea, y al de bajo poder y bajo interés se lo mantiene informado. Esta tabla completa la ficha de cada actor con la resistencia que esperamos y la estrategia.

| Actor | Resistencia esperada | Estrategia |
|---|---|---|
| Dueño | Baja. El riesgo no es que se oponga sino que no mire: si el piloto no le muestra el retorno, no aprueba | Informe corto y regular del piloto con los cuatro indicadores. Criterio de Go/No-Go acordado antes de empezar. Respaldo explícito al líder, delante del equipo |
| Hijos | **Posible, y no relevada**: perder el criterio propio al decidir la producción | Que sigan decidiendo ellos, con más información. Que fijen el stock mínimo por producto. Sumarlos a la reunión diaria durante el piloto |
| Responsable de sistemas | Sobrecarga: que sea otra tarea más sobre las que ya tiene | Asignación formal del liderazgo, con tiempo reservado. Que no sea el único que sabe cómo se carga |
| Oficina | **Esperada**: confirmar sabiendo qué hay suma un paso | Gestionar de cerca. Mostrar qué pasos reemplaza el nuevo. Guion de aviso al distribuidor. Práctica con pedidos reales del piloto |
| Producción | **Esperada**: cargar lo producido es trabajo nuevo con la planta saturada | Gestionar de cerca. Empezar por una sola línea, con la carga al cierre del turno y un suplente. Escucharlos antes de pedirles nada |
| Depósito | Baja | Dar voz: es quien sabe cuánto hay de verdad. Pedirle que valide el primer conteo y avise si lo cargado no coincide con lo que ve |
| Buenos Aires Software | Baja. El riesgo es que el módulo no ande como se espera, o que el soporte tarde | Pedirle por escrito qué incluye la licencia y qué soporte da. Probar el módulo en un solo producto antes de escalar (sección 7) |
| Distribuidores | Ninguna esperada | Informar con claridad: el aviso de que falta algo llega al confirmar, con una fecha. Vigilar que no empeore una relación que hoy está bien |

Para los tres grupos que más cambian su trabajo (Producción, Oficina y quienes deciden la producción) usamos cuatro herramientas: Heifetz para saber qué tipo de cambio es, FUD para escuchar lo que probablemente sienten, ADKAR para ubicar dónde se traba cada uno, y la negociación de la clase del 23-10 para acordar.

### Técnico o adaptativo (Heifetz)

Un desafío técnico se resuelve con conocimientos y procedimientos que ya existen. Uno adaptativo exige aprender y cambiar prácticas, prioridades o relaciones. La Clase 4 aclara que una transformación suele combinar los dos.

| Cambio | Componente técnico | Componente adaptativo | Predomina |
|---|---|---|---|
| **Cargar lo producido todos los días** (Producción) | Qué se carga, cuándo (al cierre del turno), quién carga y quién suple, y la capacitación en Discovery | Es trabajo nuevo en una planta sin holgura: hay que decidir qué se deja de hacer. Y el dato de producción deja de ser solo de producción | **Técnico**, con un borde adaptativo en la carga de trabajo |
| **Reservar stock antes de confirmar** (Oficina) | Un paso en Discovery con una sola regla de stock disponible | Aprender a decir "hay en tal fecha" en vez de confirmar siempre, y soltar el hábito de cerrar el pedido en el momento | **Mixto** |
| **Planificar la producción contra pedidos y stock mínimo** (Dirección) | Definir el mínimo por producto y mirar los pedidos pendientes | Cambiar el criterio propio por uno informado y compartir esa decisión con ventas y producción | **Adaptativo** |

Lo técnico lo controlamos nosotros: un procedimiento de una hoja, capacitación y un suplente. Lo adaptativo no se resuelve con un manual. Pide conversar, acotar el cambio, ordenar prioridades, ofrecer soporte y reservar tiempo, que son las intervenciones de la Clase 4, y probar chico antes de escalar. Por eso el piloto es de una sola línea.

Y una regla para cuando algo falle. Si la carga diaria se cae, no lo leemos como falta de compromiso: primero se revisan la capacitación, la carga laboral, los incentivos y las reglas. El indicador de días con producción cargada es la señal temprana, y es el líder quien la mira.

### Qué puede estar sintiendo cada grupo (FUD)

FUD es miedo, incertidumbre y duda. Lo usamos como guía para las conversaciones, como dice la propia lámina, y no como un diagnóstico de las personas. Lo de la tabla son hipótesis para conversar, no cosas que nos hayan dicho.

| Grupo | Miedo | Incertidumbre | Duda |
|---|---|---|---|
| **Producción** | Que la carga diaria sea trabajo de más en una planta al límite, y que el número cargado se use para señalar a alguien si no cierra | No saben cuándo cargar, qué hacer si se equivocan ni qué pasa si el responsable del turno falta | Que sirva para algo: hoy lo que cargan una vez por semana no se cruza con las ventas |
| **Oficina** | Que avisar "hoy no hay" haga que el distribuidor se enoje o pida a otro, y que la culpa caiga en quien lo dijo | Qué fecha dar si producción todavía no la confirmó | Que el stock cargado no sea confiable y haya que ir a mirar el depósito igual |
| **Dueño e hijos** | Perder el criterio propio, que viene de años de oficio | Cuánto de la decisión sigue siendo de ellos | Que un número cargado capture lo que saben del negocio. Y, en el dueño, si habrá retorno |

La Clase 4 propone una respuesta para cada letra: al miedo, explorar impactos y alternativas; a la incertidumbre, explicitar decisiones y pendientes; a la duda, revisar evidencia y condiciones. Aplicado a lo nuestro:

- **Producción.** Para el miedo, acordar con el dueño que el dato de carga se usa para planificar y no para evaluar personas. Para la incertidumbre, el instructivo de una hoja con quién carga, cuándo y qué hacer si falta alguien. Para la duda, que en la primera reunión diaria se vea que ventas usa el dato.
- **Oficina.** Para el miedo, un guion simple de aviso con fecha, y que el dueño respalde decir "hoy no hay". Para la incertidumbre, que producción confirme la fecha estimada en la reunión diaria. Para la duda, el conteo cíclico semanal y la exactitud de stock a la vista: si es baja, se dice y se corrige, no se esconde.
- **Dueño e hijos.** Para el miedo, la decisión sigue siendo de ellos: cambia que la toman mirando pedidos y stock, no que se automatice. Para la incertidumbre, una regla clara de qué se mira y quién fija el mínimo. Para la duda, el piloto con papas fritas, que muestra con datos si la mezcla es la causa. Si no lo es, la propuesta se revisa (supuesto 1 de la sección 4).

### Dónde se traba cada grupo (ADKAR)

ADKAR son cinco condiciones para que alguien adopte un cambio: conciencia de por qué, disposición a participar, conocimiento de cómo, capacidad de hacerlo en el trabajo y refuerzo para sostenerlo. La Clase 4 recuerda que capacitar da conocimiento, pero la capacidad pide además práctica, tiempo y soporte.

| Grupo | Dónde se traba | Qué hacemos |
|---|---|---|
| **Producción** | **Capacidad**: tiempo y práctica con la planta al límite. Y **disposición**, si no ven qué ganan | Capacitar en el puesto con el responsable del turno. Una sola línea al empezar. Reservar el tiempo de carga dentro del turno. Mostrar la relación con las horas extras, si el supuesto 1 se confirma |
| **Oficina** | **Disposición**: miedo a perder el pedido. **Conocimiento**: qué fecha dar y cómo usar la reserva | Guion de aviso, práctica con pedidos reales del piloto, respaldo del dueño |
| **Dueño e hijos** | **Conciencia**: la Parte 1 decía que los pedidos incompletos eran poco frecuentes y se resolvían fácil, y el relevamiento lo corrige: 30 de ~125 en una semana. Si se perciben como un problema menor, no hay motivo para cambiar la decisión | Mostrar el dato y, después, el resultado del piloto. La disposición del dueño es condicional: acepta invertir si se demuestra el retorno |
| **Responsable de sistemas** | **Capacidad**: tiempo y autoridad para sostener a los demás | Asignación formal, tiempo reservado y respaldo del dueño |
| **Todos** | **Refuerzo**: que la rutina se sostenga cuando pasa la novedad | Reunión diaria ventas y producción, conteo cíclico semanal y tablero a la vista con los cuatro indicadores |

### Cómo negociamos

La clase del 23-10 da cuatro consejos, y los aplicamos así.

- **Nunca un sí o un no: negociar en varios puntos, con toma y daca.** Un sí o no hace sentir que se pierde, y quien siente que pierde se planta. Cada parte recibe algo a cambio de lo que se le pide (lo que sigue es lo que proponemos, a acordar con cada una):
  - **Producción:** le pedimos la carga diaria. A cambio, que reemplace al control semanal propio en vez de sumarse (falta confirmar con ellos qué contiene ese control), con suplente y con la carga dentro del turno.
  - **Oficina:** le pedimos reservar antes de confirmar. A cambio, una sola consulta en lugar de dos (hoy se mira a ojo y además se pregunta a producción) y una nota de pedido que se carga una vez, no tres. Esto se cierra con el proceso TO-BE de la sección 3.
  - **Dueño e hijos:** les pedimos mirar pedidos y stock mínimo. A cambio, la decisión sigue siendo de ellos.
  - **Buenos Aires Software:** le pedimos que active y valide el módulo. A cambio, le contamos cómo lo vamos a usar y con qué prueba.
  - **Dueño como sponsor:** le pedimos presupuesto y tiempo del líder. A cambio, fijamos antes un criterio de Go/No-Go.
- **Saber qué se negocia.** Casi nunca es lo que parece. Con Producción no se negocia "cargar o no cargar" sino el tiempo de planta y que el dato se use. Con Oficina, no es el paso en Discovery sino no quedar mal con el distribuidor. Con los hijos, no es una planilla sino quién controla la decisión. Y vale preguntar cómo ve cada uno las horas extras: para quien las hace pueden ser también un ingreso, no solo un problema.
- **Que la información sea simétrica.** Nadie sabe algo que otros no. Todos ven los mismos números (los 30 de ~125 pedidos de la semana que registramos, las horas extras, el tablero) y la misma regla de stock disponible. Sin eso la otra parte se retrae y no negocia.
- **Que el punto de dolor involucre a pocos.** La resistencia es tolerable mientras sea de un grupo y se atienda con su propio trato. Si Producción y Oficina se echan la culpa entre sí y van juntas ante el dueño, se vuelven una sola parte con poder, legitimidad y urgencia. Por eso se habla primero con cada una por separado, y recién se juntan en la reunión diaria, con los mismos datos adelante.

## Cómo cambia por fase

En clase se dijo que la matriz no es una foto fija: los actores se mueven según la fase del proyecto. El ejemplo fue el jefe de finanzas, que al principio, con el presupuesto sin aprobar, es de alto poder y hay que gestionarlo de cerca, y que una vez aprobado se pasa a otro cuadrante. Las fases son las del roadmap de la sección 8; si el roadmap cambia, esta tabla se ajusta.

**Cerca** es gestionar de cerca, **Satisfecho** es mantener satisfecho, **Voz** es monitorear y dar voz, e **Informado** es mantener informado.

| Actor | Preparación y conteo inicial | Piloto (2 semanas, papas fritas) | Go/No-Go | Activar Discovery por línea | Estabilización |
|---|---|---|---|---|---|
| Dueño | Cerca | Satisfecho | Cerca | Satisfecho | Satisfecho |
| Hijos | Cerca | Cerca | Cerca | Cerca | Cerca |
| Responsable de sistemas | Cerca | Cerca | Cerca | Cerca | Cerca |
| Oficina | Voz | Cerca | Cerca | Cerca | Satisfecho |
| Producción | Voz | Cerca | Cerca | Cerca | Satisfecho |
| Depósito | Voz | Informado | Informado | Voz | Voz |
| Buenos Aires Software | Satisfecho | Informado | Satisfecho | Cerca | Informado |
| Distribuidores | Informado | Informado | Informado | Informado | Informado |

Lo que importa de la tabla:

- **El dueño sube y baja.** Está cerca cuando se aprueba el presupuesto y cuando se decide el Go/No-Go, y a distancia entre una cosa y otra. Su poder no desaparece, así que el informe corto sigue llegando aunque no esté en el día a día: es lo que evita el veto tardío.
- **Oficina y Producción activan su poder con el uso.** En la preparación todavía no hay nada que cargar, así que el poder es latente y la etapa es de escuchar cómo se carga mejor. En el piloto y en la activación suben. En la estabilización el interés baja porque ya es rutina, pero el poder queda, y es el momento de más riesgo silencioso: pueden dejar de cargar y nadie lo nota hasta que cae la exactitud. Si el indicador de días con producción cargada baja, vuelven a Cerca. Se desarrolla en la sección 8.
- **El responsable de sistemas pasa de poca autoridad a poder delegado.** Desde que el dueño le asigna formalmente el liderazgo, en la preparación, está en Cerca. Antes de eso, su poder es bajo.
- **Buenos Aires Software importa dos veces.** Al principio, para saber si el módulo existe y funciona como esperamos. Y en la activación, cuando su soporte es la dependencia. En el medio no hay nada que hacer con él, porque el piloto es con planilla y no usa Discovery. Si el soporte tiene costo, su interés sube.
- **Los hijos no se mueven, y esa es la señal.** La decisión de producción es el cambio adaptativo y el que más tarda en consolidarse. Por eso se los gestiona de cerca durante todo el proyecto y no solo al arrancar.
- **Los distribuidores casi no se mueven.** Sigue siendo así hasta "later": cuando se decida mostrarles el stock, su interés sube y pasan a Voz. Hasta ese momento alcanza con que el aviso sea claro. Con una excepción: si en la activación se juntan quejas por los avisos, su poder colectivo (son 57) puede pesar más de lo que muestra la tabla, y se los vuelve a mirar.
- **El depósito sube si le toca el conteo.** Si [dato pendiente: responsable del conteo inicial y del conteo semanal] resulta ser Depósito, pasa a Cerca en esas fases.

La matriz se revisa en cada Go/No-Go, que es el momento en que cambia la fase y cambia quién tiene que estar cerca.
