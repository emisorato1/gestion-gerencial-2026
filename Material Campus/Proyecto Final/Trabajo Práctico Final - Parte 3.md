# Trabajo Práctico Final - Parte 3

## Propuesta final para la dirección: caso de negocio, plan y defensa

### Objetivo

Cerrar el proyecto. En la Parte 1 explicaron qué le pasa a la organización. En la Parte 2 diseñaron qué hacer. En la Parte 3 muestran **cuánto cuesta, cómo se ejecuta, qué puede salir mal y qué decisión se le pide a la dirección**.

El resultado es un único documento (el *dossier*) que la dirección de la PyME pueda leer, discutir y usar para decidir, aunque ustedes no estén presentes. Una vez presentado, la organización debería poder arrancar el primer paso del plan sin pedirles nada más.

### Cómo se trabaja esta parte

1. **Parten de lo ya hecho.** Usan los resultados de las Partes 1 y 2. **No se rehace nada**: se corrige y se completa con lo que la Parte 3 agrega (ver la tabla siguiente).
2. **Usan datos reales de la organización**, aunque sean aproximados. Cada número es un *dato* (lo dio la organización), una *estimación* (la calculamos, con su base) o una *hipótesis* (a validar).
3. **Todo es proporcional a una PyME.** Se prefiere una página clara a diez de teoría. Si una herramienta no aporta a la decisión, se omite.

### Qué se toma de las partes anteriores y qué se agrega

| Ya lo hicieron en… | Se reutiliza en la Parte 3 | Lo nuevo de la Parte 3 |
|---|---|---|
| Parte 2: matriz de alternativas y supuestos de viabilidad | §2 Caso de negocio | Costos y beneficios en dinero, **solo de la alternativa elegida** |
| Parte 2: roadmap, protección de la operación e indicadores | §3 Plan y gobierno | Primeros 30 días, RACI, umbrales de decisión, línea base medida, puesta en marcha y traspaso a la operación |
| Parte 2 §7: supuestos y validación (derisking) | §4 Riesgos | Estado de cada supuesto y riesgos de **ejecución** que no estaban |
| Parte 2 §5: stakeholders, resistencias y estrategia | §5 Personas y §7 Conversación con la dirección | Comunicación, capacitación, adopción medida y objeciones de los decisores |

Si algo de las Parte anteriores cambió, se indica qué cambió y por qué. Lo que no cambió se cita, no se copia.

### Cómo leer las consignas

Cada sección indica **qué hacer**, **qué entregar** y **cuándo está bien resuelta** (el control que pueden hacerse antes de entregar).

---

## 1. Resumen ejecutivo (1 página)

**Se escribe al final**, cuando el resto está cerrado, y va **al principio**.

**Qué hacer:** responder en una página estas siete preguntas:

1. ¿Quién es la organización y qué problema tiene? (una frase)
2. ¿Qué evidencia lo muestra? (dos o tres datos)
3. ¿Cuánto cuesta seguir igual?
4. ¿Qué proponemos hacer?
5. ¿Cuánto cuesta y qué se espera ganar? (rango)
6. ¿Cuál es el principal riesgo y cómo se controla?
7. **¿Qué decisión pedimos y para cuándo?**

**Cuándo está bien:** un gerente que lee solo esta página sabe qué se le pide aprobar, cuánto le cuesta y cómo se frena si no funciona.

---

## 2. Caso de negocio

**Qué hacer:** mostrar que la propuesta conviene económicamente y que el riesgo es razonable. Usar una planilla simple.

En la Parte 2 compararon alternativas con criterios cualitativos; acá se cuantifica **solo la alternativa elegida**. No se vuelve a presentar la matriz de alternativas.

**Qué entregar:**

| Elemento | Qué incluye |
|---|---|
| **Costos** | Inversión inicial (herramientas, configuración, equipos) y costos recurrentes (suscripciones, soporte, mantenimiento). Incluir también las **horas internas** (carga de datos, capacitación, reuniones), los **costos de transición** (período en que se trabaja con dos sistemas) y lo que haga falta para arrancar (celulares, conectividad, cuentas de usuario). Sumar una **contingencia del 10 % al 20 %** para imprevistos. Calcular a **3 años**. |
| **Beneficios** | Los que se pueden medir (horas ahorradas, errores evitados, ventas retenidas, cobranzas recuperadas, stock reducido, reclamos menos) y los que no (calidad de información, menor dependencia de personas clave). Para cada beneficio medible: cómo se calcula y de qué dato sale. |
| **Costo de no actuar** | Cuánto pierde la organización por mes o por año si no cambia nada (*Cost of Delay*). Es el número del costo de no actuar que describieron. |
| **Escenarios** | El mismo cálculo hecho dos veces: **esperado** y **conservador**. Ver el paso a paso en «Cómo armar los dos escenarios», debajo. |
| **Flujo de caja mensual** | Los primeros 6 a 12 meses: cuándo se paga y cuándo se empieza a recuperar. Trabajar en una sola moneda (conviene dólares si los costos están en dólares) e indicar el tipo de cambio usado. |
| **Indicadores económicos** | Recupero (en cuántos meses se recupera la inversión) VAN y TIR. |
| **Proveedor y contrato** | Solo si la propuesta incluye contratar una herramienta o un servicio. **Dos cotizaciones** como mínimo, comparadas en una tabla con: los requisitos imprescindibles que cumple cada una (por ejemplo, funcionar sin conexión, integrarse con el facturador), precio y cómo se ajusta, soporte incluido, plazo mínimo de contrato y cómo se recuperan los datos si se deja el servicio. |


- Cualquier número del caso se puede rastrear hasta su supuesto y su fuente.
- Usan rangos ("entre 40 % y 60 %") en lugar de precisión falsa.
- Muestran qué pasa en el escenario conservador; si ahí no cierra, lo dicen y ajustan la propuesta (por ejemplo, achicando el alcance).
- Los precios salen de cotizaciones o páginas oficiales con fecha de consulta, no de supuestos.
- Si hay gasto variable en la nube o por usuario, se indica cómo se controla (tope, alerta, revisión mensual).

### Cómo armar los dos escenarios

Un escenario es **el mismo cálculo con otros valores en los supuestos más inciertos**. Sirve para responder la pregunta que se va a hacer cualquier gerente: *si las cosas salen peor de lo que esperamos, ¿el proyecto sigue conviniendo?*

1. **Elegir los 2 o 3 supuestos más inciertos**: los que más cambian el resultado y de los que menos seguridad tienen. Suelen ser cuánto beneficio se logra (ventas, cobranzas, horas ahorradas), cuándo empieza a notarse y, si hay montos en dólares, el tipo de cambio o el precio del proveedor.
2. **Darle dos valores a cada uno:**
   - *Esperado*: el valor más probable según los datos de la organización.
   - *Conservador*: un valor pesimista pero creíble. Como referencia: la mitad del beneficio, uno o dos meses más de demora, o una suba del 30 % del dólar.

   Todos los demás supuestos quedan iguales en los dos escenarios.
3. **Calcular dos veces lo mismo**: flujo de caja mensual, máximo expuesto (el saldo acumulado más negativo, es decir, lo máximo que la organización pone antes de recuperar), mes de recupero, VAN y TIR.
4. **Presentar una tabla comparativa** como esta:

   | | Conservador | Esperado |
   |---|---|---|
   | Supuesto 1 (ej.: cobranza recuperada) | 25 % de la mora | 50 % de la mora |
   | Supuesto 2 (ej.: clientes retenidos por año) | 4 | 8 |
   | Supuesto 3 (ej.: tipo de cambio) | +30 % | Sin cambios |
   | **Máximo expuesto** | USD … | USD … |
   | **Mes de recupero** | … | … |
   | **VAN a 3 años** | USD … | USD … |
   | **TIR** | … | … |

5. **Interpretar en una o dos frases**: ¿el proyecto conviene también en el escenario conservador? Si conviene, la decisión es robusta. Si no conviene, lo dicen y ajustan la propuesta: alcance menor, piloto más chico o gasto escalonado.

El presupuesto que se pide aprobar (sección 8) se calcula con el **escenario conservador**, porque es el que muestra cuánta plata puede llegar a necesitarse.

---

## 3. Plan de implementación y gobierno

**Qué hacer:** el roadmap ya está hecho en la Parte 2 (fases, hitos, responsables, calendario e indicadores). **No se rehace.** Acá se completa con lo que falta para que la organización lo ejecute: **¿qué se hace el primer mes, quién decide, con qué números decidimos si seguimos, cómo se pone en marcha y quién lo sostiene cuando el equipo ya no esté?**

**Qué entregar:**

1. **Roadmap actualizado.** Insertar el roadmap de la Parte 2 en su versión corregida. Si cambió (fases, fechas, alcance), marcar los cambios y explicar el motivo en una línea.
2. **Primeros 30 días, semana a semana.** Tareas concretas, responsable y entregable de cada semana. **La primera semana debe poder empezar apenas se apruebe.**
3. **Gobierno liviano.**
   - **Matriz RACI** con las personas reales (tomadas de los stakeholders de la Parte 2): sponsor, responsable operativo, usuarios clave y proveedor. El equipo de alumnos puede figurar solo como apoyo hasta la entrega; **ninguna tarea posterior puede depender de ustedes**.
   - **Un responsable único** del proyecto del lado de la organización.
   - **Seguimiento:** reunión breve (por ejemplo, 20 minutos por semana), tablero simple (*pendiente / en curso / listo*) y registro de acuerdos.
   - **Quién decide qué:** cambios de alcance, de costo o que afecten la operación.
4. **Puntos de decisión *Go / Ajustar / Pausar*.** Para cada uno: fecha, qué indicador se mira y qué valor define cada resultado. Ejemplo: "A los 60 días, si más del 80 % de los pedidos del piloto está cargado, se avanza; entre 50 % y 80 %, se ajusta; menos de 50 %, se pausa".
5. **Indicadores de seguimiento.** No se definen indicadores nuevos: se toman los de la Parte 2 y se completa lo que falte (línea base **medida** con la organización o la forma de medirla, fuente del dato y frecuencia). Si se descartó alguno, explicar por qué.
6. **Puesta en marcha** (una tabla o lista breve):
   - **Datos:** qué datos se limpian y cargan, quién controla que lo cargado coincide con lo anterior (por ejemplo, saldos de clientes o stock) y quién da el visto bueno.
   - **Pruebas:** entre 5 y 10 casos reales del trabajo diario (un pedido normal, una devolución, un cobro parcial) que los usuarios prueban antes de empezar, con su resultado.
   - **Día de corte:** desde qué fecha deja de usarse la forma anterior y cuánto tiempo conviven las dos.
7. **Traspaso a la operación.** Qué queda funcionando cuando el proyecto termina:
   - Quién administra la solución (altas y bajas de usuarios, datos maestros, contacto con el proveedor).
   - A quién consultan los usuarios cuando algo no funciona.
   - Qué documentación queda (procedimiento del proceso nuevo, instructivos).
   - **Revisión de beneficios** a los 3 y 6 meses: quién mide, contra qué línea base y qué se decide si no se alcanza la meta.

**Nota:** si la dirección aprobara hoy, alguien sabe qué hacer el lunes. Los criterios de decisión son números, no opiniones. Y todo el plan funciona sin el equipo de alumnos.

---

## 4. Riesgos, seguridad y continuidad

**Qué hacer:** anticipar qué puede salir mal al ejecutar y cómo se responde. En la Parte 2 identificaron supuestos a validar *antes* de invertir; acá se tratan los riesgos de **ejecutar** el proyecto. No se repiten los supuestos de la Parte 2.

**Qué entregar:**

1. **Registro de riesgos de ejecución** (los importantes). Para cada uno: descripción, probabilidad, impacto, señal de alerta, medida preventiva, plan si ocurre y responsable. Cubrir al menos: caja y financiación, dependencia de un proveedor o de una persona, datos y continuidad de la operación. La adopción va en la sección 5.
2. **Plan B (contingencias).** En la Parte 2 explicaron cómo se protege la operación durante el proyecto; acá se detalla qué se hace, paso a paso y con responsable, **si algo falla**: operación manual temporal, quién reemplaza a las personas clave, aviso a clientes o proveedores y cómo se **vuelve al proceso anterior** sin perder información.

**Nota:** cada riesgo importante tiene un responsable y una acción concreta; el plan B se puede ejecutar el mismo día en que falla algo.

---

## 5. Personas: cambio, capacitación y adopción

**Qué hacer:** asegurar que las personas realmente usen la solución. Un proyecto técnicamente bueno que nadie usa no tiene valor.

**Qué entregar:**

1. **Punto de partida: los stakeholders de la Parte 2.** Las resistencias y estrategias por actor ya están analizadas; no se rehacen. Solo se agregan las que surgieron después (en entrevistas, en la validación de supuestos o en la devolución) y lo que cambió. Las resistencias se tratan como información para mejorar el plan, no como un obstáculo.
2. **Comunicación del cambio.** Qué se dice, quién lo dice, cuándo y por qué canal, antes, durante y después del piloto. Cómo se escucha a los usuarios y qué se ajusta con lo que dicen. Pueden apoyarse en ADKAR o Kotter, de forma breve y aplicada al caso.
3. **Plan de capacitación.** Para cada grupo: qué debe saber hacer (en acciones concretas), formato (microcapacitaciones, práctica con casos reales, instructivo de una página, acompañamiento en el puesto), duración, responsable, quién da soporte después y cómo se mide que lo usan.
4. **Adopción medida.** Dos o tres indicadores (por ejemplo, porcentaje de pedidos cargados, usuarios activos por semana, errores de carga) y qué se hace si no se llega.

**Nota:** no dice "se capacitará al personal". Dice quién, qué, cómo, cuándo, con qué material y cómo sabemos que funcionó.

---

## 6. Impactos responsables

**Qué hacer:** analizar quién puede resultar afectado por el proyecto, más allá de la organización, y qué se hace al respecto.

**Qué entregar:** tabla breve (entre cuatro y seis filas) con *impacto – a quién afecta – medida de prevención o mejora*. Considerar empleo y cambio de tareas, inclusión y accesibilidad (clientes o empleados con poca conectividad o habilidad digital), proveedores locales, papel, energía y residuos electrónicos. La privacidad de las personas (clientes, empleados) puede incluirse como impacto.

**Nota:** hay medidas concretas, no solo una lista de buenas intenciones. Si un impacto negativo no tiene una medida, se explica por qué se acepta.

---

## 7. Preparación de la conversación con la dirección

**Qué hacer:** anticipar cómo reaccionarán los decisores y preparar respuestas basadas en evidencia.

**Qué entregar:**

1. **Quién decide.** No se hace un mapa nuevo: sobre la matriz de stakeholders de la Parte 2, señalar en una línea quién aprueba esta propuesta y quién influye en esa decisión.
2. **Tabla de objeciones.** Las cinco o seis más probables *en esa organización* (no genéricas) y la respuesta con evidencia. Ejemplos de objeciones reales: "no tengo tiempo", "es caro", "ya probamos algo y no funcionó", "con WhatsApp nos arreglamos", "no quiero depender de un proveedor", "¿y si se cae el sistema?", "el contador no lo va a aceptar".
3. **El mensaje central**, en tres frases: el dolor, el resultado esperado y el primer paso de bajo riesgo.

**Nota:** las objeciones salen de las entrevistas con la organización, no de la imaginación del equipo.

---

## 8. Defensa final

**Formato:** presentación ante la cátedra, que actúa como comité de dirección de la organización. **20 minutos por equipo**.
