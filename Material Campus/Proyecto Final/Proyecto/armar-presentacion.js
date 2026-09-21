// Presentacion Dulxelitos. Mismas nueve laminas que el deck del artifact.
const pptxgen = require("pptxgenjs");

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

const T_NEUTRAL = "EFEADC";
const T_GREEN = "DCEAE3";
const T_RED = "F3DFD9";
const T_BLUE = "DDE8EF";
const T_ORANGE = "F6EBD8";

const H = "Arial";
const B = "Calibri";

const W = 13.3;
const M = 0.65;
const CW = W - 2 * M; // 12.0

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Lepez Joaquin, Geyer Juan Jose, Lopez Juan, Sorato Emiliano";
pres.title = "Dulxelitos - Diagnostico gerencial";

function nuevo(bg) {
  const s = pres.addSlide();
  s.background = { color: bg || CREAM };
  return s;
}

function titulo(s, texto, color) {
  s.addText(texto, {
    x: M, y: 0.5, w: CW, h: 0.62,
    isTextBox: true, margin: 0,
    fontFace: H, fontSize: 34, bold: true, charSpacing: 1.2,
    color: color || DARK, valign: "middle",
  });
}

function bajada(s, texto, color) {
  s.addText(texto, {
    x: M, y: 1.14, w: CW, h: 0.38,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, italic: true,
    color: color || GREY, valign: "middle",
  });
}

function pie(s, color) {
  s.addText("Dulxelitos · Gestión Gerencial · UTN FRSR", {
    x: M, y: 6.85, w: CW, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 10,
    color: color || MUTED, align: "right", valign: "middle",
  });
}

// Numero dentro de un circulo: el motivo que se repite en todo el deck.
function circulo(s, n, x, y, d, relleno, tinta) {
  s.addShape(pres.ShapeType.ellipse, { x: x, y: y, w: d, h: d, fill: { color: relleno } });
  s.addText(String(n), {
    x: x, y: y, w: d, h: d, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 22, bold: true,
    color: tinta || WHITE, align: "center", valign: "middle",
  });
}

function tarjeta(s, o) {
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h, fill: { color: o.fill }, rectRadius: 0.08,
  });
  let cy = o.y + 0.26;
  if (o.titulo) {
    s.addText(o.titulo, {
      x: o.x + 0.28, y: cy, w: o.w - 0.56, h: 0.34, isTextBox: true, margin: 0,
      fontFace: H, fontSize: o.tituloPt || 15, bold: true, charSpacing: 0.8,
      color: o.tinta || DARK, valign: "middle",
    });
    cy += 0.44;
  }
  if (o.items) {
    s.addText(
      o.items.map((t, i) => ({
        text: t, options: { bullet: true, breakLine: i < o.items.length - 1 },
      })),
      {
        x: o.x + 0.28, y: cy, w: o.w - 0.56, h: o.y + o.h - cy - 0.2,
        isTextBox: true, margin: 0,
        fontFace: B, fontSize: o.pt || 14, color: o.cuerpo || DARK,
        paraSpaceAfter: 6, valign: "top",
      }
    );
  }
  if (o.texto) {
    s.addText(o.texto, {
      x: o.x + 0.28, y: cy, w: o.w - 0.56, h: o.y + o.h - cy - 0.2,
      isTextBox: true, margin: 0,
      fontFace: B, fontSize: o.pt || 14, color: o.cuerpo || DARK, valign: "top",
    });
  }
}

function dato(s, x, y, w, numero, etiqueta, tintaNum) {
  s.addText(numero, {
    x: x, y: y, w: w, h: 0.8, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 46, bold: true, color: tintaNum || DARK, valign: "bottom",
  });
  s.addText(etiqueta, {
    x: x, y: y + 0.83, w: w, h: 0.55, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 13, color: GREY, valign: "top",
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
    x: M, y: 1.9, w: CW, h: 1.5, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 88, bold: true, charSpacing: 2, color: CREAM, valign: "middle",
  });
  s.addText("Diagnóstico gerencial de una PyME de San Rafael", {
    x: M, y: 3.5, w: CW, h: 0.5, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 24, color: PALE,
  });
  s.addText("Trabajo Práctico Final · Parte 1 · Modelo de negocio actual", {
    x: M, y: 4.05, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, color: MUTED,
  });
  s.addText("Lepez Joaquín · Geyer Juan José · Lopez Juan · Sorato Emiliano", {
    x: M, y: 6.3, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 14, color: MUTED,
  });
  s.addNotes("Presentamos el diagnóstico de Dulxelitos, una fábrica de snacks de San Rafael. Aclarar de entrada que esta primera parte es solo diagnóstico: todavía no proponemos solución.");
}

/* 2 - La empresa */
{
  const s = nuevo(CREAM);
  titulo(s, "LA EMPRESA");
  bajada(s, "Fabricación, fraccionamiento y distribución de snacks · San Rafael, Mendoza · desde 1973");
  const anchoD = (CW - 2 * 0.5) / 3;
  const f1 = [
    ["1973", "53 años fabricando snacks", ORANGE],
    ["15-20", "personas, empresa familiar", ORANGE],
    ["1", "predio: fábrica, depósito y oficina", ORANGE],
  ];
  const f2 = [
    ["3", "líneas: salados, dulces, repostería", DARK],
    ["+25", "presentaciones, de 20 g a 2 Kg", DARK],
    ["RNE", "y RNPA: barrera frente a informales", DARK],
  ];
  f1.forEach((d, i) => dato(s, M + i * (anchoD + 0.5), 1.8, anchoD, d[0], d[1], d[2]));
  f2.forEach((d, i) => dato(s, M + i * (anchoD + 0.5), 3.5, anchoD, d[0], d[1], d[2]));
  tarjeta(s, {
    x: M, y: 5.2, w: CW, h: 1.35, fill: T_NEUTRAL, tinta: DARK,
    texto: "Fabrica sus líneas propias y además fracciona y envasa producto de terceros con su marca. Ese fraccionamiento es una línea de negocio declarada, no un agregado: le permite ofrecer un portafolio amplio sin agrandar la planta.",
    pt: 16,
  });
  pie(s);
  s.addNotes("Empresa familiar, 53 años en el mismo rubro. Fábrica, depósito y oficina están los tres en Av. Pedro Vargas 2400.");
}

/* 3 - A quien le vende */
{
  const s = nuevo(DARK);
  titulo(s, "LE VENDE AL CANAL", CREAM);
  bajada(s, "Nunca al consumidor final: el dato que ordena todo el análisis", PALE);
  const anchoC = (CW - 2 * 0.4) / 3;
  const cajas = [
    ["57", "Distribuidores mayoristas", "Exclusividad territorial en 7 provincias", ORANGE],
    ["1", "Cadena de supermercados", "Aiello, de San Luis, con trato directo", "7FB8A6"],
    ["0", "Venta minorista", "Sin local y sin tienda online operativa", MUTED],
  ];
  cajas.forEach((c, i) => {
    const x = M + i * (anchoC + 0.4);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 1.9, w: anchoC, h: 3.1, fill: { color: "22353F" }, rectRadius: 0.1,
    });
    s.addText(c[0], {
      x: x + 0.35, y: 2.15, w: anchoC - 0.7, h: 1.1, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 60, bold: true, color: c[3], valign: "middle",
    });
    s.addText(c[1], {
      x: x + 0.35, y: 3.35, w: anchoC - 0.7, h: 0.75, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 18, bold: true, color: CREAM, valign: "top",
    });
    s.addText(c[2], {
      x: x + 0.35, y: 4.18, w: anchoC - 0.7, h: 0.7, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: PALE, valign: "top",
    });
  });
  s.addText(
    [
      { text: "La Patagonia concentra el 61% de la red", options: { bold: true, color: ORANGE } },
      { text: ": 35 de 57. Mendoza, la provincia de origen, apenas el 10%.", options: {} },
    ],
    {
      x: M, y: 5.35, w: CW, h: 0.6, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 19, color: CREAM, valign: "middle",
    }
  );
  pie(s, MUTED);
  s.addNotes("No hay segmento minorista: el modelo entero está construido sobre mayoristas y una sola cadena. Y la red está lejos de la fábrica, así que logística, precio y servicio hay que pensarlos con el mapa de la Patagonia, no con el de San Rafael.");
}

/* 4 - Con que la miramos */
{
  const s = nuevo(ORANGE);
  s.addText("CON QUÉ LA MIRAMOS", {
    x: M, y: 0.7, w: CW, h: 0.9, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 46, bold: true, charSpacing: 1.5, color: DARK, valign: "middle",
  });
  s.addText("Tres herramientas de la materia, en este orden", {
    x: M, y: 1.6, w: CW, h: 0.45, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 19, color: DARK,
  });
  const anchoH = (CW - 2 * 0.4) / 3;
  const herr = [
    ["1", "FODA", "Ordena lo interno contra lo externo"],
    ["2", "BUSINESS MODEL CANVAS", "Muestra cómo gana plata hoy"],
    ["3", "MADUREZ DIGITAL", "Mide qué tan preparada está para cambiar"],
  ];
  herr.forEach((h, i) => {
    const x = M + i * (anchoH + 0.4);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.35, w: anchoH, h: 2.55, fill: { color: CREAM }, rectRadius: 0.1,
    });
    circulo(s, h[0], x + 0.35, 2.6, 0.6, DARK);
    s.addText(h[1], {
      x: x + 0.35, y: 3.4, w: anchoH - 0.7, h: 0.8, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 21, bold: true, color: DARK, valign: "top",
    });
    s.addText(h[2], {
      x: x + 0.35, y: 4.2, w: anchoH - 0.7, h: 0.55, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: GREY, valign: "top",
    });
  });
  s.addText("Qué dejamos afuera y por qué: PESTEL completo y FODA cruzado. El primero devolvía casilleros vacíos para una pyme regional de snacks; el segundo deriva iniciativas, y esta entrega es diagnóstico. Cadena de valor y cinco fuerzas las usamos como insumo del FODA, no como lámina aparte.", {
    x: M, y: 5.25, w: CW, h: 1.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, color: DARK, valign: "top",
  });
  s.addNotes("Importante decirlo en voz alta: elegimos herramientas, no las aplicamos todas. El criterio fue aplicar una cuando producía evidencia sobre esta empresa en particular.");
}

/* 5 - FODA */
{
  const s = nuevo(CREAM);
  titulo(s, "FODA");
  bajada(s, "Lo interno contra lo externo");
  const aw = (CW - 0.35) / 2;
  const ah = 2.35;
  tarjeta(s, {
    x: M, y: 1.75, w: aw, h: ah, fill: T_GREEN, tinta: GREEN, titulo: "FORTALEZAS",
    items: ["57 distribuidores construidos en 53 años", "Logística propia más transporte tercerizado", "Habilitaciones RNE y RNPA vigentes", "El canal está conforme: el único reclamo es rotura"],
    pt: 14,
  });
  tarjeta(s, {
    x: M + aw + 0.35, y: 1.75, w: aw, h: ah, fill: T_RED, tinta: RED, titulo: "DEBILIDADES",
    items: ["No conocen el costo real por producto", "Planta saturada, tapada con horas extras", "El saber del negocio está en los dueños", "Sistema sin integrar y sin CRM"],
    pt: 14,
  });
  tarjeta(s, {
    x: M, y: 4.25, w: aw, h: ah, fill: T_BLUE, tinta: BLUE, titulo: "OPORTUNIDADES",
    items: ["El sitio ya está armado como tienda", "Crecer por fraccionamiento sin ampliar planta", "Aiello como modelo de cadena repetible", "El equipo tiene ganas de capacitarse"],
    pt: 14,
  });
  tarjeta(s, {
    x: M + aw + 0.35, y: 4.25, w: aw, h: ah, fill: T_ORANGE, tinta: "8A5714", titulo: "AMENAZAS",
    items: ["Inflación sobre un modelo que compite por precio", "Un solo proveedor de film impreso", "Sin margen de planta si sube la demanda", "Perder un cliente sin llegar a enterarse"],
    pt: 14,
  });
  s.addNotes("Las fortalezas y debilidades salen de mirar la cadena de valor; las oportunidades y amenazas, de los factores del entorno y de las cinco fuerzas. No lo cruzamos a propósito: el cruce deriva iniciativas y esta entrega es diagnóstico.");
}

/* 6 - Business Model Canvas */
{
  const s = nuevo(CREAM);
  const MC = 0.45;
  const CWC = W - 2 * MC;
  s.addText("BUSINESS MODEL CANVAS", {
    x: MC, y: 0.42, w: CWC, h: 0.55, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 30, bold: true, charSpacing: 1.2, color: DARK, valign: "middle",
  });
  s.addText("Estado actual · los nueve bloques", {
    x: MC, y: 0.98, w: CWC, h: 0.32, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 13, italic: true, color: GREY, valign: "middle",
  });
  const g = 0.09;
  const colW = (CWC - 4 * g) / 5;
  const y1 = 1.45, hAlto = 3.6, hFila = (hAlto - g) / 2;
  const y3 = y1 + hAlto + g, h3 = 1.35;
  const col = (i) => MC + i * (colW + g);

  // Sin vinetas: en celdas angostas la sangria hace que todo se parta en dos lineas.
  function mini(x, y, w, h, fill, tit, tinta, lineas, cuerpo, remate, tintaRemate, arriba) {
    s.addShape(pres.ShapeType.roundRect, { x: x, y: y, w: w, h: h, fill: { color: fill }, rectRadius: 0.06 });
    s.addText(tit, {
      x: x + 0.13, y: y + 0.09, w: w - 0.26, h: 0.25, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 10.5, bold: true, charSpacing: 0.5, color: tinta, valign: "middle",
    });
    const filas = lineas.map((t, i) => ({
      text: t, options: { breakLine: i < lineas.length - 1 },
    }));
    if (remate && arriba) {
      filas.unshift({ text: remate, options: { bold: true, color: tintaRemate || tinta, breakLine: true } });
    } else if (remate) {
      filas[filas.length - 1].options.breakLine = true;
      filas.push({ text: remate, options: { bold: true, color: tintaRemate || tinta } });
    }
    s.addText(filas, {
      x: x + 0.13, y: y + 0.36, w: w - 0.26, h: h - 0.46, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 9.5, color: cuerpo || DARK, lineSpacing: 14, valign: "top",
    });
  }

  mini(col(0), y1, colW, hAlto, T_NEUTRAL, "8 · SOCIOS", GREY,
    ["Film impreso: un proveedor", "Materia prima a granel", "Producto terminado a granel", "Los 57 distribuidores", "Transportistas tercerizados", "Aiello Supermercados"]);
  mini(col(1), y1, colW, hFila, T_NEUTRAL, "7 · ACTIVIDADES", GREY,
    ["Producción", "Fraccionamiento y envasado", "Distribución y logística", "Compras", "Administración y cobranza"]);
  mini(col(1), y1 + hFila + g, colW, hFila, T_NEUTRAL, "6 · RECURSOS", GREY,
    ["La red de 57 clientes", "Planta al límite", "Saber en los dueños", "RNE / RNPA", "Marca y flota propia", "Planilla inexacta"]);
  mini(col(2), y1, colW, hAlto, DARK, "2 · PROPUESTA", ORANGE,
    ["Logística como diferencial", "Precio competitivo", "Portafolio en un proveedor", "Formatos de 1 y 2 Kg", "Fraccionamiento de terceros"], PALE,
    "Rentabilidad al que revende", ORANGE, true);
  mini(col(3), y1, colW, hFila, T_NEUTRAL, "4 · RELACIÓN", GREY,
    ["La mantiene la empresa", "Exclusividad territorial", "Horario acotado", "Sin CRM"]);
  mini(col(3), y1 + hFila + g, colW, hFila, T_NEUTRAL, "3 · CANALES", GREY,
    ["Flota, fletes y retiro", "Viajante con zona", "WhatsApp y teléfono", "Redes: marca, no venta", "Sin tienda operativa"]);
  mini(col(4), y1, colW, hAlto, T_NEUTRAL, "1 · SEGMENTOS", GREY,
    ["57 distribuidores mayoristas", "7 provincias, con exclusividad", "Aiello, única cadena, San Luis", "Nunca al consumidor final"], DARK,
    "61% de la red en Patagonia. Mendoza, apenas el 10%.", GREY);
  mini(MC, y3, colW * 3 + 2 * g, h3, T_RED, "9 · ESTRUCTURA DE COSTOS", RED,
    ["Materia prima · packaging y film (+25 formatos) · mano de obra · logística y flete · energía · costo financiero"], DARK,
    "Ningún costo está asignado por producto. Se fija precio sobre una base que se sabe equivocada.", RED);
  mini(col(3), y3, colW * 2 + g, h3, T_GREEN, "5 · FUENTES DE INGRESOS", GREEN,
    ["Venta mayorista · Aiello · producto fraccionado"], DARK,
    "Contado, cuenta corriente a 30 días y cheques diferidos", GREEN);
  s.addNotes("El canvas completo, igual que el póster que entregamos. El bloque oscuro del centro es la clave: le vende rentabilidad al canal. Abajo a la izquierda, en rojo, está el problema de fondo.");
}

/* 7 - Lo que muestra el canvas */
{
  const s = nuevo(CREAM);
  titulo(s, "LO QUE MUESTRA EL CANVAS");
  s.addText("No le vende sabor al consumidor: le vende rentabilidad al canal. Es liderazgo en costos, no diferenciación.", {
    x: M, y: 1.3, w: CW, h: 1.0, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 24, bold: true, color: DARK, valign: "middle", lineSpacing: 32,
  });
  const cw2 = (CW - 2 * 0.35) / 3;
  const cajas = [
    ["COMPITE POR PRECIO", "Y ningún costo está asignado por producto. La única ventaja que declara se apoya en una planilla que la empresa sabe equivocada.", T_RED, RED],
    ["EL MEJOR ACTIVO, SIN SISTEMA", "La red de 57 distribuidores no tiene CRM, no se mide cuánto pesa cada uno y la lista que publican tiene duplicados.", T_NEUTRAL, DARK],
    ["TODO PASA POR LOS DUEÑOS", "Recetas, costos y la relación con cada distribuidor no están escritos en ningún lado ni viven en ningún sistema.", T_NEUTRAL, DARK],
  ];
  cajas.forEach((c, i) => {
    tarjeta(s, {
      x: M + i * (cw2 + 0.35), y: 2.5, w: cw2, h: 2.6,
      fill: c[2], tinta: c[3], titulo: c[0], tituloPt: 13,
      texto: c[1], pt: 15,
    });
  });
  s.addText("Ninguno de los tres se ve desde afuera, porque el canal está conforme.", {
    x: M, y: 5.35, w: CW, h: 0.5, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 17, italic: true, color: GREY, valign: "middle",
  });
  pie(s);
  s.addNotes("Los tres salen directamente del canvas: el bloque de propuesta de valor, el de recursos clave y el de estructura de costos.");
}

/* 8 - Madurez digital */
{
  const s = nuevo(CREAM);
  titulo(s, "MADUREZ DIGITAL");
  bajada(s, "El modelo de la cátedra: 28 preguntas sobre 7 dimensiones, escala de 1 a 5");
  s.addText("1.79", {
    x: M, y: 1.85, w: 3.3, h: 1.5, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 88, bold: true, color: RED, valign: "middle",
  });
  s.addText("Nivel Inicial", {
    x: M, y: 3.4, w: 3.3, h: 0.45, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 22, bold: true, color: DARK,
  });
  s.addText("50 puntos sobre 28 preguntas", {
    x: M, y: 3.88, w: 3.3, h: 0.35, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 13, color: GREY,
  });
  tarjeta(s, {
    x: M, y: 4.45, w: 3.3, h: 2.1, fill: T_RED, tinta: RED,
    texto: "Las dos dimensiones más bajas no son sobre herramientas: son sobre decidir y controlar.",
    pt: 15,
  });
  // Barras dibujadas a mano: un grafico nativo no sobrevive la conversion a
  // imagenes ni la importacion a Prezi.
  const dims = [
    ["Procesos y Operaciones", 2.5, GREEN],
    ["Tecnología y Datos", 2.25, GREEN],
    ["Clientes y Canales", 2.0, GREEN],
    ["Liderazgo y Cultura", 1.5, ORANGE],
    ["Personas y Habilidades", 1.5, ORANGE],
    ["Gobierno", 1.5, RED],
    ["Estrategia", 1.25, RED],
  ];
  const gx = M + 3.85, gy = 1.85, gw = CW - 3.85, gh = 4.3;
  const etiqueta = 2.3, escala = gw - etiqueta - 0.7;
  const paso = gh / dims.length;
  for (let v = 1; v <= 5; v++) {
    const x = gx + etiqueta + (v / 5) * escala;
    s.addShape(pres.ShapeType.line, { x: x, y: gy, w: 0, h: gh, line: { color: "E2DCCC", width: 1 } });
    s.addText(String(v), {
      x: x - 0.2, y: gy + gh + 0.02, w: 0.4, h: 0.25, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 10, color: MUTED, align: "center",
    });
  }
  dims.forEach((d, i) => {
    const y = gy + i * paso;
    s.addText(d[0], {
      x: gx, y: y, w: etiqueta - 0.12, h: paso, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: DARK, align: "right", valign: "middle",
    });
    const largo = (d[1] / 5) * escala;
    s.addShape(pres.ShapeType.rect, {
      x: gx + etiqueta, y: y + paso / 2 - 0.14, w: largo, h: 0.28, fill: { color: d[2] },
    });
    s.addText(d[1].toFixed(2), {
      x: gx + etiqueta + largo + 0.1, y: y, w: 0.65, h: paso, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 13, bold: true, color: DARK, valign: "middle",
    });
  });
  pie(s);
  s.addNotes("Tres dimensiones llegan a Básico: Procesos, Tecnología y Clientes. El piso está en Estrategia y Gobierno. Agregamos Gobierno como séptima dimensión porque el enunciado pide siete y el modelo trae seis. Nivel Inicial no quiere decir mal gestionada: quiere decir que decide sin instrumentos.");
}

/* 9 - Conclusiones */
{
  const s = nuevo(DARK);
  s.addText("LAS CONCLUSIONES", {
    x: M, y: 0.5, w: CW, h: 0.6, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 30, bold: true, charSpacing: 1.2, color: CREAM, valign: "middle",
  });
  s.addText("No está mal gestionada.\nDecide sin instrumentos.", {
    x: M, y: 1.18, w: CW, h: 1.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 32, bold: true, color: ORANGE, valign: "middle", lineSpacing: 38,
  });
  const cw3 = (CW - 2 * 0.35) / 3;
  const puntos = [
    ["1", "Compite por precio sin conocer su costo", "La única ventaja que declara es el precio, y la planilla que lo sostiene la propia empresa la reconoce imprecisa."],
    ["2", "Tapa la planta saturada con horas extras", "La capacidad está al límite y se cubre pagando horas, no resolviendo el cuello de botella."],
    ["3", "Su activo más valioso no tiene sistema detrás", "57 distribuidores construidos en 53 años, sin CRM, sin medición de cartera y con la lista pública duplicada."],
  ];
  puntos.forEach((p, i) => {
    const x = M + i * (cw3 + 0.35);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.55, w: cw3, h: 3.0, fill: { color: "22353F" }, rectRadius: 0.1,
    });
    circulo(s, p[0], x + 0.32, 2.82, 0.6, ORANGE, DARK);
    s.addText(p[1], {
      x: x + 0.32, y: 3.58, w: cw3 - 0.64, h: 0.85, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 17, bold: true, color: CREAM, valign: "top",
    });
    s.addText(p[2], {
      x: x + 0.32, y: 4.42, w: cw3 - 0.64, h: 1.05, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: PALE, valign: "top",
    });
  });
  s.addText("El problema no está en el canal. El canal está conforme. Está puertas adentro.", {
    x: M, y: 5.75, w: CW, h: 0.6, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 19, color: CREAM, valign: "middle",
  });
  pie(s, MUTED);
  s.addNotes("Cerrar acá. Los tres puntos salen de cruzar el FODA, el canvas y la madurez: las tres herramientas apuntan al mismo lado. Con esto queda armado el terreno para el problema gerencial priorizado, que es la parte 2.");
}

pres.writeFile({ fileName: process.argv[2] || "Dulxelitos.pptx" }).then((f) => console.log("listo:", f));
