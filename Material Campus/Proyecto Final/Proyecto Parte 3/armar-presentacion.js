// Presentacion de la defensa final (Parte 3) de Dulxelitos: 14 laminas, ~20 minutos.
// Mismo estilo que las Partes 1 y 2 (../Proyecto Parte 2/armar-presentacion.js): paleta,
// tipografias y helpers. Ningun monto esta escrito a mano: todo sale de caso.json (la
// planilla es la unica fuente), incluidas las fechas, que se calculan desde la semana 1.
// Lo unico fijo son los datos del relevamiento que no estan en caso.json (marcados abajo),
// los umbrales de las medidas y la fecha limite de la decision.
//
// Uso (pptxgenjs vive en la carpeta de la Parte 2):
//   NODE_PATH="../Proyecto Parte 2/node_modules" nice -n 10 node armar-presentacion.js \
//     "Entrega/Presentación TP Final Parte 3 - Dulxelitos.pptx"
const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");

const C = JSON.parse(fs.readFileSync(path.join(__dirname, "caso.json"), "utf8"));
const SUP = C.supuestos;

const DARK = "1B2B34";
const CREAM = "F7F4EC";
const WHITE = "FFFFFF";
const ORANGE = "C8791E";
const GREEN = "2F6B5E";
const RED = "A33B22";
const BLUE = "1E5C85";
const GREY = "55636B";
const MUTED = "8FA3AB";
const PALE = "C3D0D4";
const LINE = "E2DCCC";

const T_NEUTRAL = "EFEADC";
const T_GREEN = "DCEAE3";
const T_RED = "F3DFD9";
const T_BLUE = "DDE8EF";
const T_ORANGE = "F6EBD8";
// Naranja oscurecido solo para texto chico sobre fondos claros (4,4:1 o mas); el
// naranja de la paleta queda para formas, numeros grandes y texto sobre oscuro.
const ORANGE_TXT = "9E5C15";

// Uso de los colores, igual en las laminas, los diagramas, el informe y el guion:
//   oscuro  = texto, trazos, tarjeta destacada; en los numeros del caso, el DINERO (caja)
//   naranja = atencion: dolores, lo que es solo del piloto; en los numeros del caso,
//             el TIEMPO del personal que cobra igual (capacidad liberada)
//   verde   = la mejora: metas, resultados clave, Go
//   azul    = sistemas y datos: Discovery (alternativa B)
//   rojo    = problemas, costo de seguir igual, Pausar
//   gris    = lo secundario

const H = "Arial";
const B = "Calibri";

const W = 13.3;
const M = 0.65;
const CW = W - 2 * M; // 12.0

const TOTAL = 14;

// ---------------------------------------------------------------- formato y cifras
// Cifras con el formato del dossier: $ con punto de miles, coma decimal, menos tipografico.
const miles = (n) => String(Math.round(Math.abs(n))).replace(/\B(?=(\d{3})+(?!\d))/g, ".");
const peso = (n) => (n < 0 ? "−$" : "$") + miles(n);
const dec = (n) => String(Math.round(n * 100) / 100).replace(".", ",");
const pct = (x) => Math.round(x * 100) + " %";
// Redondeo tipo "$2,1 M": un decimal, y dos si con uno se pierde mas del 1,5 %.
function mm(n) {
  const x = Math.abs(n) / 1e6;
  const d1 = Math.round(x * 10) / 10;
  const v = Math.abs(d1 - x) / x > 0.015 ? Math.round(x * 100) / 100 : d1;
  return (n < 0 ? "−$" : "$") + String(v).replace(".", ",") + " M";
}
// Para las notas, lo que se dice en voz alta.
const hablado = (n) => (Math.abs(n) >= 1e6 ? mm(n).replace(" M", " millones") : peso(n));
// Redondeo hacia abajo en la mitad: 22,5 -> 22 y 11,25 -> 11 (como "unas 22" del dossier).
const redondeo = (x) => Math.ceil(x - 0.5);

// ---------------------------------------------------------------- datos de la empresa
const HE_MES = SUP.HE_mes_hoy; // horas extras por mes, esperado
const HORA_EXTRA = SUP.Hora_extra;
const REC_HOY = SUP.Recortados_hoy;
const PED_SEM = SUP.Pedidos_semana;
const PCT_COMPLETOS = Math.round((1 - REC_HOY / PED_SEM) * 100); // 76 %
const META_COMPLETOS = pct(SUP.Meta_completos); // 90 %
const RED_HE_CON = SUP.RedHE_con;
const RED_HE_ESP = SUP.RedHE_esp;
const DEMORA_CON = SUP.Demora_con; // semanas
const CONT_CON = pct(SUP.Cont_con);
const TASA = pct(C.tasa_descuento_real_anual);
const HE_CON = HE_MES * (1 - RED_HE_CON);
const HE_ESP = HE_MES * (1 - RED_HE_ESP);
const FRAC_CON = (REC_HOY - C.recortados_semana_conservador) / (REC_HOY - C.recortados_semana_esperado);
const TXT_FRAC_CON = Math.abs(FRAC_CON - 0.5) < 0.01 ? "La mitad de la mejora" : "El " + pct(FRAC_CON) + " de la mejora";
// Dinero y tiempo del costo de no actuar.
const NO_ACTUAR = C.costo_no_actuar_mensual;
const NO_ACTUAR_DINERO = C.costo_no_actuar_caja_mensual;
const NO_ACTUAR_TIEMPO = NO_ACTUAR - NO_ACTUAR_DINERO;
// No estan en caso.json: relevamiento y definiciones del plan.
const HE_RANGO = "40 a 50";
const DIAS_CARGA_HOY = "20 %";
const DISTRIBUIDORES = 57;
const UMBRAL_RECORTES_LINEA = "70 %"; // Go por linea: recortes en 70 % o menos de la base (piloto: la mitad)
const LIMITE_DECISION = "15-1-2027"; // para comenzar la semana 1 el lunes de inicio

// ---------------------------------------------------------------- fechas desde la semana 1
const INI = new Date(SUP.Inicio + "T12:00:00Z");
const fd = (sem, d) => new Date(INI.getTime() + ((sem - 1) * 7 + d) * 86400000); // d: 0 lunes
const dm = (t) => t.getUTCDate() + "-" + (t.getUTCMonth() + 1); // 22-2
const dma = (t) => dm(t) + "-" + t.getUTCFullYear(); // 22-2-2027
const rango = (a, b) => (a.getUTCMonth() === b.getUTCMonth() ? a.getUTCDate() + " al " + dm(b) : dm(a) + " al " + dm(b));
const semana = (n) => rango(fd(n, 0), fd(n, 4));
const DIA = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"];
const SEM_PIL_D = SUP.Piloto_desde, SEM_PIL_H = SUP.Piloto_hasta, SEM_GO = SUP.Sem_go, SEM_FIN = SUP.Seg_hasta;
const PILOTO = rango(fd(SEM_PIL_D, 0), fd(SEM_PIL_H, 4)); // 22-2 al 5-3
const GO_FECHA = dm(fd(SEM_GO, 3)); // jueves de la semana 6
const GO_FECHA_A = dma(fd(SEM_GO, 3));
const INICIO_LUNES = dma(fd(1, 0));

// ---------------------------------------------------------------- piezas para las notas
const idxMin = (arr) => arr.indexOf(Math.min.apply(null, arr));
const iMaxCon = idxMin(C.saldo_acumulado_conservador), iMaxEsp = idxMin(C.saldo_acumulado_esperado);
const recTxt = (m) => (m == null ? "no se recupera dentro de los 3 años" : "mes " + m);

// ---------------------------------------------------------------- notas del orador
const NOTAS = [
  /* 1 */ `[~0,5 min] Presentamos el proyecto completo en unos 20 minutos. Primero repasamos lo que ya conocen: el problema, la propuesta y el piloto, en tres láminas. El resto es lo nuevo: lo que equivale seguir igual, el caso de negocio con dos escenarios, cuánto se llega a poner y cuándo se recupera, el primer mes, quién decide, qué puede salir mal, cómo nos ocupamos de las personas, y la decisión concreta que le pedimos a la dirección. Les pedimos que escuchen como si fueran la dirección de la empresa: lo que sigue está armado para que puedan decidir sin nosotros.`,

  /* 2 */ `[~1 min] El problema en una frase: la empresa acepta pedidos sin saber qué hay en stock y produce sin mirar lo que se pidió. En la semana que registramos, ${REC_HOY} de unos ${PED_SEM} pedidos salieron recortados o demorados: ${PCT_COMPLETOS} % completos y a tiempo. Es una estimación sobre una sola semana, y por eso el plan vuelve a medirla antes de empezar. Las horas extras son ${HE_RANGO} por mes según la liquidación: se midieron mejor después de la Parte 2, donde habíamos estimado unas 25; usamos ${HE_MES} como valor esperado. La carga de la producción hoy es una vez por semana, un ${DIAS_CARGA_HOY} de los días. Lo que mostró el relevamiento: el stock de producto terminado no se registra en ningún lado, y cada recorte lleva alrededor de ${SUP.Retrabajo_h} hora de trabajo entre Oficina y Depósito para avisar, re-armar, facturar y coordinar.`,

  /* 3 */ `[~1,5 min] En la Parte 2 llegamos a una sola causa vista desde tres lados: la disponibilidad se averigua dos veces, el mismo pedido se anota tres veces y producción y ventas no comparten ningún dato. La propuesta cambia tres cosas: una consulta del disponible antes de confirmar, una sola carga del pedido y la carga de producción todos los días, no una vez por semana. De las tres alternativas que evaluamos, quedaron dos casi empatadas: A, una planilla compartida, y B, activar el módulo de stock de Discovery que ya está en la licencia y no se usa. Decide el argumento y no el puntaje: A va primero como piloto de dos semanas con papas fritas, y B es el destino. La regla es la misma en las dos: el stock disponible es el físico menos lo reservado por pedidos confirmados que todavía no se facturaron.`,

  /* 4 */ `[~1 min] El piloto es el experimento mínimo: dos semanas, un solo producto, papas fritas, con la misma regla del stock disponible. Mide cuatro cosas, cada una con su umbral: la producción cargada en 8 de los 10 días hábiles, los recortados a la mitad o menos contra la semana de base, una diferencia de hasta una décima parte entre la planilla y lo contado, y 4 de cada 5 avisos con fecha estimada cumplidos. Si un día la planilla no está al día, Oficina confirma como siempre y lo anota. Dos semanas con un producto dan una señal, no una demostración: no prueban el efecto en todo el catálogo ni la baja de horas extras. Lo que se pone en juego es acotado: un tope de ${peso(C.inversion_piloto_conservador)}, de los cuales solo ${peso(C.efectivo_piloto_conservador)} salen de la caja, y el resto es tiempo de gente que cobra igual. La decisión es en la semana ${SEM_GO}.`,

  /* 5 */ `[~1 min] Seguir igual equivale a ${peso(NO_ACTUAR)} por mes, unos ${peso(C.costo_no_actuar_anual)} por año. Son dos cosas distintas y conviene no mezclarlas. Lo oscuro es dinero: ${peso(NO_ACTUAR_DINERO)} por mes de horas extras para completar pedidos, la mitad de las ${HE_MES} horas, a ${peso(HORA_EXTRA)} cada una; es lo único que sale de la caja, y la otra mitad responde a falta de capacidad y no la contamos. Lo naranja es tiempo, o capacidad: ${peso(NO_ACTUAR_TIEMPO)} por mes de re-trabajo de los recortados, horas de Oficina y Depósito en horario normal; la empresa las paga igual y no cambian lo que sale de la caja, pero esa gente podría estar haciendo otra cosa. Esta diferencia entre dinero y tiempo la mantenemos en todo el caso de negocio. Abajo, dos cosas que se suman: cada mes que se demora la decisión se pierde el neto mensual del proyecto, entre ${peso(C.neto_mensual_conservador)} y ${peso(C.neto_mensual_esperado)} según el escenario, y queda sin cuantificar el riesgo comercial de que un distribuidor se canse de recibir pedidos incompletos.`,

  /* 6 */ `[~1,5 min] Cuantificamos solo la alternativa elegida. No hay licencia ni equipos nuevos: el módulo está incluido, las horas de Juanjo son las de su servicio contratado con la empresa, sin costo extra, y las PC ya existen; el costo es tiempo del personal. Los dos escenarios cambian solo lo más incierto. En el conservador los recortados bajan de ${REC_HOY} a ${dec(C.recortados_semana_conservador)} por semana (${TXT_FRAC_CON.toLowerCase()}), las horas extras bajan ${pct(RED_HE_CON)} y el efecto tarda ${DEMORA_CON} semanas más. En el esperado se llega a la meta del ${META_COMPLETOS}, con ${dec(C.recortados_semana_esperado)} recortados por semana y ${pct(RED_HE_ESP)} menos de horas extras. Los colores son los de la lámina anterior: naranja es tiempo liberado, horas de Oficina y Depósito que la empresa ya paga; oscuro es dinero, horas extras que dejan de salir. Al beneficio hay que restarle el tiempo interno nuevo, neto de lo que reemplaza: ${peso(C.costo_recurrente_neto_mensual)} por mes. Resultado: ${peso(C.neto_mensual_conservador)} por mes en el conservador y ${peso(C.neto_mensual_esperado)} en el esperado; en caja, ${peso(C.neto_mensual_caja_conservador)} y ${peso(C.neto_mensual_caja_esperado)}. El pedido de aprobación sale del conservador. No sumamos el margen de los recortados porque la venta no se pierde, se manda después.`,

  /* 7 */ `[~1,5 min] El gráfico muestra el saldo acumulado mes a mes. Los primeros 12 meses salen de la planilla; los seis siguientes siguen con el neto mensual pleno de cada escenario. El esperado toca fondo en ${C.meses[iMaxEsp]}, con ${hablado(C.max_expuesto_esperado)} puestos, y se recupera en el ${recTxt(C.recupero_meses_esperado)}, ${C.recupero_mes_nombre_esperado}. El conservador es el que importa para decidir: el máximo expuesto es de ${hablado(C.max_expuesto_conservador)}, en ${C.meses[iMaxCon]}, y se recupera en el ${recTxt(C.recupero_meses_conservador)}, ${C.recupero_mes_nombre_conservador}. Dicho de otro modo, en el conservador el primer año cierra en ${peso(C.flujo_anio1_conservador)} y el proyecto conviene pero tarda en devolver lo invertido. Con una tasa del ${TASA} real anual, el VAN a 3 años es de ${hablado(C.van_3a_conservador)} en el conservador y de ${hablado(C.van_3a_esperado)} en el esperado. La línea punteada es solo caja, las horas extras que salen o dejan de salir: lo máximo expuesto es de ${peso(C.max_expuesto_caja_conservador)} y se recupera en el ${recTxt(C.recupero_meses_caja_conservador)}. Los meses 2 a 5 concentran el piloto, los conteos y el doble registro; por eso el máximo expuesto aparece ahí y no antes.`,

  /* 8 */ `[~1,5 min] El primer mes, semana a semana. En la semana 1 la dirección designa por escrito al responsable, a su suplente y al responsable de carga con el suyo, fija los umbrales y el tope, y Oficina vuelve a medir la línea base: cada pedido con su faltante, y se piden a liquidación las horas extras de seis meses. En la semana 2, que incluye Carnaval, se arma la planilla de papas fritas y el tablero, y se le pide por escrito a Buenos Aires Software la versión, el soporte, el plazo, la salida de datos y si hay ambiente de prueba. En la semana 3 hay prueba técnica, capacitación en el puesto con siete casos reales y el conteo inicial el fin de semana. En la semana 4 comienza el piloto. Lo importante es que la semana 1 solo necesita decisiones del dueño y datos que la empresa ya tiene. Las tareas técnicas son las del servicio que Juanjo tiene contratado con la empresa, y cada una tiene un suplente interno, así que nada depende de una sola persona. Para que la semana 1 sea el lunes ${INICIO_LUNES}, la decisión tiene que estar tomada antes del ${LIMITE_DECISION}.`,

  /* 9 */ `[~1,5 min] Hay cinco puntos de decisión. El primero, en la semana ${SEM_GO}, el jueves ${GO_FECHA_A}, es el grande: termina el piloto y se decide activar Discovery con la primera línea, repetir o parar; con el Go se libera el techo del proyecto. Después hay uno al cerrar cada línea y uno a los seis meses. En todos se miran las mismas cuatro medidas: días con la producción cargada, pedidos recortados o demorados contra su base, diferencia entre el conteo y el registro, y fechas estimadas cumplidas. El umbral de los recortados cambia según el punto: en el piloto tienen que quedar en la mitad o menos de la base; para activar cada línea, en ${UMBRAL_RECORTES_LINEA} o menos de la base. Con Go sigue el roadmap; con Ajustar se resuelve lo que falló y se repite, con el calendario corrido, y si al repetir tampoco hay Go, es Pausar; con Pausar no se gasta más y el dueño decide entre revisar la causa o volver al proceso anterior. Los umbrales son hipótesis nuestras que el dueño acuerda o cambia en la semana 1, antes de ver resultados. Decide el dueño. El responsable único es uno de los hijos, a designar por la dirección: tiene que ser alguien de adentro. Juanjo es el líder técnico, con las tareas de su servicio contratado con la empresa y un suplente interno. Una reunión de 20 minutos los lunes, con un tablero de tres columnas y un registro de acuerdos.`,

  /* 10 */ `[~1,5 min] Los riesgos que importan son los de ejecución, no los supuestos que ya probamos en el piloto. El más probable y más grave es el de los datos: que el disponible no coincida con lo que hay; se controla con un conteo inicial por línea, con el visto bueno de Depósito, y manda lo contado. Después, la dependencia de una sola persona para Discovery: Juanjo es quien mejor lo conoce y sus tareas son las de su servicio contratado con la empresa; por eso hay instructivos de una página por tarea, un suplente interno con usuario de administrador propio y un contacto de soporte con nombre. La continuidad, con un solo turno y la planta al límite: responsable de carga con suplente y el tiempo de carga dentro del turno. Y la caja, que se cuida aprobando por tramos. Probabilidad e impacto son una lectura nuestra, una hipótesis que se revisa en cada punto de decisión. El plan B lo declara el responsable el mismo día, sin esperar al dueño, porque volver a confirmar como hoy cuesta lo mismo que no haber empezado y se puede deshacer. Si la decisión es pausar: congelar con una exportación, cerrar las reservas abiertas, contar y seguir como hoy con la hoja de contingencia. Nada se borra.`,

  /* 11 */ `[~1,25 min] Lo nuevo respecto de la Parte 2 en personas: las tareas de Juanjo son las de su servicio contratado con la empresa. Configura, prueba, capacita la primera vez y deja instructivos, con un suplente interno que repite cada tarea técnica; la rutina la sostiene la empresa, con un hijo como responsable. La capacitación es en el puesto, por grupo: Producción una hora de práctica con la producción del día anterior, Oficina dos sesiones con los casos de prueba reales, Depósito una hora con el conteo inicial, y la dirección una hora para leer el tablero y aplicar Go, Ajustar o Pausar. Después capacita el hijo responsable o la encargada de Oficina, para que nada dependa de una sola persona. La adopción se mide con tres indicadores que salen de lo que registra el sistema: días con producción cargada, que hoy es ${DIAS_CARGA_HOY}; pedidos reservados antes de confirmar, una meta a validar con la línea de base; y que los suplentes carguen. Si un valor es bajo, antes de pensar en las personas se revisan la capacitación, la carga de trabajo y las reglas. Frases como «siempre anduvo así» o «la gente no va a cargar» no son obstáculos: dicen qué cuida cada persona.`,

  /* 12 */ `[~1 min] Seis impactos, y empezamos por el más sensible: la baja de horas extras, que para los operarios es ingreso. Esperamos que bajen unas ${redondeo(C.horas_extras_evitadas_horas_conservador)} horas por mes en el conservador y unas ${redondeo(C.horas_extras_evitadas_horas_esperado)} en el esperado. Las medidas: se les avisa antes del piloto cuánto se espera que bajen, baja por línea y no de golpe, solo bajan las que se hacían por pedidos faltantes y las demás se reparten en rotación, y los conteos iniciales de fin de semana, que se pagan como horas extras, se les ofrecen primero. El dato de carga no se usa para evaluar personas ni para decidir quién hace horas extras. Lo segundo es el cambio de tareas: cada tarea nueva reemplaza otra, y el caso de negocio no supone ninguna baja de personal; proponemos que el dueño lo diga al presentar el proyecto. Después, habilidad digital desigual, papel, privacidad de los ${DISTRIBUIDORES} distribuidores y equipos, que no se compran. Dos cosas quedan sin compensar y las decimos: la baja de horas extras en sí, que es el resultado buscado y las medidas solo hacen más gradual, y la energía de las PC, que es marginal. Si la dirección quiere reconocer ese ingreso de otra forma, es una decisión suya y no está en el caso de negocio.`,

  /* 13 */ `[~1,5 min] Las objeciones son las que se escuchan en la empresa, y las respondemos con evidencia propia. «Siempre anduvo así»: es cierto, y anduvo mientras el volumen se podía seguir de memoria; hoy ${REC_HOY} de unos ${PED_SEM} pedidos salen recortados o demorados, y seguir igual equivale a ${peso(NO_ACTUAR)} por mes, de los cuales ${peso(NO_ACTUAR_DINERO)} son dinero y el resto, tiempo. «Lo manejamos a simple vista»: funciona para quien conoce la planta y ese conocimiento no se descarta, pero el stock de producto terminado no se registra y el faltante aparece recién al armar; si a simple vista alcanzaba, el piloto lo va a mostrar. «La gente no va a cargar»: tiene razón en que una planta sin margen no suma tareas sola; por eso la carga reemplaza el control semanal, va dentro del turno, tiene suplente y es condición para el Go. «Con la planta al límite, un cambio puede trabar todo»: el peor caso es chico, el piloto es de dos semanas y se corta cuando la dirección quiera. «Si registramos el stock, pierdo el criterio»: ninguna regla elige qué producir; hoy se decide sin ver los pedidos pendientes. «No sabemos si lo que se gasta se recupera»: en el conservador, ${peso(C.neto_mensual_conservador)} de neto por mes, recupero en ${C.recupero_meses_conservador} meses y VAN a 3 años de ${hablado(C.van_3a_conservador)}; por eso el pedido es acotado.`,

  /* 14 */ `[~1,25 min] La decisión que pedimos es acotada. Primero, el tope: ${peso(C.inversion_piloto_conservador)} para el piloto, las semanas 1 a ${SEM_GO}, de los cuales ${peso(C.efectivo_piloto_conservador)} salen de la caja; si el piloto no da, se vuelve atrás sin haber tocado Discovery. Segundo, el techo: ${peso(C.techo_proyecto_conservador)} para el proyecto completo, las semanas 1 a ${SEM_FIN}, sin restar beneficios, de los cuales ${peso(C.efectivo_proyecto_conservador)} son caja; se libera solo con el Go de la semana ${SEM_GO}. Tercero, el responsable: que la dirección designe a uno de los hijos como responsable único, con Juanjo como líder técnico, con las tareas de su servicio contratado con la empresa, y un suplente interno. Cuarto, la fecha: pedimos la decisión antes del ${LIMITE_DECISION} para comenzar la semana 1 el lunes ${INICIO_LUNES}; el piloto es del ${PILOTO} y la decisión de Go, Ajustar o Pausar, el jueves ${GO_FECHA_A}. Aun en el escenario conservador, que usa la mitad de la mejora, el proyecto deja ${peso(C.neto_mensual_conservador)} por mes, se recupera en ${C.recupero_meses_conservador} meses y el VAN a 3 años es de ${hablado(C.van_3a_conservador)}. Y se puede cortar en cualquier momento: pausar no necesita permiso, avanzar sí. Cerrar con eso, y abrir a las preguntas.`,
];

// ---------------------------------------------------------------- pptx
const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Lepez Joaquin, Geyer Juan Jose, Lopez Juan, Olivares Manuel, Sorato Emiliano";
pres.title = "Dulxelitos - Propuesta final para la dirección";

let numLamina = 0;
function nuevo(bg) {
  numLamina += 1;
  const s = pres.addSlide();
  s.background = { color: bg || CREAM };
  s.addNotes(NOTAS[numLamina - 1]);
  return s;
}

// Rotulo chico sobre el titulo: a que parte del proyecto pertenece la lamina.
function kicker(s, texto, color) {
  s.addText(texto, {
    x: M, y: 0.2, w: CW, h: 0.26, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 11, bold: true, charSpacing: 2.5,
    color: color || ORANGE_TXT, valign: "middle",
  });
}

// Titulo de lamina: 34 pt a 0.5 in, con bajada debajo.
function titulo(s, texto, o) {
  o = o || {};
  s.addText(texto, {
    x: o.x === undefined ? M : o.x, y: 0.5, w: o.w || CW, h: 0.62,
    isTextBox: true, margin: 0,
    fontFace: H, fontSize: 34, bold: true, charSpacing: 1.2,
    color: o.color || DARK, valign: "middle",
  });
}

function bajada(s, texto, color, x, w) {
  s.addText(texto, {
    x: x === undefined ? M : x, y: 1.14, w: w || CW, h: 0.38, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, italic: true,
    color: color || GREY, valign: "middle",
  });
}

function pie(s, color) {
  s.addShape(pres.ShapeType.rect, { x: M, y: 6.97, w: 0.22, h: 0.05, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
  s.addText(String(numLamina).padStart(2, "0") + " / " + TOTAL, {
    x: M + 0.32, y: 6.85, w: 1.2, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 10, bold: true, charSpacing: 1, color: color || GREY, valign: "middle",
  });
  s.addText("Dulxelitos · Gestión Gerencial · UTN FRSR", {
    x: M, y: 6.85, w: W - 2 * M, h: 0.3, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 10, color: color || MUTED, align: "right", valign: "middle",
  });
}

function circulo(s, n, x, y, d, relleno, tinta, pt) {
  s.addShape(pres.ShapeType.ellipse, { x: x, y: y, w: d, h: d, fill: { color: relleno } });
  s.addText(String(n), {
    x: x, y: y, w: d, h: d, isTextBox: true, margin: 0,
    fontFace: H, fontSize: pt || 22, bold: true,
    color: tinta || WHITE, align: "center", valign: "middle",
  });
}

// Tarjeta con acento a la izquierda.
function tarjeta(s, o) {
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h, fill: { color: o.fill }, rectRadius: 0.08,
    line: o.fill === WHITE ? { color: LINE, width: 1 } : undefined,
  });
  if (o.acento) {
    s.addShape(pres.ShapeType.rect, { x: o.x, y: o.y + 0.16, w: 0.06, h: o.h - 0.32, fill: { color: o.acento }, line: { color: o.acento, width: 0 } });
  }
}

// Etiqueta chica con fondo de color (DINERO, TIEMPO...).
function chip(s, texto, x, y, w, fill, tinta, pt) {
  s.addShape(pres.ShapeType.roundRect, { x: x, y: y, w: w, h: 0.26, fill: { color: fill }, rectRadius: 0.13 });
  s.addText(texto, {
    x: x, y: y, w: w, h: 0.26, isTextBox: true, margin: 0,
    fontFace: H, fontSize: pt || 10, bold: true, charSpacing: 1.2, color: tinta || WHITE,
    align: "center", valign: "middle",
  });
}

/* 1 - Portada */
{
  const s = nuevo(DARK);
  s.addText("GESTIÓN GERENCIAL · UTN FRSR", {
    x: M, y: 0.8, w: CW, h: 0.35, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 14, bold: true, charSpacing: 3, color: ORANGE,
  });
  s.addText("DULXELITOS", {
    x: M, y: 2.0, w: CW, h: 1.5, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 88, bold: true, charSpacing: 2, color: CREAM, valign: "middle",
  });
  s.addShape(pres.ShapeType.rect, { x: M + 0.04, y: 3.42, w: 1.1, h: 0.07, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
  s.addText("Trabajo Práctico Final · Parte 3 · Propuesta final para la dirección", {
    x: M, y: 3.6, w: CW, h: 0.45, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 20, color: PALE,
  });
  s.addText("Del problema a la decisión: el proyecto completo", {
    x: M, y: 4.1, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 17, italic: true, color: MUTED,
  });
  s.addText("Lepez Joaquín · Geyer Juan José · Lopez Juan · Olivares Manuel · Sorato Emiliano", {
    x: M, y: 5.85, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 14, color: PALE,
  });
  s.addText("Docentes: Ing. Jeremías Pino · Ing. Martín Noguerol", {
    x: M, y: 6.3, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 14, color: MUTED,
  });
}

/* 2 - El problema (Parte 1) */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 1 · DIAGNÓSTICO");
  titulo(s, "EL PROBLEMA");
  bajada(s, "Dulxelitos acepta pedidos sin saber qué hay y produce sin mirar lo que se pidió");
  const g = 0.3;
  const aw = (CW - 3 * g) / 4;
  const datos = [
    [String(REC_HOY), "de ~" + PED_SEM + " por semana", "pedidos recortados o demorados", RED],
    [PCT_COMPLETOS + " %", "→ " + META_COMPLETOS + " en 6 meses", "pedidos completos y a tiempo", DARK, GREEN],
    [HE_RANGO + " h", "por mes", "horas extras, con un solo turno", ORANGE],
    [DIAS_CARGA_HOY, "→ 100 % de los días", "con la producción cargada", DARK, GREEN],
  ];
  datos.forEach((d, i) => {
    const x = M + i * (aw + g);
    s.addShape(pres.ShapeType.rect, { x: x, y: 1.95, w: aw, h: 0.05, fill: { color: d[3] } });
    s.addText(d[0], {
      x: x, y: 2.1, w: aw, h: 1.0, isTextBox: true, margin: 0,
      fontFace: H, fontSize: i === 2 ? 42 : 54, bold: true, color: d[3], valign: "bottom",
    });
    s.addText(d[1], {
      x: x, y: 3.2, w: aw, h: 0.4, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 17, bold: true, color: d[4] || DARK, valign: "middle",
    });
    s.addText(d[2], {
      x: x, y: 3.65, w: aw, h: 0.65, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, color: GREY, valign: "top",
    });
  });
  s.addShape(pres.ShapeType.roundRect, {
    x: M, y: 4.85, w: CW, h: 1.55, fill: { color: DARK }, rectRadius: 0.1,
  });
  s.addText("LO QUE MOSTRÓ EL RELEVAMIENTO", {
    x: M + 0.4, y: 5.05, w: CW - 0.8, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 13, bold: true, charSpacing: 2, color: ORANGE,
  });
  s.addText("El stock de producto terminado no se registra en ningún lado. Cada pedido recortado le cuesta a Oficina y Depósito alrededor de " + SUP.Retrabajo_h + " hora.", {
    x: M + 0.4, y: 5.4, w: CW - 0.8, h: 0.85, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 21, color: CREAM, valign: "top",
  });
  pie(s);
}

/* 3 - La propuesta y el proceso (Parte 2) */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 2 · PROPUESTA");
  titulo(s, "LA PROPUESTA");
  bajada(s, "Primero se mira qué hay, después se confirma");
  const g = 0.3;
  const cw3 = (CW - 2 * g) / 3;
  const cambios = [
    ["1", "consulta de disponible", "antes de confirmar, en lugar de averiguar dos veces"],
    ["1", "carga del pedido", "en lugar de anotarlo tres veces: chat, papel y lista"],
    ["a diario", "carga de producción", "en lugar de una vez por semana"],
  ];
  cambios.forEach((c, i) => {
    const x = M + i * (cw3 + g);
    const y = 1.7, h = 1.85;
    s.addShape(pres.ShapeType.roundRect, { x: x, y: y, w: cw3, h: h, fill: { color: T_GREEN }, rectRadius: 0.08 });
    s.addShape(pres.ShapeType.rect, { x: x, y: y + 0.16, w: 0.06, h: h - 0.32, fill: { color: GREEN }, line: { color: GREEN, width: 0 } });
    s.addText(c[0], {
      x: x + 0.28, y: y + 0.14, w: cw3 - 0.5, h: 0.75, isTextBox: true, margin: 0,
      fontFace: H, fontSize: i === 2 ? 38 : 46, bold: true, color: GREEN, valign: "middle",
    });
    s.addText(c[1], {
      x: x + 0.28, y: y + 0.92, w: cw3 - 0.5, h: 0.32, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 16, bold: true, color: DARK, valign: "middle",
    });
    s.addText(c[2], {
      x: x + 0.28, y: y + 1.26, w: cw3 - 0.5, h: 0.5, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: GREY, valign: "top",
    });
  });
  // Piloto (A) y destino (B).
  const ay = 3.8, ah = 1.5;
  const aw = (CW - 0.7) / 2;
  const alts = [
    { x: M, fill: T_ORANGE, tinta: ORANGE_TXT, acento: ORANGE, tag: "PRIMERO · A", nombre: "Planilla compartida", txt: "Piloto de 2 semanas con papas fritas. Casi sin costo, sin tocar Discovery." },
    { x: M + aw + 0.7, fill: T_BLUE, tinta: BLUE, acento: BLUE, tag: "DESTINO · B", nombre: "Stock en Discovery", txt: "El módulo ya está en la licencia y no se usa. Se activa por línea de producto." },
  ];
  alts.forEach((a) => {
    s.addShape(pres.ShapeType.roundRect, { x: a.x, y: ay, w: aw, h: ah, fill: { color: a.fill }, rectRadius: 0.08 });
    s.addShape(pres.ShapeType.rect, { x: a.x, y: ay + 0.16, w: 0.06, h: ah - 0.32, fill: { color: a.acento }, line: { color: a.acento, width: 0 } });
    s.addText(a.tag, {
      x: a.x + 0.28, y: ay + 0.18, w: aw - 0.5, h: 0.28, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.8, color: a.tinta, valign: "middle",
    });
    s.addText(a.nombre, {
      x: a.x + 0.28, y: ay + 0.5, w: aw - 0.5, h: 0.4, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 20, bold: true, color: DARK, valign: "middle",
    });
    s.addText(a.txt, {
      x: a.x + 0.28, y: ay + 0.92, w: aw - 0.5, h: 0.5, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: DARK, valign: "top",
    });
  });
  s.addText("→", {
    x: M + aw, y: ay, w: 0.7, h: ah, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 34, bold: true, color: GREY, align: "center", valign: "middle",
  });
  // La regla.
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.55, w: CW, h: 1.1, fill: { color: DARK }, rectRadius: 0.1 });
  s.addText("LA REGLA, IGUAL EN LA PLANILLA Y EN DISCOVERY", {
    x: M + 0.4, y: 5.68, w: CW - 0.8, h: 0.26, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 2, color: ORANGE, valign: "middle",
  });
  s.addText(
    [
      { text: "stock disponible", options: { bold: true, color: ORANGE } },
      { text: " = stock físico − reservado por pedidos confirmados sin facturar", options: { color: CREAM } },
    ],
    {
      x: M + 0.4, y: 5.98, w: CW - 0.8, h: 0.55, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 22, valign: "middle",
    }
  );
  pie(s);
}

/* 4 - El piloto (Parte 2) */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 2 · PILOTO");
  titulo(s, "EL PILOTO");
  bajada(s, "Dos semanas, solo papas fritas, en una planilla compartida. Si un día no está al día, se confirma como hoy.");
  const g = 0.3;
  const aw = (CW - 3 * g) / 4;
  const ay = 1.75, ah = 2.6;
  const medidas = [
    ["CARGA", "8 de 10", "días hábiles con la producción cargada", "hoy: " + DIAS_CARGA_HOY + " de los días"],
    ["RECORTES", "la mitad", "o menos de pedidos recortados o demorados, contra la línea de base (semanas 1 a 3)", ""],
    ["CONTEO", "10 %", "es la diferencia máxima entre la planilla y lo contado", "tolerancia provisional"],
    ["FECHAS", "4 de 5", "avisos con fecha estimada, cumplidos", "hoy el aviso no trae fecha"],
  ];
  medidas.forEach((m, i) => {
    const x = M + i * (aw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: ay, w: aw, h: ah, fill: { color: WHITE }, rectRadius: 0.08, line: { color: LINE, width: 1 } });
    s.addText(m[0], {
      x: x + 0.25, y: ay + 0.2, w: aw - 0.5, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.8, color: ORANGE_TXT, valign: "middle",
    });
    s.addShape(pres.ShapeType.rect, { x: x, y: ay + 0.16, w: 0.06, h: 0.38, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
    s.addText(m[1], {
      x: x + 0.25, y: ay + 0.55, w: aw - 0.5, h: 0.8, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 36, bold: true, color: DARK, valign: "middle",
    });
    s.addText(m[2], {
      x: x + 0.25, y: ay + 1.4, w: aw - 0.5, h: 0.75, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: DARK, valign: "top",
    });
    if (m[3]) {
      s.addText(m[3], {
        x: x + 0.25, y: ay + 2.12, w: aw - 0.5, h: 0.3, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 12, italic: true, color: GREY, valign: "middle",
      });
    }
  });
  s.addText("LO QUE SE PRUEBA Y LO QUE SE PONE EN JUEGO", {
    x: M, y: 4.62, w: CW, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 1.5, color: GREY, valign: "middle",
  });
  const tw = (CW - 2 * g) / 3;
  const datos = [
    [PILOTO.toUpperCase(), "Semanas " + SEM_PIL_D + " y " + SEM_PIL_H, "Un solo producto y una planilla. Discovery no se toca.", ORANGE_TXT, T_ORANGE],
    ["TOPE " + peso(C.inversion_piloto_conservador), "Semanas 1 a " + SEM_GO, peso(C.efectivo_piloto_conservador) + " salen de la caja; el resto es tiempo del personal.", DARK, T_NEUTRAL],
    ["SEMANA " + SEM_GO, "Decisión del dueño", "Go, Ajustar o Pausar, con los umbrales acordados antes de empezar.", GREEN, T_GREEN],
  ];
  datos.forEach((o, i) => {
    const x = M + i * (tw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: 5.0, w: tw, h: 1.65, fill: { color: o[4] }, rectRadius: 0.08 });
    s.addText(o[0], {
      x: x + 0.28, y: 5.13, w: tw - 0.56, h: 0.35, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 16, bold: true, charSpacing: 0.8, color: o[3], valign: "middle",
    });
    s.addText(o[1], {
      x: x + 0.28, y: 5.5, w: tw - 0.56, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 13, bold: true, color: DARK, valign: "middle",
    });
    s.addText(o[2], {
      x: x + 0.28, y: 5.85, w: tw - 0.56, h: 0.7, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: DARK, valign: "top",
    });
  });
  pie(s);
}

/* 5 - Lo que cuesta seguir igual: dinero y tiempo */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · EL COSTO DE NO ACTUAR");
  titulo(s, "LO QUE CUESTA SEGUIR IGUAL");
  bajada(s, "Por mes, en pesos constantes de noviembre de 2026");
  // Numero grande a la izquierda.
  const lw = 4.9;
  s.addShape(pres.ShapeType.rect, { x: M, y: 1.95, w: lw, h: 0.05, fill: { color: RED } });
  s.addText("SEGUIR IGUAL EQUIVALE A", {
    x: M, y: 2.1, w: lw, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 2, color: GREY, valign: "middle",
  });
  s.addText(peso(NO_ACTUAR), {
    x: M, y: 2.4, w: lw, h: 0.95, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 56, bold: true, color: RED, valign: "bottom",
  });
  s.addText("por mes", {
    x: M, y: 3.4, w: lw, h: 0.4, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 20, bold: true, color: DARK, valign: "middle",
  });
  s.addText(peso(C.costo_no_actuar_anual) + " por año", {
    x: M, y: 3.82, w: lw, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 18, color: GREY, valign: "middle",
  });
  s.addText("De eso, " + peso(NO_ACTUAR_DINERO) + " por mes es dinero que sale de la caja. El resto es tiempo del personal.", {
    x: M, y: 4.3, w: lw, h: 0.62, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, italic: true, color: GREY, valign: "top",
  });
  // Dos barras a la derecha, a escala.
  const bx = M + lw + 0.6, bw = W - M - bx;
  const filas = [
    { y: 1.95, chip: "TIEMPO", fill: ORANGE, tinta: ORANGE_TXT, nombre: "Re-trabajo de los recortados", valor: NO_ACTUAR_TIEMPO,
      sub: REC_HOY + " pedidos por semana, " + SUP.Retrabajo_h + " hora de Oficina y Depósito cada uno, en horario normal" },
    { y: 3.55, chip: "DINERO", fill: DARK, tinta: DARK, nombre: "Horas extras por faltantes", valor: NO_ACTUAR_DINERO,
      sub: "La mitad de las " + HE_MES + " horas por mes, las que completan pedidos, a " + peso(HORA_EXTRA) + " la hora" },
  ];
  filas.forEach((f) => {
    chip(s, f.chip, bx, f.y + 0.02, 1.25, f.fill, WHITE);
    s.addText(f.nombre, {
      x: bx + 1.4, y: f.y, w: bw - 1.4 - 1.7, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 15, bold: true, color: DARK, valign: "middle",
    });
    s.addText(peso(f.valor), {
      x: W - M - 1.7, y: f.y - 0.04, w: 1.7, h: 0.38, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 20, bold: true, color: f.tinta, align: "right", valign: "middle",
    });
    s.addShape(pres.ShapeType.rect, { x: bx, y: f.y + 0.45, w: bw, h: 0.5, fill: { color: T_NEUTRAL }, line: { color: T_NEUTRAL, width: 0 } });
    s.addShape(pres.ShapeType.rect, { x: bx, y: f.y + 0.45, w: bw * f.valor / NO_ACTUAR, h: 0.5, fill: { color: f.fill }, line: { color: f.fill, width: 0 } });
    s.addText(f.sub, {
      x: bx, y: f.y + 1.05, w: bw, h: 0.5, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: GREY, valign: "top",
    });
  });
  // Lo que se suma a cada mes que pasa.
  const by = 5.2, bh = 1.45, bwid = (CW - 0.3) / 2;
  const barras = [
    ["CADA MES QUE SE DEMORA LA DECISIÓN", "se pierde el neto mensual: " + peso(C.neto_mensual_conservador) + " a " + peso(C.neto_mensual_esperado)],
    ["SIN CUANTIFICAR", "el riesgo de que un distribuidor se canse de recibir pedidos incompletos"],
  ];
  barras.forEach((b, i) => {
    const x = M + i * (bwid + 0.3);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: by, w: bwid, h: bh, fill: { color: DARK }, rectRadius: 0.1 });
    s.addText(b[0], {
      x: x + 0.35, y: by + 0.2, w: bwid - 0.7, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 2, color: ORANGE, valign: "middle",
    });
    s.addText(b[1], {
      x: x + 0.35, y: by + 0.55, w: bwid - 0.7, h: 0.78, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 20, color: CREAM, valign: "top",
    });
  });
  pie(s);
}

/* 6 - Caso de negocio: los dos escenarios */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · CASO DE NEGOCIO");
  titulo(s, "DOS ESCENARIOS");
  bajada(s, "Por mes, con las tres líneas en uso, en pesos constantes de noviembre de 2026");
  // Una sola escala para las dos barras, para que se comparen.
  const escala = 5.1 / C.beneficio_mensual_esperado; // pulgadas por peso
  const g = 0.3, cw2 = (CW - g) / 2;
  const esc = [
    { x: M, tag: "CONSERVADOR", color: ORANGE_TXT, acento: ORANGE,
      desc: TXT_FRAC_CON + ", " + pct(RED_HE_CON) + " menos de horas extras y " + DEMORA_CON + " semanas más de demora",
      rec: dec(C.recortados_semana_conservador), he: dec(HE_CON),
      cap: C.retrabajo_evitado_mensual_conservador, caja: C.horas_extras_evitadas_mensual_conservador,
      ben: C.beneficio_mensual_conservador, neto: C.neto_mensual_conservador, netoCaja: C.neto_mensual_caja_conservador },
    { x: M + cw2 + g, tag: "ESPERADO", color: GREEN, acento: GREEN,
      desc: "La meta: " + META_COMPLETOS + " de pedidos completos y " + pct(RED_HE_ESP) + " menos de horas extras",
      rec: dec(C.recortados_semana_esperado), he: dec(HE_ESP),
      cap: C.retrabajo_evitado_mensual_esperado, caja: C.horas_extras_evitadas_mensual_esperado,
      ben: C.beneficio_mensual_esperado, neto: C.neto_mensual_esperado, netoCaja: C.neto_mensual_caja_esperado },
  ];
  esc.forEach((e) => {
    const y0 = 1.65, h = 5.0, x = e.x;
    tarjeta(s, { x: x, y: y0, w: cw2, h: h, fill: WHITE, acento: e.acento });
    s.addText(e.tag, {
      x: x + 0.3, y: y0 + 0.18, w: cw2 - 0.6, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 15, bold: true, charSpacing: 1.5, color: e.color, valign: "middle",
    });
    s.addText(e.desc, {
      x: x + 0.3, y: y0 + 0.5, w: cw2 - 0.6, h: 0.5, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, italic: true, color: GREY, valign: "top",
    });
    // Dos datos de entrada.
    const mw = (cw2 - 0.6 - 0.2) / 2;
    [[REC_HOY + " → " + e.rec, "pedidos recortados por semana"], [HE_MES + " → " + e.he + " h", "horas extras por mes"]].forEach((m, k) => {
      const mx = x + 0.3 + k * (mw + 0.2);
      s.addText(m[0], {
        x: mx, y: y0 + 1.1, w: mw, h: 0.5, isTextBox: true, margin: 0,
        fontFace: H, fontSize: 26, bold: true, color: DARK, valign: "middle",
      });
      s.addText(m[1], {
        x: mx, y: y0 + 1.6, w: mw, h: 0.3, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 12, color: GREY, valign: "top",
      });
    });
    // Beneficio por mes, en dos tramos: tiempo y dinero.
    s.addText("BENEFICIO POR MES", {
      x: x + 0.3, y: y0 + 2.08, w: 3.0, h: 0.26, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 11, bold: true, charSpacing: 1.5, color: GREY, valign: "middle",
    });
    s.addText(peso(e.ben), {
      x: x + cw2 - 0.3 - 2.2, y: y0 + 2.04, w: 2.2, h: 0.32, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 16, bold: true, color: DARK, align: "right", valign: "middle",
    });
    const bx = x + 0.3;
    s.addShape(pres.ShapeType.rect, { x: bx, y: y0 + 2.42, w: e.cap * escala, h: 0.42, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
    s.addShape(pres.ShapeType.rect, { x: bx + e.cap * escala, y: y0 + 2.42, w: e.caja * escala, h: 0.42, fill: { color: DARK }, line: { color: DARK, width: 0 } });
    // Leyenda con los montos.
    const lws = [2.9, cw2 - 0.6 - 2.9];
    [[ORANGE, "Tiempo liberado", e.cap], [DARK, "Dinero (caja)", e.caja]].forEach((l, k) => {
      const lx = bx + (k === 0 ? 0 : lws[0]);
      const lw = lws[k];
      s.addShape(pres.ShapeType.rect, { x: lx, y: y0 + 3.0, w: 0.16, h: 0.16, fill: { color: l[0] }, line: { color: l[0], width: 0 } });
      s.addText([{ text: l[1] + " ", options: {} }, { text: peso(l[2]), options: { bold: true } }], {
        x: lx + 0.26, y: y0 + 2.93, w: lw - 0.3, h: 0.3, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 14, color: DARK, valign: "middle",
      });
    });
    s.addText("menos el tiempo interno nuevo, neto: " + peso(-C.costo_recurrente_neto_mensual), {
      x: bx, y: y0 + 3.35, w: cw2 - 0.6, h: 0.3, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: GREY, valign: "middle",
    });
    // Resultado.
    s.addShape(pres.ShapeType.roundRect, { x: x + 0.3, y: y0 + 3.8, w: cw2 - 0.6, h: 0.95, fill: { color: T_GREEN }, rectRadius: 0.08 });
    s.addText(peso(e.neto), {
      x: x + 0.5, y: y0 + 3.8, w: 2.7, h: 0.95, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 32, bold: true, color: GREEN, valign: "middle",
    });
    s.addText([
      { text: "neto por mes", options: { bold: true, breakLine: true } },
      { text: "de caja: " + peso(e.netoCaja), options: {} },
    ], {
      x: x + 3.3, y: y0 + 3.8, w: cw2 - 3.6, h: 0.95, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: DARK, valign: "middle",
    });
  });
  pie(s);
}

/* 7 - Flujo acumulado, maximo expuesto y recupero */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · CASO DE NEGOCIO");
  titulo(s, "CUÁNTO SE PONE Y CUÁNDO VUELVE");
  bajada(s, "Saldo acumulado por mes, en millones de pesos constantes de noviembre de 2026");
  // 18 meses: los 12 de caso.json y seis mas con el flujo mensual pleno de cada escenario.
  const N = 18;
  const ext = (saldo, mensual) => {
    const v = saldo.slice();
    for (let i = saldo.length; i < N; i++) v.push(v[i - 1] + mensual);
    return v.map((x) => Math.round(x / 1000) / 1000);
  };
  const series = [
    { name: "Esperado", values: ext(C.saldo_acumulado_esperado, C.neto_mensual_esperado) },
    { name: "Conservador", values: ext(C.saldo_acumulado_conservador, C.neto_mensual_conservador) },
    { name: "Conservador, solo caja", values: ext(C.saldo_caja_conservador, C.neto_mensual_caja_conservador) },
  ];
  // Grafico dibujado con formas (un grafico nativo no se ve igual en todos los programas).
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 1.65, w: 7.6, h: 5.05, fill: { color: WHITE }, rectRadius: 0.08, line: { color: LINE, width: 1 } });
  const gx0 = M + 0.95, gx1 = M + 7.35, gy0 = 2.15, gy1 = 5.5;
  const todos = [].concat.apply([], series.map((q) => q.values));
  const rango0 = Math.max.apply(null, todos) - Math.min.apply(null, todos);
  const paso = [1, 2, 3, 5, 10].find((p) => rango0 / p <= 5);
  const vmin = Math.floor(Math.min.apply(null, todos) / paso) * paso;
  const vmax = Math.ceil(Math.max.apply(null, todos) / paso) * paso;
  const X = (i) => gx0 + (i * (gx1 - gx0)) / (N - 1);
  const Y = (v) => gy0 + ((vmax - v) * (gy1 - gy0)) / (vmax - vmin);
  for (let v = vmin; v <= vmax; v += paso) {
    s.addShape(pres.ShapeType.line, { x: gx0, y: Y(v), w: gx1 - gx0, h: 0, line: { color: v === 0 ? GREY : LINE, width: v === 0 ? 1.25 : 0.75 } });
    s.addText(v < 0 ? "−" + Math.abs(v) : String(v), {
      x: gx0 - 0.5, y: Y(v) - 0.14, w: 0.4, h: 0.28, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 12, color: GREY, align: "right", valign: "middle",
    });
  }
  s.addText("millones de $", {
    x: M + 0.2, y: 1.78, w: 2.0, h: 0.26, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 12, italic: true, color: GREY, valign: "middle",
  });
  for (let i = 0; i < N; i++) {
    s.addText(String(i + 1), {
      x: X(i) - 0.15, y: gy1 + 0.08, w: 0.3, h: 0.24, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 11, color: GREY, align: "center", valign: "middle",
    });
  }
  s.addText("mes (1 = " + C.meses[0] + ")", {
    x: gx0, y: gy1 + 0.36, w: gx1 - gx0, h: 0.26, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 12, color: GREY, align: "center", valign: "middle",
  });
  const estilos = [
    { color: GREEN, dash: "solid" },
    { color: ORANGE, dash: "solid" },
    { color: DARK, dash: "dash" },
  ];
  series.forEach((sr, k) => {
    for (let i = 0; i < N - 1; i++) {
      const x1 = X(i), y1 = Y(sr.values[i]), x2 = X(i + 1), y2 = Y(sr.values[i + 1]);
      s.addShape(pres.ShapeType.line, {
        x: x1, y: Math.min(y1, y2), w: x2 - x1, h: Math.abs(y2 - y1), flipV: y2 < y1,
        line: { color: estilos[k].color, width: 3, dashType: estilos[k].dash },
      });
    }
    // Puntos clave: el maximo expuesto y el primer mes con saldo positivo.
    const iMin = sr.values.indexOf(Math.min.apply(null, sr.values));
    const iRec = sr.values.findIndex((v) => v >= 0);
    [iMin, iRec].forEach((i) => {
      if (i < 0) return;
      s.addShape(pres.ShapeType.ellipse, {
        x: X(i) - 0.085, y: Y(sr.values[i]) - 0.085, w: 0.17, h: 0.17,
        fill: { color: estilos[k].color }, line: { color: WHITE, width: 1.5 },
      });
    });
  });
  // Leyenda.
  let lgx = gx0;
  const lgw = [1.5, 1.85, 2.6];
  series.forEach((sr, k) => {
    s.addShape(pres.ShapeType.line, { x: lgx, y: 6.35, w: 0.45, h: 0, line: { color: estilos[k].color, width: 3, dashType: estilos[k].dash } });
    s.addText(sr.name, {
      x: lgx + 0.55, y: 6.2, w: lgw[k] - 0.6, h: 0.3, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: DARK, valign: "middle",
    });
    lgx += lgw[k];
  });
  // Cifras clave de cada escenario.
  const rx = M + 7.9, rw = W - M - rx;
  const bloques = [
    { y: 1.65, tag: "CONSERVADOR", color: ORANGE_TXT, acento: ORANGE,
      maxx: C.max_expuesto_conservador, maxSub: C.meses[iMaxCon] + " (mes " + (iMaxCon + 1) + "). En caja: " + peso(C.max_expuesto_caja_conservador),
      rec: recTxt(C.recupero_meses_conservador), recSub: C.recupero_mes_nombre_conservador + ". En caja: " + recTxt(C.recupero_meses_caja_conservador) },
    { y: 4.25, tag: "ESPERADO", color: GREEN, acento: GREEN,
      maxx: C.max_expuesto_esperado, maxSub: C.meses[iMaxEsp] + " (mes " + (iMaxEsp + 1) + "). En caja: " + peso(C.max_expuesto_caja_esperado),
      rec: recTxt(C.recupero_meses_esperado), recSub: C.recupero_mes_nombre_esperado + ". En caja: " + recTxt(C.recupero_meses_caja_esperado) },
  ];
  bloques.forEach((b) => {
    const h = 2.45;
    tarjeta(s, { x: rx, y: b.y, w: rw, h: h, fill: WHITE, acento: b.acento });
    s.addText(b.tag, {
      x: rx + 0.28, y: b.y + 0.14, w: rw - 0.5, h: 0.28, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 13, bold: true, charSpacing: 1.5, color: b.color, valign: "middle",
    });
    s.addText("Máximo expuesto", {
      x: rx + 0.28, y: b.y + 0.52, w: 1.9, h: 0.38, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: GREY, valign: "middle",
    });
    s.addText(mm(b.maxx), {
      x: rx + 1.95, y: b.y + 0.5, w: rw - 1.95 - 0.2, h: 0.42, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 22, bold: true, color: DARK, align: "right", valign: "middle",
    });
    s.addText(b.maxSub, {
      x: rx + 0.28, y: b.y + 0.94, w: rw - 0.5, h: 0.45, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 12, color: GREY, valign: "top",
    });
    s.addText("Recupero", {
      x: rx + 0.28, y: b.y + 1.42, w: 1.9, h: 0.38, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: GREY, valign: "middle",
    });
    s.addText(b.rec, {
      x: rx + 1.95, y: b.y + 1.4, w: rw - 1.95 - 0.2, h: 0.42, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 22, bold: true, color: DARK, align: "right", valign: "middle",
    });
    s.addText(b.recSub, {
      x: rx + 0.28, y: b.y + 1.84, w: rw - 0.5, h: 0.45, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 12, color: GREY, valign: "top",
    });
  });
  pie(s);
}

/* 8 - Primeros 30 dias */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · PLAN");
  titulo(s, "LOS PRIMEROS 30 DÍAS");
  bajada(s, "Si la dirección decide antes del " + LIMITE_DECISION + ", la semana 1 comienza el lunes " + INICIO_LUNES);
  const g = 0.25;
  const aw = (CW - 3 * g) / 4;
  const ay = 1.7, ah = 4.1;
  const sems = [
    { n: "1", fechas: semana(1), resp: "Dueño",
      items: ["Designar por escrito al responsable y a los suplentes", "Fijar umbrales y tope", "Volver a medir la línea base"] },
    { n: "2", fechas: semana(2), resp: "Juanjo y suplente",
      items: ["Armar la planilla de papas fritas y el tablero", "Consultar por escrito a Buenos Aires Software"] },
    { n: "3", fechas: semana(3), resp: "Juanjo y suplente, Depósito",
      items: ["Prueba técnica del módulo", "Capacitación con 7 casos de prueba reales", "Conteo inicial el " + fd(3, 5).getUTCDate() + " y " + fd(3, 6).getUTCDate()] },
    { n: "4", fechas: semana(SEM_PIL_D), resp: "Producción y Oficina", dest: true,
      items: ["Comienza el piloto", "Carga al cierre del turno", "Reunión diaria de 10 minutos"] },
  ];
  sems.forEach((w, i) => {
    const x = M + i * (aw + g);
    const fill = w.dest ? DARK : WHITE;
    const tinta = w.dest ? CREAM : DARK;
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: ay, w: aw, h: ah, fill: { color: fill }, rectRadius: 0.08,
      line: w.dest ? undefined : { color: LINE, width: 1 },
    });
    circulo(s, w.n, x + 0.25, ay + 0.25, 0.6, w.dest ? ORANGE : DARK, w.dest ? DARK : CREAM, 22);
    s.addText("SEMANA " + w.n, {
      x: x + 1.0, y: ay + 0.25, w: aw - 1.2, h: 0.28, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.8, color: w.dest ? ORANGE : ORANGE_TXT, valign: "middle",
    });
    s.addText(w.fechas, {
      x: x + 1.0, y: ay + 0.53, w: aw - 1.2, h: 0.32, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 16, bold: true, color: tinta, valign: "middle",
    });
    s.addText(
      w.items.map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < w.items.length - 1 } })),
      {
        x: x + 0.25, y: ay + 1.15, w: aw - 0.5, h: 1.95, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 15, color: tinta, paraSpaceAfter: 8, valign: "top",
      }
    );
    s.addShape(pres.ShapeType.rect, { x: x + 0.25, y: ay + ah - 0.95, w: aw - 0.5, h: 0.015, fill: { color: w.dest ? GREY : LINE }, line: { color: w.dest ? GREY : LINE, width: 0 } });
    s.addText("RESPONSABLE", {
      x: x + 0.25, y: ay + ah - 0.85, w: aw - 0.5, h: 0.24, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 10, bold: true, charSpacing: 1.5, color: w.dest ? PALE : GREY, valign: "middle",
    });
    s.addText(w.resp, {
      x: x + 0.25, y: ay + ah - 0.58, w: aw - 0.5, h: 0.45, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, bold: true, color: tinta, valign: "top",
    });
  });
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.95, w: CW, h: 0.75, fill: { color: T_GREEN }, rectRadius: 0.08 });
  s.addText("La semana 1 solo necesita decisiones del dueño y datos que la empresa ya tiene. Las tareas técnicas son las del servicio que Juanjo tiene contratado con la empresa, con suplente interno.", {
    x: M + 0.3, y: 5.95, w: CW - 0.6, h: 0.75, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 16, bold: true, color: GREEN, valign: "middle",
  });
  pie(s);
}

/* 9 - Gobierno y puntos de decision */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · GOBIERNO");
  titulo(s, "QUIÉN DECIDE Y CUÁNDO");
  bajada(s, "Cinco puntos de decisión en 6 meses, cada uno con fecha, indicador y valores acordados antes de ver resultados");
  // Linea de tiempo con los cinco puntos.
  const pts = [
    [SEM_GO, 3, "Fin del piloto: activar Salados, repetir o parar"],
    [SUP.Sal_hasta, 4, "Salados: pasar a la segunda línea"],
    [SUP.Dul_hasta, 4, "Segunda línea: pasar a la tercera"],
    [SUP.Rep_hasta, 4, "Tercera línea: pasar a la estabilización"],
    [SEM_FIN, 4, "Cierre a los 6 meses: seguir, revisar metas o frenar"],
  ];
  const paso = (CW - 2.4) / 4;
  const cy = 2.0, d = 0.62;
  s.addShape(pres.ShapeType.rect, { x: M + 1.2, y: cy + d / 2 - 0.02, w: paso * 4, h: 0.04, fill: { color: PALE }, line: { color: PALE, width: 0 } });
  pts.forEach((p, i) => {
    const c = M + 1.2 + i * paso;
    circulo(s, "S" + p[0], c - d / 2, cy, d, i === 0 ? ORANGE : DARK, i === 0 ? DARK : CREAM, 14);
    s.addText(DIA[p[1]] + " " + dm(fd(p[0], p[1])), {
      x: c - 1.15, y: cy + d + 0.1, w: 2.3, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 14, bold: true, color: i === 0 ? ORANGE_TXT : DARK, align: "center", valign: "middle",
    });
    s.addText(p[2], {
      x: c - 1.1, y: cy + d + 0.42, w: 2.2, h: 0.75, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: GREY, align: "center", valign: "top",
    });
  });
  // Go, Ajustar, Pausar.
  s.addText("EN CADA PUNTO: CARGA DIARIA, RECORTES, EXACTITUD DEL CONTEO Y FECHAS CUMPLIDAS", {
    x: M, y: 3.78, w: CW, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 1.5, color: GREY, valign: "middle",
  });
  const g = 0.3, tw = (CW - 2 * g) / 3;
  const salidas = [
    ["GO", GREEN, T_GREEN, "Recortes en " + UMBRAL_RECORTES_LINEA + " o menos de la base por línea (la mitad en el piloto). En el punto 1 se libera el techo."],
    ["AJUSTAR", ORANGE_TXT, T_ORANGE, "Se resuelve lo que falló y se repite 2 semanas, con el calendario corrido."],
    ["PAUSAR", RED, T_RED, "No se avanza ni se gasta más. El dueño decide si revisa la causa o vuelve al proceso anterior."],
  ];
  salidas.forEach((o, i) => {
    const x = M + i * (tw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: 4.12, w: tw, h: 1.5, fill: { color: o[2] }, rectRadius: 0.08 });
    s.addText(o[0], {
      x: x + 0.28, y: 4.22, w: tw - 0.56, h: 0.32, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 15, bold: true, charSpacing: 0.8, color: o[1], valign: "middle",
    });
    s.addText(o[3], {
      x: x + 0.28, y: 4.58, w: tw - 0.56, h: 1.0, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: DARK, valign: "top",
    });
  });
  // Franja de roles.
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.82, w: CW, h: 0.88, fill: { color: DARK }, rectRadius: 0.1 });
  const roles = [
    ["DECIDE", "El dueño"],
    ["RESPONSABLE ÚNICO", "Uno de los hijos"],
    ["LÍDER TÉCNICO", "Juanjo, con suplente interno"],
    ["SEGUIMIENTO", "Lunes, 20 minutos"],
  ];
  const rw = (CW - 0.6) / 4;
  roles.forEach((r, i) => {
    const x = M + 0.3 + i * rw;
    s.addText(r[0], {
      x: x, y: 5.91, w: rw - 0.1, h: 0.26, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 10, bold: true, charSpacing: 1.8, color: ORANGE, valign: "middle",
    });
    s.addText(r[1], {
      x: x, y: 6.21, w: rw - 0.1, h: 0.4, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, bold: true, color: CREAM, valign: "middle",
    });
  });
  pie(s);
}

/* 10 - Riesgos y plan B */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · RIESGOS");
  titulo(s, "QUÉ PUEDE SALIR MAL");
  bajada(s, "Riesgos de ejecución, ordenados por urgencia, y un plan B que se activa el mismo día");
  const g = 0.25;
  const rw = 7.6, cw2 = (rw - g) / 2;
  const riesgos = [
    { tag: "DATOS", pi: "Prob. alta · Impacto alto", t: "El disponible no coincide con lo que hay", m: "Conteo inicial por línea con el visto bueno de Depósito. Manda lo contado." },
    { tag: "JUANJO", pi: "Prob. media · Impacto alto", t: "Una sola persona conoce Discovery a fondo", m: "Instructivo de 1 página por tarea, suplente interno y soporte con nombre." },
    { tag: "CONTINUIDAD", pi: "Prob. media · Impacto alto", t: "Un solo turno y la planta al límite", m: "Responsable de carga con suplente y la carga dentro del turno." },
    { tag: "CAJA", pi: "Prob. media · Impacto medio", t: "El gasto pasa el tope o el ahorro llega tarde", m: "Aprobación por tramos, contingencia del " + CONT_CON + " y una línea por vez." },
  ];
  riesgos.forEach((r, i) => {
    const x = M + (i % 2) * (cw2 + g);
    const y = 1.7 + Math.floor(i / 2) * 2.35;
    const h = 2.2;
    tarjeta(s, { x: x, y: y, w: cw2, h: h, fill: WHITE, acento: ORANGE });
    s.addText(r.tag, {
      x: x + 0.28, y: y + 0.16, w: cw2 - 0.5, h: 0.28, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 13, bold: true, charSpacing: 1.8, color: ORANGE_TXT, valign: "middle",
    });
    s.addText(r.pi, {
      x: x + 0.28, y: y + 0.45, w: cw2 - 0.5, h: 0.24, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 11, italic: true, color: GREY, valign: "middle",
    });
    s.addText(r.t, {
      x: x + 0.28, y: y + 0.78, w: cw2 - 0.5, h: 0.62, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 15, bold: true, color: DARK, valign: "top",
    });
    s.addText(r.m, {
      x: x + 0.28, y: y + 1.42, w: cw2 - 0.5, h: 0.7, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: DARK, valign: "top",
    });
  });
  s.addText("También en el registro: el soporte de Buenos Aires Software, los accesos y el respaldo de datos.", {
    x: M, y: 6.4, w: rw, h: 0.3, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 12, italic: true, color: GREY, valign: "middle",
  });
  // Plan B a la derecha.
  const px = M + rw + 0.3, pw = W - M - px, py = 1.7, ph = 5.0;
  s.addShape(pres.ShapeType.roundRect, { x: px, y: py, w: pw, h: ph, fill: { color: DARK }, rectRadius: 0.1 });
  s.addText("PLAN B", {
    x: px + 0.3, y: py + 0.2, w: pw - 0.6, h: 0.32, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 15, bold: true, charSpacing: 2.5, color: ORANGE, valign: "middle",
  });
  s.addText("Volver al proceso anterior sin perder información", {
    x: px + 0.3, y: py + 0.58, w: pw - 0.6, h: 0.6, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, italic: true, color: PALE, valign: "top",
  });
  const pasos = [
    ["Congelar", "exportar stock, reservas y movimientos"],
    ["Cerrar reservas", "facturar o liberar cada una"],
    ["Contar", "ese conteo es el punto de partida"],
    ["Seguir como hoy", "con la hoja de contingencia"],
  ];
  pasos.forEach((p, i) => {
    const y = py + 1.3 + i * 0.7;
    circulo(s, String(i + 1), px + 0.3, y + 0.03, 0.42, ORANGE, DARK, 14);
    s.addText([
      { text: p[0] + ": ", options: { bold: true, color: CREAM } },
      { text: p[1], options: { color: PALE } },
    ], {
      x: px + 0.85, y: y, w: pw - 1.15, h: 0.5, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, valign: "middle",
    });
  });
  s.addShape(pres.ShapeType.rect, { x: px + 0.3, y: py + ph - 0.95, w: pw - 0.6, h: 0.015, fill: { color: GREY }, line: { color: GREY, width: 0 } });
  s.addText("Nada se borra. Pausar no necesita permiso; avanzar, sí.", {
    x: px + 0.3, y: py + ph - 0.85, w: pw - 0.6, h: 0.7, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 15, bold: true, color: CREAM, valign: "middle",
  });
  pie(s);
}

/* 11 - Personas y adopcion */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · PERSONAS");
  titulo(s, "PERSONAS Y ADOPCIÓN");
  bajada(s, "Cada tarea nueva tiene un titular y un suplente, y los dos se capacitan");
  const g = 0.3;
  const aw = (CW - 3 * g) / 4;
  const ay = 1.7, ah = 2.3;
  const grupos = [
    ["PRODUCCIÓN", "1 h", "Práctica con la producción del día anterior, acompañados en los 2 primeros cierres"],
    ["OFICINA", "2 × 1 h", "Casos de prueba reales y guion para avisar un faltante"],
    ["DEPÓSITO", "1 h", "Conteo de papas fritas el fin de semana previo, acompañado"],
    ["DIRECCIÓN", "1 h", "Leer el tablero en 5 minutos y aplicar Go, Ajustar o Pausar"],
  ];
  grupos.forEach((q, i) => {
    const x = M + i * (aw + g);
    tarjeta(s, { x: x, y: ay, w: aw, h: ah, fill: WHITE, acento: BLUE });
    s.addText(q[0], {
      x: x + 0.28, y: ay + 0.18, w: aw - 0.5, h: 0.28, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.8, color: BLUE, valign: "middle",
    });
    s.addText(q[1], {
      x: x + 0.28, y: ay + 0.5, w: aw - 0.5, h: 0.7, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 38, bold: true, color: DARK, valign: "middle",
    });
    s.addText(q[2], {
      x: x + 0.28, y: ay + 1.25, w: aw - 0.5, h: 0.95, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: GREY, valign: "top",
    });
  });
  s.addText("ADOPCIÓN: SALE DE LO QUE REGISTRA EL SISTEMA, NO SE LE PREGUNTA A NADIE", {
    x: M, y: 4.25, w: CW, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 1.5, color: GREY, valign: "middle",
  });
  const tw = (CW - 2 * g) / 3;
  const ind = [
    ["DÍAS CON PRODUCCIÓN CARGADA", "8 de 10", "hoy, " + DIAS_CARGA_HOY + ". Si no se llega: se mira el motivo de cada día sin carga y se mueve la hora"],
    ["RESERVADOS ANTES DE CONFIRMAR", "8 de 10", "meta a validar con la línea de base. Si no se llega: se revisan los confirmados sin reserva"],
    ["SUPLENTES QUE CARGAN", "los dos", "el del parte y el de la reserva, cada semana. Si no se llega: un día fijo con el titular"],
  ];
  ind.forEach((d, i) => {
    const x = M + i * (tw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: 4.6, w: tw, h: 1.5, fill: { color: T_GREEN }, rectRadius: 0.08 });
    s.addText(d[0], {
      x: x + 0.28, y: 4.7, w: tw - 0.5, h: 0.26, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 10, bold: true, charSpacing: 1.2, color: GREEN, valign: "middle",
    });
    s.addText(d[1], {
      x: x + 0.28, y: 4.98, w: tw - 0.5, h: 0.5, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 28, bold: true, color: GREEN, valign: "middle",
    });
    s.addText(d[2], {
      x: x + 0.28, y: 5.5, w: tw - 0.5, h: 0.55, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 12, color: DARK, valign: "top",
    });
  });
  s.addText("Antes de atribuir un valor bajo a las personas se revisan la capacitación, la carga de trabajo y las reglas. El dato sirve para planificar, no para evaluar.", {
    x: M, y: 6.25, w: CW, h: 0.45, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 14, italic: true, color: GREY, valign: "middle",
  });
  pie(s);
}

/* 12 - Impactos responsables */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · IMPACTOS");
  titulo(s, "IMPACTOS RESPONSABLES");
  bajada(s, "Empezamos por el más sensible: las horas extras son ingreso de los operarios");
  const g = 0.25;
  const aw = (CW - 2 * g) / 3;
  const ah = 2.45;
  const imp = [
    { tag: "HORAS EXTRAS", big: "−" + redondeo(C.horas_extras_evitadas_horas_conservador) + " a −" + redondeo(C.horas_extras_evitadas_horas_esperado) + " h", sub: "por mes (estimación)", m: "Se avisa antes y baja por línea. Los conteos de fin de semana se les ofrecen primero.", dest: true },
    { tag: "CAMBIO DE TAREAS", big: "una sale, una entra", sub: "", m: "La carga diaria reemplaza el control semanal. El caso no supone ninguna baja de personal.", chico: true },
    { tag: "HABILIDAD DIGITAL", big: "en el puesto", sub: "", m: "Capacitación con pedidos reales. Quien tenga dificultad entrega el parte en papel, sin que cuente como error.", chico: true },
    { tag: "PAPEL", big: "nada se tira antes", sub: "", m: "Se revisa qué se anota además del pedido y se pasa a un campo de observaciones antes del corte.", chico: true },
    { tag: "PRIVACIDAD", big: String(DISTRIBUIDORES), sub: "distribuidores", m: "La planilla del piloto no lleva datos fiscales ni de contacto. Cada rol ve lo que necesita." },
    { tag: "ENERGÍA Y EQUIPOS", big: peso(C.supuestos.Costo_equipos), sub: "en equipos", m: "Se usan las PC que ya están en Producción y Depósito. Si una falla, se repara antes de comprar." },
  ];
  imp.forEach((q, i) => {
    const x = M + (i % 3) * (aw + g);
    const y = 1.7 + Math.floor(i / 3) * (ah + 0.2);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: y, w: aw, h: ah, fill: { color: q.dest ? T_ORANGE : WHITE }, rectRadius: 0.08,
      line: q.dest ? undefined : { color: LINE, width: 1 },
    });
    s.addShape(pres.ShapeType.rect, { x: x, y: y + 0.16, w: 0.06, h: ah - 0.32, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
    s.addText(q.tag, {
      x: x + 0.28, y: y + 0.17, w: aw - 0.5, h: 0.28, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.8, color: ORANGE_TXT, valign: "middle",
    });
    s.addText(q.big, {
      x: x + 0.28, y: y + 0.5, w: aw - 0.5, h: 0.62, isTextBox: true, margin: 0,
      fontFace: H, fontSize: q.chico ? 22 : 34, bold: true, color: DARK, valign: "middle",
    });
    if (q.sub) {
      s.addText(q.sub, {
        x: x + 0.28, y: y + 1.1, w: aw - 0.5, h: 0.28, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 13, italic: true, color: GREY, valign: "middle",
      });
    }
    s.addText(q.m, {
      x: x + 0.28, y: y + 1.42, w: aw - 0.5, h: 0.95, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: DARK, valign: "top",
    });
  });
  pie(s);
}

/* 13 - Objeciones de la direccion */
{
  const s = nuevo(CREAM);
  kicker(s, "PARTE 3 · CONVERSACIÓN CON LA DIRECCIÓN");
  titulo(s, "LO QUE PUEDE PREGUNTAR LA DIRECCIÓN");
  bajada(s, "Todas parten de algo cierto: cada respuesta empieza por reconocerlo");
  const g = 0.25;
  const aw = (CW - 2 * g) / 3;
  const ah = 2.4;
  const obj = [
    ["«Siempre anduvo así»", "Y anduvo. Hoy " + REC_HOY + " de ~" + PED_SEM + " pedidos salen recortados o demorados. Seguir igual equivale a " + peso(NO_ACTUAR) + " por mes, " + peso(NO_ACTUAR_DINERO) + " de ellos en dinero."],
    ["«Lo manejamos a simple vista»", "Funciona para quien conoce la planta, pero el stock no se registra. El piloto lo muestra: 2 semanas, un producto."],
    ["«La gente no va a cargar»", "Es el riesgo principal. La carga reemplaza el control semanal, va dentro del turno y se mide: 8 de 10 días o no se sigue."],
    ["«Con la planta al límite, un cambio puede trabar todo»", "El peor caso es chico: 2 semanas, se corta cuando se quiera, tope de " + peso(C.inversion_piloto_conservador) + "."],
    ["«Si registramos el stock, pierdo el criterio»", "Sigue decidiendo quien conoce la planta, pero ahora ve los pedidos pendientes."],
    ["«No sabemos si lo que se gasta se recupera»", "Conservador: " + peso(C.neto_mensual_conservador) + " de neto por mes, recupero en " + C.recupero_meses_conservador + " meses y VAN a 3 años de " + mm(C.van_3a_conservador) + "."],
  ];
  obj.forEach((o, i) => {
    const x = M + (i % 3) * (aw + g);
    const y = 1.65 + Math.floor(i / 3) * (ah + 0.2);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: y, w: aw, h: ah, fill: { color: WHITE }, rectRadius: 0.08, line: { color: LINE, width: 1 } });
    s.addShape(pres.ShapeType.rect, { x: x, y: y + 0.16, w: 0.06, h: ah - 0.32, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
    s.addText(o[0], {
      x: x + 0.28, y: y + 0.2, w: aw - 0.5, h: 0.75, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 16, bold: true, color: DARK, valign: "top",
    });
    s.addShape(pres.ShapeType.rect, { x: x + 0.28, y: y + 1.0, w: 0.5, h: 0.04, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
    s.addText(o[1], {
      x: x + 0.28, y: y + 1.12, w: aw - 0.5, h: 1.2, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, color: DARK, valign: "top",
    });
  });
  pie(s);
}

/* 14 - Cierre: la decision que se pide */
{
  const s = nuevo(DARK);
  kicker(s, "LA DECISIÓN", ORANGE);
  titulo(s, "LO QUE LE PEDIMOS A LA DIRECCIÓN", { color: CREAM });
  s.addText("Aprobar el piloto de 2 semanas con papas fritas, con estos cuatro compromisos", {
    x: M, y: 1.14, w: CW, h: 0.38, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 17, italic: true, color: PALE, valign: "middle",
  });
  const g = 0.25;
  const aw = (CW - 3 * g) / 4;
  const ay = 1.85, ah = 3.0;
  const dec4 = [
    ["TOPE", peso(C.inversion_piloto_conservador), 32, "del piloto, semanas 1 a " + SEM_GO + ". De eso, " + peso(C.efectivo_piloto_conservador) + " salen de la caja."],
    ["TECHO", peso(C.techo_proyecto_conservador), 32, "del proyecto completo, semanas 1 a " + SEM_FIN + ". Solo se libera con el Go del piloto."],
    ["RESPONSABLE", "Uno de los hijos", 26, "designado por la dirección. Juanjo, líder técnico, con suplente interno."],
    ["FECHA", "Antes del " + LIMITE_DECISION, 26, "para comenzar el " + dma(fd(1, 0)) + ". Piloto del " + PILOTO + "; Go, Ajustar o Pausar el " + GO_FECHA + "."],
  ];
  dec4.forEach((d, i) => {
    const x = M + i * (aw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: ay, w: aw, h: ah, fill: { color: "22353F" }, rectRadius: 0.1 });
    s.addShape(pres.ShapeType.rect, { x: x, y: ay + 0.2, w: 0.06, h: 0.4, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
    s.addText(d[0], {
      x: x + 0.28, y: ay + 0.22, w: aw - 0.5, h: 0.36, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 14, bold: true, charSpacing: 2.5, color: ORANGE, valign: "middle",
    });
    s.addText(d[1], {
      x: x + 0.28, y: ay + 0.75, w: aw - 0.4, h: 0.95, isTextBox: true, margin: 0,
      fontFace: H, fontSize: d[2], bold: true, color: CREAM, valign: "middle",
    });
    s.addText(d[3], {
      x: x + 0.28, y: ay + 1.85, w: aw - 0.5, h: 1.05, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: PALE, valign: "top",
    });
  });
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.1, w: CW, h: 1.55, fill: { color: GREEN }, rectRadius: 0.1 });
  s.addText("AUN EN EL ESCENARIO CONSERVADOR", {
    x: M + 0.4, y: 5.3, w: CW - 0.8, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 2, color: CREAM, valign: "middle",
  });
  s.addText(peso(C.neto_mensual_conservador) + " de neto por mes, se recupera en " + C.recupero_meses_conservador + " meses y el VAN a 3 años es de " + mm(C.van_3a_conservador) + ". Se puede cortar en cualquier momento.", {
    x: M + 0.4, y: 5.68, w: CW - 0.8, h: 0.8, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 21, bold: true, color: WHITE, valign: "top",
  });
  pie(s, MUTED);
}

if (numLamina !== TOTAL) throw new Error("TOTAL (" + TOTAL + ") no coincide con las laminas (" + numLamina + ")");
pres.writeFile({ fileName: process.argv[2] || "Dulxelitos-Parte3.pptx" }).then((f) => console.log("listo:", f));
