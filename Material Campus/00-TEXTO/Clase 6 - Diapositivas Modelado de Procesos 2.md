# Diapositivas Modelado de Procesos 2

> Texto extraido de `Clase 6/Diapositivas Modelado de Procesos 2.pdf`, 70 paginas. Generado el 2026-11-05 18:28 por `sincronizacion-campus`. No editar a mano.

---

Madurez de BPM* en la organización
(*) Business Process Management

                                  Fuente: ERBPM 2017, CETIUC

¿Para qué modelar?

                             Analizar (“levantar”)
                             Entender cómo se realiza el proceso

                             Diseñar
                             Definir cómo se debería efectuar

                             Preparar
¿Para qué                    Generar las condiciones de apoyo a su

modelar?                     ejecución (ej.: sistema de información)

En los procesos de negocio   Implementar
esto se convierte en:        Entregar instrucciones precisas a los involucrados respecto a cuál
                             es su rol en el proceso, y controlar posteriormente su desempeño

                             Mantener
                             Hacer mejoras fácilmente y reflejar cambios en el diseño

“Todos los modelos están errados,
pero existen algunos útiles”* - George box, 1997

  Existen muchas formas válidas de representar una situación, pero
  sólo algunas son de utilidad para el propósito buscado con el modelo

  El modelo tiene como objetivo fundamental la comunicación

      Contiene lenguaje adecuado para la audiencia

      Captura tipo y nivel de detalle adecuado

  La clave: reconocer sus limitaciones y tomar decisiones coherentes

   (*) “Essentially, all models are wrong, but some are useful”

Historia de BPMN

      Mayo 2004:           Febrero                  Julio 2008:
      BPMI lanza            2006:                    Comienza          Agosto 2009:
       propuesta         Versión final               discusión           Beta 1 de         Julio 2013:         Enero 2014:
       BPMN 1.0           BPMN 1.0                   BPMN 2.0            BPMN 2.0        Acreditación ISO       BPMN 2.0.2

                 2005:                   Febrero              Enero 2009:        Enero 2011:          Sept 2011:
             BPMI se fusiona              2008:                BPMN 1.2           BPMN 2.0            BPMN 2.0.1
               con OMG                   BPMN 1.1

                                               Analizar
                                               Permite reconocer roles, actividades y eventos
                                               que caracterizan el proceso de negocio actual.

                                               Diseñar
                                               Permite detallar todas las interacciones y flujos de un proceso.

 BPMN fue pensada
 específicamente                               Preparar
                                               BPMN da soporte a la generación de modelos ejecutables.
 para la modelación
 de un proceso de
 negocio                                       Implementar
 BPMN PERMITE:                                 Se puede comunicar fácilmente a personas del negocio,
(BPMS – Business Process Management Systems)   e incluso que estos contribuyan en su diseño.

                                               Mantener
                                               Idealmente, mediante herramientas de ejecución de procesos
                                               de negocio (BPMS). La documentación y el proceso son uno.

¿Qué vimos     Respondimos a la pregunta: ¿por qué modelar?

esta sesión?   Recorrimos la historia de BPMN

Actividad: el concepto fundamental en BPMN

 BPMN especifica el orden y la responsabilidad de ejecución
 de las actividades del proceso.

 A través del siguiente símbolo se representan las actividades:

                                                                  Nombre de la actividad
                         Actividad
                                                                   (verbo + sustantivo)

Conexión con SIPOC/RECI

      Hasta ahora, tenemos definidas las
      actividades del proceso, según RECI.

      …Sin embargo, nos falta especificar
      el orden de ejecución de éstas.

(*) Esquema de Software Bizagi

Flujo de secuencia: orden de
ejecución de las actividades

      A través del flujo de secuencia se
      especifica qué actividad se debe
      ejecutar antes que otra.

      Se representa a través de una
      flecha continua.

(*) Esquema de Software Bizagi

Flujo de secuencia: orden de
ejecución de las actividades

       A través del flujo de secuencia
       se especifica qué actividad se
       debe ejecutar antes que otra.

       Se representa a través
       de una flecha continua.

     Implícitamente, cada instancia
     de ejecución del proceso es una
     “ficha” que recorre el diagrama.

(*) Esquema de Software Bizagi

Pools y Lanes: organizaciones participantes
y responsabilidad de ejecución

      Para agrupar las distintas
      organizaciones involucradas en
      el proceso se ocupan los pools.

(*) Esquema de Software Bizagi

Pools y Lanes: organizaciones participantes
y responsabilidad de ejecución
  Para representar los roles y asignar la ejecución de las tareas se ocupan los lanes: carriles dentro de los pools.

Pools y Lanes: organizaciones participantes
y responsabilidad de ejecución
  BPMN permite modelar el
  aspecto interno y externo
  de los procesos:

     Los pools permiten
     representar las distintas
     organizaciones con las
     que el proceso interactúa
                                               Proveedores y
     (proveedores y clientes).                  clientes de
                                              acuerdo a SIPOC

Flujo de mensaje: comunicación entre pools

 Un Flujo de Mensaje se usa para mostrar la comunicación
 entre dos participantes de pools independientes.

     Se representa por una línea segmentada
     con el extremo sin relleno.

  Representa el envío de información desde un participante
  a otro, en una actividad o evento de mensaje específico.

Eventos: cosas que “suceden”

  Los procesos deben responder a cambios en el entorno: la llegada de un aviso, el
  paso del tiempo, etc. Estos se representan en BPMN con el concepto de “evento”.

  Los eventos afectan el flujo del proceso y tienen un causa (trigger – gatillo) o un efecto.

  Hay tres tipos de eventos básicos basado en cuándo ellos afectan el flujo:

                                    INICIO               INTERMEDIO                   FIN
                                    (start)             (intermediate)               (end)

Eventos más comunes

             INICIO                 INTERMEDIO                            FIN

            Sólo pueden          Se ocupan para especificar       Sólo pueden usarse
         usarse al principio     comportamientos durante           al final del flujo
           del diagrama                 la ejecución

                                                              Comportamiento genérico
                   Sin trigger

                                                              Llegada o envío
                      Mensaje                                 automático de mensaje

                       Tiempo                                 Paso de un plazo de tiempo u
                                                              ocurrencia de una fecha específica

Ejemplo de uso de eventos

                                        Este evento captura un
                                        mensaje, por lo que la
                                       ejecución del proceso se
                                       detiene a la espera de la
                                        ocurrencia del evento.

               Este evento indica un
               envío automático del
                     mensaje

Eventos: cosas que “suceden”

                               (*) Esquema de Software Bizagi

               Elementos básicos

¿Qué vimos        Actividad

                  Flujo de secuencia
esta sesión?      Flujo de mensaje

                  Tipos de eventos

Eventos que interrumpen una actividad
 También es posible adjuntar los eventos a las actividades, indicando que si durante la ejecución de la
 actividad ocurre el evento, se interrumpe la ejecución y se sigue un flujo de secuencia alternativo:

                                                                                                Actividades
                                                                                             completadas: A y B

                                                                                                 Actividades
                                                                                               completadas: C

(*) Esquema de Software Bizagi

 Gateways: secuencias de ejecución

       BPMN también incluye una forma de
                                                   Exclusiva
       especificar flujos de secuencia complejos                       ó
                                                   Basado en datos
                Tipos de “gateways” o compuertas                           =1
                                                   Basado en eventos

                                                   Inclusiva
                                                                           <=1

                                                   Paralela
                                                                           N

(*) Esquema de Software Bizagi

Ejemplos
                                 Exclusiva
                                                Actividades
                                             completadas: A y B

                                                Actividades
                                             completadas: A y C

                                 Paralela

                                                Actividades completadas:
                                                         A, B y C
                                                            o
                                                         A, C y B

(*) Esquema de Software Bizagi

Gateways: secuencias de ejecución

(*) Esquema de Software Bizagi

Evento terminate: terminando flujos en paralelo
Si en la ejecución en uno de los flujos requiere que el proceso
completo termine, se debe usar el evento de fin terminate

(*) Esquema de Software Bizagi

Subprocesos: agrupaciones de actividades
 Un concepto muy importante en BPMN es el de sub-proceso

    Permite definir diferentes niveles de detalle en el diagrama,
    de manera que un mismo modelo sirva a diferentes públicos.

                                                    Vista en detalle – “bajo nivel”   Vista resumida– “alto nivel”

Artefactos: elementos adicionales
que enriquecen el diagrama

                                                     Anotaciones de Texto
                                                     permiten al modelador
                                                     agregar información
                                                     adicional

       Nombre [Estado]

       Datos (Data object)        Grupo (Group)     Anotación (Annotation)
         Formularios                Agrupación de     Comentarios
                                    actividades
         Información

         Pueden ir incorporados
         en flujo de mensajes o
         como entrada y salida
         de actividades

  Asociaciones: unión entre artefactos

        Una asociación se usa para asociar datos,
        textos u otros artefactos con flujos de objetos.

               Se representa por una línea segmentada fina.

        También se usan para mostrar las entradas
        y salidas de las actividades.

(*) Esquema de Software Bizagi

Resumen de elementos básicos

               Elementos básicos

¿Qué vimos         Eventos adjuntos a las actividades

                   Gateways
esta sesión?       Artefactos adicionales de la notación

Repetición de actividades
Existen distintos tipos de repetición de actividades

                                              La actividad se ejecuta mientras cumpla la condición
                                              de repetición
                                              Se utiliza cuando no se sabe a priori cuántas veces se
                                              deberá ejecutar la actividad

                                              La actividad se ejecuta un número de veces
                                              definido a priori
                                              Las ejecuciones de esta actividad se realizan
                                              en paralelo

                                              La actividad se ejecuta un número de veces
                                              definido a priori
                                              Las ejecuciones de esta actividad se realizan en serie

Repetición de actividades: ejemplos
                                 1   Loop

                                 2   Múltiple instancia en paralelo

                                 3   Múltiple instancia en serie

(*) Esquema de Software Bizagi

Señalización

(*) Esquema de Software Bizagi

Evento condicional

  Es un evento que se gatilla dado el cumplimiento de una condición no directamente
  evaluable, que se puede cumplir inmediatamente o en algún momento futuro.

  Puede ser monitoreado de cualquier forma, inclusive un sistema externo (conocido como “motor de reglas”).

    Ejemplos

       “El cliente
      pertenece al
                            “El IPSA sube         “Temperatura
     segmento VIP, y
                             más de 5%”          mayor a 250 °C”
     compra más de
      500 dólares”

Evento condicional

(*) Esquema de Software Bizagi

Ejemplo hipódromo
  Las apuestas en carreras de caballos están regidas por reglas muy específicas.

  El periodo de apuestas para la siguiente carrera comienza cuando los jueces lo
  determinan, y lo notifican al público a través del altoparlante.

  Cuando esto sucede, un jugador puede apostar todas las veces que quiera, hasta que se cumpla el tiempo en que
  empieza la carrera, se congelen las apuestas debido a alguna razón que los jueces determinen, o se cancele la carrera.

  Estas últimas condiciones son notificadas a través de una pizarra electrónica.
  En particular, el último caso implica la devolución del total de las apuestas.

  Cuando se congelan las apuestas, los jueces evalúan los antecedentes disponibles, pudiendo
  eventualmente tomar la decisión de retomar las apuestas, o cancelar la carrera.

  Cuando finaliza la carrera, los jueces confirman los resultados, emitiéndose un aviso en la pizarra
  electrónica. El apostador por su parte, verifica si obtuvo algún premio, y si corresponde, lo cobra.

  Modele en detalle el proceso tanto desde el punto de vista del apostador como del hipódromo.

       Identifique actividades simples y complejas (por ejemplo, que requieran loops) en el diagrama.

             Hipódromo

(*) Esquema de Software Bizagi

               Repetición de actividades o subprocesos

¿Qué vimos     Otros eventos usados:

esta sesión?       Evento de señal
                   Evento condicional

               Ejemplo 2: Venta de café con eventos

(*) Esquema de Software Bizagi

Preguntas interesantes
¿Puede haber una actividad compartida entre dos lanes?
No, las actividades siempre están asociadas a un ejecutor exclusivo.

 (*) Esquema de Software Bizagi

Preguntas interesantes
¿Qué restricciones tiene el flujo de mensaje?

    No puede unir actividades dentro de un pool
    No tiene un significado de flujo, solo de intercambio de mensaje

(*) Esquema de Software Bizagi

Recomendaciones al modelar - Pools

                                 ¿Qué restricciones tiene el flujo de mensaje?

(*) Esquema de Software Bizagi

Recomendaciones al modelar - Eventos
    Los eventos deben tener un nombre diferente de las actividades

           Sustantivo con descripción del evento ocurrido

    Los eventos suceden fuera del control de los participantes del pool

(*) Esquema de Software Bizagi

Recomendaciones al modelar - Decisiones

                                          Sincronizar
                                          explícitamente
                                          flujos paralelos.

                                          Ocupar un evento
                                          “terminar” cuando
                                          se requiere finalizar
                                          la ejecución del
                                          proceso desde una
                                          rama paralela.

               Buenas practicas para:

¿Qué vimos
                  Demostrar comunicación entre procesos
                  Sincronización de flujos

esta sesión?      Eliminar ambigüedades con
                  las flechas de secuencia

               Pasos para una modelación correcta

Nuevos elementos de BPMN

                           Elementos básicos presentados hasta el momento
                           pertenecen a la versión 1.2 de BPMN

                           Con la versión 2.0 aparecen nuevos elementos que
                           ayudan a explicitar algunos comportamientos, que
                           con elementos anteriores, era más difícil de modelar

Actividades
    Las actividades son los elementos principales de un modelo BPMN

    Existen distintos tipos de actividades

                                  Es una unidad de trabajo,                                      Es una actividad que puede ser
                                  el trabajo a realizar.                                         refinada en más actividades.

                                 Es un conjunto de actividades                                  Es una referencia a un subproceso o
                                 relacionadas lógicamente, adhiriéndose                         tarea definida de forma global, que
                                 a un protocolo transaccional particular.                       se reutiliza en el proceso actual.

                                  Este se activa en la ocurrencia del evento de inicio especificado y mientras el proceso que lo
                                  contiene permanezca también activo. El subproceso de evento puede interrumpir o no al
                                  proceso que lo contiene.

(*) Esquema de Software Bizagi

Tipos de actividades/tareas

              Tarea que está diseñada                   Tarea que está diseñada para
              para enviar un mensaje a                  esperar a que llegue un mensaje
              un participante externo.                  de un participante externo.

             Es una tarea de workflow, en donde         Es una tarea en que se le envía datos
             un humano realiza la tarea con la          a un motor de reglas de negocio, y a
             asistencia de una aplicación de            cambio obtiene los resultados
             software, y está programado a través       obtenidos por éste.
             de algún gestor de la lista de tareas.

                                                        Se ejecuta por un motor de procesos
              Tarea que invoca a algún tipo de          de negocio. El modelador o
              servicio, lo que podría ser un servicio   ejecutor define una secuencia de
              Web o una aplicación automatizada.        comandos en un idioma que
                                                        el motor puede interpretar.

               Tarea que se espera llevar a
               cabo sin la ayuda de un motor de         Sin tipo especificado.
               ejecución de procesos de negocio.

Comportamiento de eventos: interrupciones
Eventos adjuntos
Algunos eventos intermedios de captura pueden adjuntarse a las actividades, generando
un nuevo flujo, que al activarse pueden no interrumpir o interrumpir la actividad.

     Interrumpir                                          No interrumpir
                       Si la actividad está activa                            Si la actividad está activa
                       y se recibe el mensaje,                                y se recibe el mensaje,
                       se interrumpe el flujo                                 NO se interrumpe el flujo

Tipo de evento
Existen 13 tipos de eventos
                                        Inicio   Intermedio   Fin

                                                                    Sin trigger
            Estos son los                                           Mensaje
            más utilizados
                                                                    Temporal

                                                                    Escalamiento
            Cada tipo tiene distintas
            representaciones según                                  Condicional
            su clase y comportamiento                               Link

                                                                    Error

                                                                    Cancelación

                                                                    Compensación

                                                                    Señal

                                                                    Múltiple

                                                                    Paralelo múltiple

                                                                    Terminación

Subproceso de evento

                       No es parte del flujo normal o principal

                          No tiene flujos de entrada ni salida

                       Se gatilla con la ocurrencia de su evento de inicio

                          Puede interrumpir o no el flujo normal

                          Se puede usar para capturar eventos
                          que pueden ocurrir en cualquier
                          parte del proceso

Solución: reserva de paquete turístico

Solución: reserva de paquete turístico

               Los nuevos tipos de actividades
¿Qué vimos     Eventos adjuntos a actividades o

esta sesión?   subprocesos que no interrumpen

               Subproceso de evento

Subproceso

             Es una actividad compleja, que puede ser refinada en más actividades.

                Es un elemento dentro de un proceso, pero también se puede
                “abrir” para mostrar el detalle de cómo se ejecuta

             1 - Subproceso colapsado vs. expandido

             2 - Subproceso normal (embebido) vs. de llamada (reutilizable)

             3 - Subproceso ad-hoc

             4 - Subproceso de evento

             5 - Subproceso transacción

1. Subproceso colapsado vs. expandido

       Vista colapsada de         Vista expandida de
         un subproceso              un subproceso

2. Subproceso normal (embebido)
   vs. de llamada (reutilizable)

Subproceso normal (embebido)

Subproceso normal de llamada (reutilizable)

Tipos de subprocesos
Existen 2 tipos de subprocesos, dependiendo del comportamiento interno que tienen:

              Subproceso normal                                    Subproceso ad-hoc

              Contiene un diagrama                                 No tiene conectores lógicos dentro.
              detallado de su flujo.                               Las tareas se realizan en cualquier orden, y el
                                                                   subproceso termina cuando todas se han ejecutado.

3. Subproceso ad-hoc

4. Subproceso de evento

5. Transacción

Ejemplo: Préstamo de libros

 Una bibliotecaria debe seguir un procedimiento estipulado para
 realizar el préstamo de libros a los usuarios de la biblioteca.

 Una vez que un cliente solicita el préstamo de uno o más libros, la
 bibliotecaria debe ingresar la información del usuario al sistema.

 Posteriormente, debe realizar una serie de acciones, para cada libro, sin un
 orden específico: timbrar los libros con la fecha de devolución, desactivar
 el sensor de seguridad de los libros, y escanear el código de barras.

 Es una vez ingresado el préstamo de todos los ejemplares al sistema,
 se le entregan los libros al cliente, finalizando el proceso.

Ejemplo: Préstamo de libros

               Tipos de subprocesos que existen

                  Colapsado

¿Qué vimos        Expandido

                  De llamada (reusable)

esta sesión?      Ad-hoc

                  Transacción

                  Evento

Recomendaciones al modelar - Pasos
No hay una receta establecida, sin embargo, recomendamos seguir cierto orden:

1    Crear los pools de acuerdo al diagrama SIPOC.

2    Crear el pool donde correrá el flujo principal, con los lanes
     de acuerdo a los Ejecutores identificados en el RECI.

3    Comenzar modelando sólo en el pool de la organización,
     basándose en la ejecución ideal y sin considerar los demás
     pools ni las interacciones con estos.

4    (Opcional) Modelar los “caminos ideales” de los demás pools e
     incluir los mensajes entre estos y el pool de la organización.

     Modelar las rutas alternativas y de excepción en el pool
5
     principal y luego en los demás, añadiendo las
     interacciones donde corresponda.

Señalización

 Es un evento que puede ser de todo tipo

    Inicio
    Intermedio
    Final

 Puede estar “atachado” a otra actividad o subproceso

 No es lo mismo que un mensaje, sino que responde
 a una arquitectura “desacoplada”

    La señal se envía a cualquiera que esté esperando por ella

    Una señal puede provenir desde otro proceso

Ejemplo: “reserva de paquetes turísticos”

 El proceso comienza cuando se recibe una orden de reserva.
 El agente de viajes registra los datos del cliente, revisa la
 orden de reserva y según los requerimientos, reserva el hotel,
 los pasajes, las actividades, o el automóvil.

 Al finalizar, el agente de viajes envía las reservas
 confirmadas al cliente.

 Mientras se está tramitando la orden, el cliente
 puede cancelarla en cualquier momento, con lo
 cual el agente debe procesar la cancelación.

 Adicionalmente, el cliente puede solicitar un
 estado de su orden en cualquier momento.

Consolidación de la modelación de procesos

 Hasta hace poco no existía una notación que permitiera
 modelar procesos de negocio satisfactoriamente

    UML representa bien ambientes estructurados, pero es difícil
    representar interacciones complejas y poco estructuradas
    Otras notaciones, como EPC, son propietarias

    En general, no estaban pensadas para comunicarse
    con personas del negocio

 Surge Business Process Model and Notation (BPMN)

    Notación creada como estándar de representación de procesos

    Específicamente diseñada para representar la secuencia de
    actividades y los mensajes que fluyen entre distintos participantes
