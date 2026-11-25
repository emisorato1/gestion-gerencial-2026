# Plan de implementación y gobierno

El plan lo lleva adelante la propia empresa. Esta sección ajusta fechas y responsables de la Parte 2 y define el primer mes, las reglas de decisión y el traspaso.

## Roadmap actualizado

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

Se pide aprobar las fases 1 a 3, con un tope de {inversion_piloto_conservador}. El techo del proyecto completo, {techo_proyecto_conservador}, se libera solo con el Go de la semana 6.

## Primeros 30 días

La aprobación se necesita antes del viernes 15-1-2027, para comenzar la semana 1 el lunes 1-2-2027. El lunes siguiente a la aprobación se hace lo que no espera a febrero y solo requiere decisiones del dueño y datos que la empresa ya tiene.

| Cuándo | Tarea | Responsable | Entregable |
|---|---|---|---|
| Lunes siguiente a la aprobación (18-1 como máximo) | Designar por escrito al hijo responsable y al suplente interno; enviar a Buenos Aires Software la consulta escrita (versión, soporte, plazo, salida de datos, ambiente de prueba); pedir a liquidación 6 meses de horas extras | Dueño; hijo responsable | Designación y consulta enviadas |
| Semana 1 (1 al 5-2) | Designar al responsable de carga y su suplente; fijar umbrales y tope; primera reunión semanal; Oficina anota cada pedido con su faltante (línea de base, semanas 1 a 3) | Dueño; Oficina | Hoja de inicio firmada |
| Semana 2 (8 al 12-2, con Carnaval) | Armar la planilla de papas fritas y el tablero de indicadores; leer la respuesta del proveedor; calcular la base de horas extras | Responsable de sistemas y suplente interno | Planilla y tablero listos |
| Semana 3 (15 al 19-2; conteo el 20 y 21) | Medición previa de papas fritas; prueba técnica; capacitación con los casos de prueba; conteo inicial el fin de semana | Juanjo y suplente interno; Depósito | Casos aprobados, instructivo, stock inicial cargado |
| Semana 4 (22 al 26-2) | Comienza el piloto: carga diaria de 14:40 a 15:00, reserva antes de confirmar, reunión diaria de 10 minutos | Producción y Oficina | Primer informe de indicadores |

## Gobierno

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

## Puntos de decisión

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

Es Go si las cuatro medidas están en Go, Pausar si la carga o dos medidas están en Pausar, y Ajustar en el resto. El Go del punto 1 exige además que la prueba técnica pase y que el recupero con costos reales no supere los {recupero_meses_conservador} meses del conservador. El de los puntos 2 a 4 exige que las horas extras no superen las de hoy, 45 por mes (sin las del conteo inicial): si las superan, la línea siguiente se frena y el punto queda en Ajustar, igual que si la carga diaria (de 14:40 a 15:00, dentro del turno) genera horas extras.

Con Go sigue el roadmap y, en el punto 1, se libera el techo. Con Ajustar se resuelve lo que falló y se repite el piloto o la medición de la línea; si al repetir no hay Go, es Pausar. Con Pausar no se avanza ni se gasta más, y a las 4 semanas el dueño decide entre revisar la causa o volver al proceso anterior (sección 4).

El punto 5 mira los resultados, con la carga y la exactitud todavía en Go. En horas extras por mes, Go es 32 o menos, Ajustar 33 a 45 y Pausar más de 45, la misma cifra que frena una línea; en pedidos completos y a tiempo, Go es 90 % o más, Ajustar 83 a 89 % y Pausar menos de 83 %. El escenario conservador del caso, con unas 38 horas extras y 83 %, queda en Ajustar.

## Indicadores de seguimiento

Son los cuatro de la Parte 2, sección 8. Oficina los carga en el tablero de indicadores, que mantiene el suplente interno.

| Indicador | Línea base | Meta a 6 meses | Fuente y frecuencia |
|---|---|---|---|
| Pedidos completos y a tiempo | 76 % (dato de una semana: 30 de ~125); se vuelve a medir en las semanas 1 a 3 | 90 % | Registro de Oficina; diario, informe semanal |
| Exactitud de stock | El conteo inicial; hoy el stock no se registra | 9 de cada 10 productos dentro de la tolerancia de 10 % | Conteo de Depósito contra planilla o Discovery; semanal |
| Días con producción cargada | 20 % (dato: una vez por semana) | 100 % | Partes de producción; diario, informe semanal |
| Horas extras por mes | 40 a 50 (dato; esperado 45), sin las del conteo inicial | 20 a 25 | Liquidación de sueldos; mensual |

Si el promedio de las semanas 1 a 3 se aleja más de 5 puntos del 76 %, el hijo responsable lo informa al dueño en la semana 4 y se revisan las metas (supuesto 9 de la Parte 2).

## Puesta en marcha

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

## Traspaso a la operación

| Tema | Cómo queda |
|---|---|
| Quién administra | El suplente interno, con autorización del hijo responsable: altas y bajas, productos, distribuidores, stock mínimo, ajustes de conteo, exportación semanal y restauración, con Juanjo de respaldo. El hijo responsable también tiene credenciales de administrador |
| A quién se consulta | Una sola cadena: referente del área, suplente interno, Juanjo y Buenos Aires Software; si uno no responde en un día hábil, se pasa al siguiente. Cuando hay que cambiar algo, decide el hijo responsable |
| Documentación | Procedimiento de 2 páginas, instructivo de 1 página por área, hoja de conteo, casos de prueba, registro de acuerdos y contactos, en una carpeta de la empresa |
| Revisiones de beneficios | A los 3 y 6 meses del cierre del proyecto (fines de octubre de 2027 y de enero de 2028) |

En cada revisión, el suplente interno prepara los datos de los tableros y de la liquidación, y el hijo responsable los presenta al dueño. Se comparan con la línea de base (76 % de pedidos completos y a tiempo, 45 horas extras por mes, 20 % de días con carga) y con el beneficio neto del caso, {neto_mensual_conservador} por mes en el conservador. A los 3 meses la referencia es ese escenario (83 % y unas 38 horas extras); a los 6, las metas (90 % y 20 a 25 horas extras). Si no se alcanzan, el dueño decide, tras revisar la causa (supuestos 2, 5 y 7 de la Parte 2), entre ajustar la meta, reforzar a quien haga falta o volver al proceso anterior (sección 4).
