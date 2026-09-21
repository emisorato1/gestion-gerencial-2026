// Presentacion Dulxelitos - un bloque por diapositiva, para cargar en Prezi.
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
    color: color || DARK, align: "left", valign: "middle",
  });
}

function bajada(s, texto, color) {
  s.addText(texto, {
    x: M, y: 1.14, w: CW, h: 0.38,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, italic: true,
    color: color || GREY, align: "left", valign: "middle",
  });
}

function pie(s, texto, color) {
  s.addText(texto || "Dulxelitos · Gestión Gerencial · UTN FRSR", {
    x: M, y: 6.85, w: CW, h: 0.3,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 10,
    color: color || MUTED, align: "right", valign: "middle",
  });
}

// Numero grande dentro de un circulo: el motivo que se repite en todo el deck.
function circulo(s, n, x, y, d, relleno, tinta) {
  s.addShape(pres.ShapeType.ellipse, {
    x: x, y: y, w: d, h: d, fill: { color: relleno },
  });
  s.addText(String(n), {
    x: x, y: y, w: d, h: d,
    isTextBox: true, margin: 0,
    fontFace: H, fontSize: 22, bold: true,
    color: tinta || WHITE, align: "center", valign: "middle",
  });
}

function tarjeta(s, o) {
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h,
    fill: { color: o.fill }, rectRadius: 0.08,
  });
  let cy = o.y + 0.26;
  if (o.titulo) {
    s.addText(o.titulo, {
      x: o.x + 0.28, y: cy, w: o.w - 0.56, h: 0.34,
      isTextBox: true, margin: 0,
      fontFace: H, fontSize: o.tituloPt || 15, bold: true, charSpacing: 0.8,
      color: o.tinta || DARK, valign: "middle",
    });
    cy += 0.44;
  }
  if (o.items) {
    s.addText(
      o.items.map((t, i) => ({
        text: t,
        options: { bullet: true, breakLine: i < o.items.length - 1 },
      })),
      {
        x: o.x + 0.28, y: cy, w: o.w - 0.56, h: o.y + o.h - cy - 0.2,
        isTextBox: true, margin: 0,
        fontFace: B, fontSize: o.pt || 14, color: o.cuerpo || DARK,
        paraSpaceAfter: 5, valign: "top",
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

function dato(s, x, y, w, numero, etiqueta, tintaNum, tintaTxt) {
  s.addText(numero, {
    x: x, y: y, w: w, h: 0.85,
    isTextBox: true, margin: 0,
    fontFace: H, fontSize: 52, bold: true,
    color: tintaNum || DARK, valign: "bottom",
  });
  s.addText(etiqueta, {
    x: x, y: y + 0.88, w: w, h: 0.55,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 13, color: tintaTxt || GREY, valign: "top",
  });
}

// Una lamina por bloque del canvas: numero, titulo, contenido y remate.
function bloqueCanvas(s, n, nombre, pregunta, items, remate, tinta) {
  circulo(s, n, M, 0.42, 0.82, tinta || DARK);
  s.addText(nombre, {
    x: M + 1.05, y: 0.42, w: CW - 1.05, h: 0.5,
    isTextBox: true, margin: 0,
    fontFace: H, fontSize: 32, bold: true, charSpacing: 1.2,
    color: DARK, valign: "middle",
  });
  s.addText(pregunta, {
    x: M + 1.05, y: 0.94, w: CW - 1.05, h: 0.34,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 14, italic: true, color: GREY, valign: "middle",
  });
  s.addText("Business Model Canvas · bloque " + n + " de 9", {
    x: M, y: 1.42, w: CW, h: 0.28,
    isTextBox: true, margin: 0,
    fontFace: B, fontSize: 11, bold: true, charSpacing: 0.6,
    color: tinta || DARK, valign: "middle",
  });

  const mitad = Math.ceil(items.length / 2);
  const cols = items.length > 4 ? [items.slice(0, mitad), items.slice(mitad)] : [items];
  const anchoCol = cols.length === 2 ? (CW - 0.5) / 2 : CW;
  cols.forEach((grupo, i) => {
    s.addText(
      grupo.map((t, j) => ({
        text: t,
        options: { bullet: true, breakLine: j < grupo.length - 1 },
      })),
      {
        x: M + i * (anchoCol + 0.5), y: 1.85, w: anchoCol, h: 2.8,
        isTextBox: true, margin: 0,
        fontFace: B, fontSize: 17, color: DARK,
        paraSpaceAfter: 9, valign: "top",
      }
    );
  });

  tarjeta(s, {
    x: M, y: 4.8, w: CW, h: 1.55,
    fill: T_NEUTRAL, titulo: "LO QUE MUESTRA", tituloPt: 12, tinta: tinta || DARK,
    texto: remate, pt: 16,
  });
  pie(s);
}

/* 1 — Portada */
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

/* 2 — La empresa */
{
  const s = nuevo(CREAM);
  titulo(s, "LA EMPRESA");
  bajada(s, "Qué hace, dónde y desde cuándo");
  const ancho = (CW - 0.5) / 2;
  s.addText(
    [
      { text: "Fabrica, fracciona y distribuye snacks.", options: { bold: true, breakLine: true } },
      { text: "Empresa familiar de San Rafael, Mendoza, fundada en 1973. Hoy trabaja la segunda generación: el dueño decide lo importante y los hijos llevan la operación del día.", options: { breakLine: true } },
      { text: " ", options: { breakLine: true } },
      { text: "Fábrica, depósito y oficina están en un mismo predio, en Av. Pedro Vargas 2400. Tiene habilitaciones RNE y RNPA, que es lo que le permite mover mercadería entre provincias y entrar a un supermercado.", options: {} },
    ],
    {
      x: M, y: 1.75, w: ancho, h: 3.65, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 17, color: DARK, lineSpacing: 26, valign: "top",
    }
  );
  const bx = M + ancho + 0.5;
  tarjeta(s, {
    x: bx, y: 1.75, w: ancho, h: 1.5, fill: T_ORANGE, tinta: RED,
    titulo: "SALADOS", tituloPt: 13,
    texto: "Papas fritas, palitos de maíz y salados, conitos, cascarones, maní", pt: 15,
  });
  tarjeta(s, {
    x: bx, y: 3.4, w: ancho, h: 1.3, fill: T_GREEN, tinta: GREEN,
    titulo: "DULCES", tituloPt: 13,
    texto: "Maíz inflado tipo tutuca, bolitas crocantes", pt: 15,
  });
  tarjeta(s, {
    x: bx, y: 4.85, w: ancho, h: 1.6, fill: T_BLUE, tinta: BLUE,
    titulo: "REPOSTERÍA", tituloPt: 13,
    texto: "Almidón de maíz, granas, esencia de vainilla: compra a granel y envasa con su marca", pt: 15,
  });
  s.addText("Más de 25 presentaciones, de 20 g a 2 Kg.", {
    x: M, y: 5.6, w: ancho, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 16, bold: true, color: RED,
  });
  pie(s);
  s.addNotes("53 años en el mismo rubro. Lo importante: no sólo fabrica, también fracciona producto de terceros y lo vende con su marca. Eso es una línea de negocio declarada, no un agregado.");
}

/* 3 — Los números */
{
  const s = nuevo(CREAM);
  titulo(s, "LOS NÚMEROS QUE RELEVAMOS");
  bajada(s, "Lo que pudimos verificar entre la página oficial, las redes y el relevamiento adentro de la empresa");
  const anchoD = (CW - 3 * 0.45) / 4;
  const fila = [
    ["1973", "53 años fabricando snacks", DARK],
    ["15-20", "personas en total", DARK],
    ["57", "distribuidores mayoristas", ORANGE],
    ["7", "provincias de cobertura", ORANGE],
  ];
  fila.forEach((d, i) => dato(s, M + i * (anchoD + 0.45), 1.85, anchoD, d[0], d[1], d[2]));
  const fila2 = [
    ["61%", "de la red está en la Patagonia", RED],
    ["3", "líneas de producto", DARK],
    ["+25", "presentaciones distintas", DARK],
    ["1", "sola cadena de supermercados", DARK],
  ];
  fila2.forEach((d, i) => dato(s, M + i * (anchoD + 0.45), 3.65, anchoD, d[0], d[1], d[2]));
  tarjeta(s, {
    x: M, y: 5.15, w: CW, h: 1.5, fill: T_RED, tinta: RED,
    titulo: "EL DATO QUE FALTA", tituloPt: 12,
    texto: "No sabemos cuánto factura cada distribuidor. Lo preguntamos y el dato no existe: la empresa no mide la concentración de su propia cartera. Esa ausencia ya es un hallazgo.",
    pt: 16,
  });
  pie(s);
  s.addNotes("Estos son los números que sostienen todo el análisis. El 61% de la Patagonia es el que más sorprende: la fábrica está en Mendoza y Mendoza es apenas el 10% de la red.");
}

/* 4 — El mapa de la red */
{
  const s = nuevo(CREAM);
  titulo(s, "DÓNDE ESTÁ LA RED");
  bajada(s, "57 distribuidores, y la mayoría lejos de la fábrica");
  const filas = [
    ["Río Negro", "19", "Gral. Roca, Cipolletti, Bariloche, El Bolsón, Villa Regina, Allen y otras"],
    ["Neuquén", "12", "Capital, Plottier, Senillosa, Zapala, Chos Malal, Rincón de los Sauces"],
    ["San Luis", "9", "San Luis, Villa Mercedes"],
    ["Mendoza", "6", "San Rafael, Gral. Alvear, Malargüe"],
    ["Chubut", "4", "Comodoro Rivadavia, Esquel, Puerto Madryn"],
    ["Buenos Aires", "4", "Bahía Blanca, Mar del Plata, Lincoln"],
    ["La Pampa", "3", "Santa Rosa, 25 de Mayo, Gral. Pico"],
  ];
  const cuerpo = filas.map((f) => [
    { text: f[0], options: { fontFace: B, fontSize: 14, bold: true, color: DARK } },
    { text: f[1], options: { fontFace: H, fontSize: 14, bold: true, color: ORANGE, align: "center" } },
    { text: f[2], options: { fontFace: B, fontSize: 12, color: GREY } },
  ]);
  s.addTable(
    [
      [
        { text: "Provincia", options: { fontFace: H, fontSize: 12, bold: true, color: CREAM, fill: { color: DARK } } },
        { text: "Distrib.", options: { fontFace: H, fontSize: 12, bold: true, color: CREAM, align: "center", fill: { color: DARK } } },
        { text: "Localidades", options: { fontFace: H, fontSize: 12, bold: true, color: CREAM, fill: { color: DARK } } },
      ],
      ...cuerpo,
    ],
    {
      x: M, y: 1.8, w: 8.0, colW: [1.75, 0.95, 5.3],
      border: { type: "solid", color: "DDD8C8", pt: 1 },
      fill: { color: WHITE },
      rowH: 0.33,
      valign: "middle",
      margin: 6,
    }
  );
  // La fila de encabezado va oscura.
  tarjeta(s, {
    x: M + 8.4, y: 1.8, w: CW - 8.4, h: 1.7, fill: DARK, tinta: ORANGE,
    titulo: "PATAGONIA", tituloPt: 13, cuerpo: CREAM,
    texto: "35 de 57 distribuidores, el 61% de la red", pt: 16,
  });
  tarjeta(s, {
    x: M + 8.4, y: 3.65, w: CW - 8.4, h: 1.8, fill: T_NEUTRAL, tinta: DARK,
    titulo: "MENDOZA", tituloPt: 13,
    texto: "Donde está la fábrica: 6 distribuidores, apenas el 10%", pt: 16,
  });
  tarjeta(s, {
    x: M, y: 5.65, w: CW, h: 1.0, fill: T_ORANGE, tinta: RED,
    texto: "Cualquier decisión sobre logística, precio o servicio hay que pensarla con este mapa y no con el de San Rafael.",
    pt: 16,
  });
  pie(s);
  s.addNotes("Hay exclusividad territorial: en casi todas las localidades figura uno o dos distribuidores, no varios compitiendo entre sí. Patagonia = Río Negro, Neuquén y Chubut.");
}

/* 5 — A quién le vende */
{
  const s = nuevo(DARK);
  titulo(s, "LE VENDE AL CANAL", CREAM);
  bajada(s, "Nunca al consumidor final: el dato que ordena todo el análisis", PALE);
  const anchoC = (CW - 2 * 0.4) / 3;
  const cajas = [
    ["57", "Distribuidores mayoristas", "Exclusividad territorial en 7 provincias", ORANGE],
    ["1", "Cadena de supermercados", "Aiello, de San Luis, con trato directo", "7FB8A6"],
    ["0", "Venta minorista", "Sin local y sin e-commerce operativo", MUTED],
  ];
  cajas.forEach((c, i) => {
    const x = M + i * (anchoC + 0.4);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.0, w: anchoC, h: 3.15, fill: { color: "22353F" }, rectRadius: 0.1,
    });
    s.addText(c[0], {
      x: x + 0.35, y: 2.25, w: anchoC - 0.7, h: 1.1, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 64, bold: true, color: c[3], valign: "middle",
    });
    s.addText(c[1], {
      x: x + 0.35, y: 3.45, w: anchoC - 0.7, h: 0.75, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 18, bold: true, color: CREAM, valign: "top",
    });
    s.addText(c[2], {
      x: x + 0.35, y: 4.3, w: anchoC - 0.7, h: 0.75, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: PALE, valign: "top",
    });
  });
  s.addText("No hay segmento minorista: el modelo entero está construido sobre mayoristas y una sola cadena.", {
    x: M, y: 5.45, w: CW, h: 0.6, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 19, color: CREAM, valign: "middle",
  });
  pie(s, null, MUTED);
  s.addNotes("Aiello es una cadena familiar puntana con 10 sucursales y política de comprarle a proveedores locales. Eso explica cómo una pyme mendocina llegó a su góndola.");
}

/* 6 — Con qué la miramos */
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

/* 7 — FODA completo */
{
  const s = nuevo(CREAM);
  titulo(s, "FODA");
  bajada(s, "Lo interno contra lo externo, en una mirada");
  const aw = (CW - 0.35) / 2;
  const ah = 2.35;
  tarjeta(s, {
    x: M, y: 1.75, w: aw, h: ah, fill: T_GREEN, tinta: GREEN, titulo: "FORTALEZAS",
    items: ["57 distribuidores construidos en 53 años", "Logística propia más transporte tercerizado", "Segunda generación trabajando en la empresa", "El canal está conforme: el único reclamo es rotura"],
    pt: 14,
  });
  tarjeta(s, {
    x: M + aw + 0.35, y: 1.75, w: aw, h: ah, fill: T_RED, tinta: RED, titulo: "DEBILIDADES",
    items: ["No conocen el costo real por producto", "Planta saturada, tapada con horas extras", "No miden casi nada de lo que hacen", "Sistema sin integrar y sin CRM"],
    pt: 14,
  });
  tarjeta(s, {
    x: M, y: 4.25, w: aw, h: ah, fill: T_BLUE, tinta: BLUE, titulo: "OPORTUNIDADES",
    items: ["La tienda online ya está hecha y apagada", "Crecer por fraccionamiento sin ampliar planta", "Aiello como modelo de cadena repetible", "El equipo tiene ganas de capacitarse"],
    pt: 14,
  });
  tarjeta(s, {
    x: M + aw + 0.35, y: 4.25, w: aw, h: ah, fill: T_ORANGE, tinta: "8A5714", titulo: "AMENAZAS",
    items: ["Inflación sobre un modelo que compite por precio", "Un solo proveedor de film impreso", "Sin margen de planta si sube la demanda", "Perder un cliente sin llegar a enterarse"],
    pt: 14,
  });
  s.addNotes("Las fortalezas y debilidades salen de mirar la cadena de valor; las oportunidades y amenazas, de los factores del entorno y de las cinco fuerzas. No lo cruzamos a propósito: el cruce deriva iniciativas y esta entrega es diagnóstico.");
}

function laminaFoda(nombre, subtitulo, tint, tinta, items, remate, notas) {
  const s = nuevo(CREAM);
  titulo(s, "FODA · " + nombre, tinta);
  bajada(s, subtitulo);
  s.addText(
    items.map((t, i) => ({
      text: t,
      options: { bullet: true, breakLine: i < items.length - 1 },
    })),
    {
      x: M, y: 1.85, w: CW * 0.62, h: 4.7, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 19, color: DARK, paraSpaceAfter: 12, valign: "top",
    }
  );
  tarjeta(s, {
    x: M + CW * 0.62 + 0.4, y: 1.85, w: CW - CW * 0.62 - 0.4, h: 4.7,
    fill: tint, tinta: tinta, titulo: "DE DÓNDE SALE", tituloPt: 12,
    texto: remate, pt: 15,
  });
  pie(s);
  s.addNotes(notas);
  return s;
}

/* 8 a 11 — FODA bloque por bloque */
laminaFoda(
  "FORTALEZAS", "Lo que la empresa tiene y le funciona", T_GREEN, GREEN,
  [
    "Una red de 57 distribuidores construida en 53 años: armar cobertura en 7 provincias lleva décadas y es la verdadera barrera de entrada",
    "Logística propia combinada con transporte tercerizado, que es lo que le permite llegar a la Patagonia",
    "Segunda generación ya trabajando: la operación diaria no depende de una sola persona",
    "El canal está conforme. El único reclamo habitual son los paquetes que se rompen en el viaje",
    "Habilitaciones RNE y RNPA vigentes, una barrera real frente a competidores informales",
  ],
  "De la cadena de valor: qué actividades hace la empresa y cuáles le agregan valor de verdad.",
  "El punto fuerte no es el producto, es el alcance. Y ese alcance no se compra: se construyó en cinco décadas."
);

laminaFoda(
  "DEBILIDADES", "Lo que le juega en contra puertas adentro", T_RED, RED,
  [
    "No conocen el costo real por producto: la planilla existe pero la propia empresa reconoce que es imprecisa",
    "La planta está al límite de su capacidad y lo tapan con horas extras sostenidas",
    "No miden casi nada: ni cuánto pesa cada cliente, ni cuánto se pierde por rotura, ni cuántas horas extras se pagan",
    "El sistema de gestión y las planillas no se hablan entre sí, y no hay CRM",
    "Los pedidos entran por canales que no se comunican: viajante, WhatsApp y teléfono",
  ],
  "De la cadena de valor y del relevamiento con el integrante que trabaja adentro de la empresa.",
  "Acá está el nudo del diagnóstico: compite por precio y no sabe cuánto le cuesta producir. Todo lo demás se desprende de ahí."
);

laminaFoda(
  "OPORTUNIDADES", "Lo que está disponible y no se está usando", T_BLUE, BLUE,
  [
    "La tienda online ya está construida, con carrito y catálogo cargado, y sin operar: es capacidad que ya se pagó",
    "La línea de fraccionamiento permite crecer sin ampliar la planta, porque envasa producto comprado a terceros",
    "Aiello funciona como modelo de cadena repetible en otras provincias",
    "El equipo tiene ganas de capacitarse y la empresa aprovecha las oportunidades de producto nuevo",
    "Mendoza está subatendida: apenas 6 distribuidores en la provincia donde está la fábrica",
  ],
  "De los factores clave del entorno y de las cinco fuerzas, sobre todo del poder de negociación del canal.",
  "La oportunidad más barata es la tienda: no hay que construir nada, hay que decidir usarla."
);

laminaFoda(
  "AMENAZAS", "Lo que puede golpear desde afuera", T_ORANGE, "8A5714",
  [
    "Inflación de costos sobre un modelo cuya única ventaja declarada es el precio",
    "Un solo proveedor de film impreso, con mínimos de compra y arte propio de la marca: cambiarlo encarece y demora",
    "Si sube la demanda no hay margen de planta para responder, y ya pierden ventas en temporada",
    "Pueden perder un distribuidor sin llegar a enterarse, porque no hay seguimiento de la cartera",
    "Competidores regionales e informales con estructura de costos más liviana",
  ],
  "De las cinco fuerzas, sobre todo del poder de los proveedores, y de los factores clave del entorno.",
  "La amenaza del film es la más concreta: es el único insumo sin sustituto rápido."
);

/* 12 — Canvas completo */
{
  const s = nuevo(CREAM);
  titulo(s, "BUSINESS MODEL CANVAS");
  bajada(s, "Estado actual del modelo de negocio, los nueve bloques en una lámina");
  const g = 0.09;
  const colW = (CW - 4 * g) / 5;
  const y1 = 1.68, hAlto = 3.4, hFila = (hAlto - g) / 2;
  const y3 = y1 + hAlto + g, h3 = 1.35;
  const col = (i) => M + i * (colW + g);

  function mini(x, y, w, h, fill, tit, tinta, lineas, negrita) {
    s.addShape(pres.ShapeType.roundRect, { x: x, y: y, w: w, h: h, fill: { color: fill }, rectRadius: 0.06 });
    s.addText(tit, {
      x: x + 0.14, y: y + 0.1, w: w - 0.28, h: 0.26, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 11, bold: true, charSpacing: 0.5, color: tinta, valign: "middle",
    });
    s.addText(
      lineas.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < lineas.length - 1 } })),
      {
        x: x + 0.14, y: y + 0.4, w: w - 0.28, h: h - 0.5, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 10.5, color: negrita || DARK, paraSpaceAfter: 3, valign: "top",
      }
    );
  }

  mini(col(0), y1, colW, hAlto, T_NEUTRAL, "8 · SOCIOS", GREY,
    ["Un solo proveedor de film", "Materia prima a granel", "Producto terminado a granel", "Los 57 distribuidores", "Transportistas tercerizados", "Aiello Supermercados"]);
  mini(col(1), y1, colW, hFila, T_NEUTRAL, "7 · ACTIVIDADES", GREY,
    ["Producción", "Fraccionamiento", "Distribución", "Compras y cobranza"]);
  mini(col(1), y1 + hFila + g, colW, hFila, T_NEUTRAL, "6 · RECURSOS", GREY,
    ["Red de 57 clientes", "Planta al límite", "Saber de la familia", "RNE y RNPA"]);
  mini(col(2), y1, colW, hAlto, DARK, "2 · PROPUESTA", ORANGE,
    ["Rentabilidad para el que revende", "Precio competitivo", "Logística a 7 provincias", "Catálogo amplio en un proveedor", "Formatos de 1 y 2 Kg"], PALE);
  mini(col(3), y1, colW, hFila, T_NEUTRAL, "4 · RELACIÓN", GREY,
    ["La lleva la empresa", "Exclusividad por zona", "Horario acotado", "Sin CRM"]);
  mini(col(3), y1 + hFila + g, colW, hFila, T_NEUTRAL, "3 · CANALES", GREY,
    ["Flota propia y fletes", "Viajante con zona", "WhatsApp y teléfono", "Tienda apagada"]);
  mini(col(4), y1, colW, hAlto, T_NEUTRAL, "1 · SEGMENTOS", GREY,
    ["57 distribuidores", "61% en Patagonia", "Aiello, San Luis", "Nunca consumidor final"]);
  mini(M, y3, colW * 3 + 2 * g, h3, T_RED, "9 · ESTRUCTURA DE COSTOS", RED,
    ["Materia prima · packaging · mano de obra · flete · energía · costo financiero", "Ningún costo está asignado por producto: fijan precio sobre una base que saben equivocada"]);
  mini(col(3), y3, colW * 2 + g, h3, T_GREEN, "5 · FUENTES DE INGRESO", GREEN,
    ["Venta mayorista · Aiello · producto fraccionado", "Contado, cuenta corriente a 30 días y cheques diferidos"]);
  pie(s);
  s.addNotes("El bloque oscuro del centro es la clave: le vende rentabilidad al canal, no sabor al consumidor. Abajo a la izquierda, en rojo, está el problema de fondo.");
}

/* 13 a 21 — un bloque del canvas por lámina */
bloqueCanvas(
  nuevo(CREAM), 1, "SEGMENTOS DE CLIENTES", "¿Para quién creamos valor?",
  [
    "57 distribuidores mayoristas activos en 7 provincias",
    "35 de esos 57 están en la Patagonia: el 61% de la red",
    "Mendoza, donde está la fábrica, tiene apenas 6",
    "Aiello Supermercados, de San Luis: la única cadena, con trato directo",
    "Nunca al consumidor final: no hay segmento minorista",
    "No se sabe cuánto factura cada distribuidor: el dato no existe",
  ],
  "El negocio es de canal, de punta a punta. Y con 57 clientes, la empresa no mide si el volumen está repartido o si unos pocos concentran todo.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 2, "PROPUESTA DE VALOR", "¿Qué problema resolvemos?",
  [
    "Rentabilidad para el distribuidor, y la empresa lo dice así en su propia página",
    "La logística como diferencial: alcance que el canal no consigue solo",
    "Precio competitivo por control de costos",
    "Catálogo amplio en un solo proveedor, así el mayorista no fragmenta sus compras",
    "Formatos de 1 y 2 Kg para que el comercio chico fraccione y saque margen",
    "Fraccionamiento: envasa y marca producto de terceros",
  ],
  "No le vende sabor al consumidor: le vende rentabilidad al canal. Es una estrategia de liderazgo en costos, no de diferenciación.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 3, "CANALES", "¿Cómo llegamos a ellos?",
  [
    "Flota propia de reparto",
    "Transporte tercerizado, que es lo que hace posible la Patagonia",
    "Retiro en fábrica",
    "Un viajante con zona asignada: entrega, no preventa",
    "WhatsApp y teléfono, por donde entran los pedidos",
    "Instagram y Facebook: marca y contacto, no venta",
    "Tienda online construida y sin operar",
  ],
  "El sitio tiene carrito, checkout y el catálogo cargado. Lo que falta no es la obra, es la decisión de encenderla: capacidad que ya se pagó y está apagada.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 4, "RELACIÓN CON CLIENTES", "¿Cómo los fidelizamos?",
  [
    "El vínculo lo sostiene la empresa, no el viajante",
    "Exclusividad territorial acordada con cada distribuidor",
    "Atención de lunes a viernes en horario acotado",
    "Sin ningún canal de autogestión fuera de esa franja",
    "Sin CRM y sin política de fidelización",
    "El cliente se queda por costumbre, precio y trato directo",
  ],
  "Que la relación no se vaya con el vendedor es bueno, pero pone 57 vínculos sobre una estructura chica. Y en la lista pública de distribuidores hay registros duplicados.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 5, "FUENTES DE INGRESO", "¿Por qué pagan nuestros clientes?",
  [
    "Venta mayorista a distribuidores: la fuente principal",
    "Venta directa a la cadena Aiello",
    "Venta de producto fraccionado: repostería y formatos de 1 y 2 Kg",
    "Volumen con poca ganancia por unidad",
    "Contado, cuenta corriente a 30 días y cheques diferidos",
    "Demanda pareja todo el año, sin estacionalidad marcada",
  ],
  "Sin cadena nacional no hay plazos de 90 días: hoy la empresa no está expuesta al estrangulamiento financiero del retail concentrado.",
  GREEN
);

bloqueCanvas(
  nuevo(CREAM), 6, "RECURSOS CLAVE", "¿Qué activos necesitamos?",
  [
    "La red de 57 distribuidores: el activo más valioso y el menos reconocido",
    "La línea de producción, hoy al límite de su capacidad",
    "El conocimiento de la familia: recetas, costos y contactos",
    "La marca, con 53 años y presencia en góndola",
    "La flota propia y la capacidad logística",
    "La planilla de costos, de la que depende el precio de todo el catálogo",
    "Las habilitaciones RNE y RNPA",
  ],
  "Hay segunda generación operando, así que la continuidad diaria está cubierta. Lo que sigue concentrado en una sola cabeza es el criterio estratégico.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 7, "ACTIVIDADES CLAVE", "¿Qué hacemos para entregar valor?",
  [
    "Producción: extrusión, freído y saborizado",
    "Fraccionamiento y envasado, incluida la línea de repostería",
    "Compras de materia prima y de packaging",
    "Distribución y logística, con flota propia y fletes",
    "Reparto y presencia en el territorio con el viajante",
    "Manejo centralizado de la relación con los 57 distribuidores",
    "Administración, facturación y cobranza",
  ],
  "La administración se reparte entre planillas y un sistema de gestión que no se hablan entre sí. Es el mismo problema que aparece en el costeo.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 8, "SOCIOS CLAVE", "¿Quiénes son nuestros aliados?",
  [
    "Proveedor de packaging y film impreso: uno solo, con mínimos de compra y arte propio",
    "Proveedores de materia prima a granel: críticos pero sustituibles",
    "Proveedores de producto terminado a granel, que abastecen el fraccionamiento",
    "Los 57 distribuidores: socios y clientes a la vez, ponen el capital de trabajo",
    "Transportistas tercerizados",
    "Aiello Supermercados, un socio de tamaño parecido y no un retailer que imponga condiciones",
  ],
  "La dependencia del film es la única que no tiene salida rápida: cambiar de proveedor encarece y demora, porque el arte es específico de la marca.",
  ORANGE
);

bloqueCanvas(
  nuevo(CREAM), 9, "ESTRUCTURA DE COSTOS", "¿Cuáles son los principales costos?",
  [
    "Materia prima: el componente más pesado",
    "Packaging y film, agravado por más de 25 presentaciones",
    "Mano de obra: entre 15 y 20 personas",
    "Logística y flete: mucho volumen y poco peso, con la red lejos",
    "Energía y mantenimiento de una línea saturada",
    "Costo financiero de la cuenta corriente y los cheques",
  ],
  "Ningún componente está asignado por producto. Fijan precio sobre una base que la propia empresa sabe equivocada, en un modelo cuya única ventaja declarada es el precio.",
  RED
);

/* 22 — Madurez, el número */
{
  const s = nuevo(CREAM);
  titulo(s, "MADUREZ DIGITAL");
  bajada(s, "El modelo de la cátedra, 28 preguntas sobre 7 dimensiones");
  s.addText("1.79", {
    x: M, y: 1.9, w: 5.0, h: 2.1, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 108, bold: true, color: RED, valign: "middle",
  });
  s.addText("Nivel Inicial, sobre 5", {
    x: M, y: 4.05, w: 5.0, h: 0.5, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 22, bold: true, color: DARK,
  });
  s.addText("50 puntos sobre 28 preguntas", {
    x: M, y: 4.6, w: 5.0, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, color: GREY,
  });
  const bx = M + 5.6;
  const bw = CW - 5.6;
  tarjeta(s, {
    x: bx, y: 1.9, w: bw, h: 1.7, fill: T_GREEN, tinta: GREEN,
    titulo: "LO QUE SÍ ESTÁ", tituloPt: 12,
    texto: "Hay un sistema de gestión, hay habilitaciones, hay planilla de costos y hay una tienda construida. Las herramientas existen.",
    pt: 15,
  });
  tarjeta(s, {
    x: bx, y: 3.75, w: bw, h: 1.75, fill: T_RED, tinta: RED,
    titulo: "LO QUE FALTA", tituloPt: 12,
    texto: "Nada de eso está integrado ni se mide. Las dos dimensiones más bajas, Estrategia y Gobierno, no son sobre herramientas: son sobre decidir y controlar.",
    pt: 15,
  });
  tarjeta(s, {
    x: M, y: 5.65, w: CW, h: 1.1, fill: T_NEUTRAL, tinta: DARK,
    texto: "Nivel Inicial no quiere decir que la empresa esté mal gestionada. Quiere decir que decide sin instrumentos: sin datos propios, sin indicadores y sin nadie que tenga el cambio como responsabilidad.",
    pt: 16,
  });
  pie(s);
  s.addNotes("El modelo de la cátedra trae seis dimensiones y el enunciado pide siete: agregamos Gobierno como séptima, y está justificado en el informe. Las respuestas salen del relevamiento con el integrante que trabaja adentro.");
}

/* 23 — Madurez por dimensión */
{
  const s = nuevo(CREAM);
  titulo(s, "MADUREZ DIGITAL POR DIMENSIÓN");
  bajada(s, "Tres dimensiones llegan a Básico; el piso está en Estrategia y Gobierno");
  // Barras dibujadas a mano: un grafico nativo no sobrevive la conversion a
  // imagenes ni la importacion a Prezi.
  {
    const dims = [
      ["Procesos y Operaciones", 2.5, GREEN],
      ["Tecnología y Datos", 2.25, GREEN],
      ["Clientes y Canales", 2.0, GREEN],
      ["Liderazgo y Cultura", 1.5, ORANGE],
      ["Personas y Habilidades", 1.5, ORANGE],
      ["Gobierno", 1.5, RED],
      ["Estrategia", 1.25, RED],
    ];
    const gx = M, gy = 1.8, gw = CW * 0.66, gh = 3.75;
    const etiqueta = 2.45;
    const escala = gw - etiqueta - 0.75; // reservo el final para el valor
    const paso = gh / dims.length;
    // guias verticales de 1 a 5
    for (let v = 1; v <= 5; v++) {
      const x = gx + etiqueta + (v / 5) * escala;
      s.addShape(pres.ShapeType.line, {
        x: x, y: gy, w: 0, h: gh,
        line: { color: "E2DCCC", width: 1 },
      });
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
        x: gx + etiqueta, y: y + paso / 2 - 0.13, w: largo, h: 0.26,
        fill: { color: d[2] },
      });
      s.addText(d[1].toFixed(2), {
        x: gx + etiqueta + largo + 0.1, y: y, w: 0.65, h: paso, isTextBox: true, margin: 0,
        fontFace: H, fontSize: 13, bold: true, color: DARK, valign: "middle",
      });
    });
  }
  tarjeta(s, {
    x: M + CW * 0.66 + 0.4, y: 1.75, w: CW - CW * 0.66 - 0.4, h: 1.85,
    fill: T_GREEN, tinta: GREEN, titulo: "NIVEL BÁSICO", tituloPt: 12,
    texto: "Procesos, Tecnología y Clientes. Hay herramientas, pero sueltas.", pt: 15,
  });
  tarjeta(s, {
    x: M + CW * 0.66 + 0.4, y: 3.75, w: CW - CW * 0.66 - 0.4, h: 2.0,
    fill: T_RED, tinta: RED, titulo: "NIVEL INICIAL", tituloPt: 12,
    texto: "Liderazgo, Personas, Gobierno y Estrategia. Acá está el piso, y no se arregla comprando software.", pt: 15,
  });
  tarjeta(s, {
    x: M, y: 5.85, w: CW, h: 0.9, fill: T_NEUTRAL, tinta: DARK,
    texto: "Las dos más bajas no son sobre herramientas: son sobre decidir y controlar.", pt: 17,
  });
  pie(s);
  s.addNotes("Escala de 1 a 5. Nivel 1 Inicial, 2 Básico, 3 Intermedio, 4 Avanzado, 5 Líder. El promedio simple de las 28 preguntas da 1.79.");
}

/* 24 — Conclusiones */
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
  const cw2 = (CW - 2 * 0.35) / 3;
  const puntos = [
    ["1", "Compite por precio sin conocer su costo", "La única ventaja que declara es el precio, y la planilla que lo sostiene la propia empresa la reconoce imprecisa."],
    ["2", "Tapa la planta saturada con horas extras", "La capacidad está al límite y se cubre pagando horas, no resolviendo el cuello de botella."],
    ["3", "Su activo más valioso no tiene sistema detrás", "57 distribuidores construidos en 53 años, sin CRM, sin medición de cartera y con la lista pública duplicada."],
  ];
  puntos.forEach((p, i) => {
    const x = M + i * (cw2 + 0.35);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.55, w: cw2, h: 3.0, fill: { color: "22353F" }, rectRadius: 0.1,
    });
    circulo(s, p[0], x + 0.32, 2.82, 0.6, ORANGE, DARK);
    s.addText(p[1], {
      x: x + 0.32, y: 3.58, w: cw2 - 0.64, h: 0.85, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 17, bold: true, color: CREAM, valign: "top",
    });
    s.addText(p[2], {
      x: x + 0.32, y: 4.42, w: cw2 - 0.64, h: 1.05, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: PALE, valign: "top",
    });
  });
  s.addText("El problema no está en el canal. El canal está conforme. Está puertas adentro.", {
    x: M, y: 5.75, w: CW, h: 0.6, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 19, color: CREAM, valign: "middle",
  });
  pie(s, null, MUTED);
  s.addNotes("Cerrar acá. Los tres puntos salen de cruzar el FODA, el canvas y la madurez: las tres herramientas apuntan al mismo lado.");
}

/* 25 — Qué sigue */
{
  const s = nuevo(CREAM);
  titulo(s, "QUÉ SIGUE");
  bajada(s, "Esta entrega es diagnóstico: el modelo actual, sin proponer solución todavía");
  const cw3 = (CW - 0.4) / 2;
  tarjeta(s, {
    x: M, y: 2.0, w: cw3, h: 2.6, fill: T_NEUTRAL, tinta: DARK,
    titulo: "LO QUE HICIMOS EN ESTA PARTE", tituloPt: 13,
    items: ["Relevamos la organización y su contexto", "Aplicamos FODA, Business Model Canvas y el modelo de madurez digital", "Identificamos los costos que la empresa ya está pagando por no actuar"],
    pt: 15,
  });
  tarjeta(s, {
    x: M + cw3 + 0.4, y: 2.0, w: cw3, h: 2.6, fill: T_ORANGE, tinta: RED,
    titulo: "LO QUE VIENE EN LA PARTE 2", tituloPt: 13,
    items: ["Priorizar el problema gerencial", "Ponerle número a los cuatro costos de no actuar", "Recién ahí, proponer la solución"],
    pt: 15,
  });
  s.addText("Gracias.", {
    x: M, y: 5.1, w: CW, h: 0.7, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 30, bold: true, color: DARK, valign: "middle",
  });
  s.addText("Lepez Joaquín · Geyer Juan José · Lopez Juan · Sorato Emiliano", {
    x: M, y: 5.8, w: CW, h: 0.4, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 14, color: GREY,
  });
  pie(s);
  s.addNotes("Los cuatro costos de no actuar están confirmados por la empresa: ventas perdidas en temporada, horas hombre para rehacer la lista de precios, roturas en el viaje y horas extras sostenidas. Ninguno está cuantificado todavía, y eso también es parte del diagnóstico.");
}

pres.writeFile({ fileName: process.argv[2] || "Dulxelitos.pptx" }).then((f) => console.log("listo:", f));
