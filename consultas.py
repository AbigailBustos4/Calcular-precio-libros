
"""Paso 2:
Realizar consultas
   - Conexión con la base de datos
   - Consulta de libros desde la base de datos
   - Mostrar resultados
   - Cerrar la conexión al final
#En el menu una opcion detalle que te traiga, segun el nombre de un libro, todos sus detalles separados (o sea cantidad de cada tipo de hoja, precio del anillado y todos los tipos disponibles para ese nombre)
#Tambien se podria hacer una especie de ticket con todos estos datos y el precio 
"""
from conexion import obtener_conexion

def consultas():
    conexion = obtener_conexion()
    if conexion is None:  
        print("No se pudo conectar a la base de datos")
        return

    cursor = conexion.cursor()

    try:
        print("\nLista de libros disponibles:")
        cursor.execute("SELECT nombre, tipo, precio, id FROM libros") 
        libros = cursor.fetchall()

        if libros:
            for libro in libros:
                print(f"Nombre: {libro[0]}, Tipo: {libro[1]}, Precio: ${libro[2]}, ID: {libro[3]}")
        else: 
            print("No hay libros disponibles en la base de datos.")
    except mysql.connector.Error as e:
        print(f"Error al realizar la consulta: {e}")
    finally:
        cursor.close()
        conexion.close()

def consulta_especifica(nombre_libro):  
    conexion = obtener_conexion()
    if conexion is None:  
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conexion.cursor()
    try:
        #para buscar el libro por nombre 
        cursor.execute("SELECT nombre, tipo, precio FROM libros WHERE LOWER(nombre) = LOWER(%s)", (nombre_libro,))
        libros_encontrados = cursor.fetchall()

        if libros_encontrados:
            print("\n*** Libros encontrados ***")
            for libro in libros_encontrados:
                print(f"Nombre: {libro[0]}, Tipo: {libro[1]}, Precio: ${libro[2]}")
                input("\nPresione Enter para continuar...")
        else:
            print("No se encontraron libros con ese nombre.")
    except mysql.connector.Error as e:
        print(f"Error al realizar la consulta: {e}")
    finally:
        cursor.close()
        conexion.close()
