# Stakeholders del proyecto de mejora

Esta sección mira a quienes hacen que la propuesta funcione o no. Usamos la matriz poder/interés de Mendelow, que es la que pide la consigna y la que se explicó en la clase del 23-10 (la lámina de la Clase 4 usa influencia e impacto, otra lectura).

**Quien aprueba el proyecto no es quien lo hace andar.** El dueño aprueba el presupuesto y el Go/No-Go, pero que el cambio funcione depende de lo que hagan todos los días Producción, Oficina y quienes deciden qué producir. Las resistencias de Producción y de Oficina las anticipamos con nuestro compañero que trabaja en la empresa. Lo demás (poder, interés, impacto y lo que decimos de los hijos) es lectura nuestra, no un dato medido: la vamos a contrastar con cada grupo antes del piloto.

## Mapa de actores

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

## Matriz poder/interés

Poder es cuánto puede ayudar o frenar el proyecto; interés, cuánto le importa y cuánto le toca. La matriz muestra la posición típica durante la ejecución, con las excepciones entre paréntesis. Las etiquetas siguen a la clase del 23-10 (en el Mendelow original las dos celdas de bajo poder se nombran al revés).

| | **Interés bajo** | **Interés alto** |
|---|---|---|
| **Poder alto** | **Mantener satisfecho:** Dueño como sponsor (cerca al arrancar el piloto y la activación), Buenos Aires Software (cerca en la activación) | **Gestionar de cerca:** Dueño como decisor de la producción, Hijos, Responsable de sistemas, Oficina, Producción |
| **Poder bajo** | **Mantener informado:** Distribuidores | **Monitorear y dar voz:** Depósito |

En las tablas siguientes los cuadrantes se abrevian: Cerca, Satisfecho, Voz e Informado.

El poder de Oficina y de Producción es de hecho, no formal: ninguno tiene autoridad sobre el proyecto, pero cualquiera lo frena con solo no usarlo. Por saliencia (poder, legitimidad, urgencia), Producción es una parte definitiva: tiene poder de hecho, la legitimidad de una planta saturada y la urgencia de las primeras semanas de carga, y se la atiende primero.

## Estrategias de involucramiento

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

Lo técnico se resuelve con procedimiento y capacitación; lo adaptativo pide conversar, acotar el cambio, ofrecer soporte y reservar tiempo (Clase 4). El de fondo es la última fila (supuesto 5 de la sección 4), y por eso el piloto es de un solo producto.

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

## Cómo cambia por fase

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
La matriz se revisa en cada Go/No-Go.
