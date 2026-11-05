# -*- coding: utf-8 -*-
"""Especificacion del BPMN AS-IS: Atender pedido de distribuidor (Dulxelitos).

Fuente: 00 - Diseño.md, seccion 3 (AS-IS, relevado por el grupo). Se dibuja con
    .venv/bin/python bpmn/generar_bpmn.py bpmn/as-is.py
Las lanes (Oficina, Depósito, Producción, Dirección) son las mismas del RECI
de 02 - Proceso actual y alternativas.md.
"""

PROCESO = {
    "nombre": "Atender pedido de distribuidor (AS-IS)",
    "pools": [
        # Pools colapsados: sin lanes ni nodos, solo reciben o mandan mensajes.
        {"id": "distribuidor", "nombre": "Distribuidor", "colapsado": True, "lanes": []},
        {"id": "dulxelitos", "nombre": "Dulxelitos", "colapsado": False, "lanes": [
            {"id": "oficina", "nombre": "Oficina", "nodos": [
                {"id": "ini_pedido", "tipo": "inicio_mensaje", "texto": "Pedido recibido", "col": 0},
                {"id": "anotar", "tipo": "tarea", "texto": "Anotar pedido en papel o planilla", "col": 1},
                {"id": "papel", "tipo": "datos", "texto": "Papel o planilla", "col": 1, "fila": 1},
                {"id": "and_ini", "tipo": "and", "texto": "", "col": 2},
                {"id": "preguntar", "tipo": "tarea", "texto": "Preguntar disponibilidad a producción", "col": 3},
                {"id": "a_transcripciones", "tipo": "anotacion", "col": 3, "fila": 1, "ancho": 190,
                 "texto": "Tarea manual: el mismo pedido se transcribe tres veces (chat, papel y lista)."},
                {"id": "and_fin", "tipo": "and", "texto": "", "col": 4},
                {"id": "lista", "tipo": "tarea", "texto": "Pasar pedido a la lista", "col": 5},
                {"id": "lista_datos", "tipo": "datos", "texto": "Lista de pedidos", "col": 5, "fila": 1},
                {"id": "xor_faltante", "tipo": "xor", "texto": "¿Qué se hace con el faltante?", "col": 8},
                {"id": "avisar", "tipo": "tarea", "texto": "Avisar al distribuidor del faltante", "col": 9},
                {"id": "union", "tipo": "xor", "texto": "", "col": 10},
                {"id": "facturar", "tipo": "tarea_usuario", "texto": "Facturar en Discovery", "col": 11},
            ]},
            {"id": "deposito", "nombre": "Depósito", "nodos": [
                {"id": "mirar", "tipo": "tarea", "texto": "Mirar el stock a ojo", "col": 3},
                {"id": "a_doble", "tipo": "anotacion", "col": 3.9, "fila": 1, "ancho": 200,
                 "texto": "Ineficiencia: doble averiguación de disponibilidad, a ojo en el depósito "
                          "y preguntando a producción."},
                {"id": "preparar", "tipo": "tarea", "texto": "Preparar pedido", "col": 6},
                {"id": "xor_falta", "tipo": "xor", "texto": "¿Falta producto?", "col": 7},
                {"id": "xor_despacho", "tipo": "xor", "texto": "¿Con qué se despacha?", "col": 11},
                {"id": "flota", "tipo": "tarea", "texto": "Despachar con flota propia", "col": 12},
                {"id": "tercerizado", "tipo": "tarea", "texto": "Entregar a transporte tercerizado",
                 "col": 12, "fila": 1},
                {"id": "fin_pedido", "tipo": "fin", "texto": "Pedido despachado", "col": 13},
            ]},
            {"id": "produccion", "nombre": "Producción", "nodos": [
                {"id": "datos_produccion", "tipo": "datos", "texto": "Registro de producción", "col": 1,
                 "etiqueta": "izq"},
                {"id": "a_datos", "tipo": "anotacion", "col": 6, "fila": 0, "ancho": 200,
                 "texto": "Flujo de datos: producción, depósito y ventas no comparten ningún dato; "
                          "no hay stock de producto terminado registrado."},
                {"id": "producir_y_registrar", "tipo": "tarea", "texto": "Producir y registrar producción",
                 "col": 1, "fila": 1},
                {"id": "fin_semana", "tipo": "fin", "texto": "Producción registrada", "col": 2, "fila": 1},
                {"id": "esperar", "tipo": "tarea", "texto": "Producir lo que falta", "col": 9},
                {"id": "horas_extras", "tipo": "tarea", "texto": "Producir con horas extras", "col": 9, "fila": 1},
            ]},
            {"id": "direccion", "nombre": "Dirección", "nodos": [
                {"id": "ini_semana", "tipo": "evento_tiempo", "texto": "Semana iniciada", "col": 0},
                {"id": "decidir", "tipo": "tarea", "texto": "Decidir producción", "col": 1},
                {"id": "a_criterio", "tipo": "anotacion", "col": 3.5,
                 "texto": "Decide el dueño o uno de los hijos, por criterio propio y sin mirar los pedidos."},
                {"id": "a_extras", "tipo": "anotacion", "col": 9,
                 "texto": "Horas extras si hace falta: unas 25 por mes."},
            ]},
        ]},
        {"id": "transporte", "nombre": "Transporte tercerizado", "colapsado": True, "lanes": []},
    ],
    "flujos": [
        # Pedido: Oficina anota, se averigua la disponibilidad (a ojo y preguntando) y se arma la lista
        {"de": "ini_pedido", "a": "anotar"},
        {"de": "anotar", "a": "and_ini"},
        {"de": "and_ini", "a": "preguntar"},
        {"de": "and_ini", "a": "mirar"},
        {"de": "preguntar", "a": "and_fin"},
        {"de": "mirar", "a": "and_fin"},
        {"de": "and_fin", "a": "lista"},
        {"de": "lista", "a": "preparar"},
        {"de": "preparar", "a": "xor_falta"},
        # Si falta producto: tres salidas posibles
        {"de": "xor_falta", "a": "union", "texto": "No", "ruta": "hv"},
        {"de": "xor_falta", "a": "xor_faltante", "texto": "Sí"},
        {"de": "xor_faltante", "a": "avisar", "texto": "Se manda incompleto"},
        {"de": "xor_faltante", "a": "esperar", "texto": "Se espera producción", "pos": "fin"},
        {"de": "xor_faltante", "a": "horas_extras", "texto": "Horas extras, si hace falta", "pos": "fin"},
        {"de": "avisar", "a": "union"},
        {"de": "esperar", "a": "union"},
        {"de": "horas_extras", "a": "union"},
        # Facturar y despachar
        {"de": "union", "a": "facturar"},
        {"de": "facturar", "a": "xor_despacho"},
        {"de": "xor_despacho", "a": "flota", "texto": "Flota propia"},
        {"de": "xor_despacho", "a": "tercerizado", "texto": "Transporte tercerizado"},
        {"de": "flota", "a": "fin_pedido"},
        {"de": "tercerizado", "a": "fin_pedido", "ruta": "hvh"},
        # Producción: independiente del pedido (Dirección decide, Producción registra una vez por semana)
        {"de": "ini_semana", "a": "decidir"},
        {"de": "decidir", "a": "producir_y_registrar"},
        {"de": "producir_y_registrar", "a": "fin_semana"},
        # Datos y anotaciones (asociaciones punteadas)
        {"de": "anotar", "a": "papel"},
        {"de": "lista", "a": "lista_datos"},
        {"de": "producir_y_registrar", "a": "datos_produccion"},
        {"de": "a_transcripciones", "a": "papel"},
        {"de": "a_transcripciones", "a": "lista_datos"},
        {"de": "a_doble", "a": "mirar"},
        {"de": "a_datos", "a": "datos_produccion"},
        {"de": "a_datos", "a": "preparar"},
        {"de": "a_criterio", "a": "decidir"},
        {"de": "a_extras", "a": "horas_extras"},
    ],
    "mensajes": [
        {"de": "distribuidor", "a": "ini_pedido", "texto": "Pedido por WhatsApp o teléfono"},
        {"de": "avisar", "a": "distribuidor", "texto": "Aviso de pedido incompleto"},
        {"de": "tercerizado", "a": "transporte", "texto": "Pedido a entregar"},
    ],
    "anchos": {8: 150, 11: 180},
}
