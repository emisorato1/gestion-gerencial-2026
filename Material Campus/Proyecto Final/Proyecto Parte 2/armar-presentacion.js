// Presentacion de la Parte 2 de Dulxelitos, 10 laminas, ~10 minutos, 5 expositores.
// Mismo estilo que la Parte 1 (../Proyecto/armar-presentacion.js): paleta, tipografias y
// helpers. El contenido sale de las secciones 01 a 08 de esta carpeta; ninguna cifra es
// nueva. Los diagramas BPMN se recortan en el propio pptx (srcRect), sin archivos nuevos.
//
// Uso: nice -n 10 node armar-presentacion.js "Entrega/Presentación TP Final Parte 2 - Dulxelitos.pptx"
const fs = require("fs");
const path = require("path");
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
//   oscuro  = texto, trazos, tarjeta destacada
//   naranja = atencion: dolores, lentes, anotaciones y lo que es solo del piloto
//   verde   = la mejora: cambios del TO-BE, metas, resultados clave, Go
//   azul    = sistemas y datos: Discovery (alternativa B)
//   rojo    = problemas, No-Go
//   gris    = lo secundario, lo que queda para mas adelante o se descarta

const H = "Arial";
const B = "Calibri";

const W = 13.3;
const M = 0.65;
const CW = W - 2 * M; // 12.0

const AS_IS = path.join(__dirname, "bpmn", "as-is.png");
const TO_BE = path.join(__dirname, "bpmn", "to-be.png");

// Tamano real de un PNG, leido del encabezado, para calcular recortes.
function tamanoPng(ruta) {
  const b = fs.readFileSync(ruta);
  return { w: b.readUInt32BE(16), h: b.readUInt32BE(20) };
}

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";
pres.author = "Lepez Joaquin, Geyer Juan Jose, Lopez Juan, Olivares Manuel, Sorato Emiliano";
pres.title = "Dulxelitos - Propuesta de mejora";

function nuevo(bg) {
  numLamina += 1;
  const s = pres.addSlide();
  s.background = { color: bg || CREAM };
  return s;
}

// Titulo de lamina. Estandar: 34 pt a 0.5 in, con bajada debajo. Compacto (laminas
// con un diagrama grande): 26 pt a 0.16 in. x y w permiten alinear con el contenido.
function titulo(s, texto, o) {
  o = o || {};
  const compacto = !!o.compacto;
  s.addText(texto, {
    x: o.x === undefined ? M : o.x, y: compacto ? 0.16 : 0.5, w: o.w || CW, h: compacto ? 0.5 : 0.62,
    isTextBox: true, margin: 0,
    fontFace: H, fontSize: compacto ? 26 : 34, bold: true, charSpacing: 1.2,
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

let numLamina = 0;
function pie(s, color, m) {
  const x0 = m === undefined ? M : m;
  s.addShape(pres.ShapeType.rect, { x: x0, y: 6.97, w: 0.22, h: 0.05, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
  s.addText(String(numLamina).padStart(2, "0") + " / 10", {
    x: x0 + 0.32, y: 6.85, w: 1.2, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 10, bold: true, charSpacing: 1, color: color || GREY, valign: "middle",
  });
  s.addText("Dulxelitos · Gestión Gerencial · UTN FRSR", {
    x: x0, y: 6.85, w: W - 2 * x0, h: 0.3, isTextBox: true, margin: 0,
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

function tarjeta(s, o) {
  s.addShape(pres.ShapeType.roundRect, {
    x: o.x, y: o.y, w: o.w, h: o.h, fill: { color: o.fill }, rectRadius: 0.08,
    line: o.fill === WHITE ? { color: LINE, width: 1 } : undefined,
  });
  if (o.acento) {
    s.addShape(pres.ShapeType.rect, { x: o.x, y: o.y + 0.16, w: 0.06, h: o.h - 0.32, fill: { color: o.acento }, line: { color: o.acento, width: 0 } });
  }
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
      o.items.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < o.items.length - 1 } })),
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

// Recorta una zona (en pixeles de la imagen original) y la dibuja con un ancho dado.
// Devuelve el alto resultante en pulgadas. alt es el texto alternativo de la imagen
// (sin el, pptxgenjs pone la ruta local del archivo).
function recorte(s, ruta, caja, dest, alt) {
  const img = tamanoPng(ruta);
  const k = dest.w / caja.w; // pulgadas por pixel
  const h = caja.h * k;
  s.addImage({
    path: ruta, altText: alt,
    x: dest.x, y: dest.y, w: img.w * k, h: img.h * k,
    sizing: { type: "crop", x: caja.x * k, y: caja.y * k, w: dest.w, h: h },
  });
  return h;
}

// Las coordenadas de abajo se midieron sobre la imagen mostrada a 2000 px de ancho;
// este factor las pasa a pixeles reales del PNG.
const kAs = 3900 / 2000;
const kTo = 3732 / 2000;
const px = (k, x0, y0, x1, y1) => ({ x: x0 * k, y: y0 * k, w: (x1 - x0) * k, h: (y1 - y0) * k });

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
  s.addText("Trabajo Práctico Final · Parte 2 · Propuesta de mejora", {
    x: M, y: 3.6, w: CW, h: 0.45, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 20, color: PALE,
  });
  s.addText("Gestión del stock de producto terminado", {
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
  s.addNotes("Joaquín. Presentamos la parte 2: la propuesta para Dulxelitos. Esta parte arranca con una corrección a lo que dijimos en la parte 1.");
}

/* 2 - El problema */
{
  const s = nuevo(CREAM);
  titulo(s, "EL PROBLEMA");
  bajada(s, "Dulxelitos acepta pedidos sin saber qué hay y produce sin mirar lo que se pidió");
  const g = 0.3;
  const aw = (CW - 3 * g) / 4;
  const datos = [
    ["30", "de ~125 por semana", "pedidos recortados o demorados", RED],
    ["76 %", "→ 90 % en 6 meses", "pedidos completos y a tiempo", DARK, GREEN],
    ["~25 h", "por mes", "horas extras sobre una planta saturada", ORANGE],
    ["20 %", "→ 100 % de los días", "con la producción cargada", DARK, GREEN],
  ];
  datos.forEach((d, i) => {
    const x = M + i * (aw + g);
    s.addShape(pres.ShapeType.rect, { x: x, y: 1.95, w: aw, h: 0.05, fill: { color: d[3] } });
    s.addText(d[0], {
      x: x, y: 2.1, w: aw, h: 1.0, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 54, bold: true, color: d[3], valign: "bottom",
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
  // Corrección a la Parte 1, en una línea.
  s.addShape(pres.ShapeType.roundRect, {
    x: M, y: 4.85, w: CW, h: 1.55, fill: { color: DARK }, rectRadius: 0.1,
  });
  s.addText("CORRECCIÓN A LA PARTE 1", {
    x: M + 0.4, y: 5.05, w: CW - 0.8, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 13, bold: true, charSpacing: 2, color: ORANGE,
  });
  s.addText("El stock de producto terminado no se registra, y los recortes vendrían de la mezcla y el momento de producción, no de la capacidad (supuesto).", {
    x: M + 0.4, y: 5.4, w: CW - 0.8, h: 0.85, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 21, color: CREAM, valign: "top",
  });
  pie(s);
  s.addNotes("Joaquín. El problema en una frase: acepta pedidos sin saber qué hay y produce sin mirar lo que se pidió. El 76 % es una cuenta nuestra sobre una semana de registro. Después, las tres correcciones a la parte 1: el stock de producto terminado no se registra (dijimos que estaba en Discovery); los recortes pasan todas las semanas (dijimos que eran poco frecuentes); y vendrían sobre todo de la mezcla y el momento de producción, no de la capacidad, que es un supuesto nuestro a medir en el piloto.");
}

/* 3 - AS-IS: el diagrama completo, con las tres lentes marcadas */
{
  const s = nuevo(CREAM);
  titulo(s, "ASÍ SE ATIENDE UN PEDIDO HOY", { compacto: true, w: 7.0 });
  // Leyenda de las lentes, a la derecha del titulo.
  const ley = [["1", "Ineficiencia"], ["2", "Tarea manual"], ["3", "Flujo de datos"]];
  let lx = 7.55;
  ley.forEach((l) => {
    circulo(s, l[0], lx, 0.24, 0.34, ORANGE, WHITE, 13);
    s.addText(l[1], {
      x: lx + 0.42, y: 0.19, w: 1.4, h: 0.44, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, bold: true, color: DARK, valign: "middle",
    });
    lx += 1.85;
  });
  // Se recorta solo el titulo del diagrama y el borde blanco: el proceso entero, al
  // maximo ancho que deja el alto de la lamina (13.333 x 7.5).
  const c0 = { x0: 15, y0: 50, x1: 1985, y1: 1047 }; // sobre 2000 px
  const caja = px(kAs, c0.x0, c0.y0, c0.x1, c0.y1);
  const iw = 13.0, ix = (13.333 - iw) / 2, iy = 0.76;
  const ih = iw * caja.h / caja.w;
  s.addShape(pres.ShapeType.rect, { x: ix - 0.06, y: iy - 0.06, w: iw + 0.12, h: ih + 0.12, fill: { color: WHITE }, line: { color: LINE, width: 1 } });
  recorte(s, AS_IS, caja, { x: ix, y: iy, w: iw },
    "Diagrama BPMN del proceso actual Atender pedido de distribuidor: Oficina, Depósito, Producción y Dirección, con el distribuidor y el transporte tercerizado.");
  // Marcadores a la derecha de cada nota del diagrama (coordenadas sobre 2000 px).
  const mx = (dx) => ix + ((dx - c0.x0) / (c0.x1 - c0.x0)) * iw;
  const my = (dy) => iy + ((dy - c0.y0) / (c0.y1 - c0.y0)) * ih;
  [["1", 752, 548], ["2", 634, 300], ["3", 1074, 662]].forEach((m) => {
    circulo(s, m[0], mx(m[1]) - 0.18, my(m[2]) - 0.18, 0.36, ORANGE, WHITE, 14);
  });
  s.addNotes("Juan José. El diagrama completo. El pedido nace en el mensaje del distribuidor; el faltante se dibujó entero porque pasa todas las semanas. Los tres números naranja son las tres lentes de la lámina que sigue. Abajo, la producción corre aparte: el dueño o los hijos deciden qué producir sin mirar los pedidos.");
}

/* 4 - Las tres lentes */
{
  const s = nuevo(CREAM);
  // En esta lamina el contenido usa un margen de 0.5 para que los recortes del
  // diagrama se lean (~10 pt la letra de las notas); el titulo se alinea con eso.
  const m4 = 0.5, cw4 = 13.333 - 2 * m4;
  titulo(s, "LAS TRES LENTES", { x: m4, w: cw4 });
  bajada(s, "Una sola causa vista desde tres lados", GREY, m4, cw4);
  const lentes = [
    {
      n: "1", nombre: "INEFICIENCIA",
      txt: "La disponibilidad se averigua dos veces: a ojo y preguntando a producción.",
      arregla: "Reservar el stock contra pedidos antes de confirmar",
      caja: px(kAs, 436, 392, 732, 590), // "Mirar el stock a ojo" y su nota
      alt: "Recorte del diagrama actual: la tarea Mirar el stock a ojo y la nota Ineficiencia, doble averiguación de disponibilidad.",
    },
    {
      n: "2", nombre: "TAREA MANUAL",
      txt: "El mismo pedido se anota tres veces: chat, papel y lista.",
      arregla: "Cargar el pedido una sola vez",
      caja: px(kAs, 186, 165, 612, 362), // "Anotar pedido", el papel y la nota
      alt: "Recorte del diagrama actual: la tarea Anotar pedido en papel o planilla, el documento Papel o planilla y la nota Tarea manual, el mismo pedido se transcribe tres veces.",
    },
    {
      n: "3", nombre: "FLUJO DE DATOS",
      txt: "Producción, depósito y ventas no comparten ningún dato.",
      arregla: "Un stock cargado todos los días, con una sola regla",
      caja: px(kAs, 804, 610, 1054, 712), // la nota de flujo de datos
      alt: "Recorte del diagrama actual: la nota Flujo de datos, la producción se registra una vez por semana y no hay stock de producto terminado registrado.",
    },
  ];
  // Una sola escala para los tres recortes; cada tarjeta mide lo que su recorte.
  const g = 0.18, pad = 0.1, ins = 0.04;
  const anchoPx = lentes.reduce((t, l) => t + l.caja.w, 0);
  const k = (cw4 - 2 * g - 3 * 2 * (pad + ins)) / anchoPx; // pulgadas por pixel
  const altoBox = Math.max(...lentes.map((l) => l.caja.h)) * k + 2 * ins;
  const ay = 1.62, ah = 5.13;
  let x = m4;
  lentes.forEach((l) => {
    const cw = l.caja.w * k + 2 * (pad + ins);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: ay, w: cw, h: ah, fill: { color: T_NEUTRAL }, rectRadius: 0.08 });
    circulo(s, l.n, x + 0.18, ay + 0.2, 0.46, ORANGE, WHITE, 19);
    s.addText(l.nombre, {
      x: x + 0.76, y: ay + 0.2, w: cw - 0.9, h: 0.46, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 17, bold: true, charSpacing: 0.6, color: DARK, valign: "middle",
    });
    // recuadro blanco con el recorte del diagrama, centrado en vertical
    const sx = x + pad, sy = ay + 0.82;
    s.addShape(pres.ShapeType.roundRect, { x: sx, y: sy, w: cw - 2 * pad, h: altoBox, fill: { color: WHITE }, rectRadius: 0.05 });
    const dh = l.caja.h * k;
    recorte(s, AS_IS, l.caja, { x: sx + ins, y: sy + (altoBox - dh) / 2, w: l.caja.w * k }, l.alt);
    const tx = x + 0.2, tw = cw - 0.4, ty = sy + altoBox + 0.14;
    s.addText(l.txt, {
      x: tx, y: ty, w: tw, h: 0.82, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 16, bold: true, color: DARK, valign: "top",
    });
    s.addText("SE ARREGLA CON", {
      x: tx, y: ty + 0.88, w: tw, h: 0.25, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 11, bold: true, charSpacing: 1.5, color: GREEN,
    });
    s.addText(l.arregla, {
      x: tx, y: ty + 1.14, w: tw, h: 0.55, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, color: DARK, valign: "top",
    });
    x += cw + g;
  });
  pie(s, undefined, m4);
  s.addNotes("Juan José. Las tres lentes dan una sola causa, no tres proyectos. Lo que se ordena no son iniciativas sino los pasos de una: primero un quick win, la planilla del piloto, y después la inversión, el stock en Discovery. Y la pregunta del proceso balde: acelerar el aviso por WhatsApp sería poner un balde; la gotera es doble: el stock no se registra y se produce sin mirar los pedidos.");
}

/* 5 - Alternativas y recomendación */
{
  const s = nuevo(CREAM);
  titulo(s, "ALTERNATIVAS Y RECOMENDACIÓN");
  bajada(s, "Puntaje de la matriz de 10 criterios, sobre 50: es nuestro juicio, no una medición");
  const g = 0.3;
  const aw = (CW - 3 * g) / 4;
  const ay = 1.7, ah = 3.75;
  const alts = [
    { tag: "NO RESUELVE", nombre: "Do Nothing", pts: "31", fill: T_RED, tinta: RED, num: RED,
      txt: "Seguir igual. No ataca la causa: los recortes siguen cada semana." },
    { tag: "PILOTO", nombre: "A · Planilla compartida", pts: "36", fill: T_ORANGE, tinta: ORANGE_TXT, num: ORANGE,
      txt: "Casi cero de costo. Se arma sin proveedor ni instalación, pero no se conecta con Discovery." },
    { tag: "RECOMENDADA", nombre: "B · Stock de Discovery", pts: "35", fill: BLUE, tinta: WHITE, num: WHITE, cuerpo: WHITE, titulo: WHITE,
      txt: "El módulo ya está en la licencia y no se usa. Un solo registro donde ya se factura." },
    { tag: "DESCARTADA", nombre: "C · SaaS de gestión", pts: "20", fill: T_NEUTRAL, tinta: GREY, num: GREY,
      txt: "Cuota nueva, migración y doble carga. No resuelve la disciplina de carga." },
  ];
  alts.forEach((a, i) => {
    const x = M + i * (aw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: ay, w: aw, h: ah, fill: { color: a.fill }, rectRadius: 0.08 });
    s.addText(a.tag, {
      x: x + 0.28, y: ay + 0.24, w: aw - 0.56, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.8, color: a.tinta, valign: "middle",
    });
    s.addText(a.nombre, {
      x: x + 0.28, y: ay + 0.62, w: aw - 0.56, h: 0.72, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 16, bold: true, color: a.titulo || DARK, valign: "top",
    });
    // puntaje y "de 50" en un mismo cuadro, para que queden pegados
    s.addText([
      { text: a.pts, options: { fontFace: H, fontSize: 56, bold: true, color: a.num } },
      { text: "  de 50", options: { fontFace: B, fontSize: 14, color: a.cuerpo ? T_BLUE : GREY } },
    ], {
      x: x + 0.28, y: ay + 1.4, w: aw - 0.56, h: 0.85, isTextBox: true, margin: 0, valign: "bottom",
    });
    s.addShape(pres.ShapeType.rect, { x: x + 0.28, y: ay + 2.3, w: 0.5, h: 0.04, fill: { color: a.tinta }, line: { color: a.tinta, width: 0 } });
    s.addText(a.txt, {
      x: x + 0.28, y: ay + 2.4, w: aw - 0.56, h: 1.25, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, color: a.cuerpo || DARK, valign: "top",
    });
  });
  // Casi empate y recomendación.
  s.addShape(pres.ShapeType.roundRect, { x: M, y: 5.75, w: CW, h: 0.95, fill: { color: WHITE }, rectRadius: 0.08, line: { color: LINE, width: 1 } });
  s.addShape(pres.ShapeType.rect, { x: M, y: 5.87, w: 0.07, h: 0.71, fill: { color: ORANGE }, line: { color: ORANGE, width: 0 } });
  s.addText(
    [
      { text: "36 contra 35 es un empate: ", options: { bold: true } },
      { text: "decide el argumento, no el puntaje. A va primero, como piloto de 2 semanas con papas fritas; B es el destino." },
    ],
    {
      x: M + 0.3, y: 5.75, w: CW - 0.6, h: 0.95, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 18, color: DARK, valign: "middle",
    }
  );
  pie(s);
  s.addNotes("Juan. Do Nothing suma 31 porque la suma premia lo fácil; se descarta porque no resuelve nada. C se descarta: la suma más baja y no es la mejor en ningún criterio. A y B quedan casi empatadas y un punto entre juicios no es una diferencia. Las notas bajas de A son estructurales; las medias de B son incógnitas que el piloto y la prueba técnica despejan. Si el equipo no sostiene la carga en una planilla, tampoco en Discovery.");
}

/* 6 - TO-BE y la regla del stock disponible */
{
  const s = nuevo(CREAM);
  titulo(s, "PRIMERO SE MIRA QUÉ HAY, DESPUÉS SE CONFIRMA", { compacto: true });
  // Recorte de la calle de Oficina del TO-BE, el tramo clave.
  const caja = px(kTo, 85, 105, 1262, 520);
  const dx = M, dw = 9.7, dy = 1.05;
  const dh = dw * caja.h / caja.w;
  s.addShape(pres.ShapeType.rect, { x: dx - 0.06, y: dy - 0.06, w: dw + 0.12, h: dh + 0.12, fill: { color: WHITE }, line: { color: LINE, width: 1 } });
  recorte(s, TO_BE, caja, { x: dx, y: dy, w: dw },
    "Recorte del diagrama propuesto, calle de Oficina: de Pedido recibido a cargar la nota de pedido, consultar el stock disponible, reservar y confirmar, o avisar con fecha estimada.");
  // Tres cambios a la derecha.
  const cx = dx + dw + 0.35, cwid = W - M - cx;
  const cambios = [
    ["1", "consulta, no 2"],
    ["1", "carga del pedido, no 3"],
    ["a diario", "carga de producción, no semanal"],
  ];
  const chh = (dh + 0.12 - 2 * 0.15) / 3;
  cambios.forEach((c, i) => {
    const y = dy - 0.06 + i * (chh + 0.15);
    s.addShape(pres.ShapeType.roundRect, { x: cx, y: y, w: cwid, h: chh, fill: { color: T_GREEN }, rectRadius: 0.06 });
    s.addShape(pres.ShapeType.rect, { x: cx, y: y + 0.12, w: 0.06, h: chh - 0.24, fill: { color: GREEN }, line: { color: GREEN, width: 0 } });
    s.addText(c[0], {
      x: cx + 0.2, y: y + 0.1, w: cwid - 0.28, h: chh * 0.42, isTextBox: true, margin: 0,
      fontFace: H, fontSize: i === 2 ? 22 : 30, bold: true, color: GREEN, valign: "middle",
    });
    s.addText(c[1], {
      x: cx + 0.2, y: y + chh * 0.5, w: cwid - 0.28, h: chh * 0.45, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: DARK, valign: "top",
    });
  });
  // La regla.
  const ry = dy + dh + 0.35;
  s.addShape(pres.ShapeType.roundRect, { x: M, y: ry, w: CW, h: 6.65 - ry, fill: { color: DARK }, rectRadius: 0.1 });
  s.addText("LA REGLA, IGUAL EN LA PLANILLA DEL PILOTO Y EN DISCOVERY", {
    x: M + 0.4, y: ry + 0.17, w: CW - 0.8, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 2, color: ORANGE,
  });
  s.addText(
    [
      { text: "stock disponible", options: { bold: true, color: ORANGE } },
      { text: " = stock físico − reservado por pedidos confirmados sin facturar", options: { color: CREAM } },
    ],
    {
      x: M + 0.4, y: ry + 0.5, w: CW - 0.8, h: 6.65 - ry - 0.65, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 22, valign: "middle",
    }
  );
  pie(s);
  s.addNotes("Juan. El tramo clave del TO-BE: Oficina carga la nota de pedido una sola vez, consulta el stock disponible y recién ahí reserva y confirma; si no hay, avisa en el momento con una fecha estimada. Lo que no entra en el recorte: Producción carga todos los días al cierre del turno, Dirección planifica la semana con pedidos pendientes y stock mínimo, y Depósito cuenta una vez por semana. El diagrama entero está en la sección 3 del informe.");
}

/* 7 - Stakeholders: Mendelow */
{
  const s = nuevo(CREAM);
  titulo(s, "STAKEHOLDERS");
  bajada(s, "Matriz de Mendelow: poder e interés");
  // Figura 2x2
  const gx = 1.2, gy = 1.75, gap = 0.1;
  const cw = 3.35, ch = 2.1;
  const cuadrantes = [
    // [col, fila, fondo, nombre, accion]
    [0, 0, WHITE, "MANTENER SATISFECHO", "poder alto, interés bajo"],
    [1, 0, T_ORANGE, "GESTIONAR DE CERCA", "poder alto, interés alto"],
    [0, 1, WHITE, "MANTENER INFORMADO", "poder bajo, interés bajo"],
    [1, 1, WHITE, "MONITOREAR Y DAR VOZ", "poder bajo, interés alto"],
  ];
  cuadrantes.forEach((c) => {
    const x = gx + c[0] * (cw + gap), y = gy + c[1] * (ch + gap);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: y, w: cw, h: ch, fill: { color: c[2] }, rectRadius: 0.06,
      line: { color: c[2] === WHITE ? LINE : "EBCF9F", width: 1 },
    });
    s.addText(c[3], {
      x: x + 0.2, y: y + 0.13, w: cw - 0.4, h: 0.3, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 12, bold: true, charSpacing: 1.0, color: c[2] === WHITE ? DARK : ORANGE_TXT, valign: "middle",
    });
    s.addText(c[4], {
      x: x + 0.2, y: y + 0.42, w: cw - 0.4, h: 0.25, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 11, italic: true, color: GREY, valign: "middle",
    });
  });
  // Ejes
  const gw = 2 * cw + gap, gh = 2 * ch + gap;
  s.addText("PODER", {
    x: gx - 1.1, y: gy + gh / 2 - 0.2, w: 1.7, h: 0.4, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 14, bold: true, charSpacing: 3, color: GREY, align: "center", valign: "middle", rotate: 270,
  });
  s.addText("alto", { x: gx - 0.5, y: gy, w: 0.42, h: 0.3, isTextBox: true, margin: 0, fontFace: B, fontSize: 12, color: GREY, align: "right" });
  s.addText("bajo", { x: gx - 0.5, y: gy + gh - 0.3, w: 0.42, h: 0.3, isTextBox: true, margin: 0, fontFace: B, fontSize: 12, color: GREY, align: "right", valign: "bottom" });
  s.addText("bajo", { x: gx, y: gy + gh + 0.05, w: 0.7, h: 0.3, isTextBox: true, margin: 0, fontFace: B, fontSize: 12, color: GREY });
  s.addText("INTERÉS", {
    x: gx + gw / 2 - 1.0, y: gy + gh + 0.05, w: 2.0, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 14, bold: true, charSpacing: 3, color: GREY, align: "center", valign: "middle",
  });
  s.addText("alto", { x: gx + gw - 0.7, y: gy + gh + 0.05, w: 0.7, h: 0.3, isTextBox: true, margin: 0, fontFace: B, fontSize: 12, color: GREY, align: "right" });

  // Actores como fichas
  function ficha(texto, x, y, w, tipo) {
    const fill = tipo === "res" ? ORANGE : tipo === "lid" ? DARK : WHITE;
    const tinta = tipo ? WHITE : DARK;
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: y, w: w, h: 0.38, fill: { color: fill }, rectRadius: 0.19,
      line: tipo ? undefined : { color: "C9C2AE", width: 0.75 },
    });
    s.addText(texto, {
      x: x, y: y, w: w, h: 0.38, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, bold: true, color: tinta, align: "center", valign: "middle",
    });
  }
  const c0 = gx, c1 = gx + cw + gap, r0 = gy, r1 = gy + ch + gap;
  // Poder alto, interés bajo
  ficha("Dueño (sponsor)", c0 + 0.2, r0 + 0.85, 1.85, "lid");
  ficha("Buenos Aires Software", c0 + 0.2, r0 + 1.35, 2.45);
  // Poder alto, interés alto (Oficina y Producción, en naranja: resistencia esperada)
  ficha("Dueño (decisor)", c1 + 0.2, r0 + 0.78, 1.75);
  ficha("Hijos", c1 + 2.1, r0 + 0.78, 0.9);
  ficha("Oficina", c1 + 0.2, r0 + 1.2, 1.2, "res");
  ficha("Producción", c1 + 1.55, r0 + 1.2, 1.45, "res");
  ficha("Resp. de sistemas", c1 + 0.2, r0 + 1.62, 1.95, "lid");
  // Poder bajo
  ficha("Distribuidores", c0 + 0.2, r1 + 0.85, 1.7);
  ficha("Depósito", c1 + 0.2, r1 + 0.85, 1.3);

  // Panel derecho
  const px0 = gx + gw + 0.5, pw = W - M - px0;
  s.addText("Quien aprueba no es quien lo hace andar.", {
    x: px0, y: 1.75, w: pw, h: 1.2, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 22, bold: true, color: DARK, valign: "top",
  });
  tarjeta(s, {
    x: px0, y: 3.05, w: pw, h: 1.3, fill: WHITE, tinta: ORANGE_TXT, titulo: "PRODUCCIÓN", tituloPt: 13, acento: ORANGE,
    texto: "Cargar todos los días es trabajo nuevo, con la planta saturada.", pt: 14,
  });
  tarjeta(s, {
    x: px0, y: 4.5, w: pw, h: 1.3, fill: WHITE, tinta: ORANGE_TXT, titulo: "OFICINA", tituloPt: 13, acento: ORANGE,
    texto: "Consultar y reservar antes de confirmar suma un paso.", pt: 14,
  });
  // Leyenda de las fichas
  [[DARK, "sponsor y líder"], [ORANGE, "resistencia esperada"]].forEach((l, i) => {
    const y = 5.98 + i * 0.4;
    s.addShape(pres.ShapeType.roundRect, { x: px0, y: y, w: 0.5, h: 0.28, fill: { color: l[0] }, rectRadius: 0.14 });
    s.addText(l[1], {
      x: px0 + 0.62, y: y - 0.02, w: pw - 0.62, h: 0.32, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: GREY, valign: "middle",
    });
  });
  pie(s);
  s.addNotes("Emiliano. La matriz de Mendelow, con la lectura de la clase del 23-10. El dueño aprueba el presupuesto y el Go/No-Go, pero el cambio lo hacen andar Producción y Oficina, y esas son las dos resistencias que anticipamos: trabajo nuevo con la planta saturada y un paso más antes de confirmar. Poder, interés y resistencias son lectura nuestra y las vamos a contrastar con cada grupo antes del piloto.");
}

/* 8 - El piloto */
{
  const s = nuevo(CREAM);
  titulo(s, "EL PILOTO");
  bajada(s, "Dos semanas, solo papas fritas, en una planilla compartida. Si un día la planilla no está al día, se confirma como hoy.");
  const g = 0.3;
  const aw = (CW - 3 * g) / 4;
  const ay = 1.75, ah = 2.6;
  const medidas = [
    ["CARGA", "8 de 10", "días hábiles con la producción cargada", "hoy: 20 % de los días"],
    ["RECORTES", "la mitad", "o menos de pedidos recortados o demorados, contra la semana 0", ""],
    ["CONTEO", "1/10", "es la diferencia máxima entre la planilla y lo contado", "tolerancia provisional"],
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
  // Go / No-Go
  s.addText("GO / NO-GO · LO DECIDE EL DUEÑO, CON LOS UMBRALES A ACORDAR ANTES DEL PILOTO", {
    x: M, y: 4.62, w: CW, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 1.5, color: GREY, valign: "middle",
  });
  const tw = (CW - 2 * g) / 3;
  const salidas = [
    ["GO", GREEN, T_GREEN, "Los cuatro umbrales y la prueba técnica de Discovery: activar por línea de producto."],
    ["GO CON AJUSTES", ORANGE_TXT, T_ORANGE, "Falla el conteo o la fecha: corregir y repetir una sola vez."],
    ["NO-GO", RED, T_RED, "La carga no llega a 8 de 10: no se gasta en Discovery."],
  ];
  salidas.forEach((o, i) => {
    const x = M + i * (tw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: 5.0, w: tw, h: 1.65, fill: { color: o[2] }, rectRadius: 0.08 });
    s.addText(o[0], {
      x: x + 0.28, y: 5.15, w: tw - 0.56, h: 0.35, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 15, bold: true, charSpacing: 0.8, color: o[1], valign: "middle",
    });
    s.addText(o[3], {
      x: x + 0.28, y: 5.55, w: tw - 0.56, h: 1.0, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 15, color: DARK, valign: "top",
    });
  });
  pie(s);
  s.addNotes("Emiliano. El piloto es el experimento mínimo: dos semanas, un solo producto, con la misma regla de stock disponible. Mide cuatro cosas y cada una tiene su umbral. Los umbrales se acuerdan con el dueño antes de arrancar, para no leer el resultado a favor; todavía no están acordados. Dos semanas con un producto dan una señal, no una demostración. Lo que no prueba: el efecto en todo el catálogo, la baja de horas extras y el retorno.");
}

/* 9 - Roadmap e indicadores */
{
  const s = nuevo(CREAM);
  titulo(s, "ROADMAP E INDICADORES");
  bajada(s, "Objetivo: que cada pedido se confirme sabiendo qué hay · 6 meses");
  const g = 0.3;
  const cw3 = (CW - 2 * g) / 3;
  // Fases como flechas encadenadas (naranja: piloto; azul: Discovery; gris: despues)
  // y debajo lo que entra en cada una.
  const rey = 1.7, flh = 0.5, reh = 1.95;
  const cols = [
    ["AHORA · SEMANAS 1 A 6", ORANGE, T_ORANGE, ["Preparación y conteo inicial", "Piloto de 2 semanas", "Go/No-Go del dueño"]],
    ["PRÓXIMO · SEMANAS 7 A 26", BLUE, T_BLUE, ["Activar Discovery, una línea por vez", "Estabilización y cierre"]],
    ["MÁS ADELANTE", GREY, T_NEUTRAL, ["Stock visible para el distribuidor", "La tienda online"]],
  ];
  cols.forEach((c, i) => {
    const x = M + i * (cw3 + g);
    s.addShape(i === 0 ? pres.ShapeType.homePlate : pres.ShapeType.chevron, {
      // la primera arranca en el margen y la ultima termina en el margen derecho
      x: i === 0 ? x : x - 0.2, y: rey, w: i === 0 ? cw3 + 0.1 : (i === 2 ? cw3 + 0.2 : cw3 + 0.3), h: flh,
      fill: { color: c[1] }, line: { color: c[1], width: 0 },
    });
    s.addText(c[0], {
      x: x + (i === 0 ? 0.25 : 0.2), y: rey, w: cw3 - 0.5, h: flh, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 14, bold: true, charSpacing: 0.8, color: WHITE, valign: "middle",
    });
    s.addShape(pres.ShapeType.roundRect, { x: x, y: rey + flh + 0.1, w: cw3, h: reh - flh - 0.1, fill: { color: c[2] }, rectRadius: 0.08 });
    s.addText(
      c[3].map((t, k) => ({ text: t, options: { bullet: true, breakLine: k < c[3].length - 1 } })),
      {
        x: x + 0.25, y: rey + flh + 0.22, w: cw3 - 0.45, h: reh - flh - 0.34, isTextBox: true, margin: 0,
        fontFace: B, fontSize: 15, color: DARK, paraSpaceAfter: 5, valign: "top",
      }
    );
  });
  s.addText("INDICADORES", {
    x: M, y: 3.9, w: CW, h: 0.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 12, bold: true, charSpacing: 1.5, color: GREY, valign: "middle",
  });
  const aw = (CW - 3 * g) / 4;
  const iy = 4.25, ih = 2.4;
  const inds = [
    ["Pedidos completos y a tiempo", "76 → 90 %", "de los pedidos de la semana", "RESULTADO CLAVE", GREEN],
    ["Exactitud de stock", "9 de 10", "productos en tolerancia (propuesta, a confirmar)", "KPI PERMANENTE", GREY],
    ["Días con producción cargada", "20 → 100 %", "de los días hábiles", "RESULTADO CLAVE", GREEN],
    ["Horas extras por mes", "25 → 12-13", "horas por mes, totales", "RESULTADO CLAVE", GREEN],
  ];
  inds.forEach((d, i) => {
    const x = M + i * (aw + g);
    s.addShape(pres.ShapeType.roundRect, { x: x, y: iy, w: aw, h: ih, fill: { color: WHITE }, rectRadius: 0.08, line: { color: LINE, width: 1 } });
    s.addShape(pres.ShapeType.rect, { x: x, y: iy + 0.16, w: 0.06, h: 0.3, fill: { color: d[4] }, line: { color: d[4], width: 0 } });
    s.addText(d[3], {
      x: x + 0.22, y: iy + 0.18, w: aw - 0.44, h: 0.25, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 10, bold: true, charSpacing: 1.5, color: d[4], valign: "middle",
    });
    s.addText(d[0], {
      x: x + 0.22, y: iy + 0.48, w: aw - 0.44, h: 0.6, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 14, bold: true, color: DARK, valign: "top",
    });
    s.addText(d[1], {
      x: x + 0.22, y: iy + 1.1, w: aw - 0.3, h: 0.7, isTextBox: true, margin: 0, fit: "shrink",
      fontFace: H, fontSize: 28, bold: true, color: d[4] === GREY ? DARK : GREEN, valign: "middle",
    });
    s.addText(d[2], {
      x: x + 0.22, y: iy + 1.82, w: aw - 0.44, h: 0.45, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 13, color: GREY, valign: "top",
    });
  });
  pie(s);
  s.addNotes("Manuel. Es un roadmap y no un Gantt: detalla lo próximo y deja abierto lo lejano, porque la activación depende de lo que muestre el piloto. Hay un solo Go/No-Go grande, al terminar el piloto, y después cada línea se activa con las mismas medidas. El OKR tiene tres resultados clave, que son los objetivos específicos. La exactitud de stock no es resultado clave: su línea de base todavía no existe, sale del conteo inicial, y es una condición que tiene que estar siempre bien: un KPI permanente. La meta de 9 de cada 10 productos en tolerancia es una propuesta nuestra, a confirmar con el conteo inicial.");
}

/* 10 - Cierre */
{
  const s = nuevo(DARK);
  titulo(s, "LA PROPUESTA", { color: CREAM });
  s.addText("Primero se mira qué hay.\nDespués se confirma.", {
    x: M, y: 1.18, w: CW, h: 1.3, isTextBox: true, margin: 0,
    fontFace: H, fontSize: 32, bold: true, color: ORANGE, valign: "middle", lineSpacing: 38,
  });
  const cw3 = (CW - 2 * 0.35) / 3;
  const puntos = [
    ["1", "Corregimos la Parte 1", "El stock no se registra y, según nuestro supuesto, los recortes vendrían de la mezcla y el momento de producción."],
    ["2", "B, probada antes con A", "El stock de Discovery como solución. Una planilla de 2 semanas lo prueba antes de gastar."],
    ["3", "Se mide y decide el dueño", "Cuatro indicadores y un OKR. El dueño decide con umbrales a acordar antes del piloto."],
  ];
  puntos.forEach((p, i) => {
    const x = M + i * (cw3 + 0.35);
    s.addShape(pres.ShapeType.roundRect, {
      x: x, y: 2.75, w: cw3, h: 2.95, fill: { color: "22353F" }, rectRadius: 0.1,
    });
    circulo(s, p[0], x + 0.32, 3.0, 0.6, ORANGE, DARK);
    s.addText(p[1], {
      x: x + 0.32, y: 3.8, w: cw3 - 0.64, h: 0.5, isTextBox: true, margin: 0,
      fontFace: H, fontSize: 17, bold: true, color: CREAM, valign: "top",
    });
    s.addText(p[2], {
      x: x + 0.32, y: 4.35, w: cw3 - 0.64, h: 1.2, isTextBox: true, margin: 0,
      fontFace: B, fontSize: 14, color: PALE, valign: "top",
    });
  });
  s.addText("Lo que todavía no sabemos: el costo de la hora extra y de activar el módulo. Sin esos dos datos no hay VAN, hay punto de equilibrio.", {
    x: M, y: 5.95, w: CW, h: 0.6, isTextBox: true, margin: 0,
    fontFace: B, fontSize: 15, italic: true, color: PALE, valign: "middle",
  });
  pie(s, MUTED);
  s.addNotes("Manuel. Cerrar con la frase. Después, las preguntas. Que los recortes vengan de la mezcla y el momento es un supuesto nuestro: decirlo así. El punto de equilibrio: si el costo mensual de B dividido el costo de la hora extra da menos de unas 12 o 13 horas, se paga con la meta.");
}

pres.writeFile({ fileName: process.argv[2] || "Dulxelitos-Parte2.pptx" }).then((f) => console.log("listo:", f));
