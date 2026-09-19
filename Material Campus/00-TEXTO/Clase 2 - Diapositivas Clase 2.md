# Diapositivas Clase 2

> Texto extraido de `Clase 2/Diapositivas Clase 2.pdf`, 47 paginas. Generado el 2026-09-18 20:36 por `sincronizacion-campus`. No editar a mano.

---

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

                                                              UTN-FRSR — Facultad Regional San Rafael

                    Clase 2: Estrategia, Cadena de Valor y Modelos de Negocio
                                Del Diagnóstico Estratégico al Diseño de Propuestas de Valor Habilitadas por Software
                                       Asignatura: Gestión Gerencial (5.º Año - ISI) | Carga Sincrónica: 2,0 hs reloj (120 min)

Ingeniería en Sistemas de Información | Plan 2026                                                                                 1

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

   🗺️ Mapa de Ruta: Estructura de la Sesión de 2 Horas
 Para construir el conocimiento de manera progresiva y con aplicación directa al Proyecto Integrador, dividiremos el trabajo en tres actos interconectados:

     ACTO 1 (40 min)                                           ACTO 2 (40 min)                                            ACTO 3 (40 min)

   Diagnóstico del Entorno                                    Arquitectura Interna                                      Modelado y Acción
   Comprenderemos qué es la estrategia corporativa,           Deconstruiremos la organización en su Cadena de           Diseñaremos el Business Model Canvas y el Value
   cómo se alinea con la tecnología y analizaremos las        Valor para entender dónde nace el margen                  Proposition Canvas para asegurar el encaje de la
   presiones macro y de la industria (PESTEL y 5              operativo, sintetizaremos con FODA Cruzado y              solución, formulando formalmente la Hipótesis del
   Fuerzas de Porter).                                        haremos un taller práctico en equipos.                    Hito 1 del TPI.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                           2

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

   🍷 Caso Guía Transversal: "Finca & Bodega San Rafael"
 A lo largo de toda la sesión utilizaremos una misma organización para comprender cómo cada herramienta de gestión aporta datos concretos para la toma de decisiones:

   🍇 "Finca & Bodega San Rafael" (Rama Caída)
   Se trata de una empresa familiar tradicional de San Rafael con 60 hectáreas de viñedos propios y una bodega de media escala. Históricamente, la empresa ha vendido
   vino a granel y botellas estándar a través de distribuidores mayoristas, sufriendo una constante pérdida de margen y plazos de cobro abusivos.

   El Desafío Estratégico: La dirección ha decidido diversificar el negocio hacia el enoturismo gastronómico de alta gama, la venta directa al consumidor (Direct-to-
   Consumer - DTC) mediante un club de vinos online, y la agricultura de precisión para afrontar la crisis hídrica regional.

   El Rol del Ingeniero en Sistemas: Actuar como consultores gerenciales para estructurar el diagnóstico y diseñar la arquitectura de procesos y software que haga viable
   este nuevo modelo de negocio.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                           3

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

    🧱 ¿Qué es (y qué NO es) la Estrategia Organizacional?
 En el ámbito tecnológico suele confundirse la estrategia con un plan operativo detallado o con la adopción de herramientas de moda. La estrategia gerencial tiene un
 significado mucho más profundo y riguroso:
 La estrategia es el conjunto coherente de elecciones deliberadas y asignación de recursos que una organización realiza para alcanzar un posicionamiento único, defendible
 y sostenible en el tiempo frente a la incertidumbre del entorno.

    ❌ Lo que NO es Estrategia                                                                           ✅ Lo que SÍ es Estrategia
    No es una lista de metas deseables ("ser líderes del mercado"), no es comprar                       Es una teoría explícita sobre cómo la empresa creará y capturará valor superior,
    software de última generación, ni es un cronograma rígido de actividades que                        definiendo claramente dónde va a competir, con qué propuesta distintiva y
    asume que el futuro es predecible.                                                                  cómo se defenderá de los rivales.

 Referencia académica: Porter, M. E. (1996). What is strategy? Harvard Business Review, 74(6), 61-78.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                          4

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🧭 Las Tres Preguntas Fundamentales de la Dirección
 Toda formulación estratégica responde a una secuencia lógica de tres interrogantes que estructuran la toma de decisiones gerenciales:

   1. ¿Dónde estamos hoy? (El Diagnóstico Riguroso)
   Requiere mirar hacia afuera para entender las presiones del entorno y de la industria, y mirar hacia adentro para evaluar con honestidad las capacidades y limitaciones
   reales de la organización.

   2. ¿Hacia dónde queremos ir? (El Propósito y la Visión)
   Define la aspiración ganadora de la empresa, su propuesta de valor para la sociedad y las metas de desempeño cuantificables a largo plazo que orientarán los esfuerzos
   colectivos.

   3. ¿Cómo llegaremos allí? (La Estrategia propiamente dicha)
   Es el puente entre el presente y el futuro deseado. Establece qué capacidades construiremos, qué modelo de negocio adoptaremos y cómo articularemos los sistemas
   de información para lograrlo.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                            5

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   ⚖️ La Regla de los Trade-offs: El Arte de Elegir qué NO Hacer
 Michael Porter demostró que una estrategia sin renuncias explícitas es simplemente una ilusión gerencial condenada al fracaso:

   "La esencia de la estrategia radica en realizar trade-offs al competir. La elección estratégica es decidir qué hacer y, fundamentalmente, qué NO hacer." — Michael E. Porter
   (1996)

   El Oportunismo Destructivo                                                                La Coherencia en Sistemas
   Las organizaciones que intentan ser todo para todos (el precio más bajo, la               Al diseñar software, los trade-offs son inevitables: no se puede optimizar
   mayor calidad, la atención más exclusiva y la mayor velocidad simultáneamente)            simultáneamente para latencia ultrabaja, consistencia estricta distribuida, costo
   terminan perdiendo su identidad y diluyen sus recursos sin destacar en nada.              mínimo y máxima flexibilidad. La estrategia del negocio guía esas prioridades
                                                                                             técnicas.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                 6

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   ⚡ Eficacia Operacional vs. Estrategia Competitiva
 El error más común en la gestión informática es confundir la optimización de procesos con tener una estrategia competitiva:

   ⚙️ Eficacia Operacional                                                                 🎯 Estrategia Competitiva
   "Hacer las mismas actividades que los rivales, pero un poco mejor, más rápido           "Hacer cosas diferentes a los rivales, o hacer actividades similares de una
   o con menos errores."                                                                   manera radicalmente distinta."

   Consiste en adoptar mejores prácticas de la industria: implementar pipelines            Consiste en ensamblar un sistema único y entrelazado de actividades diseñado
   CI/CD, metodologías ágiles, migrar a la nube o certificar normas de calidad ISO.        específicamente para entregar una propuesta de valor irrepetible para un
                                                                                           segmento de clientes elegido.
   Límite: Las mejores prácticas se difunden rápidamente; los rivales las copian y el
   beneficio termina trasladándose al cliente en forma de guerras de precios.              Impacto: Crea barreras de entrada reales y ventajas competitivas defendibles en
                                                                                           el tiempo que resultan muy complejas de clonar por la competencia.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                            7

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   ⚠️ La Trampa de la Convergencia Tecnológica
 ¿Qué sucede cuando todas las empresas de un mismo sector implementan exactamente el mismo software comercial estándar?

    🔍 El Fenómeno de la Comoditización Digital
    Si las 80 bodegas de San Rafael contratan el mismo ERP empaquetado, instalan la misma plantilla de e-commerce genérica y aplican las mismas campañas de
    marketing automatizadas en redes sociales, el resultado es la convergencia competitiva.

    Conclusión Gerencial para Ingenieros: La tecnología estándar de mercado es un *commodity* indispensable para operar (condición necesaria), pero la ventaja
    competitiva surge de cómo integramos esos sistemas con procesos propietarios, datos exclusivos y una experiencia de usuario singular (condición suficiente).

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                  8

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🏢 Los Tres Niveles Jerárquicos de la Estrategia
 Las decisiones directivas no ocurren en un solo plano; se estructuran jerárquicamente para mantener la coherencia en toda la firma:

   1. Estrategia Corporativa                                 2. Estrategia Competitiva                                 3. Estrategia Funcional / TI
   ¿En qué negocios debemos participar?                      ¿Cómo competiremos en este mercado                        ¿Cómo apoya cada área funcional?
                                                             específico?
   Define el perímetro global de la empresa:                                                                           Define cómo los sistemas de información, las
   diversificación de productos, fusiones, alianzas          Define la propuesta para superar a los                    operaciones, las finanzas y los recursos humanos
   internacionales y cómo se distribuye el presupuesto       competidores en una industria determinada: elegir         construyen las capacidades tecnológicas requeridas
   de inversión global entre las distintas unidades de       entre Liderazgo en Costos (precios bajos por gran         para ejecutar la estrategia de negocio.
   negocio.                                                  volumen) o Diferenciación (valor percibido
                                                             premium).

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                           9

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🧭 El Modelo de Alineación Estratégica (SAM)
 En 1993, John Henderson y N. Venkatraman publicaron en el IBM Systems Journal el marco conceptual definitivo sobre alineación:

   Dominio del Negocio                                                                    Dominio Tecnológico
   Estrategia del Negocio: Alcance de mercado, competencias distintivas y                 Estrategia de TI: Alcance tecnológico, competencias sistémicas y gobernanza de
   gobierno corporativo.                                                                  datos.
   Infraestructura Organizativa: Estructura jerárquica, flujos de procesos                Infraestructura de TI: Arquitectura de aplicaciones, servidores, bases de datos y
   administrativos y habilidades de las personas.                                         habilidades técnicas.

 Tesis Central de Henderson & Venkatraman: El valor de la tecnología nunca se genera de forma aislada; surge de la constante articulación entre el ajuste estratégico
 (externo) y la integración funcional (interna).

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                             10

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🧠 Diagnóstico de la Desalineación Estratégica
 ¿Cómo detecta un consultor gerencial que la tecnología de una empresa no está alineada con su estrategia?

   El Síndrome de la Solución sin Problema                                               La Brecha de Lenguaje y Métricas
   La organización adquiere herramientas complejas de Inteligencia Artificial            El área de TI reporta métricas puramente técnicas (latencia de 12ms, cobertura
   Generativa, Blockchain o microservicios simplemente porque son tendencia, sin         de código del 90%, 99.9% de uptime), mientras que la Dirección General evalúa
   haber clarificado qué ineficiencia operativa resuelven o qué valor aportan al         el negocio en retorno sobre la inversión (ROI), costo de adquisición de clientes
   cliente final.                                                                        (CAC) y margen operativo.

   Lección Gerencial: Si un proyecto informático no puede explicar con claridad cómo impactará en el estado de resultados o en la ventaja competitiva de la empresa, es
   un proyecto vulnerable y desalineado.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                           11

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🔄 El Pipeline de Herramientas de Gestión
 Para evitar la sensación de estar utilizando una "ensalada de herramientas inconexas", seguiremos un pipeline analítico riguroso:

   ┌────────────────────────────────────────────────────────┐
   │ 1. DIAGNÓSTICO DEL MACROENTORNO (PESTEL)               │ ──► Anticipa variables no controlables del contexto
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │ 2. ANÁLISIS INDUSTRIAL Y COMPETITIVO (5 FUERZAS)       │ ──► Mide el atractivo y el balance de poder sectorial
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │ 3. ANÁLISIS DE ACTIVIDADES INTERNAS (CADENA DE VALOR) │ ──► Deconstruye dónde se crea el margen y costo
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │ 4. SÍNTESIS Y DERIVACIÓN DE PROYECTOS (FODA CRUZADO)   │ ──► Convierte diagnósticos en iniciativas concretas
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │ 5. ARQUITECTURA DE VALOR Y ENCAJE (BMC + VPC)          │ ──► Modela la viabilidad económica y el valor percibido
   └──────────────────────────┬─────────────────────────────┘
                              ▼
   ┌────────────────────────────────────────────────────────┐
   │ 6. FORMULACIÓN FORMAL DEL DESAFÍO (HIPÓTESIS TPI)      │ ──► Estructura el problema para el Proyecto Integrador
   └────────────────────────────────────────────────────────┘

Ingeniería en Sistemas de Información | Plan 2026                                                                                    12

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

    🧱 Génesis y Evolución del Modelo PESTEL
 Las herramientas de gestión no son fórmulas fijas ni dogmas inmutables: son modelos conceptuales en continua construcción histórica:

     Origen Histórico (1967): Francis J. Aguilar (profesor de Harvard Business School) acuña en su libro Scanning the Business Environment el modelo pionero ETPS (Economic,
     Technical, Political, Social) como un método estructurado de "escaneo del entorno" para evitar la ceguera directiva.
     Evolución del Acrónimo: A medida que la complejidad económica y ecológica del planeta creció, el modelo se fue transformando:

     Se incorporaron explícitamente las dimensiones Ecológica/Ambiental (por el impacto del cambio climático) y Legal (por la proliferación de marcos normativos de
     privacidad y ciberdelito).
     Las Organizaciones como Sistemas Abiertos: Ninguna arquitectura de software funciona en un vacío técnico; PESTEL opera como un radar estratégico continuo que
     detecta señales tempranas antes de comprometer grandes inversiones.

 Referencia académica: Aguilar, F. J. (1967). Scanning the Business Environment. Macmillan.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                          13

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🔍 Las Seis Dimensiones del Macroentorno en Detalle
 Cada una de las dimensiones de PESTEL impone restricciones o genera oportunidades para los sistemas de información:

   🏛️ Político & Económico                                                                👥 Social & Tecnológico
   Político: Políticas fiscales, subsidios a la tecnología, estabilidad institucional y   Social: Demografía, cambios en hábitos de consumo, demandas de teletrabajo y
   acuerdos comerciales internacionales.                                                  cultura digital.

   Económico: Inflación, tipo de cambio, tasas de interés y poder adquisitivo de los      Tecnológico: Infraestructura de conectividad, madurez de la nube,
   consumidores locales.                                                                  automatización y adopción de IA.

   💧 Ecológico / Ambiental                                                                ⚖️ Legal & Regulatorio
   Ecológico: Disponibilidad de recursos naturales (agua, energía), huella de             Legal: Leyes de protección de datos personales (Ley 25.326), facturación
   carbono y regulaciones de sustentabilidad ambiental.                                   electrónica obligatoria y ciberdelito.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                        14

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🍇 PESTEL Aplicado a "Finca & Bodega San Rafael"
   Caso Guía: Diagnóstico del macroentorno para la transformación hacia enoturismo y agro-precisión

   🏛️ Político & Económico                                                                       👥 Social & Tecnológico
   Político: Programa provincial Mendoza Activa que subsidia hasta un 40% en                     Social: Nuevos turistas exigen reservas digitales inmediatas y pagos con QR sin
   equipamiento tecnológico y sistemas de riego.                                                 fricciones.
   Económico: Variación cambiaria que encarece servicios en la nube en dólares;                  Tecnológico: Escasa cobertura 4G en zonas rurales de Rama Caída; exige redes
   necesidad de evaluar arquitecturas con costos previsibles (FinOps).                           de sensores LoRaWAN de bajo consumo y protocolos livianos.

   💧 Ecológico                                                                                   ⚖️ Legal & Regulatorio
   Crisis Hídrica (Ríos Atuel y Diamante): Reducción histórica de caudales; se                   Normativas INV y ARCA: Trazabilidad física obligatoria de uvas cosechadas y
   vuelve obligatorio el riego por goteo automatizado sincronizado con los turnos                facturación electrónica instantánea en punto de venta.
   de Irrigación.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                  15

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

    🧱 Génesis y Fundamentos de las 5 Fuerzas de Porter
 En 1979, Michael Porter publicó en Harvard Business Review How competitive forces shape strategy, revolucionando el análisis de negocios:

     El Quiebre Epistemológico: Hasta ese momento, la estrategia se basaba en intuiciones o análisis FODA genéricos. Porter importó los principios de la Economía de
     Organización Industrial (el paradigma Estructura  Conducta      Desempeño de Bain y Mason) para demostrar que la rentabilidad promedio de una empresa está
     condicionada principalmente por la estructura del sector en el que opera.
     La Tesis Central: El atractivo de una industria no depende de que el producto sea sofisticado o tradicional, sino del balance de poder entre cinco fuerzas competitivas
     fundamentales que determinan cómo se distribuye el valor económico creado entre los distintos participantes del mercado.
     Un Campo de Tensiones Vivas: Las fuerzas no son un casillero estático; constituyen un sistema de presiones en constante reconfiguración.

 Referencias: Porter, M. E. (1979). How competitive forces shape strategy. Harvard Business Review, 57(2), 137-145.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                              16

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   ⚔️ Las Cinco Fuerzas que Estructuran la Competencia
   Fuerzas Verticales (Poder en la Cadena)                                              Fuerzas Horizontales (Amenazas Directas)
   1. Poder de Proveedores: Capacidad de imponer precios altos, plazos de entrega       3. Amenaza de Nuevos Entrantes: Facilidad con que nuevos competidores
   desfavorables o tecnologías cerradas que generan dependencia cautiva (*vendor        ingresan al mercado, mitigada por la altura de las barreras de entrada (capital,
   lock-in*).                                                                           datos, escala).

   2. Poder de Clientes: Capacidad de compradores concentrados de forzar                4. Amenaza de Productos Sustitutos: Tecnologías o soluciones alternativas que
   reducciones de precios, exigir mayores niveles de servicio o demandar                satisfacen la misma necesidad de fondo pero con modelos diferentes.
   integraciones a medida.

   5. Rivalidad en el Centro de la Industria:
   La intensidad con la que compiten las empresas establecidas mediante guerras de precios, publicidad masiva o diferenciación de productos.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                          17

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   ⚡ Cómo la Tecnología Reconfigura las Cinco Fuerzas
 A lo largo de cuatro décadas, Michael Porter analizó cómo los sistemas de información transforman radicalmente las dinámicas de poder sectorial:

    1985 (Porter & Millar): Demostraron que la intensidad de información en los productos y procesos altera los costos de cambio (switching costs) y crea lazos directos con
    los clientes.
    2001 (Strategy and the Internet): Porter advirtió que Internet derrumba las barreras de entrada geográficas, pero si las empresas solo compiten por precio, destruyen la
    rentabilidad del sector.
    2014 (Porter & Heppelmann): Los Smart, Connected Products transforman los productos tradicionales en sistemas inteligentes conectados, expandiendo los límites de las
    industrias hacia ecosistemas de datos y plataformas.

   Efecto Práctico en Software: Las plataformas digitales elevan las barreras de entrada al acumular datos históricos de usuarios, aumentan el costo de cambio al integrar
   flujos de trabajo en el cliente, y neutralizan intermediarios mediante canales directos.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                              18

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 1: Fundamentos y Diagnóstico del Entorno (40 min)

   🍷 5 Fuerzas Aplicadas a "Finca & Bodega San Rafael"
   Caso Guía: Diagnóstico del sector vitivinícola y respuestas estratégicas mediante sistemas

   🥊 Rivalidad Directa (Alta)                                                                   📦 Poder de Proveedores (Alto)
   Más de 80 bodegas en Cuyo disputando espacio en góndolas tradicionales.                      Monopolio en fabricantes de botellas de vidrio e insumos enológicos
   Respuesta TI: Portal e-commerce exclusivo con suscripción mensual al Club de                 importados.
   Vinos y catas sensoriales virtuales.                                                         Respuesta TI: Sistema MRP (Planificación de Requerimientos) para proyectar
                                                                                                compras críticas con 6 meses de anticipación.

   🛒 Poder de Clientes (Muy Alto en Supermercados)                                              🍻 Sustitutos y Entrantes (Media-Alta)
   Grandes cadenas comerciales imponen plazos de pago abusivos a 120 días.                      Auge del consumo juvenil de cervezas artesanales y destilados locales (gin).
   Respuesta TI: Desintermediación mediante canal Direct-to-Consumer (DTC) y                    Respuesta TI: CRM enfocado en comercializar experiencias gastronómicas y de
   cobro digital inmediato al turista.                                                          visita in situ, y no solo botellas.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                              19

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

    🧱 Génesis de la Cadena de Valor (Porter, 1985)
 Si las 5 Fuerzas explican el atractivo del sector en general... ¿por qué dentro de una misma industria algunas empresas obtienen grandes ganancias y otras quiebran?
     Abrir la "Caja Negra" de la Empresa: En su libro Competitive Advantage (1985), Michael Porter explicó que mirar a la empresa como una entidad global homogénea
     oculta las fuentes reales de la ventaja competitiva. Es indispensable descomponer la organización en su secuencia de actividades discretas y estratégicamente
     relevantes.
     El Concepto Central de Valor y Margen:
         Valor: Es el monto que los clientes están realmente dispuestos a pagar por el producto o servicio ofrecido.
         Margen: Es la ganancia neta, calculada como la diferencia entre el valor total capturado y el costo acumulado de ejecutar todas las actividades necesarias para crearlo
         y entregarlo.
     El Enfoque Sistémico: La ventaja competitiva no reside en actividades aisladas, sino en la coordinación e interconexión de eslabones, hoy articulados mediante sistemas
     de información.

 Referencia académica: Porter, M. E. (1985). Competitive Advantage: Creating and Sustaining Superior Performance. Free Press.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                              20

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   ⛓️ La Cadena de Valor: Las 5 Actividades Primarias
 Las actividades primarias están directamente involucradas en la creación física del producto, su venta y su entrega al cliente:

   1. Logística Interna                                        2. Operaciones                                              3. Logística Externa
   Recepción, pesaje, almacenamiento y control de              Procesos de transformación física o de servicio:            Almacenamiento de producto terminado, gestión
   inventario de materias primas e insumos antes de            maquinaria, envasado, control de calidad,                   de pedidos, despacho físico y distribución hacia el
   ingresar a producción.                                      mantenimiento y empaque.                                    cliente o canal.

   4. Marketing y Ventas                                                                     5. Servicios Postventa
   Canales de comercialización, fijación de precios, campañas publicitarias, gestión         Soporte técnico, garantías, resolución de quejas, capacitación de usuarios y
   de fuerza de ventas y cotizaciones.                                                       programas de fidelización a largo plazo.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                21

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   🏗️ Actividades de Soporte y los Eslabones de Información
 Las actividades de soporte sustentan a toda la cadena primaria mediante infraestructura, tecnología y recursos transversales:

   Infraestructura de la Empresa                                                           Desarrollo Tecnológico (I+D y TI)
   Gestión general, planificación financiera, asesoría legal, gestión de calidad y         Investigación de procesos, diseño de nuevos productos, arquitectura de
   gobierno corporativo. El ERP actúa como la columna vertebral de esta                    software, bases de datos y ciberseguridad que automatizan toda la empresa.
   dimensión.                                                                              Compras y Abastecimiento
   Gestión de Recursos Humanos                                                             Adquisición de insumos, negociación de contratos con proveedores y
   Reclutamiento, capacitación continua, evaluación del desempeño, liquidación de          licenciamiento de software y servicios en la nube.
   haberes y clima organizativo.

 El Poder de los Eslabones: Un error en la logística interna genera paradas en operaciones. Los sistemas de información integrados (ERP/SCM) conectan estos eslabones para
 que la información fluya sin fricción.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                       22

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   🍇 Cadena de Valor en "Finca & Bodega San Rafael"
   Caso Guía: Desglose concreto de actividades y soporte informático en la bodega

   Actividades Primarias                                                                Actividades de Soporte
       Logística Interna: Pesaje digital en báscula con lectores RFID en bines de uva     Infraestructura: ERP administrativo-contable integrado automáticamente con
       para trazar parcela de origen en tiempo real.                                      el régimen de facturación de ARCA.
       Operaciones: Sensores IoT en tanques de fermentación para monitoreo                Recursos Humanos: Aplicación móvil para registro de jornales de poda y
       térmico automático y control de prensado.                                          cosecha de cuadrillas temporarias en finca.
       Logística Externa: Despacho de cajas del Club de Vinos a todo el país con          Desarrollo Tecnológico: Algoritmos de balance hídrico y riego de precisión
       integración de tracking vía API de correos.                                        mediante sensores de suelo LoRaWAN.
       Marketing y Ventas: Portal web e-commerce con reservas enoturísticas y             Compras: Módulo de licitaciones digitales para insumos críticos (botellas,
       catálogo digital Direct-to-Consumer.                                               corchos importados, cajas de madera).
       Postventa: CRM que registra preferencias de cata y envía recomendaciones
       personalizadas de nuevas cosechas.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                      23

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   💡 Deconstrucción del Margen Operativo mediante TI
 La fórmula económica del margen es simple pero contundente:                                          ó                                         . Un sistema de
 información impacta estratégicamente en ambas variables:

   Palanca 1: Reducción de Costos                                                 Palanca 2: Aumento del Valor Percibido
   Eficiencia Operativa Interna:                                                  Diferenciación Externa:

       Ahorro del 25% en uso de agua y energía dosificando el riego mediante         El consumidor paga hasta un 30% más por botellas que incluyen código QR
       sensores agrícolas de precisión.                                              con trazabilidad de parcela y huella hídrica.
       Eliminación del 90% de errores de tipeo y reprocesos administrativos          Monetización de experiencias gastronómicas in situ con reserva digital
       mediante facturación electrónica automática.                                  garantizada y sin esperas.
       Optimización del stock de seguridad de insumos secos mediante algoritmos      Generación de flujos de caja predecibles y recurrentes mediante cobro
       de reaprovisionamiento continuo.                                              mensual automatizado del Club de Vinos.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                 24

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   🧱 Síntesis Estratégica: La Matriz FODA Cruzada
 El análisis FODA tradicional suele fracasar porque se limita a listar sustantivos sin conexión. La Matriz FODA Cruzada es un mecanismo formal para derivar proyectos e
 iniciativas de acción:

   🚀 Estrategias FO (Maxi-Maxi)                                                           🛠️ Estrategias DO (Mini-Maxi)
   Utilizar Fortalezas para capturar Oportunidades: Se aplican las capacidades            Superar Debilidades aprovechando Oportunidades: Se compensan las
   distintivas internas para capitalizar las tendencias favorables del mercado digital    carencias o brechas internas mediante la adopción de servicios tecnológicos ya
   y la tecnología.                                                                       disponibles en el mercado.

   🛡️ Estrategias FA (Maxi-Mini)                                                          ⚠️ Estrategias DA (Mini-Mini)
   Utilizar Fortalezas para neutralizar Amenazas: Se apalancan los activos y datos        Minimizar Debilidades y eludir Amenazas: Se diseñan mecanismos de
   propios para mitigar o eludir riesgos del entorno macroeconómico o de la               contingencia operativa y de ciberseguridad para evitar pérdidas críticas o la
   competencia.                                                                           paralización del negocio.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                          25

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   📊 FODA Cruzado en "Finca & Bodega San Rafael"
   Caso Guía: Derivación formal de proyectos de software a partir de la matriz cruzada

   🚀 FO: Plataforma DTC y Club de Vinos                                                  🛠️ DO: Adopción de SaaS AgroTech
   Cruce: Marca premiada en concursos [F1] + Auge del enoturismo en Cuyo [O1].           Cruce: Carencia de equipo de desarrollo interno [D1] + Créditos fiscales de
   Iniciativa TI: Portal e-commerce con membresía mensual, reservas                      Mendoza Activa [O2].
   gastronómicas online y tienda DTC con envío a domicilio.                              Iniciativa TI: Contratación de una plataforma SaaS cloud llave en mano para
                                                                                         gestión agrícola e integración de sensores de suelo.

   🛡️ FA: Algoritmo de Riego de Precisión                                                ⚠️ DA: Terminales POS Offline-First
   Cruce: Viñedos propios de alta calidad [F2] + Crisis hídrica severa en el Río Atuel   Cruce: Facturación manual lenta [D2] + Caídas frecuentes de conectividad rural
   [A1].                                                                                 [A2].
   Iniciativa TI: Sistema de balance hídrico automático que cruza lecturas de            Iniciativa TI: Implementar terminales de venta con arquitectura offline-first que
   humedad con pronósticos climáticos y turnos de riego.                                 cobran sin internet y sincronizan al recuperar señal.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                            26

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   🛠️ Actividad 1: Taller Práctico de Diagnóstico en Equipos
    ⏱️ Dinámica en Salas Virtuales de Equipo (20 minutos)
    Situación de Trabajo: Cada equipo de consultoría asumirá el rol de asesores gerenciales de "Finca & Bodega San Rafael". Deberán seleccionar una de las 4 iniciativas
    derivadas de la Matriz FODA Cruzada y estructurar su defensa ejecutiva.

    Consigna Obligatoria de Análisis:
    1. Identifiquen con precisión qué actividad de la Cadena de Valor (primaria o soporte) se verá transformada por la solución propuesta.
    2. Justifiquen si la iniciativa persigue prioritariamente la reducción de costos de ejecución o el aumento de la disposición a pagar del cliente.
    3. Expliquen qué fuerza competitiva de Porter (proveedores, clientes, rivales, etc.) se neutraliza o debilita gracias a esta capacidad de software.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                          27

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 2: Arquitectura Interna y Derivación (40 min)

   💬 Puesta en Común y Preguntas Socráticas
 Al regresar de las salas de trabajo en equipo, analizaremos en plenario los hallazgos con tres preguntas críticas de dirección:

    ❓ Preguntas de Discusión en Plenario:
    1. Sobre Viabilidad: Si la iniciativa seleccionada requiere inversión en servidores propios pero la bodega no tiene personal de ciberseguridad... ¿conviene desarrollar a
    medida o contratar un servicio administrado en la nube?
    2. Sobre Resistencia al Cambio: ¿Cómo reaccionarán los operarios del viñedo si se les exige cargar datos en una aplicación móvil durante la vendimia si la interfaz es
    compleja?
    3. Sobre Impacto en Negocio: ¿Cómo convencerían al directorio familiar de la bodega de que el proyecto no es un "gasto informático", sino una inversión que amplía
    el margen operativo?

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                               28

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🧱 ¿Qué es un Modelo de Negocio y por qué es Crucial?
 Tener una gran tecnología o un producto excelente no garantiza el éxito si la organización no cuenta con un modelo de negocio coherente:

 Un modelo de negocio describe la **lógica fundamental mediante la cual una organización crea, entrega y captura valor** económico, social o cultural de manera sostenible.

   La Creación y Entrega de Valor                                                        La Captura de Valor Económico
   Define cómo resolvemos un problema real para un segmento de clientes                  Define la ecuación financiera del negocio: cómo monetizamos el valor
   específico, qué canales utilizamos para hacer llegar la solución y qué tipo de        entregado (fuentes de ingreso) y cómo gestionamos los recursos y procesos
   relación establecemos para mantener su fidelidad.                                     clave para mantener los costos por debajo de los ingresos.

   Frase Clave: Muchas empresas fracasan no por fallas técnicas en su software, sino porque su modelo de negocio subyacente es inviable o no captura el valor que
   genera.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                        29

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

    🧱 El Lienzo de Modelo de Negocio (Business Model Canvas)
 Desarrollado por Alexander Osterwalder e Yves Pigneur (2010), el BMC sintetiza la arquitectura del negocio en 9 bloques interdependientes:

   1. Propuesta de Valor                                                     2. Segmentos de Clientes                             3. Canales
   ¿Qué paquete de productos y servicios resuelve el                         ¿Para quiénes estamos creando valor de manera        ¿A través de qué puntos de contacto comunicamos
   problema del cliente?                                                     prioritaria?                                         y entregamos la oferta?

   4. Relación con Clientes                                                  5. Fuentes de Ingreso                                6. Recursos Clave
   ¿Qué tipo de vínculo establecemos: personal,                              ¿Por qué valor están dispuestos a pagar y mediante   ¿Qué activos físicos, datos, software y personas son
   automatizado o comunitario?                                               qué mecanismo de cobro?                              indispensables?

   7. Actividades Clave                                                      8. Socios Clave                                      9. Estructura de Costos
   ¿Qué operaciones y procesos críticos debemos                              ¿Qué alianzas externas reducen riesgos y             ¿Cuáles son los costos más importantes derivados
   ejecutar con excelencia?                                                  complementan capacidades?                            de la operación?

 Referencia académica: Osterwalder, A., & Pigneur, Y. (2010). Business Model Generation. John Wiley & Sons.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                        30

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   📊 El BMC a través del Lente del Ingeniero en Sistemas
 Cada uno de los 9 bloques del Canvas se traduce directamente en artefactos, datos y decisiones de arquitectura tecnológica:

   El Frente Visible (Cliente y Mercado)                                                  El Motor Interno (Operación y Costos)
      Propuesta de Valor: Algoritmos de recomendación, velocidad de respuesta,               Recursos Clave: Modelos de datos limpios, código fuente propietario,
      disponibilidad 24/7 y personalización.                                                 infraestructura en la nube y talento técnico.
      Canales: Aplicaciones web responsivas, apps nativas, notificaciones push e             Actividades Clave: Mantenimiento de software, soporte técnico continuo y
      integraciones de mensajería.                                                           gobierno de ciberseguridad.
      Relación: Chatbots de atención, portales de autoservicio y sistemas CRM                Socios Clave: Proveedores de servicios Cloud (AWS, Azure), pasarelas de
      integrados.                                                                            pago y proveedores de APIs.
      Ingresos: Pasarelas de cobro online, pasarelas de pago recurrentes y                   Costos: Consumo de infraestructura Cloud (FinOps), licencias de software
      microtransacciones digitales.                                                          SaaS y costos de desarrollo.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                       31

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2
  ACTO 3: Modelado de Negocio y Acción (40 min)

   🍷 BMC de la Unidad Digital de "Finca & Bodega San Rafael"
   Caso Guía: Arquitectura completa del modelo Direct-to-Consumer y Enoturismo To-Be

   8. Socios Clave                                             7. Actividades Clave                                      1. Propuesta de Valor
   Operadores de turismo cuyano, pasarelas de cobro            Curaduría de experiencias en bodega, desarrollo           Vinos de autor de exportación directo del productor
   digital (MercadoPago/Stripe), proveedores de                continuo del portal DTC y despacho seguro de cajas        a la mesa, junto a experiencias enoturísticas
   sensores LoRaWAN y empresas de logística con                de vino.                                                  gastronómicas inmersivas sin intermediarios.
   tracking API.
                                                               6. Recursos Clave
                                                               Base de datos de miembros (CRM), viñedos
                                                               históricos y plataforma e-commerce cloud.

   4. Relación Clientes                                        2. Segmentos
   Membresía exclusiva en Club de Vinos con atención           Enoturistas nacionales y extranjeros que visitan
   personalizada y eventos privados.                           Cuyo, y consumidores urbanos apasionados por el
                                                               vino artesanal.
   3. Canales
   Portal web e-commerce, app de visitas a bodega,
   redes sociales y degustaciones in situ.

   9. Estructura de Costos: Comisiones por transacción de pago digital, fletes de            5. Fuentes de Ingreso: Venta de botellas de alta gama por caja (DTC), venta de
   última milla, suscripción Cloud de servidores y hosting, y mantenimiento de               entradas para almuerzos y visitas guiadas, y suscripción mensual recurrente al
   sensores en finca.                                                                        Club de Vinos.
Ingeniería en Sistemas de Información | Plan 2026                                                                                                                              32

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   💡 La Reacción en Cadena al Modificar un Bloque del Canvas
 El Business Model Canvas no es una colección de notas adhesivas estáticas; es un sistema en equilibrio dinámico donde un cambio altera todo el lienzo:

    ⚡ El Efecto Dominó de la Servitización
    Si la bodega decide pasar de vender botellas sueltas a un modelo de suscripción recurrente mensual (Club de Vinos):

       Fuentes de Ingreso: El flujo financiero se transforma de transacciones esporádicas e impredecibles a ingresos mensuales recurrentes y predecibles (*MRR - Monthly
       Recurring Revenue*).
       Actividades Clave: La empresa debe incorporar soporte continuo, gestión de bajas (*churn rate*) y curaduría editorial mensual de contenidos para los socios.
       Estructura de Costos: Se incrementan los costos de logística de entrega mensual programada y el costo de almacenamiento seguro de datos de tarjetas en
       pasarelas certificadas PCI-DSS.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                          33

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

    🧱 El Lienzo de Propuesta de Valor (Value Proposition Canvas)
 Diseñado por Osterwalder et al. (2014), el VPC hace un zoom-in riguroso en los dos bloques más críticos del BMC para asegurar el encaje problema-solución:

    👤 Perfil del Cliente (Observación)                                                                                🎁 Mapa de Valor (Diseño TI)
    Analiza con empatía la realidad del usuario antes de pensar en la solución                                        Estructura cómo la tecnología y el software resuelven esos dolores:
    técnica:
                                                                                                                          Productos y Servicios: El paquete de software, plataforma o aplicación que
        Trabajos del Cliente (Jobs-to-be-done): Tareas funcionales, emocionales o                                         ofrecemos.
        sociales que el usuario intenta resolver.                                                                         Aliviadores de Frustraciones: Cómo las funcionalidades eliminan o mitigan
        Frustraciones (Pains): Dolores, obstáculos, riesgos, costos y pérdidas de                                         los dolores específicos.
        tiempo actuales.                                                                                                  Creadores de Alegrías: Cómo el sistema produce resultados superiores y
        Alegrías (Gains): Resultados deseados, beneficios esperados y aspiraciones                                        sorpresivos para el usuario.
        de éxito.

 Referencia académica: Osterwalder, A., Pigneur, Y., Bernarda, G., & Smith, A. (2014). Value Proposition Design. John Wiley & Sons.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                                      34

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   👤 El Perfil del Cliente: Los Trabajos a Realizar (Jobs-to-be-Done)
 La teoría de los Jobs-to-be-Done (Clayton Christensen) establece que las personas no compran productos, sino que "contratan" soluciones para progresar en sus vidas:

   Trabajos Funcionales                                       Trabajos Sociales                                          Trabajos Emocionales
   Tareas operativas concretas: reservar un turno de          Cómo quieren ser percibidos por los demás: quedar          Cómo quieren sentirse internamente: sentirse
   visita para 4 personas, pagar la compra con factura        bien como anfitrión sirviendo un vino exclusivo y          relajados durante sus vacaciones, tener la
   A, recibir las botellas en su domicilio sin roturas.       poco común que compró directamente en la                   tranquilidad de que su reserva está confirmada y no
                                                              bodega.                                                    habrá sobreventa.

 Pregunta de Diseño: Si el software solo resuelve la parte funcional pero es frustrante en lo emocional o no aporta estatus social, el usuario abandonará la plataforma.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                              35

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🎁 El Mapa de Valor: La Respuesta Tecnológica
 Cómo traducir los requerimientos del usuario en capacidades específicas de software que generan valor:

   Aliviadores de Dolores (Pain Relievers)                                               Creadores de Alegrías (Gain Creators)
   No intentan resolver todos los problemas del mundo; se enfocan con precisión          Generan beneficios tangibles que superan las expectativas habituales del
   quirúrgica en los dolores más agudos del cliente:                                     mercado:

      Eliminación de la incertidumbre mediante confirmación instantánea por                 Acceso prioritario y exclusivo a partidas limitadas de vino antes de su
      WhatsApp y correo.                                                                    lanzamiento al público.
      Eliminación de colas en el mostrador mediante check-in digital por código             Pasaporte digital enoturístico que acumula puntos y otorga descuentos en
      QR en el teléfono.                                                                    restaurantes aliados.
      Garantía total de reposición ante roturas en el transporte rastreado punto a          Recomendaciones hiperpersonalizadas basadas en el historial de catas
      punto.                                                                                registradas por el usuario.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                      36

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🍷 VPC Aplicado al Enoturista en "Finca & Bodega San Rafael"
   Caso Guía: Validación del encaje entre las necesidades del turista y la plataforma web

   👤 Perfil del Turista en San Rafael                                                       🎁 Mapa de Valor de la Plataforma TI
      Trabajos: Encontrar una experiencia gastronómica auténtica, comprar vino de             Productos y Servicios: Portal web responsive de reservas en tiempo real y
      autor y disfrutar con su familia sin estrés organizativo.                               tienda e-commerce integrada con despacho a domicilio.
      Frustraciones: Llamar por teléfono y que no atiendan, no saber si hay lugar             Aliviadores: Calendario interactivo con cupos actualizados al instante, pago
      disponible, llegar y que esté cerrado, y pagar sobreprecios a agencias                  online seguro y confirmación automática vía WhatsApp.
      intermediarias.                                                                         Creadores: Membresía digital inmediata al Club de Vinos con 15% de
      Alegrías: Atención ágil, degustación guiada por sommeliers expertos, y                  descuento permanente en futuras recompras desde su hogar.
      posibilidad de recibir el vino en su casa en Buenos Aires o Córdoba.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                            37

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🎯 Los Tres Niveles de Encaje (Fit) en el Diseño de Valor
 Para validar si una propuesta de valor es realmente sólida, debemos evaluar el encaje en tres etapas progresivas:

   1. Encaje en Papel (Problem-Solution Fit)                  2. Encaje en Mercado (Product-Market Fit)                  3. Encaje en Modelo (Business Model Fit)
   Ocurre cuando demostramos conceptualmente que              Ocurre cuando lanzamos la solución y los clientes          Ocurre cuando la solución no solo gusta, sino que
   las funcionalidades del software coinciden con             reales la adoptan, pagan por ella y la recomiendan         puede ser entregada y escalada a un costo menor
   dolores y alegrías genuinas del cliente. Es la etapa       activamente, generando tracción y retención                que los ingresos que genera, asegurando la
   de diseño de lienzos.                                      medible.                                                   rentabilidad a largo plazo.

 Alerta de Consultoría: En el Proyecto Integrador nos aseguraremos de validar rigurosamente el Encaje en Papel y formular hipótesis cuantitativas para verificar el Encaje en
 Mercado.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                               38

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

    🚀 Modelos Digitales: La Transición a Plataformas
 David Rogers (The Digital Transformation Playbook, 2016) explica la transformación estructural de los modelos lineales hacia plataformas de red:

    Modelos Tradicionales de Tubería (Pipelines)                                                               Modelos de Plataforma y Ecosistemas
    Siguen una secuencia lineal: se adquieren insumos, se fabrica el producto, se                              La empresa crea una infraestructura digital donde múltiples participantes
    transporta y se vende al cliente final. El valor se genera de forma unidireccional y                       (productores, consumidores, guías turísticos, transportistas) interactúan y
    cada paso añade costo físico.                                                                              realizan transacciones directas, generando efectos de red.

    Los Efectos de Red: Cuantos más turistas utilizan la plataforma de la bodega para reservar visitas, más prestadores gastronómicos regionales desean integrarse a la
    oferta; y cuantos más prestadores participan, más atractiva resulta la plataforma para los visitantes.

 Referencia académica: Rogers, D. L. (2016). The Digital Transformation Playbook. Columbia University Press.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                            39

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🔄 Servitización: De la Venta Transaccional al Servicio Continuo
 La digitalización permite transformar la venta de bienes físicos tradicionales en servicios continuos de alto valor agregado:

    De la Transacción Aislada a la Relación Continua:
       Enfoque clásico: Vender una botella de vino en una vinoteca; la relación con el cliente termina en el momento en que se emite el ticket de compra.
       Enfoque servitizado: Incorporar al cliente a una comunidad digital por suscripción que entrega vinos curados periódicamente, acceso a catas virtuales exclusivas con el
       enólogo y beneficios en turismo.
    El Dato como Activo Estratégico: Cada interacción del usuario en la plataforma digital genera telemetría de comportamiento (qué cepas prefiere, qué días reserva, cuál
    es su ticket promedio), permitiendo a la bodega anticipar la producción y personalizar la oferta.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                            40

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🎯 Fórmula Sintáctica de la Hipótesis de Oportunidad
 Para el Proyecto Integrador, toda propuesta de transformación tecnológica debe formularse bajo la siguiente estructura sintáctica rigurosa:

    Para [Segmento de Clientes o Usuario Crítico]
    que sufre [Problema / Ineficiencia severa en la Cadena de Valor o en el Contexto],
    nuestra solución [Capacidad / Sistema de Información propuesto]
    generará [Beneficio estratégico de negocio o diferenciación cuantificable],
    lo cual validaremos cuando [Métrica / Indicador de Éxito clave medible en tiempo y forma].

 ¿Por qué esta fórmula? Evita que el estudiante formule "deseos vacíos" o "descripciones de código", obligándolo a articular el beneficiario, el dolor real, la palanca de
 software, el impacto en negocio y el criterio cuantitativo de éxito.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                            41

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   📝 Ejemplo Resuelto de Hipótesis: Caso Bodega San Rafael
 Veamos cómo se aplica la fórmula formal sobre el caso que hemos analizado a lo largo de la clase:

   🍷 Hipótesis de Transformación Enoturística y Canal DTC:
   "Para turistas y amantes del vino de todo el país que sufren dificultades para reservar visitas guiadas y altos sobreprecios impuestos por intermediarios comerciales
   tradicionales, nuestro portal Direct-to-Consumer integrado con motor de reservas y membresía inteligente generará un incremento del 40% en el margen neto por botella
   y una reducción del 80% en los tiempos de gestión de visitas, lo cual validaremos cuando alcancemos 500 suscriptores activos en el Club de Vinos y una tasa de ocupación
   del 85% en las experiencias enoturísticas durante los primeros 6 meses de operación."

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                             42

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   🌾 Ejemplos de Hipótesis para Otros Rubros de San Rafael
 Para orientar a los equipos según la organización que hayan seleccionado para su Proyecto Integrador:

   🏭 Caso 1: Secadero y Empaque Agroindustrial (Cuadro Nacional)
   "Para productores frutícolas que sufren mermas del 18% por falta de trazabilidad en cámaras frigoríficas, nuestro sistema IoT de monitoreo térmico y control de lotes
   generará la certificación de exportación a la Unión Europea, lo cual validaremos cuando se reduzcan los rechazos en destino por debajo del 2% en la vendimia 2027."

   🚚 Caso 2: Distribuidora Logística Mayorista (Sur Mendocino)
   "Para 450 almacenes y minimarkets de distritos rurales que sufren desabastecimiento por visitas semanales demoradas del preventista, nuestra aplicación B2B de
   autogestión y ruteo inteligente generará un aumento del 25% en ventas recurrentes, lo cual validaremos cuando el 60% de los pedidos se carguen de forma digital en los
   primeros 90 días."

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                           43

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   📝 Actividad 2: Entregable de Síntesis - Hito 1 (Avance A)
 Al finalizar la sesión sincrónica, los equipos estructurarán el siguiente entregable de avance para el Proyecto Integrador:
    Nombre del Entregable: Diagnóstico Estratégico y Propuesta de Valor (Hito 1 - Avance A).
    Modalidad y Formato: Documento técnico de consultoría por equipo (máximo 4 páginas, formato PDF profesional).
    Estructura Requerida Obligatoria:
     i. Caracterización de la Organización: Reseña del caso real seleccionado en San Rafael o Cuyo (rubro, escala y modelo actual).
     ii. Diagnóstico Estratégico Externo: Matriz PESTEL de macroentorno y análisis de las 5 Fuerzas de Porter.
    iii. Diagnóstico Interno y Síntesis: Cadena de Valor y Matriz FODA Cruzada con derivación de iniciativas.
    iv. Modelado To-Be: Diagrama del Lienzo de Modelo de Negocio (BMC) de la situación propuesta.
     v. Encaje de Valor: Diagrama del Lienzo de Propuesta de Valor (VPC).
    vi. Hipótesis Formal: Redacción de la Hipótesis de Oportunidad Tecnológica según la plantilla oficial.

Ingeniería en Sistemas de Información | Plan 2026                                                                                     44

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

  ACTO 3: Modelado de Negocio y Acción (40 min)

   📋 Rúbrica de Evaluación: ¿Qué Observará la Cátedra?
 Para asegurar la calidad profesional del entregable, la cátedra evaluará los siguientes criterios:

   1. Coherencia en el Pipeline Analítico                                                      3. Viabilidad del Modelo de Negocio (BMC)
   ¿Las oportunidades del FODA surgen realmente del PESTEL y las 5 Fuerzas? ¿Las               ¿La estructura de costos es coherente con los recursos y actividades declaradas?
   fortalezas surgen de la Cadena de Valor? No se aceptarán herramientas aisladas              ¿Las fuentes de ingreso compensan con creces el costo operativo tecnológico?
   o desconectadas.                                                                            4. Precisión en la Hipótesis
   2. Rigor en el Encaje del VPC                                                               ¿La hipótesis incluye una métrica cuantitativa verificable en el tiempo, o es una
   ¿Los aliviadores de frustraciones responden exactamente a dolores reales                    simple declaración de buenas intenciones?
   manifestados por el usuario, o son funcionalidades técnicas caprichosas?

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                                  45

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

   📚 Bibliografía y Referencias Académicas
    Aguilar, F. J. (1967). Scanning the Business Environment. Macmillan.
    Henderson, J. C., & Venkatraman, N. (1993). Strategic alignment: Leveraging information technology for transforming organizations. IBM Systems Journal, 32(1), 4-16.
    Mintzberg, H. (1987). The strategy concept I: Five Ps for strategy. California Management Review, 30(1), 11-24.
    Osterwalder, A., & Pigneur, Y. (2010). Business Model Generation. John Wiley & Sons.
    Osterwalder, A., Pigneur, Y., Bernarda, G., & Smith, A. (2014). Value Proposition Design. John Wiley & Sons.
    Porter, M. E. (1979). How competitive forces shape strategy. Harvard Business Review, 57(2), 137-145.
    Porter, M. E. (1980). Competitive Strategy: Techniques for Analyzing Industries and Competitors. Free Press.
    Porter, M. E. (1985). Competitive Advantage: Creating and Sustaining Superior Performance. Free Press.
    Porter, M. E., & Millar, V. E. (1985). How information gives you competitive advantage. Harvard Business Review, 63(4), 149-160.
    Porter, M. E. (1996). What is strategy? Harvard Business Review, 74(6), 61-78.
    Porter, M. E. (2001). Strategy and the Internet. Harvard Business Review, 79(3), 62-79.
    Porter, M. E., & Heppelmann, J. E. (2014). How smart, connected products are transforming competition. Harvard Business Review, 92(11), 64-88.
    Rogers, D. L. (2016). The Digital Transformation Playbook. Columbia University Press.

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                          46

Gestión Gerencial (UTN-FRSR) - Clase Virtual 2

   📌 Síntesis de la Clase y Próximos Pasos
  1. La Estrategia Guía la Arquitectura: Los sistemas de información no son fines en sí mismos; existen para apalancar una propuesta de valor distintiva y una ventaja
    competitiva sostenible.
  2. El Pipeline Diagnóstico Previene Errores Costosos: PESTEL y 5 Fuerzas diagnostican el entorno; la Cadena de Valor analiza lo interno; el FODA Cruzado deriva iniciativas
    concretas y el BMC/VPC las monetiza y valida.
  3. El Caso Guía como Modelo de Trabajo: Cada equipo replicará este mismo proceso metodológico riguroso sobre la organización seleccionada en San Rafael o Cuyo.
  4. Próximo Encuentro (Clase 3): Transformación Digital, Madurez Organizacional y Gestión Bimodal (Aprenderemos a diagnosticar la madurez de capacidades antes de
     seleccionar tecnologías).

Ingeniería en Sistemas de Información | Plan 2026                                                                                                                               47
