# Evaluación de tecnologías

> Texto extraido de `Clase 12/Evaluación de tecnologías.pdf`, 16 paginas. Generado el 2026-11-25 16:06 por `sincronizacion-campus`. No editar a mano.

---

Marco de Decisión y
Portafolio Tecnológico
¿Cómo elegimos en qué
tecnología invertir?

Qué te llevás de esta clase

●   Identificar los tres tipos de inversión tecnológica y qué criterio aplica a cada
    uno
●   Calcular y comparar TIR, VAN, TCO y payback sobre un caso real
●   Usar el marco de Weill actualizado y los horizontes de McKinsey para
    clasificar un portafolio
●   Tomar una decisión defendible combinando criterios financieros y
    estratégicos

Por qué este tema debería preocuparte

 ●   El 70% de las transformaciones digitales fracasa. (McKinsey, 2023)
 ●   El 60% de las implementaciones de ERP termina sobre presupuesto o
     atrasada. (Panorama Consulting, ERP Report 2024)
 ●   El gasto mundial en TI en 2025 supera los USD 5,7 billones. (Gartner,
     2024)

Pregunta abierta: ¿quién pasó por una implementación de software que salió mal?
¿Qué falló?

La pregunta central

   Tenemos 12 propuestas de inversión tecnológica.
   Presupuesto: alcanza para 4. ¿Cómo decidimos?

No hay UNA respuesta. Hay UN proceso.

Propuestas vs. Presupuesto

Siempre hay más propuestas viables que dinero disponible.

Un Comité Directivo de TI debe priorizar:

  ●    ✅ ¿Qué proyectos se aprueban?
  ●    ❌ ¿Cuáles no?
  ●    ⏸ ¿Cuáles se postergan?

Composición típica: CEO/Director, CFO, CIO/Gerente de Sistemas, líderes de áreas usuarias clave.

Tres tipos de inversión = tres criterios
distintos
🔴 Obligatorias — Hay que hacerlas. Punto.

  ●   Exigidas por ley: factura electrónica AFIP, régimen de información, Ley 25.326 de Datos
      Personales
  ●   Exigidas por clientes: certificaciones, integraciones
  ●   Criterio: costo mínimo viable + cumplir el plazo

🟡 Con beneficio medible — Hay un número claro

  ●   Reducción de inventario, automatización, ahorro de tiempo, menos errores
  ●   Criterio: TIR > tasa de corte, VAN > 0, payback aceptable

🟢 Estratégicas / intangibles — El número no alcanza

  ●   Experiencia del cliente, capacidades nuevas, opcionalidad futura, datos
  ●   Criterio: alineación estratégica + opciones reales + juicio directivo

TIR (Tasa Interna de Retorno)

Qué es: la tasa de descuento que hace que el VAN del proyecto sea cero.

Cómo se usa:

  ●    Si TIR > tasa de corte de la empresa → se aprueba
  ●    En Argentina, definir la "tasa de corte" con tasas reales volátiles es un arte, no una ciencia

Ejemplo simple:

  ●    Inversión inicial: USD 100.000 en sistema de gestión de inventario
  ●    Ahorros anuales: USD 35.000 durante 5 años
  ●    TIR ≈ 22% → si tasa de corte = 15%, se aprueba

⚠ Limitaciones que rara vez se mencionan:

  ●    Asume reinversión de los flujos a la misma TIR (irrealista)
  ●    Puede dar múltiples valores si los flujos cambian de signo
  ●    No dice nada del tamaño del proyecto (10% sobre USD 1M ≠ 10% sobre USD 100M)

VAN / NPV (Valor Actual Neto)
Qué es: suma de los flujos futuros descontados, menos la inversión inicial.

Cuándo conviene sobre TIR:

  ●     Proyectos de tamaños distintos (te dice cuántos dólares ganás, no qué tasa)
  ●     Flujos no convencionales
  ●     Para construir un ranking de proyectos

Mismo ejemplo, con tasa de corte 15%: VAN ≈ USD 17.300 → el proyecto agrega valor.

Lo que casi nadie hace (y deberían): análisis de sensibilidad.

  ●     ¿Y si los ahorros son 20% menores? ¿Y si el proyecto tarda 6 meses más?
  ●     Una tabla con escenarios pesimista / base / optimista se arma en 10 minutos en Excel.

TCO (Total Cost of Ownership)
Trampa típica: comparar precio de licencia o costo de desarrollo inicial entre opciones.

Realidad: el costo inicial suele ser 20-30% del costo total a 5 años.

🔑 Crítico para SaaS: el precio mensual parece barato. A 5 años puede superar a una solución
on-premise. Y el proveedor sube precios cuando estás encerrado.

Payback Period
Qué es: tiempo que tarda la inversión en recuperarse.

Cuándo es útil:

  ●    Contextos de alta incertidumbre (Argentina, inflación, tipo de cambio)
  ●    Restricciones de caja (muy común en pymes)
  ●    Como filtro grueso antes de calcular VAN/TIR

Limitación clave: ignora todo lo que pasa después del payback. Un proyecto que recupera en 18 meses
y se cae a los 24 vence en payback a otro que recupera en 30 meses y dura 10 años.

Regla práctica común:

  ●    Proyectos tácticos: payback < 18 meses
  ●    Proyectos estratégicos: payback < 3-5 años

¿Cuál criterio usar?
👉 En la práctica: se usan los cuatro juntos. Cualquier proveedor o consultor que te muestre solo uno
está vendiéndote algo

El problema: no todo se mide en pesos
Beneficios típicos que los criterios financieros no capturan bien:

 ●    Experiencia del cliente — ¿cuánto vale que el cliente no llame al call center?
 ●    Velocidad — ¿cuánto vale lanzar un producto 3 meses antes que el competidor?
 ●    Opcionalidad — una API hoy habilita 5 productos en 2 años
 ●    Datos — una base limpia hoy permite IA mañana
 ●    Talento — los buenos no quieren trabajar con sistemas obsoletos

Concepto clave: Opciones Reales (Copeland & Antikarov, 2003)

Invertir hoy compra el derecho pero no la obligación de invertir más mañana, cuando se
reduzca la incertidumbre.

Consistencia con la estrategia
Ante dos proyectos con mismo VAN y mismo TIR, gana el que apoye mejor la estrategia.

Ejemplo aplicado: CRM con servicio super-personalizado

Tres preguntas filtro antes de aprobar:

 1.   ¿Refuerza nuestra propuesta de valor diferencial?
 2.   ¿Está alineado con dónde competimos (segmento, geografía, canal)?
 3.   ¿Nos hace más o menos dependientes de un proveedor crítico?

El marco clásico de Weill
Peter Weill (MIT CISR, 2002): todo proyecto IT cae en una de cuatro categorías.

🔧 Infraestructura — plataforma compartida (red, cloud, identidad). Riesgo tecnológico.

🔄 Transaccionales — procesan operaciones (facturación, nómina, inventario). Reducen costos, bajo
riesgo.

📊 Informacionales — soportan decisiones (BI, dashboards, analítica). Riesgo medio.

🏆 Estratégicos — generan ventaja competitiva (e-commerce, CRM avanzado, IA aplicada). Alto riesgo,
alto retorno potencial.

Distribución original que reportó Weill (2002):

      Infraestructura 54% · Transaccional 13% · Informacional 20% · Estratégico 13%

Pero esa pirámide cambió

¿Por qué bajó infraestructura? Cloud y SaaS convirtieron CAPEX en OPEX, y las plataformas
modernas comparten infraestructura.

¿Qué te dice esto sobre tu empresa? Si todavía gasta 60%+ en infraestructura, probablemente está
cargando deuda técnica o atrasada en cloud.

Fuentes: Westerman, Bonnet & McAfee (2014), Leading Digital; Gartner CIO Survey 202

Portafolio balanceado: tres horizontes
(McKinsey)

Regla práctica:

  ●   100% H1 → seguro pero condena al estancamiento
  ●   100% H3 → ruleta
  ●   El balance lo define la estrategia y el momento de la empres
