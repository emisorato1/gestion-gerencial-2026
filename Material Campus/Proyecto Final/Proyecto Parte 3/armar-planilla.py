#!/usr/bin/env python3
"""Planilla del caso de negocio de la Parte 3 (Dulxelitos).

Genera, desde esta carpeta:

  Entrega/TP Final Parte 3 - Dulxelitos - Caso de negocio.xlsx
      planilla con formulas reales de Excel: todas las celdas derivadas salen
      de la hoja Supuestos (por nombres definidos, por ejemplo Hora_oficina).
  caso.json
      las mismas cifras calculadas en Python, para el dossier y la presentacion.

Uso (Python del venv de la Parte 2, que tiene openpyxl):

  ../"Proyecto Parte 2"/.venv/bin/python armar-planilla.py             # arma xlsx y json
  ../"Proyecto Parte 2"/.venv/bin/python armar-planilla.py --verificar # ademas, verifica en Excel

--verificar copia el xlsx al contenedor de Microsoft Excel (para que el sandbox
no pida permiso), lo abre por osascript, recalcula todo (calculate full), lee la
hoja "Cifras del informe" y compara cada valor con caso.json: tolerancia de 1
peso en montos, 0,01 en meses y fracciones, y 0,1 punto porcentual en las TIR.
Sale con codigo 1 si algo no coincide.

Modelo, en pocas palabras
  - Pesos constantes de noviembre de 2026; mes 1 = febrero de 2027 (semana 1 =
    1-2-2027); horizonte de 36 meses; meses de 52/12 semanas.
  - Cada costo de una vez se reparte entre las semanas en que ocurre; cada costo
    recurrente arranca cuando la linea queda en uso; cada beneficio arranca
    cuando termina la ventana de activacion de la linea (mas la demora del
    escenario). Las lineas pesan un tercio cada una.
  - Vista completa: el tiempo del personal se valora al costo de la hora (en
    costos y en el retrabajo evitado, que es capacidad liberada). Vista de
    caja: solo lo que sale o deja de salir de la caja (horas extras).
"""

import datetime
import json
import math
import os
import shutil
import subprocess
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName

BASE = os.path.dirname(os.path.abspath(__file__))
XLSX = os.path.join(BASE, "Entrega", "TP Final Parte 3 - Dulxelitos - Caso de negocio.xlsx")
JSON = os.path.join(BASE, "caso.json")
MESES = 36
INICIO = datetime.date(2027, 2, 1)
MESES_ES = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
            "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

# --- estilo (paleta de las Partes 1 y 2) -------------------------------------
DARK, CREAM, GREEN, BLUE, ORANGE, RED = "1B2B34", "F7F4EC", "2F6B5E", "1E5C85", "C8791E", "A33B22"
T_NEUTRAL, T_GREEN, T_BLUE, T_ORANGE, T_RED = "EFEADC", "DCEAE3", "DDE8EF", "F6EBD8", "F3DFD9"
LINE = "E2DCCC"
F_TITULO = Font(name="Calibri", size=14, bold=True, color=DARK)
F_SUB = Font(name="Calibri", size=10, italic=True, color="55636B")
F_HEAD = Font(name="Calibri", size=10, bold=True, color="FFFFFF")
F_SEC = Font(name="Calibri", size=10, bold=True, color=DARK)
F_NORM = Font(name="Calibri", size=10, color=DARK)
F_BOLD = Font(name="Calibri", size=10, bold=True, color=DARK)
F_INPUT = Font(name="Calibri", size=10, color=BLUE, bold=True)
F_NOTA = Font(name="Calibri", size=9, italic=True, color="55636B")
FILL_HEAD = PatternFill("solid", fgColor=DARK)
FILL_SEC = PatternFill("solid", fgColor=T_NEUTRAL)
FILL_TOT = PatternFill("solid", fgColor=CREAM)
FILL_TIPO = {"Dato": PatternFill("solid", fgColor=T_GREEN),
             "Estimación": PatternFill("solid", fgColor=T_BLUE),
             "Hipótesis": PatternFill("solid", fgColor=T_ORANGE),
             "Decisión": PatternFill("solid", fgColor=T_RED)}
BORDE = Border(bottom=Side(style="thin", color=LINE))
BORDE_TOT = Border(top=Side(style="thin", color=DARK), bottom=Side(style="thin", color=DARK))
WRAP = Alignment(wrap_text=True, vertical="top")
CENTRO = Alignment(horizontal="center", vertical="center", wrap_text=True)

FMT_PESOS = '"$" #,##0;[Red]-"$" #,##0;"–"'
FMT_PESOS0 = '"$" #,##0;[Red]-"$" #,##0;"$" 0'
FMT_PCT = '0 %'
FMT_PCT1 = '0.0 %'
FMT_NUM = '#,##0.##'
FMT_NUM1 = '#,##0.0'
FMT_NUM2 = '0.00'
FMT_FECHA = 'd/m/yyyy'
FMT_MES = 'mmm-yy'
FMT_MESLARGO = 'mmmm yyyy'

# =============================================================================
# 1. Supuestos
# Cada supuesto: (nombre, etiqueta, valor, formula_excel o None, unidad, tipo,
# fuente, formato). Si hay formula, el valor en Python se calcula aparte (abajo)
# y la verificacion en Excel confirma que coinciden.
# =============================================================================

S = {}          # nombre -> valor en Python
FILAS_SUP = []  # (seccion o fila)


def sec(titulo):
    FILAS_SUP.append(("sec", titulo))


def sup(nombre, etiqueta, valor, unidad, tipo, fuente, fmt=FMT_NUM, formula=None):
    S[nombre] = valor
    FILAS_SUP.append(("sup", nombre, etiqueta, valor, formula, unidad, tipo, fuente, fmt))


sec("Datos de la empresa")
sup("Pedidos_semana", "Pedidos de distribuidores por semana", 125, "pedidos/semana", "Dato",
    "Registro de Oficina de una semana (Parte 2, sección 2). Demanda estable en el año")
sup("Recortados_hoy", "Pedidos recortados o demorados por semana, hoy", 30, "pedidos/semana", "Dato",
    "Misma semana registrada (76 % completos y a tiempo). Que sea representativa es el supuesto 9: se vuelve a medir en las semanas 1 a 3")
sup("Hora_operario", "Hora normal de operario, con cargas sociales", 8000, "$/hora", "Dato",
    "Liquidación de sueldos, valor aproximado informado por el responsable de sistemas (noviembre de 2026)", FMT_PESOS)
sup("Hora_extra", "Hora extra (50 % más que la normal)", 12000, "$/hora", "Dato",
    "Liquidación de sueldos (noviembre de 2026)", FMT_PESOS)
sup("Hora_oficina", "Hora de Oficina o administrativa, con cargas", 10000, "$/hora", "Dato",
    "Liquidación de sueldos, valor aproximado (noviembre de 2026)", FMT_PESOS)
sup("HE_mes_hoy", "Horas extras por mes en toda la planta, hoy", 45, "horas/mes", "Dato",
    "Liquidación de sueldos: entre 40 y 50 por mes; usamos el medio. Todas son de Producción. En la Parte 2 figuraban unas 25: se relevó mejor")
sup("Retrabajo_h", "Retrabajo por cada pedido recortado (avisar, re-armar, facturar, coordinar)", 1, "horas/pedido", "Dato",
    "Oficina y Depósito, en horario normal; valor aproximado informado por la empresa")
sup("Pedido_promedio", "Pedido promedio de un distribuidor", 1200000, "$", "Dato",
    "Facturación, valor aproximado. No entra en el cálculo: la venta recortada se manda después y no se pierde", FMT_PESOS)
sup("Costo_modulo", "Activación y soporte del módulo de stock de Discovery", 0, "$", "Dato",
    "Incluido en la licencia vigente con Buenos Aires Software", FMT_PESOS0)
sup("Costo_juanjo", "Horas del responsable de sistemas (servicio externo) en el proyecto", 0, "$", "Dato",
    "Incluidas en lo que ya cobra por mes", FMT_PESOS0)
sup("Costo_equipos", "Equipos", 0, "$", "Dato",
    "Ya hay PC con Discovery en Producción y en Depósito", FMT_PESOS0)
sup("Personas_oficina", "Personas en Oficina", 4, "personas", "Dato", "Parte 2, sección 5")
sup("Personas_produccion", "Personas en Producción", 7, "personas", "Dato", "Parte 2, sección 5")
sup("Personas_deposito", "Personas en Depósito", 3, "personas", "Estimación",
    "La empresa tiene entre 15 y 20 personas; Depósito no se contó por separado")
sup("Personas_direccion", "Dirección: el dueño y sus dos hijos", 3, "personas", "Dato", "Parte 2, sección 5")

sec("Convenciones del cálculo")
sup("Sem_mes", "Semanas por mes", 52 / 12, "semanas", "Estimación",
    "52 semanas ÷ 12 meses", FMT_NUM2, "=52/12")
sup("Dias_semana", "Días hábiles por semana", 5, "días", "Dato",
    "Un turno de lunes a viernes: Producción de 6 a 15 h y Depósito de 8 a 18 h, 44 h semanales")
sup("Dias_mes", "Días hábiles por mes", 5 * 52 / 12, "días", "Estimación",
    "Días por semana × semanas por mes", FMT_NUM1, "=Dias_semana*Sem_mes")
sup("Hora_direccion", "Valor de la hora de la Dirección (dueño e hijos)", 10000, "$/hora", "Estimación",
    "No cobran por hora; la valoramos como la de Oficina para no dejar su tiempo afuera", FMT_PESOS)
sup("Hora_retrabajo", "Costo de la hora de retrabajo", 10000, "$/hora", "Estimación",
    "Mezcla de Oficina y Depósito; tomamos la hora de Oficina", FMT_PESOS, "=Hora_oficina")
sup("Hora_equipo", "Costo de una hora de todo el equipo reunido",
    S["Personas_oficina"] * S["Hora_oficina"] + S["Personas_direccion"] * S["Hora_direccion"]
    + (S["Personas_produccion"] + S["Personas_deposito"]) * S["Hora_operario"], "$/hora", "Estimación",
    "Oficina y Dirección a la hora de Oficina; Producción y Depósito a la de operario", FMT_PESOS,
    "=Personas_oficina*Hora_oficina+Personas_direccion*Hora_direccion+(Personas_produccion+Personas_deposito)*Hora_operario")
sup("Meta_completos", "Meta de pedidos completos y a tiempo", 0.90, "%", "Decisión",
    "Meta del proyecto desde la Parte 2 (de 76 % a 90 % en 6 meses). Que se alcance es la hipótesis del escenario esperado", FMT_PCT)
sup("Meta_HE", "Meta de reducción de las horas extras", 0.5, "%", "Decisión",
    "Meta del proyecto: la mitad (de 40 a 50 h a 20 a 25 h por mes). Queda como meta; el caso usa una estimación más prudente (escenarios)", FMT_PCT)
sup("Parte_HE_pedidos", "Parte de las horas extras que se hace para completar pedidos que faltaron", 0.5, "%", "Hipótesis",
    "Supuesto 7 de la Parte 2; la liquidación no separa causas", FMT_PCT)
sup("Tasa_anual", "Tasa de descuento real anual", 0.12, "%", "Decisión",
    "Elección del grupo: algo más de lo que rinde la caja en un plazo fijo ajustado por inflación y cerca de lo que costaría pedir prestado en pesos ajustados; con 20 % el VAN sigue positivo", FMT_PCT)
sup("Tasa_mensual", "Tasa de descuento real mensual equivalente", 1.12 ** (1 / 12) - 1, "%", "Estimación",
    "(1 + tasa anual) elevado a 1/12, menos 1", '0.000 %', "=(1+Tasa_anual)^(1/12)-1")
sup("Tasa_alta", "Tasa alternativa para la prueba de sensibilidad", 0.20, "%", "Decisión",
    "Para ver si el signo del VAN depende de la tasa elegida", FMT_PCT)

sec("Calendario (roadmap de la Parte 2, semana 1 = 1-2-2027)")
sup("Inicio", "Inicio de la semana 1", INICIO, "fecha", "Decisión",
    "Propuesta del grupo: después de fiestas y vacaciones; se corre si la aprobación se demora", FMT_FECHA)
sup("Base_desde", "Registro de la línea de base: desde la semana", 1, "semana", "Estimación", "Fase 1, preparación")
sup("Base_hasta", "Registro de la línea de base: hasta la semana", 3, "semana", "Estimación",
    "Tres semanas en lugar de una, para que la base no dependa de una sola semana (supuesto 9)")
sup("Sem_conteo_papas", "Conteo inicial de papas fritas y capacitación del piloto", 3, "semana", "Estimación",
    "Fin de semana anterior al piloto")
sup("Piloto_desde", "Piloto con papas fritas: desde la semana", 4, "semana", "Estimación", "Roadmap, fase 2")
sup("Piloto_hasta", "Piloto con papas fritas: hasta la semana", 5, "semana", "Estimación", "Roadmap, fase 2 (10 días hábiles)")
sup("Sem_go", "Decisión Go / Ajustar / Pausar", 6, "semana", "Estimación", "Roadmap, fase 3")
sup("Sal_desde", "Activación de Salados: desde la semana", 7, "semana", "Estimación",
    "Roadmap, fase 4 (semanas 7 a 22). Salados primero porque tiene las papas fritas")
sup("Sal_hasta", "Activación de Salados: hasta la semana", 12, "semana", "Estimación", "Seis semanas: la primera línea lleva más aprendizaje")
sup("Dul_desde", "Activación de Dulces: desde la semana", 13, "semana", "Estimación", "Roadmap, fase 4")
sup("Dul_hasta", "Activación de Dulces: hasta la semana", 17, "semana", "Estimación", "Cinco semanas")
sup("Rep_desde", "Activación de Repostería: desde la semana", 18, "semana", "Estimación", "Roadmap, fase 4")
sup("Rep_hasta", "Activación de Repostería: hasta la semana", 22, "semana", "Estimación", "Cinco semanas; la estabilización sigue hasta la semana 26")
sup("Sem_a_uso", "Semanas desde que empieza la ventana hasta que la línea queda en uso", 2, "semanas", "Estimación",
    "Semana 1: configurar productos; semana 2: conteo inicial el fin de semana y capacitación")
sup("Trans_semanas", "Semanas de doble registro al pasar cada línea a Discovery", 2, "semanas", "Estimación",
    "Conviven el control anterior y Discovery hasta comprobar que coinciden")
sup("Seg_desde", "Reunión semanal de seguimiento: desde la semana", 1, "semana", "Estimación", "Todo el proyecto")
sup("Seg_hasta", "Reunión semanal de seguimiento: hasta la semana", 26, "semana", "Estimación", "Fin de la estabilización")
sup("Reunion_desde", "Reunión diaria y tablero: desde la semana", 4, "semana", "Estimación", "Arrancan con el piloto y quedan")
sup("Parte_Sal", "Parte del beneficio y del trabajo que corresponde a Salados", 1 / 3, "%", "Hipótesis",
    "Sin registro de recortes por línea, repartimos en tercios. Papas fritas, el producto con más faltantes, es de Salados, así que es prudente", FMT_PCT)
sup("Parte_Dul", "Parte que corresponde a Dulces", 1 / 3, "%", "Hipótesis", "Ídem", FMT_PCT)
sup("Parte_Rep", "Parte que corresponde a Repostería", 1 / 3, "%", "Hipótesis", "Ídem", FMT_PCT)
for lin, nom in (("Sal", "Salados"), ("Dul", "Dulces"), ("Rep", "Repostería")):
    sup("Uso_" + lin, "%s queda en uso desde la semana" % nom, S[lin + "_desde"] + S["Sem_a_uso"], "semana",
        "Estimación", "Inicio de la ventana + semanas hasta quedar en uso", FMT_NUM, "=%s_desde+Sem_a_uso" % lin)
    sup("Ben_" + lin, "%s da beneficio desde la semana (esperado)" % nom, S[lin + "_hasta"] + 1, "semana",
        "Estimación", "La semana siguiente al cierre de su ventana: la producción ya se planifica mirando pedidos y stock", FMT_NUM,
        "=%s_hasta+1" % lin)

sec("Tiempo interno de la puesta en marcha (una vez)")
sup("Base_min", "Registro de la línea de base: minutos de Oficina por pedido", 1, "min/pedido", "Estimación",
    "Anotar si salió completo y a tiempo y, si no, la causa")
sup("CP_personas", "Conteo inicial de papas fritas: personas", 2, "personas", "Estimación", "Depósito y Producción, en fin de semana")
sup("CP_horas", "Conteo inicial de papas fritas: horas", 2, "horas", "Estimación", "Un solo producto, en horas extras")
sup("CapP_personas_op", "Capacitación del piloto: operarios", 2, "personas", "Estimación", "Responsable de carga de Producción y suplente (sección 5)")
sup("CapP_horas_op", "Capacitación del piloto: horas por operario", 1, "horas", "Estimación", "Práctica con la producción del día anterior en la PC de Producción")
sup("CapP_resto_min", "Capacitación del piloto: minutos para el resto de Producción", 15, "min/persona", "Estimación",
    "Al empezar el piloto, las personas de Producción que no cargan")
sup("CapP_personas_of", "Capacitación del piloto: personas de Oficina", 2, "personas", "Estimación", "Encargada/o de Oficina y segunda persona")
sup("CapP_horas_of", "Capacitación del piloto: horas por persona de Oficina", 2, "horas", "Estimación", "Dos sesiones de 1 hora con los casos de prueba reales")
sup("CapP_personas_dep", "Capacitación del piloto: personas de Depósito", 2, "personas", "Estimación", "Titular y suplente del conteo")
sup("CapP_horas_dep", "Capacitación del piloto: horas por persona de Depósito", 1, "horas", "Estimación", "Hoja de conteo y armado con la lista")
sup("CapP_personas_dir", "Capacitación del piloto: Dirección", 3, "personas", "Estimación", "El dueño y los dos hijos: leer el tablero y decidir la producción",
    FMT_NUM, "=Personas_direccion")
sup("CapP_horas_dir", "Capacitación del piloto: horas por persona de Dirección", 1, "horas", "Estimación", "Práctica con los datos de la semana 0")
sup("Pil_min_of", "Piloto: minutos diarios extra de Oficina", 25, "min/día", "Estimación",
    "Reservar en la planilla y descontar a mano al facturar (la planilla no está conectada con Discovery)")
sup("Pil_min_prod", "Piloto: minutos diarios de carga de Producción", 10, "min/día", "Estimación", "Un solo producto")
sup("Pil_conteo_hp", "Piloto: conteo semanal de papas fritas", 1, "horas-persona/semana", "Estimación", "Dos personas, media hora")
sup("Pil_dias", "Piloto: días hábiles", 10, "días", "Estimación", "Dos semanas")
sup("Cfg_h_of", "Por línea: horas de Oficina para revisar productos y unidades en Discovery", 2, "horas", "Estimación",
    "La configuración la hace el responsable de sistemas, sin costo extra")
sup("CL_personas", "Por línea: personas en el conteo inicial", 3, "personas", "Estimación", "Depósito y Producción, fin de semana")
sup("CL_horas", "Por línea: horas del conteo inicial", 3, "horas", "Estimación", "En horas extras; no cuentan en el indicador de horas extras")
sup("CapL_op", "Por línea: operarios que se capacitan", 2, "personas", "Estimación", "Responsable de carga y suplente de esa línea")
sup("CapL_h_op", "Por línea: horas de capacitación por operario", 1.5, "horas", "Estimación", "Práctica con la producción real del día")
sup("CapL_of", "Por línea: personas de Oficina que se capacitan", 2, "personas", "Estimación", "Reservar y consultar los productos de la línea")
sup("CapL_h_of", "Por línea: horas de capacitación de Oficina", 1, "horas", "Estimación",
    "Incluye el repaso de 30 minutos del instructivo al activar cada línea")
sup("Tr_min_of", "Doble registro: minutos diarios extra de Oficina", 15, "min/día", "Estimación", "Cotejar lo reservado con el control anterior")
sup("Tr_min_prod", "Doble registro: minutos diarios extra de Producción", 10, "min/día", "Estimación", "Cargar en los dos lados")
sup("Seg_min", "Reunión semanal de seguimiento: minutos", 20, "min", "Estimación", "Tablero pendiente / en curso / listo")
sup("Seg_dir", "Reunión semanal de seguimiento: Dirección", 1, "personas", "Estimación", "El hijo responsable del proyecto (sección 3)")
sup("Seg_of", "Reunión semanal de seguimiento: Oficina", 2, "personas", "Estimación",
    "El referente de Oficina y el suplente interno de sistemas; el responsable de sistemas, sin costo")
sup("Seg_planta", "Reunión semanal de seguimiento: Producción y Depósito", 2, "personas", "Estimación", "Un referente de cada área")
sup("Com_anuncio_min", "Comunicación: anuncio con todo el equipo", 15, "min", "Estimación",
    "Semana 1, dueño e hijo responsable, entre las 8 y las 15 h (sección 5)")
sup("Com_grupos_min", "Comunicación: diez minutos con cada grupo en su puesto", 10, "min", "Estimación",
    "Semanas 1 y 2; equivale a 10 minutos de todo el equipo")
sup("Com_dia5_min", "Comunicación: reunión del día 5 del piloto", 15, "min", "Estimación", "Todo el equipo, en la planta")
sup("Com_go_min", "Comunicación: resultado y decisión de la semana 6", 15, "min", "Estimación", "Todo el equipo, en la planta")
sup("Com_aviso_min", "Comunicación: aviso al activar cada línea y en los meses 3 y 6", 5, "min", "Estimación", "Todo el equipo, en la planta")
sup("Com_avisos", "Comunicación: cantidad de avisos posteriores al Go", 5, "avisos", "Estimación", "Uno por línea y los de los meses 3 y 6")

sec("Tiempo interno recurrente (con las tres líneas en uso)")
sup("Carga_min", "Carga diaria de lo producido en Discovery", 20, "min/día", "Estimación",
    "Responsable de carga de Producción, de 14:40 a 15:00, dentro del turno de 6 a 15 h: unos 15 a 20 productos por día, "
    "un minuto cada uno. Si genera horas extras, es Ajustar. Se mide en las semanas 1 a 5")
sup("Reu_min", "Reunión diaria entre ventas y producción", 10, "min/día", "Estimación",
    "Tres personas: Oficina, Producción y Dirección")
sup("Res_min", "Cargar el pedido y reservar en Discovery", 3, "min/pedido", "Estimación",
    "Oficina, en cada pedido. Se mide en el piloto (semanas 4 y 5)")
sup("Rev_min", "Revisión diaria de reservas", 10, "min/día", "Estimación",
    "Oficina libera reservas de pedidos cancelados y revisa fechas prometidas")
sup("Cto_personas", "Conteo semanal: personas", 2, "personas", "Estimación", "Depósito")
sup("Cto_horas", "Conteo semanal: horas", 1.5, "horas/semana", "Estimación", "Producto terminado de las tres líneas")
sup("Tab_min", "Registro de pedidos completos y tablero semanal", 30, "min/semana", "Estimación", "Oficina")
sup("Ctrl_h", "Control semanal de Producción que se deja de hacer", 1.5, "horas/semana", "Estimación",
    "Hoy Producción carga lo de la semana una vez; la carga diaria lo reemplaza")
sup("Av_min_of", "Averiguación doble que se deja de hacer: minutos de Oficina por pedido", 1.5, "min/pedido", "Estimación",
    "Hoy Oficina pregunta a Producción y Depósito mira el stock; pasa a ser una sola consulta")
sup("Av_min_planta", "Averiguación doble que se deja de hacer: minutos de Producción o Depósito por pedido", 1.5, "min/pedido",
    "Estimación", "Quien responde la pregunta o mira la estantería")
sup("Copias_min", "Copias del pedido que se dejan de hacer: minutos de Oficina por pedido", 2, "min/pedido", "Estimación",
    "Hoy el pedido se anota tres veces (mensaje, papel o planilla y lista; Parte 2, sección 2). La nota en Discovery reemplaza "
    "las dos copias a mano, de alrededor de un minuto cada una. Se mide en las semanas 1 a 5")

sec("Sensibilidades (no entran en los escenarios)")
sup("Retrabajo_sens", "Retrabajo por pedido recortado, si fuera menor", 0.5, "horas/pedido", "Hipótesis",
    "La mitad del dato de la empresa. Se mide en las semanas 1 a 3, con la línea de base")
sup("Res_sens", "Cargar el pedido y reservar, si llevara más", 5, "min/pedido", "Hipótesis", "Se mide en el piloto")
sup("Hora_juanjo", "Hora del responsable de sistemas, si se valorara", 10000, "$/hora", "Hipótesis",
    "Hoy sin costo extra (dato); la valoramos como la de Oficina para ver si el caso depende de eso", FMT_PESOS)
sup("Jj_h_piloto", "Horas del responsable de sistemas en las semanas 1 a 5", 20, "horas", "Estimación",
    "Planilla y tablero, consulta al proveedor, prueba técnica, primera capacitación de cada grupo, primer conteo y soporte del piloto")
sup("Jj_h_linea", "Horas del responsable de sistemas por línea", 6, "horas", "Estimación",
    "Configurar productos, cargar el stock inicial y repetir los casos de prueba")

# Supuestos que cambian entre escenarios: (nombre, etiqueta, esperado, conservador,
# formula esperado, formula conservador, unidad, tipo, fuente, formato)
ESC = []


def esc(nombre, etiqueta, v_esp, v_con, f_esp, f_con, unidad, tipo, fuente, fmt):
    S[nombre + "_esp"] = v_esp
    S[nombre + "_con"] = v_con
    ESC.append((nombre, etiqueta, v_esp, v_con, f_esp, f_con, unidad, tipo, fuente, fmt))


_rec_esp = S["Pedidos_semana"] * (1 - S["Meta_completos"])
esc("Recortados", "Pedidos recortados o demorados por semana con la propuesta",
    _rec_esp, S["Recortados_hoy"] - (S["Recortados_hoy"] - _rec_esp) / 2,
    "=Pedidos_semana*(1-Meta_completos)", "=Recortados_hoy-(Recortados_hoy-Recortados_esp)/2",
    "pedidos/semana", "Hipótesis",
    "Esperado: la meta del 90 % (125 × 10 %). Conservador: la mitad de esa mejora", FMT_NUM)
_red = {e: S["Parte_HE_pedidos"] * (S["Recortados_hoy"] - S["Recortados_" + e]) / S["Recortados_hoy"] for e in ("esp", "con")}
esc("RedHE", "Reducción de las horas extras", _red["esp"], _red["con"],
    "=Parte_HE_pedidos*(Recortados_hoy-Recortados_esp)/Recortados_hoy",
    "=Parte_HE_pedidos*(Recortados_hoy-Recortados_con)/Recortados_hoy", "%", "Hipótesis",
    "La mitad ligada a pedidos (supuesto 7) baja en la misma proporción que los recortados. La meta del proyecto (la mitad de las "
    "horas extras) queda como meta; el caso usa esta estimación, más prudente", FMT_PCT1)
esc("Demora", "Demora adicional del efecto", 0, 8, None, None, "semanas", "Hipótesis",
    "Conservador: unos dos meses más hasta que se note cada línea; los costos quedan en su fecha", FMT_NUM)
esc("Cont", "Contingencia sobre la puesta en marcha", 0.15, 0.20, None, None, "%", "Estimación",
    "Imprevistos: más horas de conteo, una línea que se repite", FMT_PCT)

# =============================================================================
# 2. Modelo en Python
# =============================================================================
SM = S["Sem_mes"]


def ov(ini, fin, a, b):
    return max(0.0, min(fin, b) - max(ini, a))


def ventana(total, s, e, ini, fin):
    """Monto de una vez repartido entre las semanas s a e (inclusive)."""
    return total / (e - s + 1) * ov(ini, fin, s - 1, e)


def desde(s, ini, fin):
    """Parte del mes en que ya rige algo que arranca en la semana s."""
    return max(0.0, min(1.0, (fin - (s - 1)) / SM))


LINEAS = ("Sal", "Dul", "Rep")
ped_mes = S["Pedidos_semana"] * SM


def ev(expr):
    """Valor en Python de una expresion de Excel sobre nombres de Supuestos (por ejemplo 'Sal_desde+1')."""
    return eval(expr, {"__builtins__": {}}, S)


# Costos de una vez (por vez) y recurrentes (por mes, pleno)
C = {}
C["base"] = S["Base_min"] / 60 * S["Pedidos_semana"] * (S["Base_hasta"] - S["Base_desde"] + 1) * S["Hora_oficina"]
C["conteo_papas"] = S["CP_personas"] * S["CP_horas"] * S["Hora_extra"]
C["cap_piloto"] = (S["CapP_personas_op"] * S["CapP_horas_op"] * S["Hora_operario"]
                   + (S["Personas_produccion"] - S["CapP_personas_op"]) * S["CapP_resto_min"] / 60 * S["Hora_operario"]
                   + S["CapP_personas_of"] * S["CapP_horas_of"] * S["Hora_oficina"]
                   + S["CapP_personas_dep"] * S["CapP_horas_dep"] * S["Hora_operario"]
                   + S["CapP_personas_dir"] * S["CapP_horas_dir"] * S["Hora_direccion"])
C["piloto"] = S["Pil_dias"] * (S["Pil_min_of"] / 60 * S["Hora_oficina"] + S["Pil_min_prod"] / 60 * S["Hora_operario"]) \
    + S["Pil_conteo_hp"] * S["Hora_operario"] * (S["Piloto_hasta"] - S["Piloto_desde"] + 1)
C["com_piloto"] = (S["Com_anuncio_min"] + S["Com_grupos_min"] + S["Com_dia5_min"] + S["Com_go_min"]) / 60 * S["Hora_equipo"]
C["config"] = S["Cfg_h_of"] * S["Hora_oficina"]
C["conteo_linea"] = S["CL_personas"] * S["CL_horas"] * S["Hora_extra"]
C["cap_linea"] = S["CapL_op"] * S["CapL_h_op"] * S["Hora_operario"] + S["CapL_of"] * S["CapL_h_of"] * S["Hora_oficina"]
C["trans"] = S["Trans_semanas"] * S["Dias_semana"] * (S["Tr_min_of"] / 60 * S["Hora_oficina"] + S["Tr_min_prod"] / 60 * S["Hora_operario"])
C["com_lineas"] = S["Com_aviso_min"] * S["Com_avisos"] / 60 * S["Hora_equipo"]
C["seg"] = (S["Seg_hasta"] - S["Seg_desde"] + 1) * S["Seg_min"] / 60 * (
    S["Seg_dir"] * S["Hora_direccion"] + S["Seg_of"] * S["Hora_oficina"] + S["Seg_planta"] * S["Hora_operario"])

# Cada costo de una vez: (clave, etiqueta, ventanas). Cada ventana (desde, hasta) es un par de
# expresiones de Excel sobre los Supuestos; el costo "por vez" se reparte entre esas semanas.
UNA = [
    ("base", "Registro de la línea de base", [("Base_desde", "Base_hasta")]),
    ("conteo_papas", "Conteo inicial de papas fritas (horas extras)", [("Sem_conteo_papas", "Sem_conteo_papas")]),
    ("cap_piloto", "Capacitación para el piloto", [("Sem_conteo_papas", "Sem_conteo_papas")]),
    ("piloto", "Tiempo adicional del piloto", [("Piloto_desde", "Piloto_hasta")]),
    ("com_piloto", "Comunicación del piloto (anuncio, grupos, día 5 y resultado)", [("Seg_desde", "Sem_go")]),
    ("config", "Revisión de productos en Discovery, por línea", [(l + "_desde", l + "_desde") for l in LINEAS]),
    ("conteo_linea", "Conteo inicial por línea (horas extras)", [(l + "_desde+1", l + "_desde+1") for l in LINEAS]),
    ("cap_linea", "Capacitación por línea", [(l + "_desde+1", l + "_desde+1") for l in LINEAS]),
    ("trans", "Doble registro al pasar cada línea", [("Uso_" + l, "Uso_%s+Trans_semanas-1" % l) for l in LINEAS]),
    ("com_lineas", "Avisos al activar cada línea y en los meses 3 y 6", [("Sal_desde", "Seg_hasta")]),
    ("seg", "Reunión semanal de seguimiento", [("Seg_desde", "Seg_hasta")]),
]
EFECTIVO_KEYS = ("conteo_papas", "conteo_linea")
UNA_VEZ_TOTAL = sum(C[k] * len(w) for k, _, w in UNA)
EFECTIVO_TOTAL = sum(C[k] * len(w) for k, _, w in UNA if k in EFECTIVO_KEYS)

# Sensibilidad: horas del responsable de sistemas valoradas (hoy no tienen costo extra)
CJ = {"jj_piloto": S["Jj_h_piloto"] * S["Hora_juanjo"],
      "jj_linea": S["Jj_h_linea"] * S["Hora_juanjo"],
      "jj_seg": (S["Seg_hasta"] - S["Seg_desde"] + 1) * S["Seg_min"] / 60 * S["Hora_juanjo"]}
JJ = [("jj_piloto", [("Seg_desde", "Piloto_hasta")]),
      ("jj_linea", [(l + "_desde", l + "_desde+1") for l in LINEAS]),
      ("jj_seg", [("Seg_desde", "Seg_hasta")])]
JJ_TOTAL = sum(CJ[k] * len(w) for k, w in JJ)
JJ_HORAS = S["Jj_h_piloto"] + 3 * S["Jj_h_linea"] + (S["Seg_hasta"] - S["Seg_desde"] + 1) * S["Seg_min"] / 60

R = {}
R["carga"] = S["Carga_min"] / 60 * S["Hora_operario"] * S["Dias_mes"]
R["reunion"] = S["Reu_min"] / 60 * (S["Hora_oficina"] + S["Hora_operario"] + S["Hora_direccion"]) * S["Dias_mes"]
R["reserva"] = S["Res_min"] / 60 * S["Hora_oficina"] * ped_mes
R["revision"] = S["Rev_min"] / 60 * S["Hora_oficina"] * S["Dias_mes"]
R["conteo"] = S["Cto_personas"] * S["Cto_horas"] * S["Hora_operario"] * SM
R["tablero"] = S["Tab_min"] / 60 * S["Hora_oficina"] * SM
R["ctrl"] = -S["Ctrl_h"] * S["Hora_operario"] * SM
R["averig"] = -(S["Av_min_of"] / 60 * S["Hora_oficina"] + S["Av_min_planta"] / 60 * S["Hora_operario"]) * ped_mes
R["copias"] = -S["Copias_min"] / 60 * S["Hora_oficina"] * ped_mes
REC_NETO = sum(R.values())
REC_POR_LINEA = ("carga", "reserva", "revision", "conteo", "ctrl", "averig", "copias")
REC_FIJO = ("reunion", "tablero")
# minutos de Producción por día que, si la planta no los absorbe, irían a horas extras
PROD_MIN_DIA = S["Carga_min"] + S["Reu_min"]
R_PROD_HE = PROD_MIN_DIA / 60 * S["Hora_extra"] * S["Dias_mes"]
# horas por mes del proceso nuevo, de lo que reemplaza y del retrabajo evitado
H_NUEVAS = ((S["Carga_min"] + 3 * S["Reu_min"] + S["Rev_min"]) / 60 * S["Dias_mes"] + S["Res_min"] / 60 * ped_mes
            + S["Cto_personas"] * S["Cto_horas"] * SM + S["Tab_min"] / 60 * SM)
H_REEMPL = S["Ctrl_h"] * SM + (S["Av_min_of"] + S["Av_min_planta"] + S["Copias_min"]) / 60 * ped_mes

B = {}
B["hemeta"] = S["HE_mes_hoy"] * S["Meta_HE"] * S["Hora_extra"]
for e in ("esp", "con"):
    evitados = S["Recortados_hoy"] - S["Recortados_" + e]
    B["retrabajo_" + e] = evitados * S["Retrabajo_h"] * S["Hora_retrabajo"] * SM
    B["he_" + e] = S["HE_mes_hoy"] * S["RedHE_" + e] * S["Hora_extra"]
    B["hhe_" + e] = S["HE_mes_hoy"] * S["RedHE_" + e]
    B["hrt_" + e] = evitados * S["Retrabajo_h"] * SM


def repartir(monto, ventanas, ini, fin):
    return sum(ventana(monto, ev(s), ev(e), ini, fin) for s, e in ventanas)


def modelo():
    meses = []
    for m in range(1, MESES + 1):
        ini, fin = (m - 1) * SM, m * SM
        f_uso = sum(S["Parte_" + l] * desde(S["Uso_" + l], ini, fin) for l in LINEAS)
        f_fijo = desde(S["Reunion_desde"], ini, fin)
        f_ben = {e: sum(S["Parte_" + l] * desde(S["Ben_" + l] + S["Demora_" + e], ini, fin) for l in LINEAS)
                 for e in ("esp", "con")}
        una = {k: repartir(C[k], w, ini, fin) for k, _, w in UNA}
        jj = sum(repartir(CJ[k], w, ini, fin) for k, w in JJ)
        rec = {k: R[k] * (f_uso if k in REC_POR_LINEA else f_fijo) for k in R}
        una_sub = sum(una.values())
        rec_sub = sum(rec.values())
        efectivo = sum(una[k] for k in EFECTIVO_KEYS)
        fila = {"m": m, "f_uso": f_uso, "f_fijo": f_fijo, "una": una, "rec": rec, "jj": jj,
                "una_sub": una_sub, "rec_sub": rec_sub, "efectivo": efectivo}
        for e in ("esp", "con"):
            cont = S["Cont_" + e] * una_sub
            costos = una_sub + cont + rec_sub
            b_rt = B["retrabajo_" + e] * f_ben[e]
            b_he = B["he_" + e] * f_ben[e]
            b_meta = B["hemeta"] * f_ben[e]
            caja_out = efectivo * (1 + S["Cont_" + e])
            neto = b_rt + b_he - costos
            caja = b_he - caja_out
            fila[e] = {
                "f_ben": f_ben[e], "cont": cont, "costos": costos, "b_rt": b_rt, "b_he": b_he, "b_meta": b_meta,
                "beneficios": b_rt + b_he, "neto": neto, "caja_out": caja_out, "caja": caja,
                "neto_meta": b_rt + b_meta - costos, "caja_meta": b_meta - caja_out,
                "caja_prod": caja - R_PROD_HE * f_uso,
                "neto_rt05": neto - b_rt * (1 - S["Retrabajo_sens"] / S["Retrabajo_h"]),
                "neto_res5": neto - R["reserva"] * (S["Res_sens"] / S["Res_min"] - 1) * f_uso,
                "neto_sincop": neto + R["copias"] * f_uso,
                "neto_jj": neto - jj, "caja_jj": caja - jj,
            }
        meses.append(fila)
    return meses


def acumular(flujos):
    out, s = [], 0.0
    for f in flujos:
        s += f
        out.append(s)
    return out


def recupero(saldos):
    neg = sum(1 for s in saldos if s < 0)
    # el saldo es negativo de corrido desde el mes 1 y despues queda positivo
    assert all(s < 0 for s in saldos[:neg]) and all(s >= 0 for s in saldos[neg:]), saldos
    return None if neg == len(saldos) else neg + 1


def van(flujos, r):
    return sum(f / (1 + r) ** t for t, f in enumerate(flujos, 1))


def tir_mensual(flujos):
    lo, hi = -0.99, 50.0
    if van(flujos, lo) * van(flujos, hi) > 0:
        return None
    for _ in range(300):
        mid = (lo + hi) / 2
        if van(flujos, lo) * van(flujos, mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def mes_nombre(n):
    d = datetime.date(INICIO.year + (INICIO.month - 1 + n - 1) // 12, (INICIO.month - 1 + n - 1) % 12 + 1, 1)
    return "%s de %d" % (MESES_ES[d.month - 1], d.year)


MODELO = modelo()
RM = S["Tasa_mensual"]
RM_ALTA = (1 + S["Tasa_alta"]) ** (1 / 12) - 1


def indicadores(serie):
    sal = acumular(serie)
    rec = recupero(sal)
    tm = tir_mensual(serie)
    return {
        "max_expuesto": -min(0.0, min(sal)),
        "recupero": rec,
        "recupero_mes": mes_nombre(rec) if rec else None,
        "van": van(serie, RM),
        "van_alta": van(serie, RM_ALTA),
        "tir_mensual": tm,
        "tir_anual": (1 + tm) ** 12 - 1 if tm is not None else None,
        "anual": [sum(serie[i * 12:(i + 1) * 12]) for i in range(3)],
        "saldos": sal,
    }


VISTAS = {"neto": "completa", "caja": "caja",
          "neto_meta": "completa, si se cumple la meta de horas extras",
          "caja_meta": "caja, si se cumple la meta de horas extras",
          "caja_prod": "caja, tiempo nuevo de Producción en horas extras",
          "neto_rt05": "completa, retrabajo de media hora por recortado",
          "neto_res5": "completa, 5 minutos por reserva",
          "neto_sincop": "completa, sin el ahorro de las copias del pedido",
          "neto_jj": "completa, horas del responsable de sistemas valoradas",
          "caja_jj": "caja, horas del responsable de sistemas cobradas aparte"}
# sufijo de las claves de caso.json para cada vista
SUFIJO = {"neto": "", "caja": "_caja", "neto_meta": "_meta", "caja_meta": "_caja_meta", "caja_prod": "_caja_prod",
          "neto_rt05": "_rt05", "neto_res5": "_res5", "neto_sincop": "_sincop", "neto_jj": "_jj", "caja_jj": "_caja_jj"}
IND = {(v, e): indicadores([f[e][v] for f in MODELO]) for v in VISTAS for e in ("esp", "con")}


def una_hasta(semana):
    """Costos de una vez (sin contingencia) de las semanas 1 a `semana`."""
    return sum(repartir(C[k], w, 0, semana) for k, _, w in UNA)


def rec_hasta(semana):
    """Tiempo interno recurrente de las semanas 1 a `semana`."""
    fijo = sum(R[k] for k in REC_FIJO) * ov(0, semana, S["Reunion_desde"] - 1, 1e9) / SM
    lin = sum(R[k] for k in REC_POR_LINEA) * sum(S["Parte_" + l] * ov(0, semana, S["Uso_" + l] - 1, 1e9) for l in LINEAS) / SM
    return fijo + lin


def costo_hasta(semana, e):
    """Costos (vista completa) de las semanas 1 a `semana`, con contingencia."""
    return una_hasta(semana) * (1 + S["Cont_" + e]) + rec_hasta(semana)


def efectivo_hasta(semana, e):
    t = sum(repartir(C[k], w, 0, semana) for k, _, w in UNA if k in EFECTIVO_KEYS)
    return t * (1 + S["Cont_" + e])


# =============================================================================
# 3. Cifras para el informe (claves de caso.json)
# =============================================================================

def r0(x):
    return None if x is None else int(round(x))


def r4(x):
    return None if x is None else round(x, 4)


CIFRAS = []  # (clave, descripcion, valor, tipo: pesos|meses|pct|num|texto)


def cifra(clave, desc, valor, tipo):
    CIFRAS.append((clave, desc, valor, tipo))


cifra("tasa_descuento_real_anual", "Tasa de descuento real anual", S["Tasa_anual"], "pct")
cifra("inversion_total_esperado", "Puesta en marcha completa (semanas 1 a 26), esperado, con 15 % de contingencia",
      UNA_VEZ_TOTAL * (1 + S["Cont_esp"]), "pesos")
cifra("inversion_total_conservador", "Puesta en marcha completa (semanas 1 a 26), conservador, con 20 % de contingencia",
      UNA_VEZ_TOTAL * (1 + S["Cont_con"]), "pesos")
cifra("puesta_en_marcha_sin_contingencia", "Puesta en marcha completa, sin contingencia", UNA_VEZ_TOTAL, "pesos")
cifra("conteo_inicial_tres_lineas", "Conteo inicial de las tres líneas (horas extras), sin contingencia", 3 * C["conteo_linea"], "pesos")
cifra("activacion_resto_tres_lineas", "Capacitación, revisión de productos y doble registro de las tres líneas, sin contingencia",
      3 * (C["cap_linea"] + C["config"] + C["trans"]), "pesos")
cifra("inversion_piloto_conservador", "Tope del piloto: costo de las semanas 1 a 6 (fases 1 a 3), conservador, vista completa",
      costo_hasta(S["Sem_go"], "con"), "pesos")
cifra("efectivo_piloto_conservador", "Del tope del piloto, lo que sale de la caja (horas extras del conteo)",
      efectivo_hasta(S["Sem_go"], "con"), "pesos")
cifra("techo_proyecto_conservador", "Techo del proyecto: costo de las semanas 1 a 26, conservador, vista completa, sin restar beneficios",
      costo_hasta(S["Seg_hasta"], "con"), "pesos")
cifra("efectivo_proyecto_conservador", "Del techo del proyecto, lo que sale de la caja (horas extras de los conteos)",
      efectivo_hasta(S["Seg_hasta"], "con"), "pesos")
cifra("tope_una_vez_conservador", "Del tope del piloto: costos de una vez de las semanas 1 a 6, sin contingencia",
      una_hasta(S["Sem_go"]), "pesos")
cifra("tope_contingencia_conservador", "Del tope del piloto: contingencia del conservador sobre esos costos",
      una_hasta(S["Sem_go"]) * S["Cont_con"], "pesos")
cifra("tope_recurrente_conservador", "Del tope del piloto: reunión diaria y tablero de las semanas 4 a 6",
      rec_hasta(S["Sem_go"]), "pesos")
cifra("techo_recurrente_conservador", "Del techo del proyecto: tiempo interno recurrente de las semanas 4 a 26 (lo demás es la puesta en marcha con 20 %)",
      rec_hasta(S["Seg_hasta"]), "pesos")
cifra("comunicacion_capacitacion", "Comunicación, capacitación del piloto y de las líneas, y reunión semanal, sin contingencia",
      C["com_piloto"] + C["com_lineas"] + C["cap_piloto"] + 3 * C["cap_linea"] + C["seg"], "pesos")
cifra("costo_recurrente_neto_mensual", "Tiempo interno nuevo por mes, neto de lo que reemplaza (tres líneas en uso)", REC_NETO, "pesos")
cifra("costo_recurrente_nuevo_mensual", "Tiempo interno nuevo por mes, antes de restar lo que reemplaza",
      sum(v for v in R.values() if v > 0), "pesos")
cifra("costo_recurrente_reemplazado_mensual", "Tiempo que se deja de usar por mes (control semanal, averiguación doble y copias del pedido)",
      -sum(v for v in R.values() if v < 0), "pesos")
cifra("horas_nuevas_mes", "Horas por mes que agregan las tareas nuevas (tres líneas en uso)", H_NUEVAS, "num")
cifra("horas_reemplazadas_mes", "Horas por mes de las tareas que se dejan", H_REEMPL, "num")
cifra("horas_juanjo_plan", "Horas que el plan le asigna al responsable de sistemas (semanas 1 a 26)", JJ_HORAS, "num")
cifra("costo_juanjo_sens", "Esas horas valoradas a la hora de la sensibilidad", JJ_TOTAL, "pesos")
for e, n in (("esp", "esperado"), ("con", "conservador")):
    cifra("recortados_semana_" + n, "Pedidos recortados o demorados por semana con la propuesta, " + n, S["Recortados_" + e], "num")
    cifra("retrabajo_evitado_mensual_" + n, "Capacidad liberada por retrabajo evitado, por mes, " + n, B["retrabajo_" + e], "pesos")
    cifra("horas_retrabajo_evitado_mes_" + n, "Horas de retrabajo evitado por mes, " + n, B["hrt_" + e], "num")
    cifra("horas_extras_evitadas_mensual_" + n, "Horas extras evitadas por mes, en pesos, " + n, B["he_" + e], "pesos")
    cifra("horas_extras_evitadas_horas_" + n, "Horas extras evitadas por mes, en horas, " + n, B["hhe_" + e], "num")
    cifra("beneficio_mensual_" + n, "Beneficio mensual pleno (capacidad liberada + horas extras), " + n,
          B["retrabajo_" + e] + B["he_" + e], "pesos")
    cifra("neto_mensual_" + n, "Neto mensual pleno, vista completa, " + n, B["retrabajo_" + e] + B["he_" + e] - REC_NETO, "pesos")
    cifra("neto_mensual_caja_" + n, "Neto mensual pleno de caja (horas extras evitadas), " + n, B["he_" + e], "pesos")
    for v in VISTAS:
        i, suf = IND[(v, e)], SUFIJO[v]
        cifra("max_expuesto%s_%s" % (suf, n), "Máximo expuesto, vista %s, %s" % (VISTAS[v], n), i["max_expuesto"], "pesos")
        cifra("recupero_meses%s_%s" % (suf, n), "Mes de recupero (mes 1 = febrero de 2027), vista %s, %s" % (VISTAS[v], n),
              i["recupero"], "meses")
        cifra("van_3a%s_%s" % (suf, n), "VAN a 3 años, vista %s, %s" % (VISTAS[v], n), i["van"], "pesos")
        cifra("tir%s_%s" % (suf, n), "TIR anual equivalente, vista %s, %s" % (VISTAS[v], n), i["tir_anual"], "pct")
        cifra("tir_mensual%s_%s" % (suf, n), "TIR mensual, vista %s, %s" % (VISTAS[v], n), i["tir_mensual"], "pct")
    cifra("van_3a_tasa20_" + n, "VAN a 3 años con 20 % real anual, vista completa, " + n, IND[("neto", e)]["van_alta"], "pesos")
    cifra("van_3a_caja_tasa20_" + n, "VAN a 3 años con 20 % real anual, vista de caja, " + n, IND[("caja", e)]["van_alta"], "pesos")
    for a in range(3):
        cifra("flujo_anio%d_%s" % (a + 1, n), "Flujo neto del año %d, vista completa, %s" % (a + 1, n), IND[("neto", e)]["anual"][a], "pesos")
        cifra("flujo_caja_anio%d_%s" % (a + 1, n), "Flujo de caja del año %d, %s" % (a + 1, n), IND[("caja", e)]["anual"][a], "pesos")
cifra("horas_extras_evitadas_mensual_meta", "Horas extras evitadas por mes si se cumple la meta (la mitad)", B["hemeta"], "pesos")
cifra("tiempo_produccion_en_horas_extras_mensual", "Costo por mes si la carga diaria y la reunión de Producción se pagaran como horas extras",
      R_PROD_HE, "pesos")
cifra("retrabajo_hoy_mensual", "Retrabajo por pedidos recortados hoy, por mes", S["Recortados_hoy"] * S["Retrabajo_h"] * S["Hora_retrabajo"] * SM, "pesos")
cifra("horas_retrabajo_hoy_mes", "Horas de retrabajo por pedidos recortados hoy, por mes", S["Recortados_hoy"] * S["Retrabajo_h"] * SM, "num")
cifra("horas_extras_hoy_mensual", "Horas extras de hoy, por mes", S["HE_mes_hoy"] * S["Hora_extra"], "pesos")
cifra("horas_extras_ligadas_pedidos_mensual", "Horas extras ligadas a pedidos que faltaron (la mitad), por mes",
      S["HE_mes_hoy"] * S["Parte_HE_pedidos"] * S["Hora_extra"], "pesos")
CNA = S["Recortados_hoy"] * S["Retrabajo_h"] * S["Hora_retrabajo"] * SM + S["HE_mes_hoy"] * S["Parte_HE_pedidos"] * S["Hora_extra"]
cifra("costo_no_actuar_mensual", "Costo de no actuar por mes, equivalente: retrabajo de hoy + horas extras ligadas a pedidos", CNA, "pesos")
cifra("costo_no_actuar_anual", "Costo de no actuar por año", CNA * 12, "pesos")
cifra("costo_no_actuar_caja_mensual", "Parte de dinero del costo de no actuar (horas extras ligadas a pedidos), por mes",
      S["HE_mes_hoy"] * S["Parte_HE_pedidos"] * S["Hora_extra"], "pesos")
cifra("equilibrio_recortes_evitados_semana", "Recortes evitados por semana que cubren el tiempo interno nuevo, solo con retrabajo",
      REC_NETO / (S["Retrabajo_h"] * S["Hora_retrabajo"] * SM), "num")


def armar_json():
    d = {}
    for clave, _, valor, tipo in CIFRAS:
        if tipo == "pesos":
            d[clave] = r0(valor)
        elif tipo == "pct":
            d[clave] = r4(valor)
        elif tipo == "num":
            d[clave] = round(valor, 2)
        else:
            d[clave] = valor
    for e, n in (("esp", "esperado"), ("con", "conservador")):
        d["recupero_mes_nombre_" + n] = IND[("neto", e)]["recupero_mes"]
        d["recupero_mes_nombre_caja_" + n] = IND[("caja", e)]["recupero_mes"]
        d["flujo_mensual_" + n] = [r0(f[e]["neto"]) for f in MODELO[:12]]
        d["saldo_acumulado_" + n] = [r0(s) for s in IND[("neto", e)]["saldos"][:12]]
        d["costos_mensual_" + n] = [r0(f[e]["costos"]) for f in MODELO[:12]]
        d["beneficios_mensual_" + n] = [r0(f[e]["beneficios"]) for f in MODELO[:12]]
        d["flujo_caja_mensual_" + n] = [r0(f[e]["caja"]) for f in MODELO[:12]]
        d["saldo_caja_" + n] = [r0(s) for s in IND[("caja", e)]["saldos"][:12]]
    d["costos_una_vez"] = {k: r0(v) for k, v in C.items()}
    d["supuestos"] = {k: (v.isoformat() if isinstance(v, datetime.date) else round(v, 6)) for k, v in S.items()}
    d["costos_recurrentes_mensual"] = {k: r0(v) for k, v in R.items()}
    d["meses"] = [mes_nombre(m) for m in range(1, 13)]
    d["_nota"] = ("Pesos constantes de noviembre de 2026. Mes 1 = febrero de 2027 (semana 1 = 1-2-2027). "
                  "Vista completa: tiempo del personal valorado al costo de la hora. Vista de caja: solo horas extras. "
                  "Generado por armar-planilla.py; no editar a mano.")
    return d


# =============================================================================
# 4. Planilla
# =============================================================================

def nombre_def(wb, nombre, hoja, celda):
    col = "".join(c for c in celda if c.isalpha())
    fila = "".join(c for c in celda if c.isdigit())
    ref = "'%s'!$%s$%s" % (hoja, col, fila)
    wb.defined_names[nombre] = DefinedName(nombre, attr_text=ref)


def titulo(ws, texto, sub=None):
    ws["A1"] = texto
    ws["A1"].font = F_TITULO
    if sub:
        ws["A2"] = sub
        ws["A2"].font = F_SUB
    ws.sheet_view.showGridLines = False


def encabezado(ws, fila, textos, col0=1):
    for i, t in enumerate(textos):
        c = ws.cell(row=fila, column=col0 + i, value=t)
        c.font, c.fill, c.alignment = F_HEAD, FILL_HEAD, CENTRO
    ws.row_dimensions[fila].height = 30


def seccion(ws, fila, texto, ncols):
    for j in range(1, ncols + 1):
        ws.cell(row=fila, column=j).fill = FILL_SEC
    c = ws.cell(row=fila, column=1, value=texto)
    c.font = F_SEC


def celda(ws, fila, col, valor, fmt=None, font=F_NORM, fill=None, borde=BORDE, align=None):
    c = ws.cell(row=fila, column=col, value=valor)
    c.font = font
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if borde:
        c.border = borde
    if align:
        c.alignment = align
    return c


def hoja_supuestos(wb):
    ws = wb.create_sheet("Supuestos")
    titulo(ws, "Supuestos del caso de negocio",
           "Pesos constantes de noviembre de 2026. Las celdas en azul son las que se pueden cambiar; todo lo demás de la planilla se recalcula.")
    encabezado(ws, 4, ["Supuesto", "Valor", "Unidad", "Tipo", "Fuente o base"])
    f = 5
    for item in FILAS_SUP:
        if item[0] == "sec":
            f += 1 if f > 5 else 0
            seccion(ws, f, item[1], 5)
            f += 1
            continue
        _, nombre, etiqueta, valor, formula, unidad, tipo, fuente, fmt = item
        celda(ws, f, 1, etiqueta, align=WRAP)
        v = formula if formula else valor
        celda(ws, f, 2, v, fmt, font=F_NORM if formula else F_INPUT)
        celda(ws, f, 3, unidad)
        celda(ws, f, 4, tipo, fill=FILL_TIPO[tipo], align=CENTRO)
        celda(ws, f, 5, fuente, align=WRAP, font=F_NOTA if not fuente else F_NORM)
        nombre_def(wb, nombre, "Supuestos", "B%d" % f)
        f += 1
    f += 1
    seccion(ws, f, "Supuestos que cambian entre escenarios (los más inciertos)", 6)
    f += 1
    encabezado(ws, f, ["Supuesto", "Esperado", "Conservador", "Unidad", "Tipo", "Fuente o base"])
    f += 1
    for nombre, etiqueta, v_esp, v_con, f_esp, f_con, unidad, tipo, fuente, fmt in ESC:
        celda(ws, f, 1, etiqueta, align=WRAP)
        celda(ws, f, 2, f_esp or v_esp, fmt, font=F_NORM if f_esp else F_INPUT)
        celda(ws, f, 3, f_con or v_con, fmt, font=F_NORM if f_con else F_INPUT)
        celda(ws, f, 4, unidad)
        celda(ws, f, 5, tipo, fill=FILL_TIPO[tipo], align=CENTRO)
        celda(ws, f, 6, fuente, align=WRAP)
        nombre_def(wb, nombre + "_esp", "Supuestos", "B%d" % f)
        nombre_def(wb, nombre + "_con", "Supuestos", "C%d" % f)
        f += 1
    f += 1
    celda(ws, f, 1, "Tipo: dato = lo dio la empresa; estimación = la calculamos, con su base; hipótesis = a validar en el piloto o en la operación; "
          "decisión = la elige el grupo o la dirección. Los tiempos de las tareas se miden en las semanas 1 a 5 y la planilla se recalcula antes del Go.",
          font=F_NOTA, borde=None)
    for col, w in zip("ABCDEF", (58, 15, 15, 14, 14, 70)):
        ws.column_dimensions[col].width = w
    ws.column_dimensions["E"].width = 70
    ws.freeze_panes = "A5"
    return ws


def hoja_costos(wb):
    ws = wb.create_sheet("Costos y beneficios")
    titulo(ws, "Costos y beneficios", "Cada monto es una fórmula sobre la hoja Supuestos. El tiempo del personal se valora al costo de su hora.")
    f = 4
    seccion(ws, f, "Puesta en marcha (una vez)", 6)
    f += 1
    encabezado(ws, f, ["Concepto", "Cómo se calcula", "Por vez", "Veces", "Total", "Semanas"])
    f += 1
    items = [
        ("C_base", "Registro de la línea de base", "1 min de Oficina × 125 pedidos × 3 semanas",
         "=Base_min/60*Pedidos_semana*(Base_hasta-Base_desde+1)*Hora_oficina", 1, "1 a 3"),
        ("C_conteo_papas", "Conteo inicial de papas fritas (horas extras)", "2 personas × 2 h × hora extra",
         "=CP_personas*CP_horas*Hora_extra", 1, "3"),
        ("C_cap_piloto", "Capacitación para el piloto",
         "Producción: 2 × 1 h y 15 min para los otros 5; Oficina: 2 × 2 sesiones de 1 h; Depósito: 2 × 1 h; Dirección: 3 × 1 h",
         "=CapP_personas_op*CapP_horas_op*Hora_operario+(Personas_produccion-CapP_personas_op)*CapP_resto_min/60*Hora_operario"
         "+CapP_personas_of*CapP_horas_of*Hora_oficina+CapP_personas_dep*CapP_horas_dep*Hora_operario"
         "+CapP_personas_dir*CapP_horas_dir*Hora_direccion", 1, "3"),
        ("C_piloto", "Tiempo adicional del piloto", "10 días × (25 min de Oficina + 10 min de Producción) + conteo de 1 h-persona por semana",
         "=Pil_dias*(Pil_min_of/60*Hora_oficina+Pil_min_prod/60*Hora_operario)+Pil_conteo_hp*Hora_operario*(Piloto_hasta-Piloto_desde+1)", 1, "4 y 5"),
        ("C_com_piloto", "Comunicación del piloto", "Anuncio de 15 min, 10 min con cada grupo, 15 min el día 5 y 15 min con el resultado, todo el equipo",
         "=(Com_anuncio_min+Com_grupos_min+Com_dia5_min+Com_go_min)/60*Hora_equipo", 1, "1 a 6"),
        ("C_config", "Revisión de productos y unidades en Discovery, por línea", "2 h de Oficina (la configuración, sin costo)",
         "=Cfg_h_of*Hora_oficina", 3, "7, 13 y 18"),
        ("C_conteo_linea", "Conteo inicial por línea (horas extras de fin de semana)", "3 personas × 3 h × hora extra",
         "=CL_personas*CL_horas*Hora_extra", 3, "8, 14 y 19"),
        ("C_cap_linea", "Capacitación por línea", "2 operarios × 1,5 h + 2 de Oficina × 1 h",
         "=CapL_op*CapL_h_op*Hora_operario+CapL_of*CapL_h_of*Hora_oficina", 3, "8, 14 y 19"),
        ("C_trans", "Doble registro al pasar cada línea", "2 semanas × 5 días × (15 min de Oficina + 10 min de Producción)",
         "=Trans_semanas*Dias_semana*(Tr_min_of/60*Hora_oficina+Tr_min_prod/60*Hora_operario)", 3, "9-10, 15-16, 20-21"),
        ("C_com_lineas", "Avisos al activar cada línea y en los meses 3 y 6", "5 avisos de 5 min con todo el equipo",
         "=Com_aviso_min*Com_avisos/60*Hora_equipo", 1, "7 a 26"),
        ("C_seg", "Reunión semanal de seguimiento", "26 semanas × 20 min × (hijo responsable, 2 de Oficina, Producción y Depósito)",
         "=(Seg_hasta-Seg_desde+1)*Seg_min/60*(Seg_dir*Hora_direccion+Seg_of*Hora_oficina+Seg_planta*Hora_operario)", 1, "1 a 26"),
    ]
    ini = f
    for nombre, concepto, como, formula, veces, semanas in items:
        celda(ws, f, 1, concepto, align=WRAP)
        celda(ws, f, 2, como, align=WRAP, font=F_NOTA)
        celda(ws, f, 3, formula, FMT_PESOS)
        celda(ws, f, 4, veces, FMT_NUM)
        celda(ws, f, 5, "=C%d*D%d" % (f, f), FMT_PESOS)
        celda(ws, f, 6, semanas, align=CENTRO)
        nombre_def(wb, nombre, "Costos y beneficios", "C%d" % f)
        f += 1
    for concepto, nombre in (("Módulo de stock de Discovery (incluido en la licencia)", "Costo_modulo"),
                             ("Horas del responsable de sistemas (incluidas en su servicio)", "Costo_juanjo"),
                             ("Equipos (ya hay PC en Producción y Depósito)", "Costo_equipos")):
        celda(ws, f, 1, concepto, align=WRAP)
        celda(ws, f, 2, "Dato de la empresa", font=F_NOTA)
        celda(ws, f, 3, "=" + nombre, FMT_PESOS0)
        celda(ws, f, 4, 1)
        celda(ws, f, 5, "=C%d*D%d" % (f, f), FMT_PESOS0)
        f += 1
    fin = f - 1
    celda(ws, f, 1, "Subtotal puesta en marcha", font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    for j in (2, 3, 4, 6):
        celda(ws, f, j, None, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 5, "=SUM(E%d:E%d)" % (ini, fin), FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    nombre_def(wb, "Una_vez_total", "Costos y beneficios", "E%d" % f)
    f += 1
    celda(ws, f, 1, "Con contingencia, esperado (15 %)", font=F_BOLD)
    celda(ws, f, 5, "=Una_vez_total*(1+Cont_esp)", FMT_PESOS, F_BOLD)
    f += 1
    celda(ws, f, 1, "Con contingencia, conservador (20 %)", font=F_BOLD)
    celda(ws, f, 5, "=Una_vez_total*(1+Cont_con)", FMT_PESOS, F_BOLD)
    f += 1
    celda(ws, f, 1, "De la puesta en marcha, lo que sale de la caja (horas extras de los conteos, sin contingencia)", align=WRAP)
    celda(ws, f, 5, "=C_conteo_papas+3*C_conteo_linea", FMT_PESOS)
    nombre_def(wb, "Efectivo_total", "Costos y beneficios", "E%d" % f)
    f += 2

    seccion(ws, f, "Tiempo interno recurrente, por mes, con las tres líneas en uso", 6)
    f += 1
    encabezado(ws, f, ["Concepto", "Cómo se calcula", "Por mes", "", "", "Desde"])
    f += 1
    recs = [
        ("R_carga", "Carga diaria de lo producido", "20 min de operario × días hábiles", "=Carga_min/60*Hora_operario*Dias_mes", "Cada línea en uso"),
        ("R_reunion", "Reunión diaria (Oficina, Producción, Dirección)", "10 min × 3 personas × días hábiles",
         "=Reu_min/60*(Hora_oficina+Hora_operario+Hora_direccion)*Dias_mes", "Semana 4"),
        ("R_reserva", "Cargar el pedido y reservar en Discovery", "3 min de Oficina × 125 pedidos × semanas por mes",
         "=Res_min/60*Hora_oficina*Pedidos_semana*Sem_mes", "Cada línea en uso"),
        ("R_revision", "Revisión diaria de reservas", "10 min de Oficina × días hábiles", "=Rev_min/60*Hora_oficina*Dias_mes", "Cada línea en uso"),
        ("R_conteo", "Conteo semanal de producto terminado", "2 personas × 1,5 h × semanas por mes",
         "=Cto_personas*Cto_horas*Hora_operario*Sem_mes", "Cada línea en uso"),
        ("R_tablero", "Registro de pedidos completos y tablero", "30 min de Oficina por semana", "=Tab_min/60*Hora_oficina*Sem_mes", "Semana 4"),
        ("R_ctrl", "Menos: control semanal de Producción que se deja", "1,5 h de operario por semana", "=-Ctrl_h*Hora_operario*Sem_mes",
         "Cada línea en uso"),
        ("R_averig", "Menos: averiguación doble que se deja", "1,5 min de Oficina + 1,5 min de planta por pedido",
         "=-(Av_min_of/60*Hora_oficina+Av_min_planta/60*Hora_operario)*Pedidos_semana*Sem_mes", "Cada línea en uso"),
        ("R_copias", "Menos: copias del pedido que se dejan (papel o planilla y lista)", "2 min de Oficina por pedido",
         "=-Copias_min/60*Hora_oficina*Pedidos_semana*Sem_mes", "Cada línea en uso"),
    ]
    ini = f
    for nombre, concepto, como, formula, desde_txt in recs:
        celda(ws, f, 1, concepto, align=WRAP)
        celda(ws, f, 2, como, align=WRAP, font=F_NOTA)
        celda(ws, f, 3, formula, FMT_PESOS)
        celda(ws, f, 6, desde_txt, align=CENTRO)
        nombre_def(wb, nombre, "Costos y beneficios", "C%d" % f)
        f += 1
    celda(ws, f, 1, "Tiempo interno neto por mes", font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 2, None, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 3, "=SUM(C%d:C%d)" % (ini, f - 1), FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    nombre_def(wb, "Rec_neto", "Costos y beneficios", "C%d" % f)
    f += 1
    celda(ws, f, 1, "Si la carga diaria y la reunión de Producción se pagaran como horas extras (sensibilidad de caja)", align=WRAP)
    celda(ws, f, 3, "=(Carga_min+Reu_min)/60*Hora_extra*Dias_mes", FMT_PESOS)
    nombre_def(wb, "R_prod_he", "Costos y beneficios", "C%d" % f)
    f += 2

    seccion(ws, f, "Tiempo, en horas por mes, con las tres líneas en uso", 6)
    f += 1
    encabezado(ws, f, ["Concepto", "Cómo se calcula", "Esperado", "Conservador", "", ""])
    f += 1
    for nombre, concepto, como, fx_e, fx_c in [
        ("H_nuevas", "Horas que agregan las tareas nuevas", "Carga, reunión diaria (3 personas), revisión, reservas, conteo y tablero",
         "=(Carga_min+3*Reu_min+Rev_min)/60*Dias_mes+Res_min/60*Pedidos_semana*Sem_mes+Cto_personas*Cto_horas*Sem_mes+Tab_min/60*Sem_mes", None),
        ("H_reempl", "Horas de las tareas que se dejan", "Control semanal, averiguación doble y copias del pedido",
         "=Ctrl_h*Sem_mes+(Av_min_of+Av_min_planta+Copias_min)/60*Pedidos_semana*Sem_mes", None),
        ("H_retrabajo", "Horas de retrabajo evitado", "Recortes evitados × 1 h × semanas por mes",
         "=(Recortados_hoy-Recortados_esp)*Retrabajo_h*Sem_mes", "=(Recortados_hoy-Recortados_con)*Retrabajo_h*Sem_mes"),
    ]:
        celda(ws, f, 1, concepto, align=WRAP)
        celda(ws, f, 2, como, align=WRAP, font=F_NOTA)
        celda(ws, f, 3, fx_e, FMT_NUM1)
        celda(ws, f, 4, fx_c or "=C%d" % f, FMT_NUM1)
        if fx_c:
            nombre_def(wb, nombre + "_esp", "Costos y beneficios", "C%d" % f)
            nombre_def(wb, nombre + "_con", "Costos y beneficios", "D%d" % f)
        else:
            nombre_def(wb, nombre, "Costos y beneficios", "C%d" % f)
        f += 1
    celda(ws, f, 1, "El proceso nuevo se paga con el tiempo que libera: agrega menos horas netas que las de retrabajo que evita.",
          font=F_NOTA, borde=None, align=WRAP)
    ws.merge_cells(start_row=f, start_column=1, end_row=f, end_column=6)
    f += 2

    seccion(ws, f, "Sensibilidad: horas del responsable de sistemas valoradas (hoy sin costo extra)", 6)
    f += 1
    encabezado(ws, f, ["Concepto", "Cómo se calcula", "Por vez", "Veces", "Total", "Semanas"])
    f += 1
    jj0 = f
    for nombre, concepto, como, fx, veces, semanas in [
        ("C_jj_piloto", "Preparación, primeras capacitaciones y soporte del piloto", "20 h × hora valorada", "=Jj_h_piloto*Hora_juanjo", 1, "1 a 5"),
        ("C_jj_linea", "Configuración, stock inicial y casos de prueba, por línea", "6 h × hora valorada", "=Jj_h_linea*Hora_juanjo", 3,
         "7-8, 13-14, 18-19"),
        ("C_jj_seg", "Reunión semanal de seguimiento", "26 × 20 min × hora valorada", "=(Seg_hasta-Seg_desde+1)*Seg_min/60*Hora_juanjo", 1, "1 a 26"),
    ]:
        celda(ws, f, 1, concepto, align=WRAP)
        celda(ws, f, 2, como, align=WRAP, font=F_NOTA)
        celda(ws, f, 3, fx, FMT_PESOS)
        celda(ws, f, 4, veces, FMT_NUM)
        celda(ws, f, 5, "=C%d*D%d" % (f, f), FMT_PESOS)
        celda(ws, f, 6, semanas, align=CENTRO)
        nombre_def(wb, nombre, "Costos y beneficios", "C%d" % f)
        f += 1
    celda(ws, f, 1, "Total horas del responsable de sistemas valoradas", font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    for j in (2, 3, 4, 6):
        celda(ws, f, j, None, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 5, "=SUM(E%d:E%d)" % (jj0, f - 1), FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    nombre_def(wb, "Jj_total", "Costos y beneficios", "E%d" % f)
    f += 2

    seccion(ws, f, "Beneficios por mes, con el efecto pleno (las tres líneas)", 6)
    f += 1
    encabezado(ws, f, ["Beneficio", "Cómo se calcula", "Esperado", "Conservador", "", "Es caja"])
    f += 1
    bens = [
        ("B_retrabajo", "Retrabajo evitado (capacidad liberada)", "(30 − recortados con la propuesta) × 1 h × hora de retrabajo × semanas por mes",
         "=(Recortados_hoy-Recortados_%s)*Retrabajo_h*Hora_retrabajo*Sem_mes", "No: tiempo de gente con sueldo que queda para otras tareas"),
        ("B_he", "Horas extras evitadas", "45 h × 50 % ligadas a pedidos × (recortes evitados ÷ 30) × hora extra",
         "=HE_mes_hoy*RedHE_%s*Hora_extra", "Sí"),
    ]
    for nombre, concepto, como, formula, caja in bens:
        celda(ws, f, 1, concepto, align=WRAP)
        celda(ws, f, 2, como, align=WRAP, font=F_NOTA)
        celda(ws, f, 3, formula % "esp", FMT_PESOS)
        celda(ws, f, 4, formula % "con", FMT_PESOS)
        celda(ws, f, 6, caja, align=WRAP)
        nombre_def(wb, nombre + "_esp", "Costos y beneficios", "C%d" % f)
        nombre_def(wb, nombre + "_con", "Costos y beneficios", "D%d" % f)
        f += 1
    celda(ws, f, 1, "Total beneficio mensual", font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 2, None, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 3, "=B_retrabajo_esp+B_he_esp", FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    celda(ws, f, 4, "=B_retrabajo_con+B_he_con", FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    f += 1
    celda(ws, f, 1, "Neto mensual pleno (beneficio − tiempo interno neto)", font=F_BOLD)
    celda(ws, f, 3, "=B_retrabajo_esp+B_he_esp-Rec_neto", FMT_PESOS, F_BOLD)
    celda(ws, f, 4, "=B_retrabajo_con+B_he_con-Rec_neto", FMT_PESOS, F_BOLD)
    f += 1
    celda(ws, f, 1, "Sensibilidad: horas extras evitadas si se cumple la meta (la mitad de 45 h)", align=WRAP)
    celda(ws, f, 2, "45 h × 50 % × hora extra", font=F_NOTA, align=WRAP)
    celda(ws, f, 3, "=HE_mes_hoy*Meta_HE*Hora_extra", FMT_PESOS)
    celda(ws, f, 4, "=C%d" % f, FMT_PESOS)
    nombre_def(wb, "B_hemeta", "Costos y beneficios", "C%d" % f)
    f += 1
    celda(ws, f, 1, "No se suma el margen de los pedidos recortados: lo que falta se manda después y la venta no se pierde. "
          "Beneficios que no se suman: cobranza que no se demora, distribuidor que no paga un segundo flete, información de stock para decidir "
          "y menos dependencia de mirar el depósito.", font=F_NOTA, borde=None, align=WRAP)
    ws.merge_cells(start_row=f, start_column=1, end_row=f, end_column=6)
    ws.row_dimensions[f].height = 42
    for col, w in zip("ABCDEF", (48, 52, 15, 14, 15, 30)):
        ws.column_dimensions[col].width = w
    return ws


def col(m):
    """Columna del mes m (1..36) en Flujo mensual: B..AK."""
    return get_column_letter(m + 1)


COL_TOTAL = get_column_letter(MESES + 2)


def hoja_flujo(wb):
    ws = wb.create_sheet("Flujo mensual")
    titulo(ws, "Flujo mensual (36 meses; los meses 13 a 36 están agrupados: el botón + de arriba los muestra)",
           "Mes 1 = febrero de 2027. Pesos constantes de noviembre de 2026. Los costos van en positivo y el flujo neto los resta; en el flujo y el saldo, negativo = se pone.")
    filas = {}
    encabezado(ws, 4, ["Concepto"] + list(range(1, MESES + 1)) + ["Total 3 años"])
    celda(ws, 5, 1, "Mes calendario", font=F_NOTA)
    celda(ws, 6, 1, "Semana desde (fin de la anterior)", font=F_NOTA)
    celda(ws, 7, 1, "Semana hasta", font=F_NOTA)
    for m in range(1, MESES + 1):
        c = col(m)
        celda(ws, 5, m + 1, "=EDATE(Inicio,%d)" % (m - 1), FMT_MES, F_NOTA, align=CENTRO)
        celda(ws, 6, m + 1, "=(%s$4-1)*Sem_mes" % c, FMT_NUM1, F_NOTA)
        celda(ws, 7, m + 1, "=%s$4*Sem_mes" % c, FMT_NUM1, F_NOTA)
    f = 9

    def fila(clave, etiqueta, formula_mes, fmt=FMT_PESOS, total=True, font=F_NORM, fill=None, borde=BORDE):
        nonlocal f
        celda(ws, f, 1, etiqueta, font=font, fill=fill, borde=borde)
        for m in range(1, MESES + 1):
            c = col(m)
            fx = formula_mes(c, m).replace("{ini}", "%s$6" % c).replace("{fin}", "%s$7" % c)
            celda(ws, f, m + 1, "=" + fx, fmt, font, fill, borde)
        if total:
            celda(ws, f, MESES + 2, "=SUM(B%d:%s%d)" % (f, col(MESES), f), fmt, F_BOLD, fill, borde)
        else:
            celda(ws, f, MESES + 2, None, fill=fill, borde=borde)
        filas[clave] = f
        f += 1

    def desde_x(s):
        return "MAX(0,MIN(1,({fin}-((%s)-1))/Sem_mes))" % s

    def vent_x(monto, s, e):
        return "%s*MAX(0,MIN({fin},%s)-MAX({ini},(%s)-1))/((%s)-(%s)+1)" % (monto, e, s, e, s)

    seccion(ws, f, "Calendario del roadmap (parte del mes)", MESES + 2)
    f += 1
    fila("f_uso", "Parte de las líneas en uso (costos recurrentes)",
         lambda c, m: "+".join("Parte_%s*%s" % (l, desde_x("Uso_" + l)) for l in LINEAS), FMT_PCT, False)
    fila("f_fijo", "Reunión diaria y tablero en marcha", lambda c, m: desde_x("Reunion_desde"), FMT_PCT, False)
    for e, n in (("esp", "esperado"), ("con", "conservador")):
        fila("f_ben_" + e, "Parte de las líneas con efecto, " + n,
             lambda c, m, e=e: "+".join("Parte_%s*%s" % (l, desde_x("Ben_%s+Demora_%s" % (l, e))) for l in LINEAS), FMT_PCT, False)
    f += 1
    seccion(ws, f, "Puesta en marcha (igual en los dos escenarios)", MESES + 2)
    f += 1
    for k, etiqueta, w in UNA:
        fila("u_" + k, etiqueta, lambda c, m, k=k, w=w: "+".join(vent_x("C_" + k, s_, e_) for s_, e_ in w))
    u0, u1 = filas["u_" + UNA[0][0]], filas["u_" + UNA[-1][0]]
    fila("u_sub", "Subtotal puesta en marcha", lambda c, m: "SUM(%s%d:%s%d)" % (c, u0, c, u1), font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    f += 1
    seccion(ws, f, "Tiempo interno recurrente, neto de lo que reemplaza (igual en los dos escenarios)", MESES + 2)
    f += 1
    etiquetas = {"carga": "Carga diaria de lo producido", "reunion": "Reunión diaria", "reserva": "Cargar el pedido y reservar",
                 "revision": "Revisión de reservas", "conteo": "Conteo semanal", "tablero": "Registro de pedidos y tablero",
                 "ctrl": "Menos: control semanal de Producción", "averig": "Menos: averiguación doble",
                 "copias": "Menos: copias del pedido"}
    rk = list(R)
    for k in rk:
        fr = "f_uso" if k in REC_POR_LINEA else "f_fijo"
        fila("r_" + k, etiquetas[k], lambda c, m, k=k, fr=fr: "R_%s*%s$%d" % (k, c, filas[fr]))
    r0_, r1_ = filas["r_" + rk[0]], filas["r_" + rk[-1]]
    fila("r_sub", "Subtotal tiempo interno recurrente", lambda c, m: "SUM(%s%d:%s%d)" % (c, r0_, c, r1_), font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    f += 1
    seccion(ws, f, "Sensibilidad: horas del responsable de sistemas valoradas (igual en los dos escenarios)", MESES + 2)
    f += 1
    fila("jj", "Horas del responsable de sistemas, valoradas",
         lambda c, m: "+".join(vent_x("C_" + k, s_, e_) for k, w in JJ for s_, e_ in w))

    def par(clave, etiqueta, formula_mes, bold=False):
        """Fila de flujo y fila de saldo acumulado."""
        fila(clave, etiqueta, formula_mes, font=F_BOLD if bold else F_NORM)
        fila("sal_" + clave, "Saldo acumulado",
             lambda c, m: ("%s%d" % (c, filas[clave])) if m == 1 else ("%s%d+%s%d" % (col(m - 1), f, c, filas[clave])),
             total=False)

    for e, n in (("esp", "ESPERADO"), ("con", "CONSERVADOR")):
        f += 1
        seccion(ws, f, "Escenario %s: vista completa (el tiempo del personal valorado al costo de la hora)" % n.lower(), MESES + 2)
        f += 1
        fila("cont_" + e, "Contingencia sobre la puesta en marcha", lambda c, m, e=e: "Cont_%s*%s%d" % (e, c, filas["u_sub"]))
        fila("costos_" + e, "Total costos", lambda c, m, e=e: "%s%d+%s%d+%s%d" % (c, filas["u_sub"], c, filas["cont_" + e], c, filas["r_sub"]),
             font=F_BOLD)
        fila("brt_" + e, "Retrabajo evitado (capacidad liberada)", lambda c, m, e=e: "B_retrabajo_%s*%s$%d" % (e, c, filas["f_ben_" + e]))
        fila("bhe_" + e, "Horas extras evitadas", lambda c, m, e=e: "B_he_%s*%s$%d" % (e, c, filas["f_ben_" + e]))
        fila("ben_" + e, "Total beneficios", lambda c, m, e=e: "%s%d+%s%d" % (c, filas["brt_" + e], c, filas["bhe_" + e]), font=F_BOLD)
        fila("neto_" + e, "Flujo neto del mes", lambda c, m, e=e: "%s%d-%s%d" % (c, filas["ben_" + e], c, filas["costos_" + e]),
             font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
        fila("sal_neto_" + e, "Saldo acumulado",
             lambda c, m, e=e: ("%s%d" % (c, filas["neto_" + e])) if m == 1 else ("%s%d+%s%d" % (col(m - 1), f, c, filas["neto_" + e])),
             total=False, font=F_BOLD)
        f += 1
        seccion(ws, f, "Escenario %s: solo caja (lo que sale o deja de salir: horas extras)" % n.lower(), MESES + 2)
        f += 1
        fila("caja_out_" + e, "Horas extras de los conteos, con contingencia",
             lambda c, m, e=e: "(%s%d+%s%d)*(1+Cont_%s)" % (c, filas["u_conteo_papas"], c, filas["u_conteo_linea"], e))
        fila("caja_" + e, "Flujo de caja del mes (horas extras evitadas − horas extras de los conteos)",
             lambda c, m, e=e: "%s%d-%s%d" % (c, filas["bhe_" + e], c, filas["caja_out_" + e]), font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
        fila("sal_caja_" + e, "Saldo acumulado de caja",
             lambda c, m, e=e: ("%s%d" % (c, filas["caja_" + e])) if m == 1 else ("%s%d+%s%d" % (col(m - 1), f, c, filas["caja_" + e])),
             total=False, font=F_BOLD)
        f += 1
        seccion(ws, f, "Escenario %s: sensibilidades" % n.lower(), MESES + 2)
        f += 1
        fila("bmeta_" + e, "Horas extras evitadas si se cumple la meta (la mitad)",
             lambda c, m, e=e: "B_hemeta*%s$%d" % (c, filas["f_ben_" + e]))
        par("neto_meta_" + e, "Flujo neto, vista completa, con la meta de horas extras",
            lambda c, m, e=e: "%s%d+%s%d-%s%d" % (c, filas["brt_" + e], c, filas["bmeta_" + e], c, filas["costos_" + e]))
        par("caja_meta_" + e, "Flujo de caja con la meta de horas extras",
            lambda c, m, e=e: "%s%d-%s%d" % (c, filas["bmeta_" + e], c, filas["caja_out_" + e]))
        par("caja_prod_" + e, "Flujo de caja si la carga y la reunión de Producción se pagan como horas extras",
            lambda c, m, e=e: "%s%d-R_prod_he*%s$%d" % (c, filas["caja_" + e], c, filas["f_uso"]))
        par("neto_rt05_" + e, "Flujo neto, vista completa, con media hora de retrabajo por recortado",
            lambda c, m, e=e: "%s%d-%s%d*(1-Retrabajo_sens/Retrabajo_h)" % (c, filas["neto_" + e], c, filas["brt_" + e]))
        par("neto_res5_" + e, "Flujo neto, vista completa, con 5 minutos por reserva",
            lambda c, m, e=e: "%s%d-R_reserva*(Res_sens/Res_min-1)*%s$%d" % (c, filas["neto_" + e], c, filas["f_uso"]))
        par("neto_sincop_" + e, "Flujo neto, vista completa, sin el ahorro de las copias del pedido",
            lambda c, m, e=e: "%s%d+R_copias*%s$%d" % (c, filas["neto_" + e], c, filas["f_uso"]))
        par("neto_jj_" + e, "Flujo neto, vista completa, con las horas del responsable de sistemas valoradas",
            lambda c, m, e=e: "%s%d-%s$%d" % (c, filas["neto_" + e], c, filas["jj"]))
        par("caja_jj_" + e, "Flujo de caja si el responsable de sistemas cobrara esas horas aparte",
            lambda c, m, e=e: "%s%d-%s$%d" % (c, filas["caja_" + e], c, filas["jj"]))
    ws.column_dimensions["A"].width = 62
    for m in range(1, MESES + 1):
        ws.column_dimensions[col(m)].width = 12.5
    ws.column_dimensions[COL_TOTAL].width = 15
    ws.column_dimensions.group(col(13), col(MESES), hidden=True, outline_level=1)
    ws.sheet_properties.outlinePr.summaryRight = True
    ws.freeze_panes = "B8"
    return ws, filas


def hoja_anual(wb, filas):
    ws = wb.create_sheet("Flujo anual")
    titulo(ws, "Flujo anual a 3 años", "Año 1 = febrero de 2027 a enero de 2028. Suma de los meses de la hoja Flujo mensual.")
    encabezado(ws, 4, ["Concepto", "Año 1", "Año 2", "Año 3", "Total"])
    f = 5
    rangos = [(col(1), col(12)), (col(13), col(24)), (col(25), col(36))]
    for e, n in (("esp", "Esperado"), ("con", "Conservador")):
        seccion(ws, f, n, 5)
        f += 1
        lista = [("Costos (con contingencia)", "costos_", -1), ("Beneficios: retrabajo evitado (capacidad liberada)", "brt_", 1),
                 ("Beneficios: horas extras evitadas", "bhe_", 1), ("Flujo neto, vista completa", "neto_", 1),
                 ("Flujo de caja (solo horas extras)", "caja_", 1)]
        for etiqueta, clave, signo in lista:
            bold = clave in ("neto_", "caja_")
            celda(ws, f, 1, etiqueta, font=F_BOLD if bold else F_NORM)
            for j, (a, b) in enumerate(rangos):
                fx = "=%sSUM('Flujo mensual'!%s%d:%s%d)" % ("-" if signo < 0 else "", a, filas[clave + e], b, filas[clave + e])
                celda(ws, f, 2 + j, fx, FMT_PESOS, F_BOLD if bold else F_NORM)
            celda(ws, f, 5, "=SUM(B%d:D%d)" % (f, f), FMT_PESOS, F_BOLD)
            f += 1
        celda(ws, f, 1, "Saldo acumulado al cierre del año, vista completa", font=F_NOTA)
        for j, mm in enumerate((12, 24, 36)):
            celda(ws, f, 2 + j, "='Flujo mensual'!%s%d" % (col(mm), filas["sal_neto_" + e]), FMT_PESOS, F_NOTA)
        f += 2
    celda(ws, f, 1, "En esta hoja los costos van con signo negativo: el flujo neto es la suma de las tres filas anteriores.", font=F_NOTA, borde=None)
    ws.column_dimensions["A"].width = 55
    for c in "BCDE":
        ws.column_dimensions[c].width = 16
    return ws


IND_CELDAS = {}  # (vista, escenario, indicador) -> referencia absoluta


def hoja_indicadores(wb, filas):
    ws = wb.create_sheet("Indicadores", 0)
    titulo(ws, "Indicadores económicos del caso de negocio",
           "Dulxelitos: activar el stock de Discovery, con un piloto previo de 2 semanas con papas fritas. Pesos constantes de noviembre de 2026; 3 años.")
    f = 4
    rango = lambda clave: "'Flujo mensual'!$B$%d:$%s$%d" % (filas[clave], col(MESES), filas[clave])
    titulos = {
        "neto": "Vista completa: el tiempo del personal valorado al costo de la hora (base del pedido de aprobación)",
        "caja": "Solo caja: horas extras evitadas menos horas extras de los conteos",
        "neto_meta": "Sensibilidad, vista completa: se cumple la meta de horas extras (la mitad)",
        "caja_meta": "Sensibilidad, caja: se cumple la meta de horas extras (la mitad)",
        "caja_prod": "Sensibilidad, caja: la carga diaria y la reunión de Producción se pagan como horas extras",
        "neto_rt05": "Sensibilidad, vista completa: media hora de retrabajo por recortado en lugar de una",
        "neto_res5": "Sensibilidad, vista completa: 5 minutos por reserva en lugar de 3",
        "neto_sincop": "Sensibilidad, vista completa: sin el ahorro de las copias del pedido",
        "neto_jj": "Sensibilidad, vista completa: horas del responsable de sistemas valoradas",
        "caja_jj": "Sensibilidad, caja: el responsable de sistemas cobra esas horas aparte",
    }
    bloques = [(v, titulos[v], v + "_", "sal_" + v + "_") for v in VISTAS]
    for v, tit, kf, ks in bloques:
        seccion(ws, f, tit, 3)
        f += 1
        encabezado(ws, f, ["Indicador", "Conservador", "Esperado"])
        f += 1
        filas_ind = [("max", "Máximo expuesto (saldo acumulado más negativo)", FMT_PESOS0),
                     ("rec", "Mes de recupero (mes 1 = febrero de 2027)", FMT_NUM),
                     ("recmes", "Mes de recupero, en el calendario", FMT_MESLARGO),
                     ("van", "VAN a 3 años (tasa real anual de la hoja Supuestos)", FMT_PESOS),
                     ("tir", "TIR anual equivalente", FMT_PCT),
                     ("tirm", "TIR mensual", FMT_PCT1)]
        if v in ("neto", "caja"):
            filas_ind.append(("van20", "VAN a 3 años con la tasa alternativa (20 %)", FMT_PESOS))
        for k, etiqueta, fmt in filas_ind:
            celda(ws, f, 1, etiqueta)
            for j, e in enumerate(("con", "esp")):
                cc = get_column_letter(2 + j)
                if k == "max":
                    fx = "=-MIN(0,MIN(%s))" % rango(ks + e)
                elif k == "rec":
                    fx = '=IF(COUNTIF(%s,"<0")=%d,"Más de %d",COUNTIF(%s,"<0")+1)' % (rango(ks + e), MESES, MESES, rango(ks + e))
                elif k == "recmes":
                    fx = '=IF(ISNUMBER(%s%d),EDATE(Inicio,%s%d-1),"–")' % (cc, f - 1, cc, f - 1)
                elif k == "van":
                    fx = "=NPV(Tasa_mensual,%s)" % rango(kf + e)
                elif k == "tir":
                    fx = '=IFERROR((1+IRR(%s,0.1))^12-1,"–")' % rango(kf + e)
                elif k == "tirm":
                    fx = '=IFERROR(IRR(%s,0.1),"–")' % rango(kf + e)
                else:
                    fx = "=NPV((1+Tasa_alta)^(1/12)-1,%s)" % rango(kf + e)
                celda(ws, f, 2 + j, fx, fmt, F_BOLD if k in ("max", "rec", "van") else F_NORM, align=Alignment(horizontal="right"))
                IND_CELDAS[(v, e, k)] = "Indicadores!$%s$%d" % (cc, f)
            f += 1
        f += 1
    notas = [
        "Máximo expuesto: lo más que se pone antes de empezar a recuperar. Recupero: primer mes con saldo acumulado positivo.",
        "La TIR da valores muy altos porque lo que se pone al principio es chico frente a lo que vuelve después; para decidir conviene mirar el máximo expuesto, el recupero y el VAN.",
        "Vista completa: incluye el tiempo del personal en horario normal, que no es plata que sale sino capacidad que se usa o se libera.",
    ]
    for t in notas:
        celda(ws, f, 1, t, font=F_NOTA, borde=None, align=WRAP)
        ws.merge_cells(start_row=f, start_column=1, end_row=f, end_column=3)
        ws.row_dimensions[f].height = 28
        f += 1
    ws.column_dimensions["A"].width = 70
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 18
    return ws


def hoja_escenarios(wb):
    ws = wb.create_sheet("Escenarios", 1)
    titulo(ws, "Escenarios esperado y conservador",
           "El mismo cálculo dos veces; solo cambian los supuestos más inciertos. El presupuesto que se pide aprobar sale del conservador.")
    encabezado(ws, 4, ["", "Conservador", "Esperado"])
    f = 5
    seccion(ws, f, "Supuestos que cambian", 3)
    f += 1
    for etiqueta, a, b, fmt in [
        ("Pedidos recortados o demorados por semana (hoy 30)", "Recortados_con", "Recortados_esp", FMT_NUM),
        ("Reducción de las horas extras (hoy 45 h por mes)", "RedHE_con", "RedHE_esp", FMT_PCT1),
        ("Demora adicional del efecto, en semanas", "Demora_con", "Demora_esp", FMT_NUM),
        ("Contingencia sobre la puesta en marcha", "Cont_con", "Cont_esp", FMT_PCT),
    ]:
        celda(ws, f, 1, etiqueta)
        celda(ws, f, 2, "=" + a, fmt)
        celda(ws, f, 3, "=" + b, fmt)
        f += 1
    f += 1
    seccion(ws, f, "Por mes, con las tres líneas en uso", 3)
    f += 1
    for etiqueta, a, b in [
        ("Retrabajo evitado (capacidad liberada)", "=B_retrabajo_con", "=B_retrabajo_esp"),
        ("Horas extras evitadas (caja)", "=B_he_con", "=B_he_esp"),
        ("Tiempo interno nuevo, neto", "=-Rec_neto", "=-Rec_neto"),
        ("Neto mensual, vista completa", "=B_retrabajo_con+B_he_con-Rec_neto", "=B_retrabajo_esp+B_he_esp-Rec_neto"),
        ("Neto mensual de caja", "=B_he_con", "=B_he_esp"),
    ]:
        bold = etiqueta.startswith("Neto")
        celda(ws, f, 1, etiqueta, font=F_BOLD if bold else F_NORM)
        celda(ws, f, 2, a, FMT_PESOS, F_BOLD if bold else F_NORM)
        celda(ws, f, 3, b, FMT_PESOS, F_BOLD if bold else F_NORM)
        f += 1
    f += 1
    seccion(ws, f, "Resultados", 3)
    f += 1
    for etiqueta, v, k, fmt in [
        ("Máximo expuesto, vista completa", "neto", "max", FMT_PESOS0),
        ("Mes de recupero, vista completa", "neto", "rec", FMT_NUM),
        ("VAN a 3 años, vista completa", "neto", "van", FMT_PESOS),
        ("TIR anual equivalente, vista completa", "neto", "tir", FMT_PCT),
        ("Máximo expuesto, solo caja", "caja", "max", FMT_PESOS0),
        ("Mes de recupero, solo caja", "caja", "rec", FMT_NUM),
        ("VAN a 3 años, solo caja", "caja", "van", FMT_PESOS),
        ("VAN, vista completa, si se cumple la meta de horas extras", "neto_meta", "van", FMT_PESOS),
        ("VAN, solo caja, si la carga y la reunión de Producción se pagan como horas extras", "caja_prod", "van", FMT_PESOS),
        ("VAN, vista completa, con media hora de retrabajo por recortado", "neto_rt05", "van", FMT_PESOS),
        ("VAN, vista completa, con 5 minutos por reserva", "neto_res5", "van", FMT_PESOS),
        ("VAN, vista completa, sin el ahorro de las copias del pedido", "neto_sincop", "van", FMT_PESOS),
        ("VAN, vista completa, con las horas del responsable de sistemas valoradas", "neto_jj", "van", FMT_PESOS),
        ("VAN, solo caja, si el responsable de sistemas cobrara esas horas aparte", "caja_jj", "van", FMT_PESOS),
    ]:
        celda(ws, f, 1, etiqueta, align=WRAP)
        celda(ws, f, 2, "=" + IND_CELDAS[(v, "con", k)], fmt, align=Alignment(horizontal="right"))
        celda(ws, f, 3, "=" + IND_CELDAS[(v, "esp", k)], fmt, align=Alignment(horizontal="right"))
        f += 1
    f += 1
    seccion(ws, f, "Lo que se pide aprobar (conservador)", 3)
    f += 1
    refs = {}
    for marcador, etiqueta, clave in [
        ("C_TOPE", "Tope del piloto: semanas 1 a 6, vista completa", "inversion_piloto_conservador"),
        ("C_TOPE_UNA", "   = línea de base, conteo y capacitación del piloto, piloto, su comunicación y 6 reuniones semanales", "tope_una_vez_conservador"),
        ("C_TOPE_CONT", "   + contingencia del 20 % sobre eso", "tope_contingencia_conservador"),
        ("C_TOPE_REC", "   + reunión diaria y tablero de las semanas 4 a 6", "tope_recurrente_conservador"),
        ("C_TOPE_EF", "   de todo eso, sale de la caja (horas extras del conteo)", "efectivo_piloto_conservador"),
        ("C_TECHO", "Techo del proyecto, que se libera con el Go: semanas 1 a 26, sin restar beneficios", "techo_proyecto_conservador"),
        ("C_TECHO_UNA", "   = puesta en marcha completa con 20 % de contingencia", "inversion_total_conservador"),
        ("C_TECHO_REC", "   + tiempo interno recurrente de las semanas 4 a 26, a medida que cada línea queda en uso", "techo_recurrente_conservador"),
        ("C_TECHO_EF", "   de todo eso, sale de la caja (horas extras de los conteos)", "efectivo_proyecto_conservador"),
    ]:
        bold = marcador in ("C_TOPE", "C_TECHO")
        celda(ws, f, 1, etiqueta, font=F_BOLD if bold else F_NORM, align=WRAP)
        celda(ws, f, 2, None, FMT_PESOS, F_BOLD if bold else F_NORM)
        refs[marcador] = (f, clave)
        f += 1
    ws.column_dimensions["A"].width = 70
    ws.column_dimensions["B"].width = 18
    ws.column_dimensions["C"].width = 18
    return ws, refs


def hoja_no_actuar(wb):
    ws = wb.create_sheet("Costo de no actuar")
    titulo(ws, "Costo de no actuar", "Lo que equivale a seguir como hoy, cada mes: una parte es dinero (horas extras) y el resto, tiempo de la gente.")
    encabezado(ws, 4, ["Concepto", "Por mes", "Por año", "Dinero o tiempo"])
    f = 5
    for etiqueta, fx, caja in [
        ("Retrabajo de los 30 pedidos recortados por semana (1 h × hora de retrabajo)", "=Recortados_hoy*Retrabajo_h*Hora_retrabajo*Sem_mes",
         "Tiempo de Oficina y Depósito, en horario normal"),
        ("Horas extras ligadas a completar pedidos (la mitad de 45 h, supuesto 7)", "=HE_mes_hoy*Parte_HE_pedidos*Hora_extra",
         "Dinero: horas extras que se pagan"),
    ]:
        celda(ws, f, 1, etiqueta, align=WRAP)
        celda(ws, f, 2, fx, FMT_PESOS)
        celda(ws, f, 3, "=B%d*12" % f, FMT_PESOS)
        celda(ws, f, 4, caja, align=WRAP)
        f += 1
    celda(ws, f, 1, "Costo de no actuar (equivale a)", font=F_BOLD, fill=FILL_TOT, borde=BORDE_TOT)
    celda(ws, f, 2, "=SUM(B5:B6)", FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    celda(ws, f, 3, "=SUM(C5:C6)", FMT_PESOS, F_BOLD, FILL_TOT, BORDE_TOT)
    celda(ws, f, 4, None, fill=FILL_TOT, borde=BORDE_TOT)
    f += 2
    celda(ws, f, 1, "Como referencia: todas las horas extras de hoy (45 h)")
    celda(ws, f, 2, "=HE_mes_hoy*Hora_extra", FMT_PESOS)
    celda(ws, f, 3, "=B%d*12" % f, FMT_PESOS)
    f += 1
    celda(ws, f, 1, "Cada mes que se demora la decisión, se pierde el neto mensual pleno: conservador")
    celda(ws, f, 2, "=B_retrabajo_con+B_he_con-Rec_neto", FMT_PESOS)
    f += 1
    celda(ws, f, 1, "Ídem, esperado")
    celda(ws, f, 2, "=B_retrabajo_esp+B_he_esp-Rec_neto", FMT_PESOS)
    f += 2
    celda(ws, f, 1, "Sin cuantificar: el riesgo comercial de que un distribuidor patagónico se canse de recibir pedidos incompletos, la cobranza que se "
          "demora hasta completar el pedido y el segundo flete que paga el distribuidor. La venta recortada no se cuenta: se manda después.",
          font=F_NOTA, borde=None, align=WRAP)
    ws.merge_cells(start_row=f, start_column=1, end_row=f, end_column=4)
    ws.row_dimensions[f].height = 42
    ws.column_dimensions["A"].width = 70
    ws.column_dimensions["B"].width = 16
    ws.column_dimensions["C"].width = 16
    ws.column_dimensions["D"].width = 30
    return ws


def formula_cifra(clave, filas):
    """Formula de Excel para cada clave de caso.json."""
    vistas = {suf: v for v, suf in SUFIJO.items()}
    es = {"esperado": "esp", "conservador": "con"}
    for suf, v in sorted(vistas.items(), key=lambda x: -len(x[0])):
        for n, e in es.items():
            if clave == "max_expuesto%s_%s" % (suf, n):
                return "=" + IND_CELDAS[(v, e, "max")]
            if clave == "recupero_meses%s_%s" % (suf, n):
                return "=" + IND_CELDAS[(v, e, "rec")]
            if clave == "van_3a%s_%s" % (suf, n):
                return "=" + IND_CELDAS[(v, e, "van")]
            if clave == "tir%s_%s" % (suf, n):
                return "=" + IND_CELDAS[(v, e, "tir")]
            if clave == "tir_mensual%s_%s" % (suf, n):
                return "=" + IND_CELDAS[(v, e, "tirm")]
    for n, e in es.items():
        tabla = {
            "recortados_semana_" + n: "=Recortados_" + e,
            "retrabajo_evitado_mensual_" + n: "=B_retrabajo_" + e,
            "horas_extras_evitadas_mensual_" + n: "=B_he_" + e,
            "horas_extras_evitadas_horas_" + n: "=HE_mes_hoy*RedHE_" + e,
            "horas_retrabajo_evitado_mes_" + n: "=H_retrabajo_" + e,
            "beneficio_mensual_" + n: "=B_retrabajo_%s+B_he_%s" % (e, e),
            "neto_mensual_" + n: "=B_retrabajo_%s+B_he_%s-Rec_neto" % (e, e),
            "neto_mensual_caja_" + n: "=B_he_" + e,
            "van_3a_tasa20_" + n: "=" + IND_CELDAS[("neto", e, "van20")],
            "van_3a_caja_tasa20_" + n: "=" + IND_CELDAS[("caja", e, "van20")],
        }
        rangos = [(col(1), col(12)), (col(13), col(24)), (col(25), col(36))]
        for a, (c0, c1) in enumerate(rangos):
            tabla["flujo_anio%d_%s" % (a + 1, n)] = "=SUM('Flujo mensual'!%s%d:%s%d)" % (c0, filas["neto_" + e], c1, filas["neto_" + e])
            tabla["flujo_caja_anio%d_%s" % (a + 1, n)] = "=SUM('Flujo mensual'!%s%d:%s%d)" % (c0, filas["caja_" + e], c1, filas["caja_" + e])
        if clave in tabla:
            return tabla[clave]

    def una_semanas(semana):
        partes = ["C_%s*MAX(0,MIN({W},%s)-MAX(0,(%s)-1))/((%s)-(%s)+1)" % (k, e_, s_, e_, s_) for k, _, w in UNA for s_, e_ in w]
        return ("(" + "+".join(partes) + ")").replace("{W}", semana)

    def rec_semanas(semana):
        fx = "(R_reunion+R_tablero)*MAX(0,{W}-(Reunion_desde-1))/Sem_mes"
        fx += "+(" + "+".join("R_" + k for k in REC_POR_LINEA) + ")*(" + "+".join(
            "Parte_%s*MAX(0,{W}-(Uso_%s-1))" % (l, l) for l in LINEAS) + ")/Sem_mes"
        return fx.replace("{W}", semana)

    def costo_semanas(semana, e):
        return "=%s*(1+Cont_%s)+%s" % (una_semanas(semana), e, rec_semanas(semana))

    def efectivo_semanas(semana, e):
        partes = ["C_%s*MAX(0,MIN({W},%s)-MAX(0,(%s)-1))/((%s)-(%s)+1)" % (k, e_, s_, e_, s_)
                  for k, _, w in UNA if k in EFECTIVO_KEYS for s_, e_ in w]
        return ("=(" + "+".join(partes) + ")*(1+Cont_%s)" % e).replace("{W}", semana)

    otras = {
        "tasa_descuento_real_anual": "=Tasa_anual",
        "inversion_total_esperado": "=Una_vez_total*(1+Cont_esp)",
        "inversion_total_conservador": "=Una_vez_total*(1+Cont_con)",
        "puesta_en_marcha_sin_contingencia": "=Una_vez_total",
        "conteo_inicial_tres_lineas": "=3*C_conteo_linea",
        "activacion_resto_tres_lineas": "=3*(C_cap_linea+C_config+C_trans)",
        "inversion_piloto_conservador": costo_semanas("Sem_go", "con"),
        "efectivo_piloto_conservador": efectivo_semanas("Sem_go", "con"),
        "techo_proyecto_conservador": costo_semanas("Seg_hasta", "con"),
        "efectivo_proyecto_conservador": efectivo_semanas("Seg_hasta", "con"),
        "costo_recurrente_neto_mensual": "=Rec_neto",
        "costo_recurrente_nuevo_mensual": "=R_carga+R_reunion+R_reserva+R_revision+R_conteo+R_tablero",
        "costo_recurrente_reemplazado_mensual": "=-(R_ctrl+R_averig+R_copias)",
        "tope_una_vez_conservador": "=" + una_semanas("Sem_go"),
        "tope_contingencia_conservador": "=" + una_semanas("Sem_go") + "*Cont_con",
        "tope_recurrente_conservador": "=" + rec_semanas("Sem_go"),
        "techo_recurrente_conservador": "=" + rec_semanas("Seg_hasta"),
        "comunicacion_capacitacion": "=C_com_piloto+C_com_lineas+C_cap_piloto+3*C_cap_linea+C_seg",
        "horas_nuevas_mes": "=H_nuevas",
        "horas_reemplazadas_mes": "=H_reempl",
        "horas_juanjo_plan": "=Jj_h_piloto+3*Jj_h_linea+(Seg_hasta-Seg_desde+1)*Seg_min/60",
        "costo_juanjo_sens": "=Jj_total",
        "horas_extras_evitadas_mensual_meta": "=B_hemeta",
        "horas_retrabajo_hoy_mes": "=Recortados_hoy*Retrabajo_h*Sem_mes",
        "tiempo_produccion_en_horas_extras_mensual": "=R_prod_he",
        "retrabajo_hoy_mensual": "=Recortados_hoy*Retrabajo_h*Hora_retrabajo*Sem_mes",
        "horas_extras_hoy_mensual": "=HE_mes_hoy*Hora_extra",
        "horas_extras_ligadas_pedidos_mensual": "=HE_mes_hoy*Parte_HE_pedidos*Hora_extra",
        "costo_no_actuar_mensual": "=Recortados_hoy*Retrabajo_h*Hora_retrabajo*Sem_mes+HE_mes_hoy*Parte_HE_pedidos*Hora_extra",
        "costo_no_actuar_anual": "=12*(Recortados_hoy*Retrabajo_h*Hora_retrabajo*Sem_mes+HE_mes_hoy*Parte_HE_pedidos*Hora_extra)",
        "costo_no_actuar_caja_mensual": "=HE_mes_hoy*Parte_HE_pedidos*Hora_extra",
        "equilibrio_recortes_evitados_semana": "=Rec_neto/(Retrabajo_h*Hora_retrabajo*Sem_mes)",
    }
    return otras[clave]


def hoja_cifras(wb, filas):
    ws = wb.create_sheet("Cifras del informe")
    titulo(ws, "Cifras que usa el informe", "Cada cifra del dossier y de la presentación sale de esta lista (clave = nombre en caso.json).")
    encabezado(ws, 4, ["Clave", "Descripción", "Valor"])
    f = 5
    posiciones = {}
    fmts = {"pesos": FMT_PESOS0, "pct": FMT_PCT1, "num": FMT_NUM2, "meses": FMT_NUM}
    for clave, desc, valor, tipo in CIFRAS:
        celda(ws, f, 1, clave, font=F_NOTA)
        celda(ws, f, 2, desc, align=WRAP)
        celda(ws, f, 3, formula_cifra(clave, filas), fmts[tipo], align=Alignment(horizontal="right"))
        posiciones[clave] = f
        f += 1
    ws.column_dimensions["A"].width = 40
    ws.column_dimensions["B"].width = 80
    ws.column_dimensions["C"].width = 18
    return ws, posiciones


def armar_xlsx():
    wb = Workbook()
    wb.remove(wb.active)
    hoja_supuestos(wb)
    hoja_costos(wb)
    ws_flujo, filas = hoja_flujo(wb)
    hoja_anual(wb, filas)
    hoja_indicadores(wb, filas)
    ws_esc, refs = hoja_escenarios(wb)
    hoja_no_actuar(wb)
    ws_cif, pos = hoja_cifras(wb, filas)
    # referencias de Escenarios a Cifras del informe
    for marcador, (fila_esc, clave) in refs.items():
        ws_esc.cell(row=fila_esc, column=2).value = "='Cifras del informe'!$C$%d" % pos[clave]
    # orden: Indicadores, Escenarios, Supuestos, Costos, Flujo mensual, Flujo anual, Costo de no actuar, Cifras
    orden = ["Indicadores", "Escenarios", "Supuestos", "Costos y beneficios", "Flujo mensual", "Flujo anual",
             "Costo de no actuar", "Cifras del informe"]
    wb._sheets = [wb[n] for n in orden]
    wb.active = 0
    for ws in wb.worksheets:
        ws.page_setup.orientation = "landscape"
        ws.page_setup.fitToWidth = 1
        ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
    wb.calculation.fullCalcOnLoad = True
    os.makedirs(os.path.dirname(XLSX), exist_ok=True)
    wb.save(XLSX)
    return pos


# =============================================================================
# 5. Verificacion con Excel
# =============================================================================

def verificar_excel():
    cont = os.path.expanduser("~/Library/Containers/com.microsoft.Excel/Data/Documents")
    os.makedirs(cont, exist_ok=True)
    copia = os.path.join(cont, "verificar-caso-dulxelitos.xlsx")
    shutil.copyfile(XLSX, copia)
    script = '''
set f to POSIX file "%s"
set sep to tab
set nl to linefeed
tell application "Microsoft Excel"
    set display alerts to false
    open f
    set wb to active workbook
    calculate full
    set ws to worksheet "Cifras del informe" of wb
    set n to %d
    set salida to ""
    repeat with i from 5 to (n + 4)
        set k to value of cell 1 of row i of ws
        set v to value of cell 3 of row i of ws
        set salida to salida & k & sep & (v as string) & nl
    end repeat
    save wb
    close wb saving no
end tell
return salida
''' % (copia, len(CIFRAS))
    res = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, timeout=300)
    if res.returncode != 0:
        print("Excel no respondió:", res.stderr.strip())
        return False
    with open(JSON, encoding="utf-8") as fh:
        caso = json.load(fh)
    tipos = {c[0]: c[3] for c in CIFRAS}
    exactos = {c[0]: c[2] for c in CIFRAS}
    fallas = 0
    for linea in res.stdout.strip().splitlines():
        k, _, v = linea.partition("\t")
        k = k.strip()
        v = v.strip().replace(",", ".")
        try:
            ve = float(v)
        except ValueError:
            ve = v
        esperado = caso.get(k)
        tipo = tipos[k]
        if tipo == "pesos":
            ok = isinstance(ve, float) and abs(ve - esperado) <= 1
        elif tipo == "pct" and exactos[k] is None:
            ok = isinstance(ve, str)
        elif tipo == "pct":
            ok = isinstance(ve, float) and abs(ve - exactos[k]) * 100 <= 0.1
        elif tipo == "meses":
            ok = (esperado is None and isinstance(ve, str)) or (isinstance(ve, float) and abs(ve - esperado) < 0.01)
        else:
            ok = isinstance(ve, float) and abs(ve - exactos[k]) < 0.01
        estado = "ok " if ok else "MAL"
        fallas += 0 if ok else 1
        print("%s %-42s excel=%-22s json=%s" % (estado, k, v, esperado))
    print("Excel: %d cifras comparadas, %d diferencias" % (len(CIFRAS), fallas))
    # la copia quedó guardada por Excel con los valores calculados: se vuelve a poner en Entrega
    # para que las vistas previas sin Excel (Finder, OneDrive) muestren los números
    if fallas == 0:
        shutil.copyfile(copia, XLSX)
        print("Guardé la planilla con los valores calculados por Excel")
    os.remove(copia)
    return fallas == 0


def main():
    armar_xlsx()
    d = armar_json()
    with open(JSON, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=2)
    print("Escribí", os.path.relpath(XLSX, BASE), "y caso.json")
    for k in ("inversion_piloto_conservador", "techo_proyecto_conservador", "inversion_total_esperado", "inversion_total_conservador",
              "costo_recurrente_neto_mensual", "neto_mensual_esperado", "neto_mensual_conservador", "max_expuesto_esperado",
              "max_expuesto_conservador", "recupero_meses_esperado", "recupero_meses_conservador", "van_3a_esperado", "van_3a_conservador",
              "max_expuesto_caja_conservador", "recupero_meses_caja_conservador", "van_3a_caja_conservador",
              "tir_mensual_esperado", "tir_mensual_conservador", "costo_no_actuar_mensual", "costo_no_actuar_caja_mensual"):
        print("  %-34s %s" % (k, d[k]))
    for v in VISTAS:
        print("  sens %-12s con: VAN %s rec %s | esp: VAN %s" % (SUFIJO[v] or "base", d["van_3a%s_conservador" % SUFIJO[v]],
                                                                d["recupero_meses%s_conservador" % SUFIJO[v]], d["van_3a%s_esperado" % SUFIJO[v]]))
    if "--verificar" in sys.argv:
        sys.exit(0 if verificar_excel() else 1)


if __name__ == "__main__":
    main()
