# PARTE 2: Diseño de la propuesta de transformación

*Dominio de la solución: propuesta gerencial viable, centrada en cómo se va a resolver y llevar a cabo.*

---

## 1. Objetivo y alcance

### 🤔 Preguntas

> - *¿Qué resultado concreto vería Carlos al final del proyecto?*
> - *¿Con qué lo mediría él, no nosotros?*
> - *¿Qué queda explícitamente fuera?*

### ✅ Ejemplo

**Objetivo general**: Reducir la pérdida de clientes y la deuda incobrable mediante la integración del proceso de pedido, stock y cobranza en un flujo único y trazable, en un plazo de 6 meses.

**Objetivos específicos**:
1. Centralizar la toma de pedidos en un canal digital con confirmación y precio visible → reducir pedidos incompletos un 50%.
2. Automatizar el estado de cuenta por cliente → reducir la cartera morosa de ARS 8M a ARS 4M.
3. Vincular los pedidos con el stock real → reducir roturas de stock un 30%.

**Fuera de alcance**: Cambio de facturador electrónico, ampliación de rutas, contratación de personal nuevo, rediseño del depósito.

---

## 2. Proceso actual (AS-IS) y alternativas de solución

### 🤔 Preguntas

> - *Si le pidieras al vendedor que te describa su día paso a paso, ¿qué te diría?*
> - *¿Dónde se "pierde" información entre un paso y otro?*
> - *¿Cuál es la opción más simple que ya mejoraría algo? ¿Y si no hacemos nada, qué pasa?*

### ✅ Proceso AS-IS (resumen narrativo + diagrama conceptual)

```
Vendedor visita cliente → Anota pedido en agenda de papel → Le manda foto por WhatsApp a depósito
→ Depósito arma el pedido mirando la planilla de Excel (¿hay stock?) → Chofer entrega y cobra en efectivo
→ Le pasa la plata y los remitos a Laura → Laura actualiza el cuaderno de cobranza y factura a fin de día
```

**Dolores del proceso**: El pedido se pierde entre la foto de WhatsApp y el depósito. El stock en Excel no refleja la realidad. Laura cruza facturas vs. cobros una vez al mes. Si un cliente no paga, lo detecta 30 días tarde.

### ✅ Alternativas comparadas

| Criterio | A: Do Nothing | B: Planilla Google compartida + WhatsApp Business | C: SaaS de distribución (ej. Driv.in, Datascope, Nube) |
|---|---|---|---|
| Alineación al problema | ❌ No resuelve | ⚠️ Parcial: centraliza pedidos pero no integra stock ni cobranza | ✅ Integra pedido, stock y cuenta corriente |
| Costo mensual | $0 | ~$0 (herramientas gratuitas) | ~USD 50-80/mes |
| Adopción y curva | – | Fácil: ya usan WhatsApp | Media: requiere capacitación de 2-3 hs |
| Integración con facturador | – | Manual | Posible exportación CSV o API |
| Escalabilidad | – | Se rompe si crece | Soporta más rutas y clientes |
| Riesgo de continuidad | Pérdida de clientes crece | Mejora parcial; riesgo de abandono por esfuerzo manual | Dependencia de un proveedor externo |

**Recomendación**: **Alternativa C** (SaaS de distribución), porque es la única que integra los tres procesos rotos (pedido, stock y cobranza) en un solo flujo, con un costo proporcional al tamaño de Montaña (~USD 70/mes = ~0,2% de la facturación).

---

## 3. Diseño del proceso futuro (TO-BE)

### 🤔 Preguntas

> - *¿Cómo sería el día del vendedor con el nuevo proceso?*
> - *¿En qué momento exacto se genera el dato que hoy falta?*
> - *¿Qué controles simples evitan que se repitan los errores actuales?*

### ✅ Proceso TO-BE

```
Kiosquero hace pedido por catálogo digital (link o app) → El sistema valida stock en tiempo real
→ Vendedor confirma o ajusta en su visita → Depósito recibe pedido armado automáticamente
→ Chofer entrega y registra cobro en la app → El sistema actualiza cuenta corriente y stock
→ Laura ve el tablero de cobranzas con alertas de mora automáticas
```

**Diferencias clave**:
- El kiosquero puede pedir fuera de la visita; ve precios y disponibilidad.
- El stock se descuenta al confirmar el pedido, no al entregar.
- Laura no espera a fin de mes: ve la mora en tiempo real.
- Carlos tiene un tablero con ventas, stock y cobranza integrados.

---

## 4. Transformación del modelo de negocio (BMC Shift) y propuesta de valor

### 🤔 Preguntas

> - *Mirando el BMC de la Parte 1, ¿qué bloques cambian concretamente? ¿Solo los del "backstage" o también los que ve el cliente?*
> - *¿La propuesta de valor que le llega al kiosquero es la misma de antes o cambia?*
> - *¿Qué estamos asumiendo que sea cierto para que esto funcione? ¿Lo validamos o lo "creemos"?*

### ✅ Ejemplo

**BMC Shift (Delta)**:

| Bloque | AS-IS (Parte 1) | TO-BE (cambio) |
|---|---|---|
| **Canales** *(Frontstage)* | Visita presencial + WhatsApp | Catálogo digital + visita presencial (complementarios) |
| **Relación** *(Frontstage)* | Solo personal | Personal + autoservicio digital con estado de cuenta |
| **Actividades clave** *(Backstage)* | Pedido manual, stock en Excel, cobranza en cuaderno | Pedido digital, stock integrado, cobranza automatizada |
| **Recursos clave** *(Backstage)* | Conocimiento en la cabeza de Carlos | Datos en el sistema, accesibles por todo el equipo |
| **Costos** *(Backstage)* | Sin costo TI | +USD 70/mes SaaS |

**VPC TO-BE**: La propuesta de valor al kiosquero ahora incluye: pedir cuando quiera, ver precios actualizados, saber cuánto debe y recibir pedidos completos. Los cuatro dolores detectados en la Parte 1 se alivian directamente.

**Supuestos críticos de la transformación**:

| Supuesto | Tipo | Riesgo si es falso |
|---|---|---|
| El kiosquero usará el catálogo digital | Deseabilidad | Inversión sin adopción del cliente |
| Los vendedores cargarán datos en la app en vez de la agenda | Factibilidad | Doble registro; se abandona el sistema |
| El SaaS se integra con el facturador actual | Factibilidad | Carga manual que anula el beneficio |
| El ahorro en cobranza y retención justifica USD 70/mes | Viabilidad | Gasto sin retorno visible |

---

## 5. Stakeholders del proyecto de mejora

### 🤔 Preguntas

> - *¿Quién tiene el poder de frenar este proyecto con solo "no usarlo"?*
> - *¿Quién pierde algo con el cambio (control, costumbre, autonomía)?*
> - *¿Quién debe ser el sponsor para que esto avance?*

### ✅ Matriz Poder/Interés (Mendelow)

| Actor | Poder | Interés | Estrategia |
|---|---|---|---|
| **Carlos** (dueño) | Alto | Alto | Sponsor del proyecto. Involucrar en todas las decisiones. |
| **Laura** (administración) | Alto | Alto | Usuaria clave de cobranza. Capacitar primero; su éxito valida el sistema. |
| **Vendedores** (2) | Medio | Bajo | Pueden resistir por pérdida de autonomía. Demostrar que el sistema les ahorra tiempo, no los controla. |
| **Choferes** (2) | Bajo | Bajo | Impacto mínimo. Informar y entrenar en registro de entregas/cobros. |
| **Depósito** (1) | Medio | Medio | Recibe pedidos armados del sistema; mejora su trabajo. Aliado natural. |
| **Proveedor SaaS** | Medio | Alto | Socio técnico. Negociar soporte y período de prueba. |

---

## 6-9. Arquitectura, Seguridad, Derisking y Roadmap (resumen)

### 🤔 Preguntas para estas secciones

> - *Arquitectura*: *¿Cuántos "sistemas" realmente necesita una empresa de 7 personas? ¿Es un diagrama de NASA o un flujo simple?*
> - *Derisking*: *¿Qué es lo mínimo que podemos probar antes de pagar la suscripción anual?*
> - *Roadmap*: *¿En qué mes del año conviene empezar para no chocar con la temporada alta?*

### ✅ Derisking (ejemplo de un supuesto)

| Supuesto | Experimento | Duración | Decisión |
|---|---|---|---|
| El kiosquero usará catálogo digital | Crear un catálogo en Google Sheets compartido con 10 clientes amigos por 2 semanas | 2 semanas | Si >5 de 10 hacen al menos 1 pedido, avanzar |
| Los vendedores cargan datos | Piloto de 1 semana con 1 vendedor usando la app en su ruta | 1 semana | Si carga >80% de los pedidos, escalar |

### ✅ Roadmap preliminar (6 meses)

| Fase | Mes | Foco |
|---|---|---|
| 1. Preparación | Mes 1 | Selección y contratación SaaS, carga de datos maestros (clientes, productos, precios) |
| 2. Piloto | Mes 2-3 | 1 ruta, 30 clientes, 1 vendedor. Laura usa cobranza digital. |
| 3. Evaluación | Mes 3 | Go/No-Go con indicadores del piloto |
| 4. Escalamiento | Mes 4-5 | Segunda ruta, integración con facturador, catálogo abierto a clientes |
| 5. Estabilización | Mes 6 | Ajustes, capacitación final, cierre de cuaderno de Laura |

*Se inicia en marzo (post-temporada alta de verano) para no interferir con el pico de ventas.*
