# Problema gerencial, objetivos y alcance

Esta sección cierra dos pendientes de la Parte 1. Uno es el problema gerencial priorizado, que dijimos que íbamos a presentar por separado. El otro es una corrección: al relevar el proceso para esta parte encontramos que varias cosas que afirmamos en el diagnóstico no eran del todo ciertas. Empezamos por la corrección, porque lo que sigue se apoya en la versión corregida.

## Lo que corrige el relevamiento

Para la Parte 2 volvimos a recorrer un pedido de distribuidor de punta a punta, desde que llega hasta que sale el camión, con nuestro compañero que trabaja en Dulxelitos (Juan José Geyer). Ese recorrido corrige tres cosas de la Parte 1. Nos pasó lo mismo que con el catálogo web que contamos en la Parte 1: al cruzar lo que habíamos concluido con lo que se ve adentro, un dato cambió. Esta vez el que se corrige es el diagnóstico nuestro.

**El stock de producto terminado no se registra.** En la sección 5.2 de la Parte 1 pusimos "Facturación y stock sí" como proceso digitalizado, y "Facturación, stock y cuentas corrientes en el sistema" como nivel de automatización. La facturación sí está en Discovery y eso se mantiene. El stock de producto terminado no: no se lleva ni en Discovery ni en ningún otro registro. Para saber si hay mercadería se mira a ojo en el depósito y se le pregunta a producción. Producción lleva su propio control, lo carga una vez por semana y no tiene relación con las ventas. El módulo de stock de Discovery está dentro de la licencia y no se usa. Lo corregimos al seguir un pedido real por el depósito.

**Los pedidos recortados no son raros, pasan todas las semanas.** En la sección 5.5 escribimos que los pedidos incompletos "son poco frecuentes y se resuelven fácil", y que la empresa los percibía como menores. En una semana de registro, 30 de los ~125 pedidos (25 por día durante 5 días) salieron recortados o demorados. Eso es un ~24 %, o dicho al revés, un ~76 % de pedidos completos y a tiempo. El 76 % es una cuenta nuestra sobre una sola semana, no un promedio anual, y así lo usamos en el resto del trabajo.

**Los recortes no vienen de la capacidad total de la planta.** En la sección 2.1 atribuimos los faltantes de papas fritas a "la capacidad de planta". La planta sigue saturada y eso no se corrige: las horas extras que la tapan siguen ahí. Pero los recortes semanales se explican sobre todo por mezcla y momento: se produce lo que no hace falta y falta lo que se pide, porque la producción la deciden el dueño o los hijos por criterio propio, sin mirar los pedidos. Que la mezcla explique la mayoría de los recortes es un supuesto crítico y lo vamos a medir en el piloto, no lo damos por probado.

Las tres correcciones no cambian el diagnóstico de fondo, lo refuerzan. En la Parte 1 Gobierno quedó en 1.50, con la idea de que la empresa decide y controla sin instrumentos integrados, y de que el costo de no actuar "no está bajo, está sin observar". Ahora sabemos por qué no se podía cuantificar: ni el stock ni los recortes se registraban, así que no había nada que contar.

## Problema gerencial

Es la sección 6 de la Parte 1, que quedó pendiente. Sigue la plantilla de la Clase 3: dolor, causa raíz, magnitud y métrica de éxito, en no más de 60 palabras y sin nombrar ninguna herramienta, porque la solución se elige recién en la sección 2 de esta parte.

> Dulxelitos recorta o demora unos 30 de ~125 pedidos semanales porque los acepta sin conocer el stock de producto terminado, que no se registra, y decide la producción sin mirar las ventas. Esto genera faltantes y ~25 horas extras mensuales sobre una planta saturada. Éxito: pedidos completos y a tiempo del 76 % al 90 % en 6 meses.

Cómo se lee, bloque por bloque:

- **Dolor:** pedidos recortados o demorados, con faltantes y horas extras para taparlos.
- **Causa raíz, técnica y de organización a la vez:** no hay un registro del stock de producto terminado (lo técnico), y los pedidos se aceptan y la producción se decide sin mirarse entre sí, con el criterio del dueño o de los hijos (lo social).
- **Magnitud:** unos 30 de ~125 pedidos por semana, y ~25 horas extras por mes.
- **Métrica de éxito:** pedidos completos y a tiempo, del 76 % al 90 % en 6 meses. "A tiempo" quiere decir dentro del plazo estándar de cada zona (en la Patagonia, hasta una semana). Un pedido que se rechaza o se reprograma de entrada para que el número cierre no cuenta como completo.

**Por qué 90 % y no 100 %.** La meta es nuestra, no un dato de la empresa. Si la mezcla y el momento de producción son la causa principal, planificar contra pedidos ataca esa causa y justifica prometer una baja real. Pero es una pyme con la planta saturada, y siempre va a haber roturas e imprevistos. Un 90 % deja un 10 % de margen (100 menos 90) y es una meta que el equipo puede sostener. Si el piloto muestra que la mezcla explica menos de lo que suponemos, la meta se revisa.

## Objetivo general

Que cada pedido de distribuidor se confirme sabiendo qué hay en stock de producto terminado, y que la producción se planifique contra los pedidos pendientes, para llevar los pedidos completos y a tiempo del 76 % al 90 % en un plazo de 6 meses.

Según lo que pide el enunciado:

- **Problema abordado:** recortes y demoras semanales por aceptar pedidos sin conocer el stock y producir sin mirar las ventas.
- **Resultado esperado:** pedidos completos y a tiempo del 76 % al 90 %.
- **Proceso y capacidad alcanzados:** el proceso "Atender pedido de distribuidor", de la recepción al despacho, y la planificación semanal de producción. La capacidad nueva es saber qué hay y qué falta antes de comprometer un pedido.
- **Plazo:** 6 meses. Se puede arrancar en cualquier momento, porque la demanda es pareja todo el año.

## Objetivos específicos

Son tres. Cada uno tiene una métrica que la empresa puede obtener, una línea de base, una meta y un plazo. Las líneas de base salen de los datos de Juan José Geyer del relevamiento; no inventamos ninguna.

**1. Que los pedidos se confirmen sabiendo qué hay en stock.**

- **Métrica:** pedidos completos y a tiempo sobre pedidos recibidos, por semana.
- **Línea de base:** 76 % (30 recortados o demorados de ~125, en una semana de registro; cuenta nuestra).
- **Meta:** 90 %.
- **Plazo:** 6 meses.
- **De dónde sale:** del registro semanal de pedidos recortados o demorados, el mismo que dio la semana base.

**2. Que la producción se cargue todos los días.**

- **Métrica:** días hábiles con producción cargada sobre días hábiles.
- **Línea de base:** 20 % (hoy se carga 1 vez por semana, o sea 1 de 5 días hábiles).
- **Meta:** 100 % de los días hábiles.
- **Plazo:** dentro de los 6 meses. La primera prueba es un piloto de 2 semanas con papas fritas, el producto que más falta.
- **De dónde sale:** del control de producción. Es un indicador de avance: avisa antes de que falle el stock, porque sin carga diaria no hay stock en el que confiar.

**3. Que bajen las horas extras.**

- **Métrica:** horas extras totales por mes, de la liquidación de sueldos.
- **Línea de base:** ~25 horas por mes.
- **Meta:** la mitad, unas 12 horas por mes. Es un supuesto de meta nuestro (25 dividido 2) que hay que confirmar con el dueño. La liquidación no distingue las horas extras que tapan un faltante de las que tapan la saturación de planta, así que la meta puede quedar corta o larga hasta que el piloto muestre cuánto pesa cada causa.
- **Plazo:** 6 meses.
- **De dónde sale:** de la liquidación de sueldos, que la empresa ya tiene. Falta el costo de la hora extra para llevarlo a pesos: [dato pendiente: costo por hora extra].

Hay un cuarto indicador, la **exactitud de stock**, que no es un objetivo sino la condición de los otros tres: si lo cargado no coincide con el conteo físico semanal, ninguno se sostiene. Su línea de base sale del primer conteo físico: [dato pendiente: exactitud de stock en el conteo inicial]. La meta se fija con ese conteo. La ficha completa de los cuatro indicadores está en la sección 8 de esta parte.

## Alcance

**Proceso.** "Atender pedido de distribuidor": empieza cuando llega el pedido por WhatsApp o teléfono y termina con el pedido facturado en Discovery y despachado. Incluye además la planificación semanal de producción contra pedidos, y los indicadores con su rutina de seguimiento.

**Áreas y actores.** Oficina, depósito, producción y dirección (el dueño y los hijos). El dueño es el sponsor del proyecto, que aprueba el presupuesto y las decisiones de Go/No-Go. El líder es el responsable de sistemas, a quien la propuesta le asigna formalmente la gobernanza que en la Parte 1 le faltaba. Los distribuidores y el transporte tercerizado participan del proceso pero no cambian su trabajo: los distribuidores siguen pidiendo por WhatsApp o teléfono, y lo que cambia es que, si falta algo, se les avisa en el momento con una fecha estimada.

**Cambios de trabajo incluidos.**

- Producción carga lo producido todos los días, al cierre de turno.
- Oficina consulta el stock y lo reserva antes de confirmar un pedido.
- Dirección planifica la producción de la semana mirando los pedidos pendientes y un stock mínimo por producto.
- Una reunión corta diaria entre ventas y producción (~10 minutos) y un conteo cíclico semanal.

**Capacidades, datos y herramientas requeridas.**

- **Capacidades:** disciplina de carga diaria, un responsable de carga por turno con suplente, y un criterio único de stock disponible.
- **Datos:** stock físico de producto terminado por producto, reservas por pedido confirmado sin facturar, pedidos pendientes, stock mínimo y horas extras. El criterio es siempre el mismo: **stock disponible = stock físico menos lo reservado por pedidos confirmados sin facturar.**
- **Herramientas:** Discovery, que ya tiene la empresa, para facturación y para el módulo de stock, pedidos y reserva que hoy no se usa; y una planilla compartida para el piloto de 2 semanas. Cuál va como solución y cuál como prueba se fundamenta en la sección 2 de esta parte.

## Fuera de alcance

Dejamos afuera lo que no es necesario para el problema, y decimos por qué.

- **Insumos y packaging.** También tienen problemas, pero son otro problema. Quedan declarados como deuda; el proveedor único de film ya figura como riesgo en la Parte 1.
- **Visibilidad de stock para el distribuidor.** Por ahora el stock es solo interno. Va al roadmap como "later", junto con la tienda online de 2020.
- **Ampliación de planta.** La saturación sigue. Lo que atacamos es la mezcla y el momento de producción, no la capacidad total.
- **Cambiar Discovery por otro sistema.** Un SaaS de gestión lo evaluamos y lo descartamos en la sección 2 de esta parte.
- **CRM.** Es un problema real de la Parte 1 (Clientes y Canales), pero no es este.
- **Costeo y listas de precios.** Tampoco se tocan en esta propuesta.

**Se queda manual a propósito.** No todo conviene digitalizarlo ahora. El armado del pedido en el depósito se queda como está: según nuestro compañero de la empresa es rápido y no se mide, así que no es la restricción. El conteo físico sigue siendo a mano. Y la decisión de qué producir sigue siendo del dueño y de los hijos: lo que cambia es que la toman mirando pedidos y stock, no que se automatice. Digitalizar sin rediseñar no mejora el tiempo de ciclo.
