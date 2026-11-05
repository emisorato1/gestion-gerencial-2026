# -*- coding: utf-8 -*-
"""Especificacion del BPMN TO-BE: Atender pedido de distribuidor (Dulxelitos).

Fuente: 00 - Diseño.md, seccion 3 (TO-BE, sobre la alternativa recomendada) y las
reglas de datos de 06 - Arquitectura y datos.md. Se dibuja con
    .venv/bin/python bpmn/generar_bpmn.py bpmn/to-be.py
Mismas lanes y mismos pools que el AS-IS (bpmn/as-is.py): Oficina, Depósito,
Producción y Dirección, con los pools colapsados Distribuidor y Transporte
tercerizado. Tres cosas arrancan por su cuenta, como en la sección 3: el pedido
(mensaje del distribuidor), la semana de producción (Dirección) y el conteo
semanal (Depósito).
"""

PROCESO = {
    "nombre": "Atender pedido de distribuidor (TO-BE)",
    "pools": [
        {"id": "distribuidor", "nombre": "Distribuidor", "colapsado": True, "lanes": []},
        {"id": "dulxelitos", "nombre": "Dulxelitos", "colapsado": False, "lanes": [
            {"id": "oficina", "nombre": "Oficina", "nodos": [
                {"id": "ini_pedido", "tipo": "inicio_mensaje", "texto": "Pedido recibido",
                 "col": 0, "fila": 1},
                {"id": "cargar_nota", "tipo": "tarea_usuario",
                 "texto": "Cargar nota de pedido en Discovery", "col": 1, "fila": 1},
                {"id": "union_consulta", "tipo": "xor", "texto": "", "col": 2, "fila": 1},
                {"id": "consultar", "tipo": "tarea_usuario", "texto": "Consultar stock disponible",
                 "col": 3, "fila": 1},
                {"id": "xor_stock", "tipo": "xor", "texto": "¿Hay stock disponible?", "col": 4,
                 "fila": 1, "ancho_etiqueta": 170},
                {"id": "reservar", "tipo": "tarea_usuario", "texto": "Reservar stock",
                 "col": 5, "fila": 1},
                {"id": "confirmar", "tipo": "tarea", "texto": "Confirmar pedido al distribuidor",
                 "col": 6, "fila": 1},
                {"id": "facturar", "tipo": "tarea_usuario", "texto": "Facturar en Discovery",
                 "col": 8, "fila": 1},
                {"id": "avisar", "tipo": "tarea", "texto": "Avisar faltante con fecha estimada",
                 "col": 4, "fila": 0},
                {"id": "espera", "tipo": "evento_tiempo", "texto": "Fecha estimada cumplida",
                 "col": 3, "fila": 0},
                {"id": "a_regla", "tipo": "anotacion", "col": 5.2, "fila": 0, "ancho": 215,
                 "texto": "Stock disponible = stock físico menos lo reservado por pedidos "
                          "confirmados sin facturar. Si alcanza solo para una parte, se "
                          "reserva eso y el resto queda pendiente."},
                {"id": "a_factura", "tipo": "anotacion", "col": 8, "fila": 0, "ancho": 180,
                 "texto": "La factura consume la reserva (a probar en Discovery)."},
            ]},
            {"id": "deposito", "nombre": "Depósito", "nodos": [
                {"id": "ini_conteo", "tipo": "evento_tiempo", "texto": "Conteo semanal programado",
                 "col": 1},
                {"id": "contar", "tipo": "tarea", "texto": "Contar stock", "col": 3},
                {"id": "fin_conteo", "tipo": "fin", "texto": "Stock contado", "col": 4},
                {"id": "a_ajuste", "tipo": "anotacion", "col": 3.5, "fila": 1, "ancho": 250,
                 "texto": "Si hay diferencias, manda lo contado: el responsable de sistemas "
                          "carga el ajuste en Discovery, con el motivo."},
                {"id": "preparar", "tipo": "tarea", "texto": "Preparar pedido", "col": 7},
                {"id": "xor_despacho", "tipo": "xor", "texto": "¿Con qué se despacha?", "col": 9},
                {"id": "flota", "tipo": "tarea", "texto": "Despachar con flota propia", "col": 10},
                {"id": "tercerizado", "tipo": "tarea", "texto": "Entregar a transporte tercerizado",
                 "col": 10, "fila": 1},
                {"id": "fin_pedido", "tipo": "fin", "texto": "Pedido despachado", "col": 11},
            ]},
            {"id": "produccion", "nombre": "Producción", "nodos": [
                {"id": "producir", "tipo": "tarea", "texto": "Producir lo planificado",
                 "col": 1, "fila": 1},
                {"id": "cargar_produccion", "tipo": "tarea_usuario",
                 "texto": "Cargar producción del día", "col": 3, "fila": 1},
                {"id": "fin_produccion", "tipo": "fin", "texto": "Producción cargada",
                 "col": 4, "fila": 1},
                {"id": "datos_stock", "tipo": "datos", "texto": "Stock en Discovery",
                 "col": 3, "fila": 0, "etiqueta": "izq"},
                {"id": "a_carga", "tipo": "anotacion", "col": 1, "fila": 0, "ancho": 215,
                 "texto": "Se carga todos los días, al cierre del turno, y no una vez por "
                          "semana. Un responsable de carga por turno, con suplente."},
                {"id": "a_reunion", "tipo": "anotacion", "col": 5.4, "fila": 0, "ancho": 260,
                 "texto": "Reunión diaria ventas–producción (~10 min): se mira el disponible, "
                          "los pedidos pendientes y los avisos, y Producción confirma la fecha."},
            ]},
            {"id": "direccion", "nombre": "Dirección", "nodos": [
                {"id": "ini_semana", "tipo": "evento_tiempo", "texto": "Semana iniciada", "col": 0},
                {"id": "planificar", "tipo": "tarea", "texto": "Planificar producción de la semana",
                 "col": 1},
                {"id": "tablero", "tipo": "datos", "texto": "Tablero de 4 indicadores",
                 "col": 1, "fila": 1},
                {"id": "a_plan", "tipo": "anotacion", "col": 3.5, "fila": 0, "ancho": 270,
                 "texto": "Decide el dueño o uno de los hijos, mirando los pedidos pendientes "
                          "(los avisados con faltante) y el stock mínimo por producto."},
                {"id": "a_extras", "tipo": "anotacion", "col": 3.5, "fila": 1, "ancho": 270,
                 "texto": "Las horas extras son una excepción que se decide en este plan, no "
                          "el arreglo habitual del faltante."},
            ]},
        ]},
        {"id": "transporte", "nombre": "Transporte tercerizado", "colapsado": True, "lanes": []},
    ],
    "flujos": [
        # Pedido: se carga una vez, se consulta el disponible y se decide con ese dato
        {"de": "ini_pedido", "a": "cargar_nota"},
        {"de": "cargar_nota", "a": "union_consulta"},
        {"de": "union_consulta", "a": "consultar"},
        {"de": "consultar", "a": "xor_stock"},
        # Si hay: reserva, confirma y Depósito arma desde el pedido confirmado
        {"de": "xor_stock", "a": "reservar", "texto": "Sí", "dy": 20},
        {"de": "reservar", "a": "confirmar"},
        {"de": "confirmar", "a": "preparar"},
        {"de": "preparar", "a": "facturar"},
        {"de": "facturar", "a": "xor_despacho"},
        {"de": "xor_despacho", "a": "flota", "texto": "Flota propia"},
        {"de": "xor_despacho", "a": "tercerizado", "texto": "Transporte tercerizado"},
        {"de": "flota", "a": "fin_pedido"},
        {"de": "tercerizado", "a": "fin_pedido", "ruta": "hvh"},
        # Si no hay: aviso con fecha, espera y vuelve a consultar (sin bucle infinito: si hay, reserva)
        {"de": "xor_stock", "a": "avisar", "texto": "No"},
        {"de": "avisar", "a": "espera"},
        {"de": "espera", "a": "union_consulta", "ruta": "hv"},
        # Producción: planificada contra pedidos y cargada todos los días
        {"de": "ini_semana", "a": "planificar"},
        {"de": "planificar", "a": "producir"},
        {"de": "producir", "a": "cargar_produccion"},
        {"de": "cargar_produccion", "a": "fin_produccion"},
        # Conteo cíclico semanal
        {"de": "ini_conteo", "a": "contar"},
        {"de": "contar", "a": "fin_conteo"},
        # Datos y anotaciones (asociaciones punteadas)
        {"de": "cargar_produccion", "a": "datos_stock"},
        {"de": "planificar", "a": "tablero"},
        {"de": "a_regla", "a": "xor_stock"},
        {"de": "a_factura", "a": "facturar"},
        {"de": "a_ajuste", "a": "contar"},
        {"de": "a_carga", "a": "cargar_produccion"},
        {"de": "a_reunion", "a": "datos_stock"},
        {"de": "a_plan", "a": "planificar"},
        {"de": "a_extras", "a": "planificar"},
    ],
    "mensajes": [
        {"de": "distribuidor", "a": "ini_pedido", "texto": "Pedido por WhatsApp o teléfono"},
        {"de": "confirmar", "a": "distribuidor", "texto": "Confirmación del pedido"},
        {"de": "avisar", "a": "distribuidor", "texto": "Aviso de faltante con fecha estimada"},
        {"de": "tercerizado", "a": "transporte", "texto": "Pedido a entregar"},
    ],
    "anchos": {9: 190},
}
