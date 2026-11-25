# Diseño: TP Final Parte 3 (Dulxelitos)

_Acordado con el grupo el 2026-11-25 en una Meet con Juanjo presente. Defensa: **lunes 30-11-2026**._

## Qué es y para qué

La Parte 3 cierra el TP de Gestión Gerencial: un **dossier** que la dirección de Dulxelitos pueda leer y usar para decidir aunque el grupo no esté, y una **defensa de 20 a 25 minutos de todo el proyecto** ante la cátedra, que actúa como comité de dirección. La consigna está en `../Trabajo Práctico Final - Parte 3.md` y la guía resuelta de un caso ficticio en `../guia_socratica_parte3.html` (convertir a texto para leerla).

Reglas de la consigna que mandan sobre todo lo demás:

- No se rehace nada de las Partes 1 y 2: se cita lo que no cambió y se dice qué cambió y por qué.
- Cada número es un **dato** (lo dio la empresa), una **estimación** (cálculo con su base) o una **hipótesis** (a validar). Rangos y no precisión falsa.
- Proporcional a una pyme: una página clara antes que diez de teoría.
- El plan tiene que funcionar **sin el equipo de alumnos** y sin depender de una sola persona.
- Las objeciones salen de la empresa, no de la imaginación.

Antigoals: que delate cómo se armó (referencias a clases, transcripciones, IA, la Parte 2 contada como error), números sin fuente, o un caso que solo cierra en el escenario optimista sin decirlo.

## Base: lo entregado en la Parte 2

Fuente: `../Proyecto Parte 2/` (secciones 01 a 08 y `Entrega/`). Se reutiliza: problema (30 de ~125 pedidos semanales recortados o demorados, 76 % → 90 % en 6 meses), alternativa B (activar el módulo de stock de Discovery) con A (planilla) como piloto de 2 semanas con papas fritas, regla de stock disponible, roadmap de 5 fases en 26 semanas, 9 supuestos, 4 indicadores, stakeholders.

**Cambios respecto de la Parte 2** (se declaran en el dossier, en tono de "medido mejor", sin presentarlo como error):

| Qué | Parte 2 | Parte 3 | Por qué |
|---|---|---|---|
| Horas extras por mes | ~25 | **40 a 50** (esperado 45) | Se relevó mejor con la empresa después de la entrega |
| Meta de horas extras | ~12 o 13 | **la mitad: 20 a 25** | Misma lógica (supuesto 7), nueva base |
| Responsable del proyecto | Responsable de sistemas | **Uno de los hijos** como responsable único; **Juanjo** (responsable de sistemas, servicio externo contratado) como líder técnico | Juanjo no es empleado: la consigna pide un responsable de adentro y que nada dependa de una persona externa |
| Turnos | Pendiente | **Un turno**: Producción de 6 a 15 h, Depósito de 8 a 18 h, 44 h semanales; horas extras si hace falta | Dato de la empresa |
| Inicio del piloto | "Cuando el dueño apruebe" | **Febrero o marzo de 2027** | Decisión del grupo: después de fiestas y vacaciones |

## Datos de la empresa (Juanjo, 2026-11-25)

| Dato | Valor | Tipo |
|---|---|---|
| Hora normal de operario, con cargas | ~$8.000 | Dato aproximado |
| Hora extra | +50 %: ~$12.000 | Dato |
| Hora de Oficina / administrativa | ~$10.000 | Dato aproximado |
| Horas extras por mes, toda la planta | 40 a 50 | Dato |
| Pedido promedio de distribuidor | ~$1.200.000 | Dato aproximado |
| Parte que falta en un pedido recortado | 10 a 30 % | Dato aproximado |
| Qué pasa con lo faltante | Se manda después (no se pierde la venta); fuera de Mendoza va en otro envío | Dato |
| Flete | Lo paga el cliente, según el valor de la mercadería | Dato |
| Re-trabajo por pedido recortado (avisar, re-armar, facturar, coordinar) | ~1 hora (Oficina y Depósito) | Dato aproximado |
| Margen de la venta a distribuidores | 20 a 35 % | Dato aproximado |
| Módulo de stock de Discovery | Incluido en la licencia, **sin costo** de activación ni soporte | Dato |
| Horas de Juanjo en el proyecto | Incluidas en lo que ya cobra: **sin costo extra** | Dato |
| Equipos | Ya hay PC con Discovery en Producción y Depósito: **sin compra** | Dato |

Objeciones del dueño que Juanjo le escucharía: "siempre anduvo así", "la gente no va a cargar", miedo al cambio, "lo manejamos a simple vista, no hace falta". Más las que ya están en la Parte 2 (FUD del dueño e hijos: perder criterio, dudar del retorno).

Roles para RACI y textos: **solo roles**, sin nombres (repo público): dueño (sponsor), hijo responsable del proyecto, otro hijo, Juanjo como "responsable de sistemas (servicio externo)", encargada/o de Oficina, responsable de carga de Producción y suplente, Depósito, Buenos Aires Software, distribuidores.

## Caso de negocio (primera cuenta, a refinar en la planilla)

En **pesos constantes de noviembre de 2026** (sin inflación, para que los números se comparen), horizonte **3 años**, flujo mensual de 12 meses y anual después. Tasa de descuento real: la elige el builder y la declara (orden de magnitud 10 a 15 % anual real), con una frase de por qué.

| Concepto | Esperado | Conservador |
|---|---|---|
| Recortados por semana, de 30 a… | ~12,5 (meta 90 %) | ~21 (la mitad de la mejora) |
| Re-trabajo evitado (1 h × $10.000 por recortado) | ~$760.000/mes | ~$380.000/mes |
| Horas extras evitadas (de 45 h a $12.000; todas son de producción) | −50 %: ~$270.000/mes | −25 %: ~$135.000/mes |
| Demora de efecto | según roadmap | 1 o 2 meses más |
| Tiempo interno nuevo: carga diaria, reunión diaria, conteo semanal, revisión de reservas, neto de lo que reemplaza | ~$300.000/mes | ~$300.000/mes (o algo más) |
| Inversión inicial: conteos iniciales por línea (fin de semana, horas extras), capacitación, semana 0 y piloto, contingencia 15 % | ~$1,1 millones | ~$1,1 millones + contingencia 20 % |

Beneficios no medibles (se nombran, no se suman): cobranza que no se demora, distribuidor que no paga un segundo flete, información de stock, menor dependencia del "a simple vista". El margen de los recortados **no** se suma como venta ganada porque la venta no se pierde. Costo de no actuar = re-trabajo + horas extras de hoy (~$1,3M + ~$0,54M por mes), más el riesgo comercial sin cuantificar.

Proveedor y contrato: no se contrata herramienta nueva, así que **no aplican las dos cotizaciones**; se explica en una línea y se lista qué confirmar por escrito con Buenos Aires Software (versión, soporte, plazo, salida de datos).

El presupuesto que se pide aprobar sale del **escenario conservador**.

## Decisión que se pide

Aprobar el **piloto de 2 semanas con papas fritas para febrero o marzo de 2027**, con un tope de gasto (del conservador) y fecha de Go/Ajustar/Pausar; la activación de Discovery por línea se decide después con los resultados. Responsable: el hijo designado, con Juanjo como líder técnico.

## Entregables

Carpeta: `Material Campus/Proyecto Final/Proyecto Parte 3/` (esta).

1. **Dossier** en PDF y Word, armado con un `armar-entrega.py` derivado del de la Parte 2 (portada, índice, secciones 01 a 07, bibliografía), mismo estilo visual. Largo objetivo: 8.000 a 10.000 palabras, estilo resumido como la última versión de la Parte 2.
   - 01 Resumen ejecutivo (1 página, se escribe al final, va primero): las 7 preguntas.
   - 02 Caso de negocio.
   - 03 Plan de implementación y gobierno: roadmap actualizado (marcar cambios), primeros 30 días semana a semana (la semana 1 arranca apenas se aprueba), RACI con roles, responsable único, seguimiento (reunión de 20 min semanal, tablero pendiente/en curso/listo, registro de acuerdos), quién decide qué, puntos Go/Ajustar/Pausar con fecha, indicador y valores, indicadores con línea base y fuente, puesta en marcha (datos, 5 a 10 casos de prueba reales, día de corte), traspaso a la operación (quién administra, a quién se consulta, documentación, revisión a los 3 y 6 meses).
   - 04 Riesgos de ejecución y plan B (caja, dependencia de Juanjo y de Buenos Aires Software, datos, continuidad; vuelta al proceso anterior sin perder información).
   - 05 Personas: lo nuevo respecto de la Parte 2, comunicación (ADKAR, ya usado en la Parte 2), capacitación por grupo, 2 o 3 indicadores de adopción.
   - 06 Impactos responsables: tabla de 4 a 6 filas (horas extras como ingreso de los operarios, cambio de tareas, habilidad digital, papel, energía y equipos, privacidad de datos de distribuidores).
   - 07 Conversación con la dirección: quién aprueba e influye (sobre la matriz de la Parte 2), 5 o 6 objeciones reales con respuesta y evidencia, mensaje central en 3 frases.
2. **Planilla Excel** con fórmulas (`Entrega/... - Caso de negocio.xlsx`): hoja de supuestos (con tipo dato/estimación/hipótesis y fuente), escenarios esperado y conservador, flujo mensual de 12 meses y anual a 3 años, máximo expuesto, recupero, VAN y TIR. Los números del dossier salen de acá.
3. **Presentación** PowerPoint de la defensa: **todo el proyecto** (Partes 1, 2 y 3) en 20 a 25 minutos, foco en la Parte 3 y en la decisión; mismo estilo y paleta que las anteriores (`armar-presentacion.js`).
4. **Guion** de exposición en PDF, sin asignar quién dice cada cosa.

## Cómo se trabaja

- **Coordinación (sesión principal)**: reparte, integra, escribe el resumen ejecutivo y arma el dossier.
- **Agente Opus**: planilla y sección 02 (caso de negocio), donde están los cálculos y la trazabilidad; y la revisión final del dossier completo.
- **Agentes Sonnet en paralelo**: secciones 03 a 07, presentación y guion, con una guía común de estilo (la de humanizar de la Parte 2) y estos datos; después se revisa todo junto.
- Verificación: un `verificar.py` adaptado (delatores, encabezados obligatorios, cifras que coincidan con la planilla).
- Commit y push al terminar, con el OK del usuario.

## Respuestas a la revisión del diseño

- **Horas extras y re-trabajo no se superponen**: las horas extras se usan todas en producción y el re-trabajo de Oficina y Depósito es en horario normal (dato del grupo). La baja de horas extras se apoya en el supuesto 7: el esperado usa la meta (−50 %) y el conservador −25 %; la planilla muestra además qué pasa si baja solo en proporción a los recortados.
- **Fuente de los datos**: salen de registros de la empresa (liquidación, facturación) a los que accede Juanjo: se marcan como **dato**. El 76 % sigue siendo de una sola semana (supuesto 9) y la semana 1 del plan incluye volver a medir la línea base.
- **Cifras reales**: se usan los valores reales; el grupo autoriza publicarlos.
- **Fechas de entrega**: no las fija el diseño; el grupo termina todo antes de la defensa del lunes 30-11. Presentación pensada para 20 minutos con margen hasta 25.
- **Mis decisiones (marcadas en el dossier como propuestas)**:
  - Calendario en semanas relativas (S1, S2…) con un ejemplo anclado: **semana 1 = 1-2-2027**, preparación en febrero, piloto entre fines de febrero y principios de marzo, Go/No-Go a la semana 6. Decide el dueño, como en la Parte 2.
  - Lo que se pide aprobar: **tope del piloto** (fases 1 a 3, escenario conservador) y un **techo del proyecto completo** que se libera solo con el Go. El conservador usa 20 % de contingencia en lugar del 15 %.
  - El responsable único figura como **"a designar por la dirección; proponemos a uno de los hijos"**, y el dossier se redacta para que lo pueda leer la propia empresa: las objeciones y resistencias se presentan como lo que puede aparecer, con respeto.

## Lo que queda al builder

Tasa de descuento, distribución mensual exacta de costos y beneficios según el roadmap, horas de cada actividad interna (con base explícita), cantidad y diseño de láminas, casos de prueba concretos, redacción de las respuestas a objeciones.
