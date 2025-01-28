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

from conexion import obtener_conexion 

""" Lista para almacenar los libros temporalmente que ya no esta en uso
lista = []"""

def agregar_libro():
    try:
        conexion = obtener_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos.")
            return

        cursor = conexion.cursor()

        # información del libro
        nombre = input("¿Cómo se llama el libro? ") 
        simple_faz = int(input("¿Cuántas hojas simple ByN tiene? "))
        doble_faz = int(input("¿Cuántas hojas doble ByN tiene? "))
        color_simple = int(input("¿Cuántas hojas simple COLOR tiene? "))
        color_doble = int(input("¿Cuántas hojas doble COLOR tiene? "))

        # tipo del libro
        tipo = (
            1 if simple_faz > 0 and doble_faz == 0 and color_simple == 0 and color_doble == 0 else
            2 if doble_faz > 0 and simple_faz == 0 and color_simple == 0 and color_doble == 0 else
            3 if color_simple > 0 and simple_faz == 0 and doble_faz == 0 and color_doble == 0 else
            4 if color_doble > 0 and simple_faz == 0 and doble_faz == 0 and color_simple == 0 else
            5
        )

        # Calcular el precio de las hojas
        precio_hojas = (simple_faz * 60) + (doble_faz * 80) + (color_simple * 150) + (color_doble * 230)

        # Determinar el precio del anillado según la cantidad de hojas
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

        # Preguntar si el libro será anillado
        anillado = input("¿Desea que el libro sea anillado? (SI: 1 / NO: 2): ").strip().lower()
        if anillado == "1":
            nombre += " - Anillado"
            precio_libro = precio_hojas + precio_anillado
        else:
            nombre += " - Sin anillar"
            precio_libro = precio_hojas

        # GUARDO el libro en la base de datos
        sql = "INSERT INTO libros (nombre, tipo, precio) VALUES (%s, %s, %s)"
        valores = (nombre, tipo, precio_libro)
        cursor.execute(sql, valores)
        conexion.commit()

        print(f"\nLibro agregado con éxito. El precio es ${precio_libro}. ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"Error al interactuar con la base de datos: {err}")
    finally:
        # Cerrar la conexión a la base de datos
        if 'conexion' in locals() and conexion.is_connected():
            conexion.close()

"""FUERA DE USO
        libro = {
            "ID": cursor.lastrowid,
            "Nombre": nombre,
            "Tipo": tipo,
            "Precio": precio_libro
        }
        lista.append(libro)"""

    




