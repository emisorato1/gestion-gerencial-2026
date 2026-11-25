# Riesgos, seguridad y continuidad

Esta sección trata lo que puede salir mal al ejecutar el plan. Los supuestos de la Parte 2 se prueban en el piloto (Parte 2, sección 7) y la adopción, el riesgo más probable, está en la sección 5.

## Registro de riesgos

Probabilidad e impacto son una lectura nuestra (hipótesis) y se revisan en cada punto de decisión. Van ordenados por urgencia.

| Riesgo | Prob. | Impacto | Señal de alerta | Medida preventiva | Plan si ocurre | Responsable |
|---|---|---|---|---|---|---|
| Datos: el disponible no coincide con lo que hay | Alta | Alto | Menos de 9 de cada 10 productos dentro de la tolerancia de 10 %; reservas abiertas pasadas de plazo | Conteo inicial por línea con visto bueno de Depósito; manda lo contado; Oficina revisa las reservas cada semana | Se frena la línea siguiente, se recuenta la afectada y Oficina confirma como hoy | Hijo responsable; Depósito cuenta |
| Dependencia de Juanjo: es externo y el único que conoce Discovery a fondo | Media | Alto | No responde en un día hábil; una tarea técnica que solo él sabe hacer | Instructivo por tarea técnica, que el suplente interno hace una vez con él mirando; contacto de soporte con nombre en Buenos Aires Software | El suplente interno usa el instructivo y consulta al proveedor; pasados 5 días hábiles, Plan B | Hijo responsable; el dueño acuerda la disponibilidad con Juanjo |
| Continuidad: un solo turno (Producción de 6 a 15 h, Depósito de 8 a 18 h) | Media | Alto | La carga de 14:40 a 15:00 se atrasa; falta quien carga o quien reserva | Responsable de carga con suplente; carga dentro del turno; segunda persona de Oficina que sepa reservar; conteo semanal solo de las líneas activas | Oficina confirma como hoy, anota en la hoja de contingencia y se carga al día siguiente | Hijo responsable |
| Seguridad y respaldo: usuarios compartidos, accesos abiertos o pérdida de datos | Media | Alto | Una clave compartida; una baja que no se hizo; una exportación semanal que no se hizo o que no abre | Un usuario por persona, con permisos según la tarea si Discovery lo permite; baja el mismo día; exportación semanal fuera de las PC de la planta; prueba de restauración en el piloto | Cambiar la clave y revisar los movimientos del usuario; restaurar la última copia y recargar lo posterior desde la hoja de contingencia | Hijo responsable; el suplente interno hace altas, bajas, exportación y restauración, con Juanjo de respaldo |
| Buenos Aires Software: soporte lento o un paso que el módulo no resuelve (reparto parcial, factura que consume la reserva) | Media | Medio | Consultas sin respuesta; una prueba técnica falla; Discovery contradice al conteo | Versión, soporte, plazo y salida de datos por escrito antes del piloto; casos de prueba tras cada actualización | Seguir con la planilla y no activar más líneas hasta resolverlo | Hijo responsable, con apoyo del responsable de sistemas |
| Caja: el gasto pasa el tope o el ahorro llega tarde | Media | Medio | Gasto cerca del tope del piloto ({inversion_piloto_conservador}); dos meses después de activar una línea, las horas extras no bajan | Aprobación por tramos: tope del piloto ahora y techo ({techo_proyecto_conservador}) solo con el Go; contingencia de 20 % | Frenar la línea siguiente, sostener la activa y decidir en el próximo punto; nada se gasta sobre el tope sin el dueño | Dueño, con el hijo responsable |

## Plan B

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
