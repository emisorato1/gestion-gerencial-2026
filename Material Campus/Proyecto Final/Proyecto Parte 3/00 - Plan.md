# Parte 3 (Dulxelitos): plan de ejecución

> Para agentes: usar superpowers:subagent-driven-development. Pasos con casillas (`- [ ]`).

**Objetivo:** dossier (PDF y Word), planilla del caso de negocio, presentación de la defensa y guion, listos antes del lunes 30-11-2026.

**Arquitectura:** igual que la Parte 2. Secciones sueltas `NN - *.md` en esta carpeta, que `armar-entrega.py` junta en `Entrega/`. La planilla la genera un script Python con openpyxl (fórmulas reales de Excel) y es la única fuente de los números: el dossier y la presentación copian de ella. La presentación sale de `armar-presentacion.js` (pptxgenjs) y el guion de `guion-exposicion.html` (weasyprint).

**Herramientas:** Python del venv de la Parte 2 (`../Proyecto Parte 2/.venv`, con weasyprint; se le instala openpyxl), pandoc, node con pptxgenjs (`../Proyecto Parte 2/node_modules`), Excel para recalcular y chequear la planilla (osascript), Keynote o PowerPoint para exportar miniaturas.

**Diseño:** `00 - Diseño.md` (esta carpeta). Todo agente lo lee entero antes de empezar.

## Reglas globales

- Estilo: `00 - Estilo.md` (esta carpeta) (grupo de alumnos, sin referencias a clases, transcripciones, cátedra, consigna ni IA; la Parte 2 como antecedente y nunca como error; sin "[dato pendiente]"; sin muletillas).
- Cada cifra lleva su tipo cuando se presenta por primera vez: dato, estimación o hipótesis.
- Solo roles, nunca nombres de personas (salvo "Juanjo" como responsable de sistemas, servicio externo, que el grupo autorizó).
- Pesos constantes de noviembre de 2026; horizonte 3 años.
- Línea de base de horas extras: 40 a 50 por mes (esperado 45). Se declara una vez como cambio respecto de la Parte 2 ("se midió mejor").
- Lo que no cambió de la Parte 2 se cita ("ver Parte 2, sección N"), no se copia.
- Largo total del dossier: 8.000 a 10.000 palabras.

## Puntos de revisión

1. Que las cifras del dossier, el resumen y la presentación coincidan exactamente con la planilla.
2. Que el escenario conservador cierre o, si no cierra, que se diga y se ajuste el alcance.
3. Que la semana 1 del plan sea ejecutable apenas se aprueba, sin depender del grupo ni solo de Juanjo.
4. Que las objeciones sean las de la empresa (diseño, sección "Datos") y las respuestas usen evidencia propia.
5. Que nada delate cómo se armó.

---

### Tarea 1 (Opus): planilla y caso de negocio

**Archivos:** crear `armar-planilla.py`, `02 - Caso de negocio.md`; genera `Entrega/TP Final Parte 3 - Dulxelitos - Caso de negocio.xlsx` y `caso.json`.

**Produce:** `caso.json` con las cifras que usan las demás tareas, con estas claves como mínimo: `inversion_piloto_conservador`, `techo_proyecto_conservador`, `inversion_total_esperado`, `inversion_total_conservador`, `neto_mensual_esperado`, `neto_mensual_conservador`, `max_expuesto_esperado`, `max_expuesto_conservador`, `recupero_meses_esperado`, `recupero_meses_conservador`, `van_3a_esperado`, `van_3a_conservador`, `tir_esperado`, `tir_conservador`, `costo_no_actuar_mensual`, `tasa_descuento_real_anual`.

- [ ] Instalar openpyxl en el venv de la Parte 2.
- [ ] Escribir `armar-planilla.py` con hojas: Supuestos (valor, unidad, tipo, fuente; los de la sección "Datos" del diseño más los que fije el agente, con su base), Escenarios (esperado y conservador lado a lado), Flujo mensual (12 meses según el roadmap: semana 1 = 1-2-2027, efectos desde la activación), Flujo anual (3 años), Indicadores (máximo expuesto, mes de recupero, VAN, TIR), Costo de no actuar. Todas las celdas derivadas con fórmulas de Excel que referencian a Supuestos; el script además calcula los mismos valores en Python y escribe `caso.json`.
- [ ] Verificar: abrir el xlsx en Excel (osascript), recalcular, exportar los indicadores y comparar con `caso.json` (tolerancia 1 peso; TIR 0,1 punto). Documentar el comando en el docstring.
- [ ] Escribir `02 - Caso de negocio.md` (`##` obligatorios: Costos, Beneficios, Costo de no actuar, Escenarios, Flujo de caja, Indicadores económicos, Proveedor y contrato), con las tablas que pide la consigna y cifras de `caso.json`. Incluir la sensibilidad del diseño (horas extras que bajan solo en proporción a los recortados).
- [ ] Reportar las cifras clave y si el conservador cierra.

### Tarea 2 (Sonnet): plan de implementación y gobierno

**Archivos:** crear `03 - Plan y gobierno.md`. **Consume:** diseño, Parte 2 secciones 03, 05, 07 y 08, y `caso.json` cuando exista (si no, deja las cifras como `{inversion_piloto_conservador}` para que la integración las reemplace).

- [ ] `##` obligatorios: Roadmap actualizado, Primeros 30 días, Gobierno, Puntos de decisión, Indicadores de seguimiento, Puesta en marcha, Traspaso a la operación. RACI con roles; responsable "a designar por la dirección (proponemos a uno de los hijos)"; Juanjo como líder técnico externo con suplente; 5 a 10 casos de prueba reales (pedido normal, pedido con faltante parcial, cancelación con reserva liberada, factura que consume la reserva, carga diaria, ajuste de conteo, etc.).

### Tarea 3 (Sonnet): riesgos y personas

**Archivos:** crear `04 - Riesgos y continuidad.md` y `05 - Personas.md`.

- [ ] 04: `##` Registro de riesgos (de ejecución, no repetir los supuestos de la Parte 2; cubrir caja, dependencia de Juanjo y de Buenos Aires Software, datos, continuidad) y Plan B (operación manual, reemplazos, aviso a distribuidores, vuelta al proceso anterior sin perder datos).
- [ ] 05: `##` Lo que cambió desde la Parte 2, Comunicación del cambio (ADKAR breve), Plan de capacitación (por grupo: qué sabe hacer, formato, duración, responsable, soporte, cómo se mide), Adopción medida (2 o 3 indicadores y qué se hace si no se llega).

### Tarea 4 (Sonnet): impactos y conversación con la dirección

**Archivos:** crear `06 - Impactos responsables.md` y `07 - Conversación con la dirección.md`.

- [ ] 06: tabla de 4 a 6 filas impacto / a quién afecta / medida (incluye que las horas extras son un ingreso de los operarios), con medidas concretas.
- [ ] 07: `##` Quién decide, Objeciones (5 o 6 de la empresa, con respuesta y evidencia; cifras de `caso.json` o marcadores), Mensaje central (3 frases).

### Tarea 5 (coordinación): armado, resumen y verificación

**Archivos:** copiar y adaptar `armar-entrega.py` y `verificar.py` de la Parte 2; crear `01 - Resumen ejecutivo.md`.

- [ ] `verificar.py`: delatores (como en la Parte 2), encabezados obligatorios de cada archivo, marcadores `{...}` sin reemplazar, y cifras del dossier que no estén en `caso.json` (advertencia).
- [ ] `armar-entrega.py`: portada "Trabajo Práctico Final - Parte 3 / Propuesta final para la dirección", secciones 01 a 07, bibliografía (libros de la Parte 2 más Kotter si se usa, Porter y Kramer si se usa, Cagan si se usa), salida `Entrega/TP Final Parte 3 - Dulxelitos.{md,docx,pdf}`.
- [ ] Reemplazar marcadores con `caso.json`, escribir el resumen (7 preguntas, 1 página), armar, verificar en OK.

### Tarea 6 (Sonnet): presentación

**Archivos:** copiar y adaptar `armar-presentacion.js` de la Parte 2 → `Entrega/Presentación TP Final Parte 3 - Dulxelitos.pptx`.

- [ ] 12 a 15 láminas para 20 minutos: el proyecto completo en 3 láminas (problema, propuesta, piloto) y el resto en la Parte 3 (caso con los dos escenarios, plan de 30 días, decisión que se pide, riesgos y plan B, personas, objeciones, cierre con el pedido). Misma paleta y estilo. Notas del orador sin nombres.

### Tarea 7 (Sonnet): guion

**Archivos:** adaptar `guion-exposicion.html` de la Parte 2 → `Entrega/Guion de exposición Parte 3 - Dulxelitos.pdf`, con miniaturas de las láminas.

- [ ] Por lámina: qué decir, en qué fijarse y preguntas probables del comité con su respuesta; sin asignar quién habla.

### Tarea 8 (Opus): revisión final

- [ ] Leer el dossier armado completo, la planilla y la presentación como el comité de dirección: coherencia de cifras con `caso.json`, consigna cubierta sección por sección, tono, delatores. Devolver hallazgos; la coordinación los corrige, rearma y verifica.

**Orden:** 1, 2, 3 y 4 en paralelo → 5 → 6 → 7 → 8. Commit y push al final, con el OK del grupo.
