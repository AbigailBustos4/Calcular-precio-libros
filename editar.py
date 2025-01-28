from conexion import obtener_conexion

def editar():
    conexion = obtener_conexion()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        return
    
    cursor = conexion.cursor()

    try:
        #lista de libros 
        print("\nLista de libros:")
        cursor.execute("SELECT id, nombre, tipo, precio FROM libros")
        libros = cursor.fetchall()

        if not libros:
            print("No hay libros en la base de datos.")
            return
        
        for libro in libros:
            print(f"ID: {libro[0]}, Nombre: {libro[1]}, Tipo: {libro[2]}, Precio: ${libro[3]}")
        
        #libro a editar
        editar_id = int(input("\nPara seleccionar el libro a editar debe ingresar el ID correspondiente: "))
        cursor.execute("SELECT id, nombre, tipo, precio FROM libros WHERE id = %s", (editar_id,))
        libro = cursor.fetchone()

        if not libro:
            print("No se encontró un libro con ese ID.")
            return

        print(f"\nLibro seleccionado: ID: {libro[0]}, Nombre: {libro[1]}, Tipo: {libro[2]}, Precio: ${libro[3]}")

        #qué editar
        print("\n¿Qué desea editar?")
        print("1. Nombre\n2. Tipo\n3. Precio")
        a_editar = int(input("Elegir una opción (El ID no es editable): "))

        if a_editar == 1:
            # Editar nombre
            nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
            cursor.execute("UPDATE libros SET nombre = %s WHERE id = %s", (nuevo_nombre, editar_id))
            conexion.commit()
            print("Nombre actualizado correctamente.")

        elif a_editar == 2:
            # Editar tipo
            tipo = calcular_tipo()
            cursor.execute("UPDATE libros SET tipo = %s WHERE id = %s", (tipo, editar_id))
            conexion.commit()
            print("Tipo actualizado correctamente.")

        elif a_editar == 3:
            # Editar precio
            cursor.execute("SELECT nombre FROM libros WHERE id = %s", (editar_id,))
            resultado = cursor.fetchone()

            if resultado:
                nombre_actual = resultado[0]

                # Calcular el nuevo precio usando el nombre actual
                nombre_actualizado, precio_libro = calcular_precio(nombre_actual)

                # Actualizar el precio y el nombre en la base de datos
                cursor.execute(
                    "UPDATE libros SET precio = %s, nombre = %s WHERE id = %s",
                    (precio_libro, nombre_actualizado, editar_id)
                )
                conexion.commit()
                print(f"Precio y nombre actualizados correctamente. Nuevo precio: ${precio_libro}, Nuevo nombre: {nombre_actualizado}")

        else:
            print("Opción no válida.")

    except Exception as e:
        print(f"Error al editar el libro: {e}")
    finally:
        cursor.close()
        conexion.close()

def calcular_tipo():
    """Calcula el tipo de libro según las hojas."""
    simple_faz = int(input("¿Cuántas hojas simple ByN tiene? "))
    doble_faz = int(input("¿Cuántas hojas doble ByN tiene? "))
    color_simple = int(input("¿Cuántas hojas simple COLOR tiene? "))
    color_doble = int(input("¿Cuántas hojas doble COLOR tiene? "))

    if simple_faz >= 1 and doble_faz == 0 and color_doble == 0 and color_simple == 0:
        return 1
    elif simple_faz == 0 and doble_faz >= 1 and color_doble == 0 and color_simple == 0:
        return 2
    elif simple_faz == 0 and doble_faz == 0 and color_simple >= 1 and color_doble == 0:
        return 3
    elif simple_faz == 0 and doble_faz == 0 and color_simple == 0 and color_doble >= 1:
        return 4
    else:
        return 5

def calcular_precio(nombre):
    """
    Calcula el precio del libro según las hojas y el anillado.
    Actualiza el nombre con "Anillado" o "Sin anillar".
    """
    # Solicitar la cantidad de hojas por tipo
    simple_faz = int(input("¿Cuántas hojas simple ByN tiene? "))
    doble_faz = int(input("¿Cuántas hojas doble ByN tiene? "))
    color_simple = int(input("¿Cuántas hojas simple COLOR tiene? "))
    color_doble = int(input("¿Cuántas hojas doble COLOR tiene? "))

    # Calcular el precio de las hojas
    precio_hojas = simple_faz * 60 + doble_faz * 80 + color_doble * 230 + color_simple * 150
    cantidad_hojas = simple_faz + doble_faz + color_simple + color_doble


    # Preguntar si el usuario desea anillado
    anillado = input("¿Desea que el libro sea anillado? (SI/NO): ").strip().lower()

    # Ajustar el precio y el nombre según la elección de anillado
    if anillado == "si":
        nombre += " - Anillado"
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
        precio_libro = precio_hojas + precio_anillado
    else:
        nombre += " - Sin anillar"
        precio_libro = precio_hojas

    print(f"\nDetalles del libro:")
    print(f"Precio total: ${precio_libro}")

    # Retornar el nombre actualizado y el precio calculado
    return nombre, precio_libro

