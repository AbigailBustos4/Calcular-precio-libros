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
from menucompleto import lista
def consultas():
    while True:
        print("1. Realizar consulta sobre algun libro")
        print("2. Volver al manú")
        opcion3 = int(input("Elija una opcion: "))
        if opcion3 == 1: #Aca debo traer toda la info de un libro con su nombre
            print("\nLista de libros:")
            for libro in lista:
                print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")
        elif opcion3 == 2: 
            print("Volviendo al menu")
            break
        else:
            print("Volviendo al menu")
            break

consultas()