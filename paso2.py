
"""Paso 2:
Realizar consultas
Un buscador dentro del diccionario que te traiga todos los datos asociados a ese nombre
¿Que pasa si n nombre tiene asignado mas de un precio y tipo? o sea mismo libro, precio a color o precio blanco y negro
Si, vamos a ver como mierda lo hago :O 
#En el menu una opcion detalle que te traiga, segun el nombre de un libro, todos sus detalles separados (o sea cantidad de cada tipo de hoja, precio del anillado y todos los tipos disponibles para ese nombre)
#Tambien se podria hacer una especie de ticket con todos estos datos y el precio 

esto es de un intento de opccion :     nombre_libro = input("ingrese el nombre del libro a consultar: ")
            if nombre_libro in lista:
                print("\n--- Información del libro ---")
                print(f"Nombre: {libro['nombre']}")  
"""
def consultas():
    from paso1 import lista
    while True:
        print("\nLista de libros disponibles:")
        for libro in lista:
            print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}, ID: {libro['ID']}")

        print("Presiona Enter para volver al menú principal")
        opcion3 = input(" ")

        if opcion3 == "":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def consulta_especifica():
    from paso1 import lista
    while True:
        print("\n1. Buscar un libro")
        print("2. Volver al menú")
        opcion4 = int(input("Elija una opción: "))

        if opcion4 == 1:
            nombre_libro = input("¿Qué libro estás buscando? ")
            libros_encontrados = [libro for libro in lista if libro['Nombre'].lower() == nombre_libro.lower()] #Por cada libroen mi dic libro que esta en lista, si el libro(minusculaa) esta, se vuelve libro encontrado
            
            if libros_encontrados:
                print("\n*** Libros encontrados ***")
                for libro in libros_encontrados:
                    print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")
            else:
                print("No se encontraron libros con ese nombre.")
        elif opcion4 == 2:
            print("Volviendo al menú...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


