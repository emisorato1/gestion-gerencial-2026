# TP Final Parte 2 · Dulxelitos — Plan de trabajo

> **Para agentes:** usar superpowers:subagent-driven-development (recomendado) o superpowers:executing-plans,
> tarea por tarea. Los pasos usan casillas (`- [ ]`). Subagentes con **modelo sonnet** (pedido de Emiliano).

**Objetivo:** escribir la Parte 2 del TP Final (8 secciones más el problema gerencial pendiente de la Parte 1), con
BPMN AS-IS y TO-BE, informe en md/docx/pdf, presentación pptx y guion de exposición en PDF.

**Enfoque:** cada sección es un `.md` en esta carpeta, igual que la Parte 1. Un script verifica las reglas de la
cátedra en cada archivo y otro arma la entrega. Los BPMN se generan con un script desde una especificación en Python
(XML `.bpmn` que abre en Bizagi/Camunda + SVG/PNG para el informe).

**Herramientas:** Python 3 (venv local con `weasyprint` y `cairosvg`), pandoc, Node con `pptxgenjs`.

**Diseño:** `00 - Diseño.md` (aprobado por Emiliano el 2026-11-05). El plan argumenta desde el diseño: leer los dos.

Carpeta base de todas las rutas: `Material Campus/Proyecto Final/Proyecto Parte 2/` (abreviada `P2/`).

## Restricciones globales

- Lenguaje llano y en castellano rioplatense, como la Parte 1. Sin inventar datos.
- Cifras faltantes: `[dato pendiente: …]`. Nunca un número que no venga del diseño §9 o de una cuenta declarada.
- Datos del grupo: ~25 pedidos/día (~125/semana), 30 recortados o demorados por semana (~24 % → **76 %** completos y a
  tiempo, cuenta nuestra), ~25 horas extras/mes, producción cargada 1 vez por semana (**20 %** de los días).
- Problema gerencial: ≤ 60 palabras, sin las palabras `software`, `sistema`, `app`, `módulo`, `Discovery`, `planilla`.
- Corrección a la Parte 1 dicha explícitamente: el stock de producto terminado no se registra y los recortes vienen de
  mezcla y momento de producción, no de capacidad total.
- Stock disponible = stock físico − reservado por pedidos confirmados sin facturar (mismo criterio en A y en B).
- Alternativas: Do Nothing, A planilla compartida (piloto 2 semanas, papas fritas), B stock de Discovery
  (recomendada), C SaaS solo como evaluada y descartada.
- Sponsor: el dueño. Líder del proyecto: el responsable de sistemas. Matriz **Mendelow** (poder/interés).
- Fuera de alcance: insumos y packaging, visibilidad para el distribuidor ("later"), ampliación de planta, CRM, costeo.
- Indicadores: pedidos completos y a tiempo (plazo estándar por zona), exactitud de stock, días con producción cargada,
  horas extras por mes (totales). Cada uno con ficha de 8 elementos y meta en 5 partes. Más un OKR.
- Plazo del objetivo general: 6 meses. Roadmap now/next/later con Go/No-Go.
- Portada: Lepez Joaquín, Geyer Juan José, Lopez Juan, Olivares Manuel, Sorato Emiliano. Docentes: Ing. Jeremías Pino,
  Ing. Martín Noguerol.
- **No publicar Artifacts.** Trabajo pesado (pdf, pptx) con `nice -n 10`, de a uno.
- No mencionar a Claude ni a IA en el contenido entregable.

## Foco de revisión

1. **Contradicción con la Parte 1.** Cualquier frase que repita "el stock está en Discovery" o "los faltantes son por
   capacidad" sin la corrección. Lo verifica `verificar.py` (regla `parte1`).
2. **Números inventados.** Un costo, margen o VAN con cifra que no esté en el diseño. Lo verifica la regla `cifras`
   (lista blanca de números permitidos) y la revisión humana.
3. **El problema nombra una herramienta** o pasa de 60 palabras. Regla `problema`.
4. **BPMN inválido:** flujo de secuencia entre pools, flujo de mensaje dentro de un pool, actividad sin lane, falta
   evento de inicio o fin. Lo verifica `bpmn/generar_bpmn.py --validar`.
5. **Secciones desconectadas:** un indicador de §8 que no tenga línea de base del diseño, o una lane del BPMN que no
   esté en el RECI. Regla `trazas`.

---

### Tarea 1: Base de trabajo y verificador

**Archivos:**
- Crear: `P2/verificar.py`, `P2/.gitignore` (`.venv/`, `__pycache__/`)
- Crear: `P2/.venv/` (no se versiona)

**Interfaces:**
- Produce: `python3 verificar.py [archivo.md ...]` → imprime `OK` o una línea por falla con `archivo:línea regla
  mensaje`, y sale con código 1 si hay fallas. Sin argumentos, revisa todos los `NN - *.md` menos `00 - *`.
- Reglas: `problema` (en `01`: el bloque citado bajo "Problema gerencial" tiene ≤ 60 palabras y ninguna palabra
  prohibida), `parte1` (si el archivo menciona "Parte 1" junto a "stock" debe contener "corrige" o "corrección"),
  `cifras` (porcentajes y "horas" fuera de la lista blanca 76, 24, 25, 30, 125, 20, 6 meses, 2 semanas → advertencia,
  no error), `encabezados` (cada sección tiene los encabezados `##` que exige su tarea), `trazas` (cada indicador de
  `08` aparece con su línea de base; cada lane de `bpmn/as-is.py` aparece en el RECI de `02`), `pendientes` (cuenta
  los `[dato pendiente` y los lista, sin fallar).

- [ ] **Paso 1:** crear la venv: `python3 -m venv .venv && .venv/bin/pip install weasyprint cairosvg`. Esperado: sin
  errores. Instalar `pptxgenjs` en `P2/node_modules` con `npm install pptxgenjs` (agregar `node_modules/` al
  `.gitignore`).
- [ ] **Paso 2:** escribir `verificar.py` con las reglas de arriba y probarlo contra un archivo de prueba con un
  problema de 70 palabras que dice "sistema": esperado 2 fallas (`problema`). Borrar el archivo de prueba.
- [ ] **Paso 3:** commit `Base de la Parte 2: verificador y entorno`.

### Tarea 2: Problema gerencial, corrección a la Parte 1 y objetivos (§0 y §1)

**Archivo:** crear `P2/01 - Problema y objetivos.md`

Encabezados obligatorios: `## Lo que corrige el relevamiento`, `## Problema gerencial`, `## Objetivo general`,
`## Objetivos específicos`, `## Alcance`, `## Fuera de alcance`.

- [ ] **Paso 1:** redactar. Problema: partir del borrador del diseño §2 y fijar la meta (90 % sugerido) en el bloque
  citado. Objetivos específicos: 3, cada uno con métrica, línea de base, meta y plazo (pedidos completos 76 % → meta;
  producción cargada 20 % → 100 % de los días; horas extras ~25 → meta). La corrección cita las dos afirmaciones de la
  Parte 1 (§5.2 y §5.5 del informe de la Parte 1) y explica qué se encontró, con el mismo tono que el caso del
  catálogo web.
- [ ] **Paso 2:** `.venv/bin/python verificar.py "01 - Problema y objetivos.md"` → `OK`.
- [ ] **Paso 3:** commit.

### Tarea 3: Generador de BPMN y diagrama AS-IS

**Archivos:**
- Crear: `P2/bpmn/generar_bpmn.py`, `P2/bpmn/as-is.py` (especificación)
- Salidas: `P2/bpmn/as-is.bpmn`, `P2/bpmn/as-is.svg`, `P2/bpmn/as-is.png`

**Interfaces:**
- Produce: una especificación es un módulo Python con `PROCESO = {"nombre", "pools": [...], "flujos": [...],
  "mensajes": [...]}`. Cada pool: `{"id", "nombre", "colapsado": bool, "lanes": [{"id", "nombre", "nodos":
  [{"id", "tipo", "texto", "col"}]}]}`. `tipo` ∈ `inicio`, `inicio_mensaje`, `fin`, `tarea`, `tarea_usuario`,
  `xor`, `and`, `evento_tiempo`, `evento_mensaje`, `anotacion`, `datos`. `col` es la columna en la grilla.
- `python3 bpmn/generar_bpmn.py bpmn/as-is.py` escribe `.bpmn` (BPMN 2.0 con BPMNDI), `.svg` y `.png` (cairosvg).
- `--validar` falla si: hay flujo de secuencia entre pools, flujo de mensaje dentro de un pool, un pool no colapsado
  sin evento de inicio y de fin, o un nodo sin lane.

- [ ] **Paso 1:** escribir `generar_bpmn.py` con layout en grilla (columna × lane, 160 × 100 px), formas BPMN
  estándar (rectángulo redondeado, rombo con X o +, círculo fino/grueso, sobre para mensaje).
- [ ] **Paso 2:** escribir `as-is.py` según el diseño §3: pool Dulxelitos (lanes Oficina, Depósito, Producción,
  Dirección), pools colapsados Distribuidor y Transporte tercerizado. Incluir: anotar en papel/planilla, mirar a ojo,
  preguntar a producción, armar lista, preparar, XOR "¿Falta producto?" con tres salidas (mandar incompleto avisando,
  esperar producción, horas extras), facturar en Discovery, despachar. En Dirección: decidir producción, sin conexión
  con Oficina. Anotaciones con los dolores de las 3 lentes.
- [ ] **Paso 3:** `python3 bpmn/generar_bpmn.py bpmn/as-is.py --validar` → sin errores. Abrir el `.png` y revisarlo a
  ojo: que se lea en una hoja apaisada.
- [ ] **Paso 4:** commit.

### Tarea 4: Proceso AS-IS y alternativas (§2)

**Archivo:** crear `P2/02 - Proceso actual y alternativas.md`

Encabezados: `## Matriz de descubrimiento`, `## SIPOC`, `## RECI`, `## Diagrama AS-IS`, `## Tres lentes`,
`## Alternativas`, `## Matriz multicriterio`, `## Recomendación`.

- [ ] **Paso 1:** redactar. Matriz de descubrimiento (nombre, empieza, termina en camino feliz, áreas, volumen 25/día).
  SIPOC de 4 a 6 pasos. RECI con un solo R por actividad y con las mismas lanes que el BPMN. Diagrama: `![](bpmn/as-is.png)`
  con un párrafo de lectura, incluyendo las dependencias informales (WhatsApp, papel, autorizaciones de palabra). Tres
  lentes con un hallazgo concreto cada una y la pregunta del proceso balde. Alternativas Do Nothing, A, B, C con costo,
  qué resuelve y qué no. Matriz: los 10 criterios del enunciado, escala 1–5, justificación por celda, C descartada.
  Recomendación: B con A como piloto; retorno como punto de equilibrio con `[dato pendiente: costo de la hora extra]`.
- [ ] **Paso 2:** `verificar.py` → `OK` (incluye `trazas` contra `as-is.py`).
- [ ] **Paso 3:** commit.

### Tarea 5: Diagrama y sección TO-BE (§3)

**Archivos:** crear `P2/bpmn/to-be.py` (salidas `.bpmn/.svg/.png`) y `P2/03 - Proceso futuro.md`

Encabezados: `## Diagrama TO-BE`, `## Qué cambia`, `## Responsables y decisiones`, `## Datos y controles`.

- [ ] **Paso 1:** `to-be.py` según el diseño §3 TO-BE: carga diaria de producción, nota de pedido con reserva,
  XOR "¿Hay stock disponible?", aviso con fecha estimada, facturación que consume la reserva, planificación semanal en
  Dirección contra pedidos pendientes y stock mínimo, conteo cíclico semanal (evento de tiempo), reunión diaria
  ventas–producción. Validar con `--validar`.
- [ ] **Paso 2:** redactar `03` con tabla AS-IS vs TO-BE y la regla del stock disponible.
- [ ] **Paso 3:** `verificar.py` → `OK`. Commit.

### Tarea 6: Modelo de negocio y propuesta de valor (§4)

**Archivo:** crear `P2/04 - Modelo de negocio y propuesta de valor.md`

Encabezados: `## Cambios en el BMC`, `## VPC TO-BE`, `## Supuestos clave`.

- [ ] **Paso 1:** tabla de bloques AS-IS (de `../Proyecto/BMC - Dulxelitos.md`) → TO-BE, separando frontstage
  (relación: aviso confiable de faltantes) y backstage (actividades, recursos, costos). VPC del distribuidor
  patagónico (de `../Proyecto/04 - VPC - Distribuidor mayorista.md`): qué dolores alivia. Supuestos de deseabilidad,
  factibilidad y viabilidad, incluido el de la mezcla como causa.
- [ ] **Paso 2:** `verificar.py` → `OK`. Commit.

### Tarea 7: Stakeholders (§5)

**Archivo:** crear `P2/05 - Stakeholders.md`

Encabezados: `## Mapa de actores`, `## Matriz poder/interés`, `## Estrategias de involucramiento`,
`## Cómo cambia por fase`.

- [ ] **Paso 1:** actores del diseño §6. Matriz de Mendelow en tabla 2×2 y tabla por actor (interés, poder, impacto,
  resistencia, estrategia). Resistencias de Producción y Oficina con FUD y Heifetz (técnico vs. adaptativo). Movimiento
  por fase según 23-10.
- [ ] **Paso 2:** `verificar.py` → `OK`. Commit.

### Tarea 8: Arquitectura y flujo de datos (§6)

**Archivos:** crear `P2/06 - Arquitectura y datos.md` y `P2/diagramas/arquitectura.svg` (+ `.png` con cairosvg)

Encabezados: `## Diagrama`, `## Datos`, `## Integraciones`, `## Reglas de datos`.

- [ ] **Paso 1:** diagrama proporcional: WhatsApp/teléfono → Oficina → Discovery (pedidos, reservas, stock,
  facturación) ← carga diaria de Producción; planilla solo en el piloto; tablero de indicadores. SVG escrito a mano o
  desde un script chico en `diagramas/`.
- [ ] **Paso 2:** tabla de datos (dato, origen, destino, uso, responsable), maestros (productos, distribuidores, stock
  mínimo por producto) vs. transaccionales (pedidos, reservas, partes de producción, conteos), integraciones (carga
  manual controlada; exportación CSV para el tablero), reglas de alta, corrección y depuración.
- [ ] **Paso 3:** `verificar.py` → `OK`. Commit.

### Tarea 9: Validación de supuestos (§7)

**Archivo:** crear `P2/07 - Validación de supuestos.md`

Encabezados: `## Supuestos críticos`, `## Piloto`, `## Criterio de decisión`.

- [ ] **Paso 1:** tabla por supuesto (de `04` y `03`): tipo, probabilidad, impacto, señal temprana, mecanismo. Piloto
  A: 2 semanas, papas fritas, planilla con la misma regla de disponible, qué se mide (recortes de papas fritas, días
  cargados, diferencias de conteo) y el umbral de Go/No-Go. Incluir "el módulo de stock de Discovery funciona como se
  espera" con prueba en un producto antes de escalar. MVP como experimento mínimo, no versión beta (Clase 7).
- [ ] **Paso 2:** `verificar.py` → `OK`. Commit.

### Tarea 10: Roadmap, OKR e indicadores (§8)

**Archivo:** crear `P2/08 - Roadmap e indicadores.md`

Encabezados: `## Roadmap`, `## Cómo se protege la operación`, `## OKR`, `## Indicadores`.

- [ ] **Paso 1:** roadmap de 6 meses en tabla (fase, hito, entregable, responsable, duración, recursos,
  dependencias, Go/No-Go) y vista now/next/later. Protección de la operación del diseño §7. OKR con 3 resultados
  clave. Una ficha de 8 elementos por indicador, meta en 5 partes en una oración, contrapeso y si es de resultado o
  de avance.
- [ ] **Paso 2:** `verificar.py` → `OK` (regla `trazas`: cada línea de base coincide con el diseño). Commit.

### Tarea 11: Integración y entrega del informe

**Archivos:**
- Crear: `P2/00 - Integración.md` (cómo se encadenan las secciones, como el de la Parte 1)
- Crear: `P2/armar-entrega.py` (adaptado de `../Proyecto/armar-entrega.py`)
- Salidas: `P2/Entrega/TP Final Parte 2 - Dulxelitos.{md,docx,pdf}`

- [ ] **Paso 1:** `00 - Integración.md`: tabla de trazabilidad hallazgo → sección, y la cadena problema → proceso →
  alternativas → TO-BE → indicadores.
- [ ] **Paso 2:** adaptar el script: `NOMBRE`, `INTEGRANTES` con los cinco, orden de secciones 01–08, imágenes
  embebidas, anexo de datos pendientes (salida de la regla `pendientes`). Correr con
  `nice -n 10 .venv/bin/python armar-entrega.py`. Esperado: tres archivos en `Entrega/`.
- [ ] **Paso 3:** abrir el PDF y revisar portada, índice, que los diagramas se lean y que no haya texto cortado.
- [ ] **Paso 4:** commit.

### Tarea 12: Presentación y guion

**Archivos:** crear `P2/armar-presentacion.js` (adaptado de `../Proyecto/armar-presentacion.js`); salidas
`P2/Entrega/Presentación TP Final Parte 2 - Dulxelitos.pptx` y `P2/Entrega/Guion de exposición Parte 2 - Dulxelitos.pdf`

- [ ] **Paso 1:** 8–10 láminas, ~10 minutos, 5 expositores: problema, AS-IS, tres lentes, alternativas y
  recomendación, TO-BE, stakeholders, piloto, roadmap e indicadores, cierre. Mismo estilo que la Parte 1.
- [ ] **Paso 2:** guion en el formato del de la Parte 1 (qué decir por lámina, tiempos, datos que no podés errar,
  revisar antes de exponer). Generar el PDF con weasyprint desde un md/html.
- [ ] **Paso 3:** `nice -n 10 node armar-presentacion.js` y generar el guion; abrir ambos y revisar. Commit.

### Tarea 13: Revisión final

- [ ] **Paso 1:** `verificar.py` sobre todo → `OK`; listar los `[dato pendiente]` que quedan para Emiliano.
- [ ] **Paso 2:** revisión completa con un subagente sonnet nuevo contra el diseño, la consigna oficial y la Parte 1
  (contradicciones, números, coherencia entre secciones). Corregir lo que vuelva.
- [ ] **Paso 3:** commit final y resumen para Emiliano con lo que falta completar.

## Orden y paralelismo

Tarea 1 → 2 → 3 → 4 → 5. Después 6, 7, 8 y 9 en paralelo (dependen de 01–03). Después 10 → 11 → 12 → 13.
