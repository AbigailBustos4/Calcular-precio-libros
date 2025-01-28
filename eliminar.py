""" No funciono
    eliminar = int(input("Para seleccionar el libro a eliminar debe poner el ID correspondiente: "))
    posicion = eliminar -1 #El menos uno es porque el ID empieza en uno, pero las ubicaciones en 0
    encontrado = [libro for libro in lista if libro['ID'].lower() == posicion]
    lista.remove(posicion)
    if encontrado:
        print("Libro eliminado")
        for libro in encontrado:
            lista.remove(posicion)
            print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")
    else:
        print("libro no encontrado")
"""
from conexion import obtener_conexion

def eliminar():
    """Elimina un libro"""
    conexion = obtener_conexion()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    cursor = conexion.cursor() #crea un objeto de tipo cursor asociado a la conexión activa con la base de datos

    try:
        # Mostrar lista de libros
        print("\nLista de libros:")
        cursor.execute("SELECT id, nombre, tipo, precio FROM libros") #Envía la consulta SQL al servidor de la base de datos.
        libros = cursor.fetchall() #Recupera todos los resultados de la consulta ejecutada, retornándolos como una lista de tuplas.

        if not libros:
            print("No hay libros en la base de datos.")
            return

        for libro in libros:
            print(f"ID: {libro[0]}, Nombre: {libro[1]}, Tipo: {libro[2]}, Precio: ${libro[3]}")

        #solicitar ID 
        eliminar_id = int(input("\nIngrese el ID del libro que desea eliminar: "))
        cursor.execute("SELECT id, nombre FROM libros WHERE id = %s", (eliminar_id,))
        libro_a_eliminar = cursor.fetchone() # recuperar una sola fila de los resultados

        if libro_a_eliminar:
            confirmacion = input(f"¿Está seguro que desea eliminar el libro '{libro_a_eliminar[1]}'? (si: 1 / no: 2): ").lower()
            if confirmacion == "1":
                cursor.execute("DELETE FROM libros WHERE id = %s", (eliminar_id,))
                conexion.commit()
                print(f"Libro '{libro_a_eliminar[1]}' eliminado con éxito.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró un libro con ese ID.")

    except ValueError:
        print("Por favor, ingrese un ID válido.")
    except Exception as e:
        print(f"Error al eliminar el libro: {e}")
    finally:
        cursor.close() #CIERRO EL CANAL CREADO POR EL CURSOR
        conexion.close() #CIERRO LA CONEXION
