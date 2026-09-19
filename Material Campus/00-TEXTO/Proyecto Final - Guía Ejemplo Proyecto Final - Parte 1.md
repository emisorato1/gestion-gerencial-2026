# Guía Ejemplo Proyecto Final - Parte 1

> Copia de `Proyecto Final/Guía Ejemplo Proyecto Final - Parte 1.md`. Generado el 2026-09-18 20:35 por `sincronizacion-campus`. No editar a mano.

---

# Guía Ejemplo: Trabajo Práctico Final

## Caso ficticio: **Distribuidora Montaña SRL**

> [!NOTE]
> En cada sección se plantean preguntas que guían el razonamiento antes de mostrar el ejemplo resuelto. El objetivo es pensar antes de leer la respuesta.

---

## Sobre la empresa ficticia

**Distribuidora Montaña SRL** es una pequeña empresa familiar de Maipú, Mendoza, que distribuye productos de almacén, limpieza y bazar a ~120 comercios minoristas (kioscos, despensas y almacenes) en Maipú, Guaymallén y Godoy Cruz.

- **Fundada**: 2012 por Carlos Montaña y su esposa Laura.
- **Empleados**: 7 personas (Carlos como gerente general/vendedor, Laura en administración/cobranza, 2 vendedores de ruta, 2 choferes/repositores y 1 persona en depósito).
- **Facturación anual estimada**: ARS 480M (~USD 400k).
- **Herramientas actuales**: Facturador electrónico (obligatorio AFIP), planilla Excel de stock, WhatsApp para pedidos, cuaderno de cobranzas de Laura y agenda de papel de los vendedores.

---

# PARTE 1: Diagnóstico gerencial

*Dominio del problema: comprender la organización y detectar el problema gerencial con evidencia.*

---

## 1. Organización

### 🤔 Preguntas

> - *¿Qué necesita saber alguien externo para entender esta empresa en 2 minutos?*
> - *¿Cuáles son las funciones reales que se cumplen, aunque no existan cargos formales?*
> - *¿A qué información puede realmente acceder el equipo consultor?*

### ✅ Ejemplo

**Distribuidora Montaña SRL** distribuye productos de consumo masivo (almacén, limpieza y bazar) a comercios minoristas del Gran Mendoza desde su depósito en Maipú. Atiende ~120 clientes activos en tres departamentos.

| Aspecto | Detalle |
|---|---|
| Actividad | Distribución mayorista B2B |
| Ubicación | Maipú, Mendoza |
| Tamaño | 7 personas, 2 camionetas |
| Oferta | ~800 SKU de terceros |
| Clientes | Kioscos, despensas y almacenes |

Carlos fundó la empresa hace 13 años con una camioneta; hoy tiene dos rutas diarias. Laura maneja la administración, facturación y cobranza. No hay organigrama formal: Carlos vende y decide compras; los vendedores relevan pedidos en ruta; los choferes entregan y cobran en efectivo; la persona de depósito prepara pedidos y recibe mercadería.

**Acceso disponible**: Entrevistas con Carlos y Laura, observación del depósito, facturas electrónicas, planillas de Excel y cuaderno de cobranzas.

---

## 2. Contexto

### 🤔 Preguntas

> - *¿Quiénes son los competidores directos y qué alternativas tiene el kiosquero para abastecerse?*
> - *¿Qué factores del entorno mendocino afectan a este negocio concretamente, no en abstracto?*
> - *¿Cuál es la diferencia entre listar un factor PESTEL y explicar su impacto real en esta empresa?*

### ✅ Ejemplo (FODA + factores clave)

**Análisis FODA**:

| | Positivo | Negativo |
|---|---|---|
| **Interno** | Relación personal con clientes, rutas consolidadas, conocimiento del barrio | Stock a ojo, cobranza informal, toda la información en la cabeza de Carlos y Laura |
| **Externo** | Crecimiento de kioscos saludables y pet shops (nuevos segmentos), digitalización de pagos | Competencia de distribuidoras más grandes con app de pedidos, inflación que erosiona márgenes, atraso cambiario en productos importados |

**Factores regionales relevantes**:
- **Estacionalidad**: Diciembre-febrero pico de bebidas y helados; baja en invierno.
- **Logística**: Rutas dependen del estado de calles y del precio del gasoil.
- **Competencia**: Dos distribuidoras grandes (una con app de pedidos y catálogo digital) ofrecen descuentos por volumen.

**Interpretación**: La presión competitiva no viene del precio sino de la *experiencia de compra*: los competidores permiten al comerciante hacer pedidos desde el celular a cualquier hora, ver catálogo con precios y recibir confirmación inmediata. Montaña depende de la visita presencial del vendedor, que pasa una vez por semana.

---

## 3. Modelo de negocio actual (BMC AS-IS)

### 🤔 Preguntas

> - *¿Cómo gana dinero realmente esta empresa? ¿Es por volumen, por margen, por servicio?*
> - *Si Carlos se enfermara 15 días, ¿qué partes del negocio se detendrían? ¿Por qué?*
> - *¿Cuáles de estas actividades son el "día a día" que no puede parar (Run) y cuáles deberían cambiar (Change)?*
> - *¿Qué dato concreto le falta a Carlos para tomar mejores decisiones?*

### ✅ Ejemplo

| Bloque BMC | Estado actual |
|---|---|
| **Segmentos** | Kioscos, despensas y almacenes en Maipú, Guaymallén y Godoy Cruz |
| **Propuesta de valor** | Entrega en puerta, crédito informal (7-15 días), variedad de productos de consumo masivo, trato personal |
| **Canales** | Visita presencial del vendedor (1 vez/semana), WhatsApp para pedidos urgentes, entrega con camioneta propia |
| **Relación** | Personal y directa. Carlos conoce a cada comerciante por nombre |
| **Ingresos** | Margen sobre precio de lista (~18-25%), plazo de cobro 7-15 días, efectivo y transferencia |
| **Recursos clave** | Depósito, 2 camionetas, relaciones con proveedores, conocimiento de Carlos sobre precios y márgenes |
| **Actividades clave** | Compra a proveedores, armado de pedidos, distribución en ruta, cobranza, facturación |
| **Socios clave** | Proveedores mayoristas (Arcor, Unilever, P&G, regionales), contador externo |
| **Estructura de costos** | Mercadería (~75%), sueldos, combustible, alquiler depósito, mantenimiento camionetas, monotributo/IVA |

**Lectura analítica del canvas**:

- **Lógica de valor**: Montaña genera valor por *conveniencia* (le lleva al kiosquero lo que necesita a su puerta) y por *financiamiento informal* (le fía 7-15 días). No compite por precio sino por cercanía y confianza.
- **Run the Business**: Compras, armado, despacho, ruta y cobranza son el motor diario que no puede parar.
- **Change the Business**: El canal de pedidos (hoy presencial/WhatsApp) y la gestión de cobranza (hoy cuaderno) necesitan transformarse para no perder clientes ante competidores con app.
- **Debilidades y dependencias**:
  - *Conocimiento concentrado*: Solo Carlos sabe los márgenes reales por producto y los acuerdos de precio con proveedores.
  - *Stock a ciegas*: La planilla de Excel se actualiza 1 vez por semana; hay roturas de stock y sobrestock simultáneamente.
  - *Cobranza en cuaderno*: Laura no sabe la deuda real de cada cliente hasta que cruza facturas a fin de mes. Hay ~ARS 8M en cuentas "dudosas".
  - *Venta sin seguimiento*: No hay registro de qué compra cada cliente ni frecuencia; si un cliente deja de comprar, nadie lo detecta hasta semanas después.
- **Tensiones del modelo**: El modelo funciona por la relación personal de Carlos, pero no escala. Si Carlos suma una tercera ruta o se enferma, el negocio se detiene. La informalidad genera pérdidas invisibles por cobros no realizados, mercadería vencida y clientes que migran silenciosamente.

---

## 4. Propuesta de valor actual (VPC AS-IS)

### 🤔 Preguntas

> - *¿Qué "trabajo" le resuelve Montaña al kiosquero? ¿Solo le vende productos o le soluciona algo más?*
> - *¿Qué le duele al kiosquero de su relación actual con Montaña?*
> - *¿Qué brecha hay entre lo que el kiosquero espera y lo que Montaña realmente entrega?*

### ✅ Ejemplo

**Segmento**: Kiosquero/despensero del Gran Mendoza.

| Customer Jobs | Pains | Gains esperados |
|---|---|---|
| Reponer mercadería sin cerrar el local | El vendedor pasa solo 1 vez por semana; si necesita algo urgente, depende de WhatsApp sin confirmación | Poder pedir cuando necesita y recibir confirmación |
| Conocer precios actualizados antes de pedir | No tiene catálogo ni lista de precios; pregunta uno por uno | Lista digital actualizada para planificar compras |
| Controlar cuánto debe y cuándo pagar | Solo Laura sabe cuánto debe cada uno; el kiosquero no tiene su estado de cuenta | Transparencia en su deuda y plazos |
| Recibir la mercadería completa y a tiempo | A veces faltan productos porque el stock estaba mal; el pedido llega incompleto | Entrega completa y predecible |

**Brecha**: Montaña ofrece conveniencia y crédito, pero el kiosquero hoy no puede pedir fuera de la visita, no ve precios, no conoce su deuda y recibe pedidos incompletos. Los competidores con app ya resuelven los tres primeros dolores.

---

## 5. Madurez y capacidades

### 🤔 Preguntas

> - *¿Tiene sentido pedirle a esta empresa un ERP integrado o un data warehouse? ¿Por qué no?*
> - *¿Cuál es el "costo de no actuar" en cada dimensión?*
> - *¿En qué dimensión el nivel actual es aceptable para su tamaño y en cuál es peligrosamente bajo?*

### ✅ Ejemplo

| Dimensión | Nivel | Evidencia | Costo de no actuar |
|---|---|---|---|
| Estrategia | Bajo | No hay plan; Carlos reacciona al día a día | Pierde clientes sin entender por qué |
| Liderazgo | Medio | Carlos lidera con experiencia, pero centraliza todo | Único punto de falla |
| Procesos | Bajo | Informales, no documentados, sin indicadores | Errores repetidos, pérdidas invisibles |
| Tecnología y datos | Bajo | Facturador + Excel + WhatsApp; sin integración | Decisiones a ciegas, stock incierto |
| Personas | Medio | Equipo leal y estable, pero sin capacitación ni autonomía | Dependencia de Carlos |
| Clientes | Medio-bajo | Relación personal fuerte, pero sin datos de comportamiento | Fuga silenciosa de clientes |
| Gobierno | Bajo | No hay reuniones, indicadores ni revisión periódica | No detectan problemas hasta que es tarde |

**Nota**: Para una empresa de 7 personas, un nivel "medio" en liderazgo y personas es razonable. Las brechas críticas están en **procesos**, **tecnología/datos** y **gobierno**, porque afectan directamente la caja y la capacidad de retener clientes.

---

## 6. Problema gerencial priorizado

### 🤔 Preguntas

> - *¿Estás describiendo un problema o ya estás proponiendo una solución disfrazada?*
> - *¿Puedes expresar el problema como "situación + causa + impacto en el negocio"?*
> - *¿Este problema le quitaría el sueño a Carlos? Si no, ¿es realmente prioritario?*

### ✅ Ejemplo

> **Problema**: Distribuidora Montaña pierde clientes y acumula deuda incobrable porque gestiona pedidos, stock y cobranza con herramientas inconexas (WhatsApp, Excel, cuaderno), lo que provoca pedidos incompletos, falta de seguimiento comercial y desconocimiento de la deuda real de cada cliente. En el último año, al menos 15 clientes dejaron de comprar sin que nadie lo detectara a tiempo, y la cartera morosa creció a ~ARS 8M (5% de la facturación).

**¿Por qué funciona esta formulación?**
- Describe **situación**: pierde clientes y acumula deuda.
- Identifica **causa raíz**: herramientas inconexas y falta de datos.
- Cuantifica **impacto**: 15 clientes perdidos, ARS 8M en morosos.
- **No nombra una solución** (no dice "necesita un sistema" ni "necesita un CRM").
