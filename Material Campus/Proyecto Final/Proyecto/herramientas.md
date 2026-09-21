# Herramientas de análisis que usamos

Este documento resume qué herramienta aplicamos en cada parte del trabajo, de dónde sale cada una y para qué nos sirvió. Lo armamos porque las herramientas no están sueltas: cada una alimenta a la siguiente, y esa cadena es parte de lo que queremos mostrar. Al final está también lo que decidimos no usar, con el motivo.

## Cuadro general

| Sección | Herramienta | Autor / origen | Para qué la usamos | Dónde la vimos |
|--------------|------------------|----------------|-----------------------------|--------------|
| 1. La organización | No aplica | | Es relevamiento descriptivo. Seguimos la estructura que pide el enunciado | Enunciado del TP |
| 2. El contexto | Factores del entorno con impacto real | Adaptado de PESTEL | Tomar las restricciones económicas, regulatorias, sociales y tecnológicas que el enunciado pide, pero contando qué le hace cada una a esta empresa | Clase 2 y guía de la cátedra |
| 2. El contexto | Cinco fuerzas | Porter (1979, 1980) | Analizar el sector: rivalidad, proveedores, compradores, entrantes y sustitutos | Clase 2 |
| 2. El contexto | Cadena de valor | Porter (1985) | Ver dónde se crea y dónde se pierde margen puertas adentro | Clase 2 (aparece también en la Clase 1) |
| 2. El contexto | FODA | Herramienta clásica de planeamiento | Sintetizar lo interno y lo externo en un solo cuadro | Clase 2 y guía de la cátedra |
| 3. Modelo de negocio | Business Model Canvas | Osterwalder y Pigneur (2010) | Describir cómo la empresa crea, entrega y captura valor hoy | Clase 2 |
| 3. Modelo de negocio | Explotación y exploración (Run / Change the Business) | Enfoque bimodal de la materia | Separar lo que sostiene la operación de lo que la transforma | Presentación introductoria y Clase 3 |
| 3. Modelo de negocio | Liderazgo en costos vs. diferenciación | Porter (1980) | Definir cuál es la ventaja competitiva real de la empresa | Clase 2 |
| 4. Propuesta de valor | Value Proposition Canvas | Osterwalder, Pigneur, Bernarda y Smith (2014) | Cruzar lo que el cliente necesita con lo que la empresa ofrece, y medir el encaje | Clase 2 |
| 5. Madurez | Modelo de madurez digital de la cátedra | Cátedra de Gestión Gerencial | Evaluar seis dimensiones con escala A a E, más una séptima que agregamos | Material de cátedra |
| 5. Madurez | Costo de No Actuar (CoI) | Fórmula de tres componentes | Poner en plata lo que cuesta no resolver cada brecha | Clase 3 |

## Cómo se encadenan

El orden en que las aplicamos no es casual. Cada herramienta produce algo que la siguiente necesita.

```
SECCIÓN 1
  Relevamiento de la organización
       |
       v
SECCIÓN 2
  Factores del entorno ----+
                           |--> Oportunidades y Amenazas --+
  Cinco fuerzas -----------+                               |
                                                           +--> FODA
  Cadena de valor ----> Fortalezas y Debilidades ----------+
       |
       v
SECCIÓN 3                          SECCIÓN 4                    SECCIÓN 5
  Business Model Canvas              Value Proposition Canvas      Modelo de madurez
  + Run / Change the Business        (segmento prioritario)        + Costo de No Actuar
       |                                   |                             |
       +-----------------------------------+-----------------------------+
                                           |
                                           v
                                    SECCIÓN 6 (se entrega aparte)
                                    Problema gerencial priorizado
```

En concreto:

- Los **factores del entorno** y las **cinco fuerzas** producen las oportunidades y las amenazas del FODA.
- La **cadena de valor** produce las fortalezas y las debilidades.
- El **segmento prioritario** de la sección 4 se justifica con lo que vimos en las cinco fuerzas.
- La **madurez** de la sección 5 se apoya en evidencia que fue apareciendo en las secciones 1 a 4.

## Herramientas que decidimos no usar, y por qué

El enunciado dice "usar FODA, PESTEL, cinco fuerzas u otra herramienta equivalente", o sea que deja elegir. Estas quedaron afuera a propósito.

| Herramienta | Por qué la dejamos afuera |
|---|---|
| **PESTEL completo** | Lo probamos y cuatro de sus seis dimensiones volvían vacías en este caso: ninguna regulación los complicó, la presión ecológica no se siente, lo legal se pisa con lo político y lo tecnológico ya lo mide la sección 5 con más rigor. Llenar seis casilleros para que cuatro digan "sin impacto" es justo lo que advierte la guía de la cátedra cuando pregunta cuál es la diferencia entre listar un factor PESTEL y explicar su impacto real. Nos quedamos con los factores que sí impactan |
| **FODA cruzado** | El cruce existe para derivar iniciativas, y esta entrega es diagnóstico: el enunciado pide explícitamente no proponer solución todavía. El FODA simple sí lo hicimos, que además es la forma que usa la guía de la cátedra en su ejemplo resuelto |
| Hipótesis de Oportunidad Tecnológica | Es una propuesta de solución (To-Be) y este trabajo es diagnóstico del estado actual (AS-IS) |
| Business Model Canvas en versión To-Be | Mismo motivo: el enunciado pide el modelo actual, no el propuesto |
| Balanced Scorecard y OKR | Corresponden al Hito 3, no a esta entrega |
| Design Thinking | Se vio en la Clase 3 pero apunta a idear soluciones, que todavía no toca |
| Plantilla canónica del problema gerencial | Es para la sección 6, que entregamos aparte |

## Una adaptación que hicimos

El enunciado pide evaluar siete dimensiones de madurez: estrategia, liderazgo, procesos, tecnología y datos, personas, clientes y gobierno. El modelo de la cátedra trae seis, porque mete gobierno adentro de "Procesos y Operaciones", en una sola pregunta.

Dejamos las seis dimensiones del modelo con sus 24 preguntas originales y agregamos **Gobierno** como séptima, con cuatro preguntas nuestras armadas con el mismo criterio y la misma escala. En una empresa sin reuniones de dirección ni indicadores gerenciales, el gobierno da para una dimensión propia. El enunciado permite adaptaciones justificadas y esta es la nuestra.

## Un solapamiento que conviene tener claro

La cadena de valor y el Business Model Canvas cubren un inventario parecido: actividades, recursos y socios aparecen en los dos. No es una repetición: **la cadena de valor pregunta dónde se crea y dónde se pierde margen, y el canvas pregunta cómo se crea y se captura valor**. Mismo material, lectura distinta.
