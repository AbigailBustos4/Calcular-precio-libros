"""Paso 1: 
Pedir el nombre del libro (Nombre-escuela-grado)
Preguntar cuantas hojas son simple faz:
Preguntar cuantas hojas son doble faz:
Preguntar cuantas hojas son simple faz color:
Preguntar cuantas hojas son doble faz color:      

Agregar una descripcion que te muestre cuantas hojas tenes de cada tipo y te muestre el numero que se le asigno:
Asigna 1 hojas son simple faz:
Asigna 2 hojas son doble faz:
Asigna 3 hojas son simple faz color:
Asigna 4 cuantas hojas son doble faz color:
Asigna 5 si es mixto
"""
"""# Intento de agregar SQL. LO PASE A CONEXION.PY
conexion = mysql.connector.connect(
    host="127.0.0.1",  # O "localhost"
    user="root",
    password="root",
    database="gestion_libros",
    port=3306  
)"""

from nicegui import ui
from conexion import obtener_conexion
import mysql.connector

def agregar_libro_ui():
    try:
        # Obtener los valores de los inputs
        nombre = input_nombre.value.strip()
        simple_faz = int(input_simple_faz.value or 0)
        doble_faz = int(input_doble_faz.value or 0)
        color_simple = int(input_color_simple.value or 0)
        color_doble = int(input_color_doble.value or 0)
        anillado = input_anillado.value == "1"

        # Validar nombre
        if not nombre:
            ui.notify("El nombre del libro no puede estar vacío.", type="warning")
            return

        # Calcular tipo del libro
        tipo = (
            1 if simple_faz > 0 and doble_faz == 0 and color_simple == 0 and color_doble == 0 else
            2 if doble_faz > 0 and simple_faz == 0 and color_simple == 0 and color_doble == 0 else
            3 if color_simple > 0 and simple_faz == 0 and doble_faz == 0 and color_doble == 0 else
            4 if color_doble > 0 and simple_faz == 0 and doble_faz == 0 and color_simple == 0 else
            5
        )

        # Calcular precio de las hojas
        precio_hojas = (simple_faz * 60) + (doble_faz * 80) + (color_simple * 150) + (color_doble * 230)

        # Calcular precio del anillado
        cantidad_hojas = simple_faz + doble_faz + color_simple + color_doble
        if cantidad_hojas <= 20:
            precio_anillado = 800
        elif cantidad_hojas <= 50:
            precio_anillado = 970
        elif cantidad_hojas <= 100:
            precio_anillado = 1100
        elif cantidad_hojas <= 150:
            precio_anillado = 1400
        else:
            precio_anillado = 1800

        # Calcular precio total
        if anillado:
            nombre += " - Anillado"
            precio_libro = precio_hojas + precio_anillado
        else:
            nombre += " - Sin anillar"
            precio_libro = precio_hojas

        # Conectar a la base de datos
        conexion = obtener_conexion()
        if conexion is None:
            ui.notify("No se pudo conectar a la base de datos", type="negative")
            return

        # Insertar datos en la base de datos
        cursor = conexion.cursor()
        sql = "INSERT INTO libros (nombre, tipo, precio) VALUES (%s, %s, %s)"
        valores = (nombre, tipo, precio_libro)
        cursor.execute(sql, valores)
        conexion.commit()

        # Notificación de éxito
        ui.notify(f"Libro agregado con éxito. Precio: ${precio_libro}. ID: {cursor.lastrowid}", type="positive")
    
    except mysql.connector.Error as err:
        ui.notify(f"Error al interactuar con la base de datos: {err}", type="negative")
    except ValueError:
        ui.notify("Por favor, ingresa valores numéricos válidos.", type="negative")
    finally:
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()

# Crear la interfaz gráfica
with ui.card().style("width: 400px; margin: auto; padding: 20px;"):
    ui.label("Agregar un libro nuevo").style("font-size: 20px; font-weight: bold; text-align: center; margin-bottom: 20px;")

    # Inputs
    input_nombre = ui.input("Nombre del libro").style("margin-bottom: 10px;")
    input_simple_faz = ui.number("Hojas simple ByN").style("margin-bottom: 10px;")
    input_doble_faz = ui.number("Hojas doble ByN").style("margin-bottom: 10px;")
    input_color_simple = ui.number("Hojas simple COLOR").style("margin-bottom: 10px;")
    input_color_doble = ui.number("Hojas doble COLOR").style("margin-bottom: 10px;")
    input_anillado = ui.select({"1": "Sí", "2": "No"}, label="¿Anillado?").style("margin-bottom: 20px;")

    # Botón para agregar libro
    ui.button("Agregar libro", on_click=agregar_libro_ui).style("width: 100%;")

# Ejecutar la app
ui.run()





