---
lang: es
---
<div class="portada">

<p class="p-titulo">Trabajo Práctico Final - Parte 3</p>
<p class="p-sub">Propuesta final para la dirección de Dulxelitos</p>
<p class="p-materia">Gestión Gerencial</p>
<p class="p-carrera">Ingeniería en Sistemas de Información</p>
<p class="p-equipo">Integrantes: Lepez Joaquín, Geyer Juan José, Lopez Juan, Olivares Manuel, Sorato Emiliano</p>
<p class="p-docente">Docentes: Ing. Jeremías Pino, Ing. Martín Noguerol</p>

</div>

---

# Índice

- 1\. Resumen ejecutivo
- 2\. Caso de negocio
- 3\. Plan de implementación y gobierno
- 4\. Riesgos, seguridad y continuidad
- 5\. Personas: cambio, capacitación y adopción
- 6\. Impactos responsables
- 7\. Preparación de la conversación con la dirección
- 8\. Bibliografía

---

---

# 1. Resumen ejecutivo

| Pregunta | Respuesta |
|---|---|
| ¿Quién es la organización y qué problema tiene? | Dulxelitos, fábrica familiar de snacks de San Rafael, recorta o demora pedidos de sus distribuidores todas las semanas porque los acepta sin saber qué hay en stock y produce sin mirar lo que se pidió. |
| ¿Qué evidencia lo muestra? | En la semana registrada, 30 de unos 125 pedidos salieron recortados o demorados (76 % completos y a tiempo). Cada uno lleva alrededor de una hora de trabajo extra entre Oficina y Depósito, y la planta hace entre 40 y 50 horas extras por mes. |
| ¿Cuánto cuesta seguir igual? | Equivale a unos $1.570.000 por mes, de los cuales $270.000 son horas extras pagadas; el resto es tiempo de Oficina y Depósito. A eso se suma el riesgo comercial con los distribuidores, que no cuantificamos. |
| ¿Qué proponemos? | Registrar el stock de producto terminado en el módulo de Discovery que la empresa ya paga y no usa, confirmar cada pedido mirando ese stock y planificar la producción contra los pedidos. Primero se prueba durante 2 semanas con papas fritas en una planilla compartida. |
| ¿Cuánto cuesta y qué se espera ganar? | No hay licencias ni equipos nuevos: el costo es tiempo del personal. La puesta en marcha completa va de $1,75 millones a $1,83 millones, y el beneficio neto, una vez activas las tres líneas, de $343.000 a $801.000 por mes. En el escenario conservador se recupera en 13 meses y el VAN a 3 años es de $6,1 millones. |
| ¿Cuál es el principal riesgo y cómo se controla? | Que Producción no sostenga la carga diaria. Se mide todos los días durante el piloto: con 8 o más de 10 días cargados se sigue, con 5 a 7 se ajusta y se repite, y con menos de 5 se pausa y la operación vuelve a confirmar pedidos como hoy, sin perder información. |
| ¿Qué decisión pedimos y para cuándo? | Que la dirección apruebe el piloto para febrero o marzo de 2027, con un tope de $712.600 (de los cuales $57.600 son pagos en efectivo), y designe como responsable a uno de los hijos. Se necesita antes del viernes 15 de enero de 2027, para comenzar el lunes 1-2-2027. El techo del proyecto completo, $2.457.883, se libera solo si el piloto da Go en la semana 6. |

Todas las cifras están en pesos constantes de noviembre de 2026 y salen de la planilla del caso de negocio que acompaña este documento.

---

# 2. Caso de negocio

Cuantificamos solo la alternativa elegida en la Parte 2: activar el módulo de stock de Discovery, con un piloto previo de 2 semanas con papas fritas. Todo está en pesos constantes de noviembre de 2026, a 3 años, y sale de la planilla "TP Final Parte 3 - Dulxelitos - Caso de negocio.xlsx", donde cada número lleva su tipo (dato, estimación, hipótesis o decisión) y su fuente. El calendario es el del roadmap de la Parte 2; proponemos que la semana 1 sea la del 1 de febrero de 2027, una fecha que se corre si la aprobación se demora. No hay costos en dólares.

Un cambio respecto de la Parte 2: según la liquidación, las horas extras son entre 40 y 50 por mes, no unas 25; se midieron mejor con la empresa. Usamos 45, y la meta pasa a ser la mitad.

Casi todo el costo y buena parte del beneficio son horas de gente que cobra su sueldo de todos modos. Ese tiempo se usa o se libera, pero no cambia lo que sale de la caja. Por eso mostramos dos vistas: la completa valora ese tiempo al costo de la hora, y la de caja cuenta solo lo que sale o deja de salir, que son horas extras.

## 2.1 Costos

No hay licencia, equipos ni servicio nuevo: el módulo está en la licencia, ya hay PC con Discovery en Producción y Depósito, y las horas del responsable de sistemas entran en lo que ya cobra (datos de la empresa). El costo es tiempo interno, a $8.000 la hora de operario, $10.000 la de Oficina y $12.000 la extra, datos aproximados de la liquidación. El tiempo de la Dirección lo valoramos como el de Oficina. Las horas de cada tarea son estimaciones nuestras, con su base en la hoja Supuestos, y siguen lo que proponen las secciones 3 y 5.

Puesta en marcha, semanas 1 a 26:

| Concepto | Base | Monto |
|---|---|---|
| Registro de la línea de base | 1 minuto de Oficina por pedido, semanas 1 a 3 | $62.500 |
| Conteo inicial de papas fritas | 2 personas, 2 horas extras | $48.000 |
| Capacitación para el piloto | Producción: 1 hora para el responsable de carga y su suplente y 15 minutos para el resto. Oficina: 2 sesiones de 1 hora para 2 personas. Depósito: 1 hora para 2. Dirección: 1 hora para el dueño y los dos hijos | $112.000 |
| Piloto, semanas 4 y 5 | Reservar en la planilla, descontar a mano al facturar, cargar y contar | $71.000 |
| Comunicación del piloto | Anuncio de 15 minutos con todo el equipo, 10 minutos con cada grupo, reunión del día 5 y del resultado | $137.500 |
| Conteo inicial de las tres líneas | 3 personas, 3 horas extras por línea | $324.000 |
| Capacitación, revisión de productos y 2 semanas de doble registro por línea | Hoja Costos y beneficios | $307.000 |
| Avisos al activar cada línea y en los meses 3 y 6 | 5 minutos con todo el equipo, 5 veces | $62.500 |
| Reunión semanal de seguimiento | 20 minutos, 26 semanas, con el hijo responsable, los referentes de Oficina, Producción y Depósito y el suplente interno | $399.000 |
| Subtotal | | $1.523.000 |
| Con contingencia (15 % esperado / 20 % conservador) | | $1.752.000 / $1.828.000 |

Lo único que sale de la caja son las horas extras de los conteos: $446.400 con la contingencia del conservador.

Tiempo interno recurrente por mes, con las tres líneas en uso:

| Tarea | Base | Por mes |
|---|---|---|
| Carga diaria de lo producido | 20 minutos, de 14:40 a 15:00 | $58.000 |
| Reunión diaria entre ventas y producción | 10 minutos, 3 personas | $101.000 |
| Cargar el pedido y reservar | 3 minutos por pedido | $271.000 |
| Revisión de reservas | 10 minutos por día | $36.000 |
| Conteo semanal | 2 personas, 1,5 horas | $104.000 |
| Registro de pedidos y tablero | 30 minutos por semana | $22.000 |
| Menos: control semanal de Producción | 1,5 horas por semana | −$52.000 |
| Menos: averiguación doble, que pasa a ser una consulta | 3 minutos por pedido | −$244.000 |
| Menos: copias del pedido en papel o planilla y en la lista | 2 minutos por pedido | −$181.000 |
| Neto | | $115.000 |

Es igual en los dos escenarios y comienza a medida que cada línea queda en uso. La carga diaria va dentro del turno de Producción, de 14:40 a 15:00; si en algún momento genera horas extras, se toma como Ajustar en el punto de decisión. Hoy el pedido se anota tres veces, y la nota en Discovery reemplaza las dos copias a mano: estimamos un minuto cada una.

## 2.2 Beneficios

| Beneficio | Cálculo | Esperado | Conservador | ¿Caja? |
|---|---|---|---|---|
| Retrabajo evitado | Recortes evitados × 1 hora × $10.000 | $758.000 | $379.000 | No |
| Horas extras evitadas | La mitad de 45 horas, en proporción a los recortes evitados, × $12.000 | $158.000 | $79.000 | Sí |
| Total por mes, tres líneas | | $916.000 | $458.000 | |

Hoy hay 30 pedidos recortados o demorados por semana, dato de la semana registrada. Con la propuesta bajarían a unos 12 o 13 en el esperado, la meta del 90 %, y a unos 21 en el conservador, la mitad de esa mejora (hipótesis). Cada recortado lleva alrededor de una hora de Oficina y Depósito para avisar, rearmar, facturar y coordinar, según la empresa, en horario normal: la empresa no paga menos, pero recupera tiempo para otras tareas sin contratar.

Las horas extras evitadas sí son dinero. La mitad de las 45 horas se hace para completar pedidos que faltaron (supuesto 7) y suponemos que esa mitad baja en la misma proporción que los recortados: unas 13 horas por mes en el esperado y unas 6,6 en el conservador. La meta del proyecto sigue siendo la mitad de las horas extras, de 20 a 25 por mes, y se mide en los puntos de decisión; para el caso usamos esta estimación, más prudente.

El proceso nuevo se paga con el tiempo que libera. Con las tres líneas en uso, las tareas nuevas suman unas 64 horas por mes y reemplazan unas 52, entre el control semanal, la averiguación doble y las copias del pedido, así que agregan unas 12 horas netas. El retrabajo evitado libera unas 76 horas por mes en el esperado y unas 38 en el conservador.

No sumamos el margen de los recortados, porque lo que falta se manda después y la venta no se pierde. Tampoco lo que no se puede medir: la cobranza que no espera a completar el pedido, el distribuidor que no paga un segundo flete, el stock a la vista para decidir qué producir.

Sin registro de recortes por línea, suponemos que cada línea aporta un tercio del beneficio. Es una hipótesis prudente, porque las papas fritas, el producto con más faltantes, son de Salados. Cada línea empieza a aportar la semana siguiente al cierre de su activación: Salados en la 13, Dulces en la 18 y Repostería en la 23. El piloto no suma beneficio.

## 2.3 Costo de no actuar

| Concepto | Por mes | Qué es |
|---|---|---|
| Retrabajo de los 30 recortados por semana | $1.300.000 | Tiempo: unas 130 horas de Oficina y Depósito |
| Horas extras ligadas a completar pedidos, la mitad de 45 | $270.000 | Dinero: 22,5 horas extras pagadas |
| Costo de no actuar | $1.570.000 | |

Seguir como hoy equivale a unos $1,6 millones por mes, casi $19 millones por año. De eso, $270.000 por mes son dinero que se paga en horas extras; el resto, $1,3 millones, es tiempo de gente con sueldo que hoy se va en rearmar y avisar. La otra mitad de las horas extras responde a la falta de capacidad y no la contamos. Queda sin cuantificar el riesgo de que un distribuidor se canse de recibir pedidos incompletos. Cada mes de demora en decidir se pierde el neto mensual: entre $343.000 y $801.000.

## 2.4 Escenarios

Cambian solo los supuestos más inciertos.

| | Conservador | Esperado |
|---|---|---|
| Recortados por semana (hoy 30) | unos 21 | 12 o 13 |
| Horas extras evitadas por mes (hoy 45) | unas 6,6 | unas 13 |
| Demora adicional del efecto | 8 semanas | Ninguna |
| Contingencia | 20 % | 15 % |
| Neto mensual pleno, completa / caja | $343.000 / $79.000 | $801.000 / $158.000 |
| Máximo expuesto, completa / caja | $2,2 millones / $436.000 | $1,3 millones / $254.000 |
| Mes de recupero, completa / caja | 13 / 12 | 7 / 7 |
| VAN a 3 años, completa / caja | $6,1 millones / $1,5 millones | $19,2 millones / $3,8 millones |
| TIR mensual, vista completa | 10 % | 28 % |

El conservador cierra en las dos vistas: el VAN es positivo y se recupera dentro de los 3 años. En la vista completa el primer año queda en unos −$300.000 y el recupero llega en febrero de 2028; en caja, en enero de 2028. El proyecto conviene, aunque en el conservador tarda un año en devolver lo invertido.

Probamos varias sensibilidades sobre el conservador:

| Si… | Vista completa | Caja |
|---|---|---|
| El retrabajo fuera de media hora por recortado y no de una | VAN de $1,4 millones, recupero en el mes 22 | No cambia |
| Cargar y reservar llevara 5 minutos y no 3, o no se ahorraran las copias del pedido (pesan lo mismo) | VAN de $1,2 millones, recupero en el mes 24 | No cambia |
| Las 47 horas que el plan le asigna al responsable de sistemas se valoraran a $10.000 | VAN de $5,7 millones, recupero en el mes 15 | Si las cobrara aparte: VAN de $1,1 millones, mes 18 |
| La tasa fuera del 20 % en lugar del 12 % | VAN de $5,2 millones | VAN de $1,3 millones |
| Se cumpliera la meta de horas extras, la mitad | VAN de $10,9 millones, mes 11 | VAN de $6,3 millones, mes 8 |
| La carga diaria y la reunión de Producción se pagaran como horas extras ($130.000 por mes) | No cambia | VAN de −$2 millones: no cierra |

El conservador sigue cerrando en todas menos en la última. Por eso la carga y la reunión van dentro del turno, y no se activa otra línea si las horas extras pasan de las 45 por mes de hoy, sin contar las de los conteos iniciales. Los tiempos de retrabajo, de reserva y de las copias se miden en las semanas 1 a 5, con la línea de base y el piloto, y la planilla se recalcula con esos valores antes del Go.

## 2.5 Flujo de caja

Saldo acumulado de los primeros 12 meses, redondeado a miles:

| Mes | Esperado, completa | Conservador, completa | Conservador, caja |
|---|---|---|---|
| 1. Febrero de 2027 | −$539.000 | −$560.000 | −$58.000 |
| 2. Marzo | −$1.031.000 | −$1.069.000 | −$187.000 |
| 3. Abril | −$1.225.000 | −$1.339.000 | −$187.000 |
| 4. Mayo | −$1.333.000 | −$1.790.000 | −$317.000 |
| 5. Junio | −$1.165.000 | −$2.188.000 | −$436.000 |
| 6. Julio | −$480.000 | −$2.211.000 | −$404.000 |
| 7. Agosto | $321.000 | −$2.009.000 | −$349.000 |
| 8. Septiembre | $1.122.000 | −$1.667.000 | −$271.000 |
| 9. Octubre | $1.922.000 | −$1.324.000 | −$192.000 |
| 10. Noviembre | $2.723.000 | −$981.000 | −$113.000 |
| 11. Diciembre | $3.524.000 | −$639.000 | −$34.000 |
| 12. Enero de 2028 | $4.324.000 | −$296.000 | $44.000 |

Los meses 1 a 5 concentran la preparación, el piloto, los conteos y el doble registro. Los años 2 y 3 dejan unos $9,6 millones por año en el esperado y $4,1 millones en el conservador, en la vista completa. El detalle de los 36 meses está en la hoja Flujo mensual.

## 2.6 Indicadores económicos

Los indicadores de los dos escenarios están en la tabla de escenarios. Descontamos al 12 % real anual, una decisión nuestra: algo más de lo que rinde un plazo fijo ajustado por inflación y cerca de lo que costaría pedir prestado en pesos ajustados. La TIR da valores muy altos, más de 200 % anual en el conservador, porque lo que se pone al principio es chico frente a lo que vuelve; por eso decidimos con el máximo expuesto, el recupero y el VAN. Como referencia, alcanza con evitar unos 3 recortes por semana para cubrir el tiempo interno nuevo, sin contar las horas extras.

El pedido de aprobación usa la vista completa del conservador, porque muestra todo lo que el proyecto le pide a la empresa, incluido el tiempo de su gente:

- Tope del piloto, semanas 1 a 6: $712.600, de los cuales $57.600 salen de la caja. Se compone de $523.000 de costos de una vez (línea de base, conteo y capacitación del piloto, el piloto, su comunicación y 6 de las 26 reuniones semanales), $105.000 de contingencia y $85.000 de reunión diaria y tablero en las semanas 4 a 6. Si el piloto no da, se vuelve atrás sin haber tocado Discovery.
- Techo del proyecto, semanas 1 a 26, sin restar beneficios: $2.457.883, de los cuales $446.400 son caja. Es la puesta en marcha completa con 20 % de contingencia, $1,83 millones, más $630.000 del tiempo interno recurrente de las semanas 4 a 26, a medida que cada línea queda en uso. Se libera solo con el Go de la semana 6.

## 2.7 Proveedor y contrato

No se contrata una herramienta ni un servicio nuevo, así que no corresponde comparar cotizaciones: el módulo de stock ya está en la licencia, sin costo de activación ni de soporte. Antes del Go hay que confirmar por escrito con Buenos Aires Software la versión de Discovery y que el módulo sigue incluido, el plazo de activación por línea y el soporte durante la puesta en marcha, si sumar usuarios en Producción y Depósito tiene costo, si hay ambiente de prueba y cómo se exportan el stock y los movimientos si algún día se deja Discovery. No hay gasto variable por uso; si alguno de estos puntos tuviera costo, se suma a la planilla y se revisa el caso antes de activar.

---

# 3. Plan de implementación y gobierno

El plan lo lleva adelante la propia empresa. Esta sección ajusta fechas y responsables de la Parte 2 y define el primer mes, las reglas de decisión y el traspaso.

## 3.1 Roadmap actualizado

Las cinco fases son las de la Parte 2, sección 8. Cambian las fechas (semana 1 = lunes 1-2-2027) y el responsable, según la segunda tabla.

| Fase | Semanas | Fechas | Cambios |
|---|---|---|---|
| 1. Preparación | 1 a 3 | 1 al 19-2 | A, B, C, D |
| 2. Piloto con papas fritas | 4 y 5 | 22-2 al 5-3 | B |
| 3. Decisión | 6 | 8 al 12-3 | B |
| 4. Activación por línea | 7 a 22 | 15-3 al 4-7 | A, B |
| 5. Estabilización | 23 a 26 | 5-7 al 1-8 | A, B |

| | De la Parte 2 a ahora | Motivo |
|---|---|---|
| A. Responsable | Del responsable de sistemas (Juanjo, servicio externo contratado) a un hijo como responsable único; Juanjo pasa a líder técnico, con suplente interno | Juanjo no es empleado |
| B. Calendario | De semanas relativas a semana 1 = 1-2-2027 | Se comienza después de las fiestas y las vacaciones |
| C. Horas extras | De ~25 por mes y meta de 12 o 13 a 40 a 50 (dato; esperado 45) y meta de 20 a 25 | Se midió mejor |
| D. Línea de base | De una semana de medición a tres, las semanas 1 a 3 | El 76 % sale de una sola semana (supuesto 9) |

Se pide aprobar las fases 1 a 3, con un tope de $712.600. El techo del proyecto completo, $2.457.883, se libera solo con el Go de la semana 6.

## 3.2 Primeros 30 días

La aprobación se necesita antes del viernes 15-1-2027, para comenzar la semana 1 el lunes 1-2-2027. El lunes siguiente a la aprobación se hace lo que no espera a febrero y solo requiere decisiones del dueño y datos que la empresa ya tiene.

| Cuándo | Tarea | Responsable | Entregable |
|---|---|---|---|
| Lunes siguiente a la aprobación (18-1 como máximo) | Designar por escrito al hijo responsable y al suplente interno; enviar a Buenos Aires Software la consulta escrita (versión, soporte, plazo, salida de datos, ambiente de prueba); pedir a liquidación 6 meses de horas extras | Dueño; hijo responsable | Designación y consulta enviadas |
| Semana 1 (1 al 5-2) | Designar al responsable de carga y su suplente; fijar umbrales y tope; primera reunión semanal; Oficina anota cada pedido con su faltante (línea de base, semanas 1 a 3) | Dueño; Oficina | Hoja de inicio firmada |
| Semana 2 (8 al 12-2, con Carnaval) | Armar la planilla de papas fritas y el tablero de indicadores; leer la respuesta del proveedor; calcular la base de horas extras | Responsable de sistemas y suplente interno | Planilla y tablero listos |
| Semana 3 (15 al 19-2; conteo el 20 y 21) | Medición previa de papas fritas; prueba técnica; capacitación con los casos de prueba; conteo inicial el fin de semana | Juanjo y suplente interno; Depósito | Casos aprobados, instructivo, stock inicial cargado |
| Semana 4 (22 al 26-2) | Comienza el piloto: carga diaria de 14:40 a 15:00, reserva antes de confirmar, reunión diaria de 10 minutos | Producción y Oficina | Primer informe de indicadores |

## 3.3 Gobierno

### Responsable único y líder técnico

La dirección designa al responsable único; proponemos a uno de los hijos, que ya decide la producción y mira los pedidos. Convoca la reunión semanal, lleva el tablero de tareas y decide cuando hay que cambiar algo; si falta una semana, lo reemplaza el otro hijo. Juanjo, responsable de sistemas y servicio externo contratado, es el líder técnico: planilla, prueba técnica y trato con Buenos Aires Software. Su suplente interno, una persona de Oficina que maneja Discovery, tiene usuario de administrador propio y repite con él cada tarea técnica durante el piloto.

Juanjo integra el grupo que redactó este trabajo, pero sus tareas en el plan son las de su servicio contratado con la empresa, que sigue después de este trabajo; si ese servicio termina, lo reemplazan el suplente interno y Buenos Aires Software.

### Matriz RACI

R hace, A responde, C se consulta, I se informa.

| Tarea | Dueño | Hijo resp. | Otro hijo | Resp. sistemas | Suplente interno | Oficina | Producción | Depósito | Proveedor |
|---|---|---|---|---|---|---|---|---|---|
| Decidir Go/Ajustar/Pausar y gastos | A | R | C | C | I | I | I | I | - |
| Conducir el proyecto y el tablero de tareas | I | A/R | C | C | C | C | C | C | - |
| Cargar el tablero de indicadores y mantenerlo | I | A | I | C | R | R | I | I | - |
| Planilla, prueba técnica y administración de Discovery | I | A | I | R | R | C | I | C | - |
| Cargar pedidos, reservar y avisar faltantes | I | A | I | C | C | R | I | I | - |
| Cargar producción y contar stock | I | A | I | C | I | I | R | R | - |
| Activar el módulo por línea | I | A | I | R | R | C | C | C | R |

### Seguimiento

Reunión semanal de 20 minutos, los lunes, con el hijo responsable, el suplente interno o el responsable de sistemas y un referente de cada área: 5 minutos para indicadores, 10 para tareas y 5 para acuerdos. El tablero de tareas (pendiente, en curso, listo; una tarjeta con responsable y fecha) lo lleva el hijo responsable; el de indicadores lo carga Oficina y lo mantiene el suplente interno. Los acuerdos van a una hoja compartida con fecha, responsable y plazo, y lo incumplido vuelve a la reunión siguiente.

### Quién decide

| Decisión | Quién |
|---|---|
| Ajustes dentro de lo acordado (horario de la carga, orden de tareas) | Hijo responsable; queda en el registro |
| Pausar o activar el plan B | El hijo responsable, el mismo día; reanudar o avanzar, el dueño |
| Alcance: sumar o sacar una línea, repetir el piloto, cambiar el orden | Dueño, a propuesta del hijo responsable |
| Costo: gasto fuera del tope del piloto o del techo | Dueño; dentro de esos montos, el hijo responsable |
| Operación: horarios, tareas de una persona, atención a distribuidores | Dueño con el otro hijo |

## 3.4 Puntos de decisión

Partimos de los umbrales de la Parte 2, sección 7; el dueño los acuerda o cambia en la semana 1, antes de ver resultados, y decide en cada punto. Para la carga se agrega un tramo intermedio (5 a 7 de 10 días): ya hay hábito y se resuelve con capacitación.

| Punto | Cuándo | Qué se decide |
|---|---|---|
| 1 | Semana 6 (jueves 11-3-2027) | Piloto: activar Salados, repetir o parar |
| 2 | Semana 12 (viernes 23-4-2027) | Salados: pasar a la segunda línea |
| 3 | Semana 17 (viernes 28-5-2027) | Segunda línea: pasar a la tercera |
| 4 | Semana 22 (viernes 2-7-2027) | Tercera línea: pasar a la estabilización |
| 5 | Semana 26 (viernes 30-7-2027) | Cierre: seguir, revisar metas o frenar |

En los puntos 1 a 4 se miran las mismas cuatro medidas, sobre papas fritas o sobre las semanas completas desde el corte de la línea recién activada (4 en Salados, 3 en las otras dos).

| Medida | Go | Ajustar | Pausar |
|---|---|---|---|
| Días con producción cargada | 80 % o más (8 de 10 en el piloto) | 50 a 79 % | Menos de 50 % |
| Pedidos recortados o demorados, contra su base | Piloto: la mitad o menos. Líneas: 70 % o menos. Sin que suban los rechazados | Piloto: 51 a 80 %. Líneas: 71 a 80 % | Más de 80 % |
| Exactitud de stock: productos dentro de la tolerancia de 10 % | 9 de cada 10 o más | 80 a 89 % | Menos de 80 % |
| Fechas estimadas cumplidas | 80 % o más | 60 a 79 % | Menos de 60 % |

Es Go si las cuatro medidas están en Go, Pausar si la carga o dos medidas están en Pausar, y Ajustar en el resto. El Go del punto 1 exige además que la prueba técnica pase y que el recupero con costos reales no supere los 13 meses del conservador. El de los puntos 2 a 4 exige que las horas extras no superen las de hoy, 45 por mes (sin las del conteo inicial): si las superan, la línea siguiente se frena y el punto queda en Ajustar, igual que si la carga diaria (de 14:40 a 15:00, dentro del turno) genera horas extras.

Con Go sigue el roadmap y, en el punto 1, se libera el techo. Con Ajustar se resuelve lo que falló y se repite el piloto o la medición de la línea; si al repetir no hay Go, es Pausar. Con Pausar no se avanza ni se gasta más, y a las 4 semanas el dueño decide entre revisar la causa o volver al proceso anterior (sección 4).

El punto 5 mira los resultados, con la carga y la exactitud todavía en Go. En horas extras por mes, Go es 32 o menos, Ajustar 33 a 45 y Pausar más de 45, la misma cifra que frena una línea; en pedidos completos y a tiempo, Go es 90 % o más, Ajustar 83 a 89 % y Pausar menos de 83 %. El escenario conservador del caso, con unas 38 horas extras y 83 %, queda en Ajustar.

## 3.5 Indicadores de seguimiento

Son los cuatro de la Parte 2, sección 8. Oficina los carga en el tablero de indicadores, que mantiene el suplente interno.

| Indicador | Línea base | Meta a 6 meses | Fuente y frecuencia |
|---|---|---|---|
| Pedidos completos y a tiempo | 76 % (dato de una semana: 30 de ~125); se vuelve a medir en las semanas 1 a 3 | 90 % | Registro de Oficina; diario, informe semanal |
| Exactitud de stock | El conteo inicial; hoy el stock no se registra | 9 de cada 10 productos dentro de la tolerancia de 10 % | Conteo de Depósito contra planilla o Discovery; semanal |
| Días con producción cargada | 20 % (dato: una vez por semana) | 100 % | Partes de producción; diario, informe semanal |
| Horas extras por mes | 40 a 50 (dato; esperado 45), sin las del conteo inicial | 20 a 25 | Liquidación de sueldos; mensual |

Si el promedio de las semanas 1 a 3 se aleja más de 5 puntos del 76 %, el hijo responsable lo informa al dueño en la semana 4 y se revisan las metas (supuesto 9 de la Parte 2).

## 3.6 Puesta en marcha

### Datos

Cada producto se cuenta entero antes de usarse: papas fritas el 20 y 21-2 y cada línea el fin de semana anterior a su corte. Cuenta Depósito con una segunda persona que anota (esas horas extras están en la inversión inicial, sección 2). Ese conteo es el stock inicial de la línea: lo carga el suplente interno, Depósito firma la hoja y el hijo responsable da el visto bueno. Otra persona recuenta al azar hasta 10 productos; la línea se da por buena si al menos 9 de cada 10 están dentro de la tolerancia de 10 %, y si no se repite el conteo. Oficina revisa que no haya productos o distribuidores duplicados antes de cada línea.

### Pruebas

Los casos los prueban quienes los hacen a diario, con pedidos de la semana anterior, y el suplente interno o el responsable de sistemas anota el resultado. Se aprueba con 7 de 7 y se repiten antes de cada línea. Sin ambiente de prueba, el caso 4 espera al primer pedido real.

| # | Caso | Resultado esperado |
|---|---|---|
| 1 | Pedido normal, con stock | Se reserva y confirma; baja el disponible |
| 2 | Faltante parcial | Oficina avisa con fecha; lo disponible sale si el distribuidor acepta |
| 3 | Cancelación con reserva | Se anula la nota y el disponible vuelve a subir |
| 4 | Factura que consume la reserva | Baja el físico y el disponible no cambia |
| 5 | Carga diaria | De 14:40 a 15:00 suben físico y disponible, con fecha y responsable |
| 6 | Ajuste por conteo | Movimiento nuevo con motivo; manda lo contado |
| 7 | Carga del suplente | El parte queda cargado sin ayuda del responsable de sistemas |

### Día de corte y convivencia

En el piloto, papas fritas va en la planilla desde el lunes 22-2, con el control semanal de Producción en paralelo solo para comparar. En Discovery, cada línea tiene su corte el lunes posterior a su conteo inicial y su capacitación: Salados el 29-3, la segunda línea el 10-5 y la tercera el 14-6. Durante 2 semanas hay doble registro con el control semanal y después vale solo Discovery. La planilla se archiva en el corte de Salados sin trasladar su saldo: el stock inicial de cada línea sale de su propio conteo. Si un día el dato no está al día, Oficina confirma como siempre y lo anota; si una línea falla, vuelve atrás solo esa (sección 4).

## 3.7 Traspaso a la operación

| Tema | Cómo queda |
|---|---|
| Quién administra | El suplente interno, con autorización del hijo responsable: altas y bajas, productos, distribuidores, stock mínimo, ajustes de conteo, exportación semanal y restauración, con Juanjo de respaldo. El hijo responsable también tiene credenciales de administrador |
| A quién se consulta | Una sola cadena: referente del área, suplente interno, Juanjo y Buenos Aires Software; si uno no responde en un día hábil, se pasa al siguiente. Cuando hay que cambiar algo, decide el hijo responsable |
| Documentación | Procedimiento de 2 páginas, instructivo de 1 página por área, hoja de conteo, casos de prueba, registro de acuerdos y contactos, en una carpeta de la empresa |
| Revisiones de beneficios | A los 3 y 6 meses del cierre del proyecto (fines de octubre de 2027 y de enero de 2028) |

En cada revisión, el suplente interno prepara los datos de los tableros y de la liquidación, y el hijo responsable los presenta al dueño. Se comparan con la línea de base (76 % de pedidos completos y a tiempo, 45 horas extras por mes, 20 % de días con carga) y con el beneficio neto del caso, $343.000 por mes en el conservador. A los 3 meses la referencia es ese escenario (83 % y unas 38 horas extras); a los 6, las metas (90 % y 20 a 25 horas extras). Si no se alcanzan, el dueño decide, tras revisar la causa (supuestos 2, 5 y 7 de la Parte 2), entre ajustar la meta, reforzar a quien haga falta o volver al proceso anterior (sección 4).

---

# 4. Riesgos, seguridad y continuidad

Esta sección trata lo que puede salir mal al ejecutar el plan. Los supuestos de la Parte 2 se prueban en el piloto (Parte 2, sección 7) y la adopción, el riesgo más probable, está en la sección 5.

## 4.1 Registro de riesgos

Probabilidad e impacto son una lectura nuestra (hipótesis) y se revisan en cada punto de decisión. Van ordenados por urgencia.

| Riesgo | Prob. | Impacto | Señal de alerta | Medida preventiva | Plan si ocurre | Responsable |
|---|---|---|---|---|---|---|
| Datos: el disponible no coincide con lo que hay | Alta | Alto | Menos de 9 de cada 10 productos dentro de la tolerancia de 10 %; reservas abiertas pasadas de plazo | Conteo inicial por línea con visto bueno de Depósito; manda lo contado; Oficina revisa las reservas cada semana | Se frena la línea siguiente, se recuenta la afectada y Oficina confirma como hoy | Hijo responsable; Depósito cuenta |
| Dependencia de Juanjo: es externo y el único que conoce Discovery a fondo | Media | Alto | No responde en un día hábil; una tarea técnica que solo él sabe hacer | Instructivo por tarea técnica, que el suplente interno hace una vez con él mirando; contacto de soporte con nombre en Buenos Aires Software | El suplente interno usa el instructivo y consulta al proveedor; pasados 5 días hábiles, Plan B | Hijo responsable; el dueño acuerda la disponibilidad con Juanjo |
| Continuidad: un solo turno (Producción de 6 a 15 h, Depósito de 8 a 18 h) | Media | Alto | La carga de 14:40 a 15:00 se atrasa; falta quien carga o quien reserva | Responsable de carga con suplente; carga dentro del turno; segunda persona de Oficina que sepa reservar; conteo semanal solo de las líneas activas | Oficina confirma como hoy, anota en la hoja de contingencia y se carga al día siguiente | Hijo responsable |
| Seguridad y respaldo: usuarios compartidos, accesos abiertos o pérdida de datos | Media | Alto | Una clave compartida; una baja que no se hizo; una exportación semanal que no se hizo o que no abre | Un usuario por persona, con permisos según la tarea si Discovery lo permite; baja el mismo día; exportación semanal fuera de las PC de la planta; prueba de restauración en el piloto | Cambiar la clave y revisar los movimientos del usuario; restaurar la última copia y recargar lo posterior desde la hoja de contingencia | Hijo responsable; el suplente interno hace altas, bajas, exportación y restauración, con Juanjo de respaldo |
| Buenos Aires Software: soporte lento o un paso que el módulo no resuelve (reparto parcial, factura que consume la reserva) | Media | Medio | Consultas sin respuesta; una prueba técnica falla; Discovery contradice al conteo | Versión, soporte, plazo y salida de datos por escrito antes del piloto; casos de prueba tras cada actualización | Seguir con la planilla y no activar más líneas hasta resolverlo | Hijo responsable, con apoyo del responsable de sistemas |
| Caja: el gasto pasa el tope o el ahorro llega tarde | Media | Medio | Gasto cerca del tope del piloto ($712.600); dos meses después de activar una línea, las horas extras no bajan | Aprobación por tramos: tope del piloto ahora y techo ($2.457.883) solo con el Go; contingencia de 20 % | Frenar la línea siguiente, sostener la activa y decidir en el próximo punto; nada se gasta sobre el tope sin el dueño | Dueño, con el hijo responsable |

## 4.2 Plan B

Se activa el mismo día y sin esperar al dueño, porque volver a confirmar como hoy cuesta lo mismo que no haber empezado (sección 2) y se puede deshacer. Lo declara el hijo responsable o, si no está, el otro hijo, cuando Discovery no anda, cuando lo que muestra no es confiable (dos conteos seguidos con menos de 9 de cada 10 productos dentro de la tolerancia, o un caso de prueba que falla) o cuando falta alguien clave sin reemplazo.

### Operación manual, paso a paso

| Paso | Qué se hace | Responsable |
|---|---|---|
| 1. Declarar | Avisa a Oficina, Producción y Depósito y anota hora y motivo en el registro de acuerdos | Hijo responsable |
| 2. Confirmar como hoy | Mira el depósito y consulta a Producción antes de confirmar, sin dar fecha estimada; cada pedido va a la hoja de contingencia (fecha, distribuidor, producto, cantidad, quién confirmó) | Oficina |
| 3. Producir y armar | Antes de las 15 h se anota lo producido en un parte en papel, con los datos de la carga; Depósito arma con la lista de siempre y anota faltantes y diferencias | Responsable de carga o su suplente; Depósito |
| 4. Avisar | Avisa ese día solo a quienes tienen una fecha estimada pendiente, para sostenerla o moverla | Oficina |
| 5. Resolver la causa | Diagnostica y consulta por la cadena de la sección 3 (traspaso) | Suplente interno, con el responsable de sistemas; el hijo responsable decide los cambios |
| 6. Revisar | Cada día de Plan B se mira en la reunión diaria; a los 5 días hábiles se decide reanudar o pausar | Dueño |

### Quién reemplaza a quién

| Rol | Lo reemplaza |
|---|---|
| Hijo responsable | El otro hijo, con el registro de acuerdos y el tablero de tareas |
| Juanjo | El suplente interno en las tareas del instructivo; Buenos Aires Software en Discovery |
| Suplente interno | El hijo responsable, que también tiene credenciales de administrador, y Juanjo |
| Responsable de carga | Su suplente, con el instructivo y el parte en papel |
| Oficina (reserva y confirma) | La segunda persona que sabe reservar, con la hoja de contingencia |
| Depósito (conteo) | Otro operario; si no hay nadie, el conteo se posterga una semana en vez de hacerlo apurado |

El hijo responsable puede pausar o activar el Plan B en cualquier momento; reanudar o avanzar lo decide el dueño, y sin él no se aprueba gasto nuevo.

### Vuelta al proceso anterior sin perder información

Si la decisión es pausar, o la falla no se resuelve:

1. Congelar. El suplente interno exporta el stock, las reservas abiertas y los movimientos, guarda el archivo con la fecha fuera de las PC y verifica que abre.
2. Cerrar reservas. Oficina factura o libera cada reserva abierta, para que no queden pedidos reservados sin armar.
3. Contar. Depósito cuenta la línea; ese conteo es el punto de partida si se reanuda.
4. Seguir como hoy y mantener la hoja de contingencia. Lo ya cargado queda en Discovery y en el archivo: nada se borra.
5. Cerrar. El dueño anota el motivo y el gasto hecho, que no pasa el tope.

Para volver a usar Discovery, Depósito cuenta de nuevo, Oficina y Producción cargan lo pendiente con su fecha y el hijo responsable confirma que el primer día coincide con lo contado.

---

# 5. Personas: cambio, capacitación y adopción

Los actores y sus estrategias son los de la Parte 2, sección 5. Acá van lo que cambió y cómo se comunica, se capacita y se mide el uso.

## 5.1 Lo que cambió desde la Parte 2

Juanjo es un servicio externo y sus horas ya están incluidas en lo que cobra. Su papel pasa a ser técnico: configura, prueba, capacita la primera vez y deja instructivos, pero no sostiene la rutina, que se reparte entre el suplente interno y el hijo responsable. La dependencia se trata en la sección 4.

En la Parte 2 los hijos aparecían como decisores con una posible resistencia a perder peso; ahora uno, el que designe la dirección (sección 3), lidera el cambio. Está en la planta y tiene autoridad ante el equipo, pero mide lo mismo que decide y puede no tener tiempo. Por eso el otro hijo revisa con él el tablero de tareas cada semana y el dueño acuerda por escrito el tiempo que se le reserva.

Las frases que se escuchan en la empresa se responden en la sección 7. Acá queda el miedo al cambio, que cuida tres cosas: no tener más trabajo, que el dato señale a alguien y que bajen las horas extras, que son ingreso. El dueño confirma ante todos que el dato sirve para planificar y no para evaluar, se dice qué tarea se saca por cada una que se suma y lo de las horas extras se habla de frente (sección 6).

## 5.2 Comunicación del cambio

Usamos ADKAR de forma práctica: conciencia y deseo se trabajan antes del piloto, conocimiento y habilidad en la capacitación, y refuerzo durante y después.

| Momento | Qué se dice | Quién | Cuándo y canal |
|---|---|---|---|
| Antes (conciencia) | 30 de ~125 pedidos por semana salen recortados o demorados; el piloto es de un producto, dura 2 semanas y se puede cortar; el dato no evalúa a nadie | Dueño, con el hijo responsable | Semana 1, reunión de 15 minutos con todos |
| Antes (deseo) | Qué les preocupa y qué pasos les hacen perder tiempo hoy; qué gana cada grupo: Oficina consulta y carga una vez, Producción cambia el control semanal por la carga diaria | Hijo responsable | Semanas 1 y 2, diez minutos con cada grupo en su puesto |
| Durante | Qué se trabó ayer y se resuelve en 2 días hábiles; qué molesta y qué ya cambió | Hijo responsable; dueño el día 5 | Últimos 5 minutos de la reunión diaria; reunión de 15 minutos el día 5; tablero de indicadores a la vista |
| Después (refuerzo) | El resultado con números y la decisión, también si es Pausar; en cada línea nueva, el mismo anuncio en 5 minutos; en las revisiones de beneficios, los recortes por semana contra la línea de base | Dueño | En los 2 días hábiles siguientes a cada punto de decisión y en cada revisión, en la planta |

## 5.3 Plan de capacitación

Cada tarea tiene un titular y un suplente, y los dos se capacitan. El responsable de sistemas da la primera sesión de cada grupo y deja un instructivo de una página; después capacita el hijo responsable o quien esté a cargo de Oficina, para que nada dependa de una persona externa.

| Grupo | Tiene que saber | Formato y duración | Responsable | Cómo se mide |
|---|---|---|---|---|
| Producción: responsable de carga y suplente (el resto, 15 minutos al empezar el piloto) | Cargar el parte de 14:40 a 15:00; corregir un error con un movimiento nuevo y su motivo, sin borrar | Práctica con la producción del día anterior, 1 hora; acompañado en los 2 primeros cierres | Juanjo la primera vez; hijo responsable después | Días con producción cargada |
| Oficina: referente y segunda persona | Consultar el disponible antes de confirmar; cargar y reservar una vez; avisar el faltante con fecha; liberar o facturar reservas viejas; usar la hoja de contingencia | Práctica con los casos de prueba, 2 sesiones de 1 hora; guion de aviso | El responsable de sistemas la primera vez; el referente capacita a la segunda persona | Pedidos reservados antes de confirmar; errores de carga |
| Depósito | Contar con la hoja de conteo; anotar faltantes y diferencias al armar; armar con la lista de Discovery | Conteo de papas fritas el fin de semana previo, acompañado; 1 hora | Hijo responsable, con Juanjo en el primer conteo | Conteos hechos contra los planificados; exactitud de stock |
| Dirección: dueño y los dos hijos | Leer el tablero de indicadores en 5 minutos; decidir qué producir con pedidos pendientes y stock mínimo; aplicar Go, Ajustar o Pausar | Práctica con los datos de las semanas 1 a 3, 1 hora | El responsable de sistemas la primera vez | Reuniones diarias hechas; decisiones de producción cambiadas por un pedido pendiente |

El soporte de cada grupo sigue la cadena de consulta del traspaso a la operación (sección 3). Al activar cada línea, los grupos repasan el instructivo en 30 minutos.

## 5.4 Adopción medida

Los tres indicadores salen de lo que el sistema registra (la planilla, en el piloto); no se le pregunta a nadie si lo usa. Se miran en la reunión semanal.

Los días con producción cargada (partes de producción; base 20 %) siguen la regla de la sección 3: en el piloto, 8 o más de 10 días es Go, 5 a 7 es Ajustar y menos de 5 es Pausar. Si no se llega, se mira el motivo anotado de cada día sin carga (turno apretado, PC ocupada, suplente sin capacitar) y se acorta lo que se carga, siempre dentro del turno; si la carga genera horas extras, es Ajustar.

Los otros dos tienen su propia escala:

| Indicador y fuente | En meta | Alerta | Fuera de meta | Si no se llega |
|---|---|---|---|---|
| Pedidos reservados antes de confirmar (hora de la reserva contra la de la confirmación; meta propuesta, a validar con las semanas 1 a 3) | 8 de cada 10 o más | 5 a 7 de cada 10 | Menos de 5 de cada 10 | Ver los confirmados sin reserva: dato desactualizado, olvido (lista corta junto a la PC) o presión de un distribuidor (guion de aviso) |
| Suplentes que cargan (movimientos por usuario; base anotada en las semanas 1 a 3) | El suplente del parte y el de la reserva cargaron esta semana | Solo uno de los dos | Ninguno | Fijar un día por semana en que el suplente hace la tarea, con el titular al lado; ajustar el instructivo |

Antes de atribuir un valor bajo a las personas se revisan la capacitación, la carga de trabajo y las reglas, en ese orden. Un valor en Alerta se ajusta durante 2 semanas; si sigue fuera de meta, el hijo responsable lo lleva al dueño, que decide si se pausa el avance.

---

# 6. Impactos responsables

El proyecto cambia sobre todo el trabajo de quienes ya están en la empresa; a los distribuidores casi no los toca, porque siguen pidiendo por WhatsApp o teléfono. Las medidas se revisan en cada punto de decisión.

| Impacto | A quién afecta | Medida de prevención o mejora |
|---|---|---|
| Menos horas extras, que para los operarios son ingreso. La meta es bajarlas de 40 a 50 por mes (dato) a 20 o 25 (hipótesis); el caso de negocio usa una baja más prudente, de unas 7 horas en el conservador y unas 13 en el esperado (estimación) | Operarios de Producción que hoy las hacen | Se avisa antes del piloto cuánto se espera que bajen, y baja por línea. Solo bajan las que se hacían por pedidos faltantes; las demás rotan entre quienes las hacen hoy. Los conteos de fin de semana, que se pagan como horas extras, se ofrecen primero a ellos. El dato de carga no se usa para evaluar personas ni para repartir horas extras |
| Cambio de tareas: se suman una carga diaria, una consulta antes de confirmar, un conteo semanal y una reunión diaria | Producción, Oficina, Depósito, dueño e hijos | Cada tarea nueva reemplaza otra: la carga diaria, al control semanal de Producción, y Oficina anota el pedido una vez en lugar de tres. La carga es de 14:40 a 15:00, dentro del turno. El caso no supone ninguna baja de personal y proponemos que el dueño lo diga al presentar el proyecto |
| Habilidad digital desigual: no todos usan la computadora con la misma soltura | Responsable de carga y personal de Oficina con menos práctica | Capacitación en el puesto con pedidos reales e instructivo de una página; el parte pide solo producto y cantidad. Quien tenga dificultad entrega el parte en papel y el suplente lo carga, sin que cuente como error |
| Papel: hoy el pedido se anota hasta en tres lugares, y parte de esas notas (avisos, acuerdos con cada distribuidor) no está en ningún otro lado | Oficina y Depósito; el ambiente | Antes del corte se revisa qué anotan además del pedido y se pasa a un campo de observaciones de la nota de pedido; papel y registro conviven hasta ese día. Después, el papel con datos de distribuidores se tritura o se recicla |
| Privacidad de los datos de los distribuidores: qué compra cada uno y cuánto pasa a más manos y, en el piloto, a una planilla fuera de Discovery | Los 57 distribuidores | La planilla usa número de pedido, producto y cantidad, sin datos fiscales ni de contacto, y la ven con cuenta de la empresa solo Oficina, Producción y el responsable; al terminar el piloto se archiva y se retira el acceso. En Discovery cada rol ve lo que necesita. Se confirma por escrito con Buenos Aires Software dónde se guardan los datos y quién accede |
| Energía y equipos: no se compran equipos | Ambiente | Se usan las PC que ya están en Producción y Depósito (dato). Si una falla, se repara o se reasigna antes de comprar, y la descartada va a reciclaje electrónico |

Dos cosas quedan sin compensar. La baja de horas extras en sí se acepta porque es el resultado que se busca: esas horas se hacían para completar pedidos que faltaron. Si la dirección quiere reconocer ese ingreso de otra forma, es una decisión suya que el caso de negocio no incluye. La energía de las PC, ya encendidas durante el turno, es un consumo marginal.

---

# 7. Preparación de la conversación con la dirección

Anticipamos lo que puede aparecer cuando la dirección analice la propuesta. Las objeciones son las que se escuchan en la empresa, según el relevamiento con el responsable de sistemas y las entrevistas de la Parte 1, más las que la Parte 2 ya había previsto. Todas parten de algo cierto y cada respuesta lo toma en cuenta.

## 7.1 Quién decide

Sobre la matriz de la Parte 2 (sección 5), aprueba el dueño, como sponsor y decisor de cada punto. Influyen los hijos, que deciden con él qué se produce; Juanjo, responsable de sistemas (servicio externo), con la mirada técnica; y Oficina y Producción, que no deciden pero pueden frenar el cambio con solo no cargar.

## 7.2 Objeciones

Cada cifra lleva su tipo: dato (lo dio la empresa), estimación (la calculamos, con su base) o hipótesis (a validar). Los montos están en pesos constantes de noviembre de 2026.

| Objeción | Respuesta con evidencia |
|---|---|
| «Siempre anduvo así» | Anduvo mientras el volumen y la mezcla de productos se podían seguir de memoria. En la semana que registramos, 30 de unos 125 pedidos salieron recortados o demorados (dato; el plan vuelve a medirlo en las semanas 1 a 3), cada uno con una hora de re-trabajo entre Oficina y Depósito (dato aproximado), y hay 40 a 50 horas extras por mes (dato). Seguir igual equivale a unos $1.570.000 por mes (estimación), de los cuales $270.000 son horas extras pagadas; el resto es tiempo de Oficina y Depósito |
| «Lo manejamos a simple vista, no hace falta» | Quien conoce la planta ve mucho, y ese conocimiento no se descarta. El límite es que el stock de producto terminado no se registra en ningún lado y Producción carga su control una vez por semana, así que el faltante aparece recién al armar el pedido. Si a simple vista alcanzaba, el piloto lo va a mostrar: 2 semanas con un solo producto, papas fritas, sobre una planilla y sin tocar Discovery; si los recortes no bajan, no se sigue |
| «La gente no va a cargar» | En una planta sin margen, una tarea más no se sostiene sola, y por eso es el riesgo principal. La carga diaria reemplaza el control semanal de Producción, se hace de 14:40 a 15:00 dentro del turno y el responsable de carga tiene suplente. Además se mide: en el piloto, cargar 8 de los 10 días hábiles es condición para el Go, y el dato se usa para planificar, no para evaluar. La sección 6 cuida el ingreso de quienes cargan |
| «No quiero depender de Juanjo o del proveedor» | Hoy el conocimiento técnico está en una sola persona externa, y el plan lo reparte. Un suplente interno aprende cada tarea con instructivos y hace las altas, bajas, exportaciones y restauraciones. El módulo de stock está dentro de la licencia, sin costo de activación ni de soporte (dato), y antes del piloto se confirman por escrito con Buenos Aires Software la versión, el soporte, el plazo y la salida de datos, con un contacto de soporte con nombre. Si algo falla, el plan B manual permite confirmar pedidos como hoy, sin perder información (sección 4) |
| «Si registramos el stock, pierdo el criterio al decidir qué producir» | El criterio de quienes conocen la planta sigue decidiendo: ningún sistema elige qué producir. Hoy se decide sin ver los pedidos pendientes, y por eso hay recortes aunque la planta trabaje al límite; con el stock y los pedidos en una hoja se decide con más información. Los hijos, además, fijan el stock mínimo de cada producto |
| «No sabemos si lo que se gasta se recupera» | Por eso el pedido es acotado. En el escenario conservador (la mitad de la mejora y más demora) el proyecto deja un neto de $343.000 por mes y se recupera en 13 meses; lo máximo que la empresa llega a poner antes de recuperar es $2,2 millones (estimaciones). Se aprueba el piloto, con tope de $712.600, y el techo, $2.457.883, se libera solo con un Go. No hay compra de equipos ni costo extra por las horas del responsable de sistemas (dato). Parte del beneficio es tiempo liberado en Oficina y Depósito, valorado al costo de su hora (sección 2) |

## 7.3 Mensaje central

Los pedidos que salen recortados o demorados, unos 30 de cada 125 por semana, equivalen para Dulxelitos a unos $1.570.000 por mes, de los cuales $270.000 son horas extras pagadas; el resto es tiempo de Oficina y Depósito. Con el stock a la vista esperamos llegar a 9 de cada 10 pedidos completos y a tiempo y a la mitad de las horas extras como meta (el caso de negocio usa una baja más prudente, de unas 6,6 a 13 horas por mes), y aun en el escenario conservador el proyecto deja $343.000 por mes una vez en marcha. Proponemos empezar con un piloto de 2 semanas con papas fritas, que se puede cortar en cualquier momento y cuesta como máximo $712.600; la decisión se necesita antes del viernes 15 de enero de 2027, para comenzar el lunes 1-2-2027.

---

# 8. Bibliografía

**Herramientas de análisis**

- Hiatt, J. M. (2006). *ADKAR: A Model for Change in Business, Government and Our Community*. Prosci.
- Mendelow, A. L. (1981). Environmental scanning: the impact of the stakeholder concept. *Proceedings of the Second International Conference on Information Systems*, 407-418.

**Fuentes primarias del caso**

- Lepez, J., Geyer, J. J., Lopez, J. y Sorato, E. (2026). *Trabajo Práctico Final - Parte 1: diagnóstico gerencial de Dulxelitos*.
- Lepez, J., Geyer, J. J., Lopez, J., Olivares, M. y Sorato, E. (2026). *Trabajo Práctico Final - Parte 2: propuesta de transformación de Dulxelitos*.
- Registros de la empresa (liquidación de sueldos, facturación y pedidos) relevados con el responsable de sistemas (2026).
- Relevamiento del proceso de atención de pedidos con un integrante del equipo que trabaja en Dulxelitos (2026), y entrevistas y observación directa del equipo en la organización (Parte 1).
