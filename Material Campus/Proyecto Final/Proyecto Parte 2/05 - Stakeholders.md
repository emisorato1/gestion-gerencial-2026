# Stakeholders del proyecto de mejora

El dueño aprueba el presupuesto y decide el Go/No-Go, pero el cambio lo sostienen todos los días Producción, Oficina y quienes deciden qué producir. Las resistencias que esperamos surgen del relevamiento.

## Mapa de actores

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

## Matriz poder/interés

El poder es cuánto puede un actor ayudar o frenar el proyecto, y el interés, cuánto le importa y le toca el cambio.

| | **Interés bajo** | **Interés alto** |
|---|---|---|
| **Poder alto** | **Mantener satisfecho:** Dueño como sponsor, Buenos Aires Software | **Gestionar de cerca:** Dueño como decisor, Hijos, Responsable de sistemas, Oficina, Producción |
| **Poder bajo** | **Mantener informado:** Distribuidores | **Monitorear y dar voz:** Depósito |

Oficina y Producción tienen poder de hecho, porque cualquiera de las dos frena el proyecto con solo no usarlo. Producción además suma legitimidad y urgencia, así que, en términos de saliencia, es la parte que hay que atender primero.

## Estrategias de involucramiento

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

## Cómo cambia por fase

La matriz se revisa en cada Go/No-Go, porque algunos actores cambian de cuadrante según la fase del roadmap (sección 8). En la tabla, Cerca, Satisfecho y Voz abrevian los cuadrantes de la matriz.

| Actor | Preparación | Piloto | Go/No-Go | Activación por línea | Estabilización |
|---|---|---|---|---|---|
| Dueño como sponsor | Cerca | Satisfecho | Cerca | Satisfecho | Satisfecho |
| Decisores y responsable de sistemas | Cerca | Cerca | Cerca | Cerca | Cerca |
| Oficina y Producción | Voz | Cerca | Cerca | Cerca | Satisfecho |
| Buenos Aires Software | Satisfecho | Satisfecho | Satisfecho | Cerca | Satisfecho |

En la estabilización Oficina y Producción pierden interés por la rutina, pero conservan el poder de dejar de cargar; si baja la carga diaria, vuelven a gestionarse de cerca. Depósito y los distribuidores no cambian de lugar en ninguna fase.
