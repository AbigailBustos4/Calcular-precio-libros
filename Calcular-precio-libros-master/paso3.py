#la idea aca es editar algun libro. Lo que tengo que hacer es encontrar la posicion de mi elemento en la lista, traerlo y decirle que esa posicion es igual a.... 
from paso1 import lista
print("\nLista de libros:")
for libro in lista:
    print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}, ID: {libro['ID']}")

editar = int(input("Para seleccionar el libro a editar debe poner el ID correspondiente: "))
posicion = editar -1
encontrado = [libro for libro in lista if libro['ID'].lower() == posicion]

if encontrado:
    print("\n*** Libros encontrados ***")
    for libro in encontrado:
        print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")
        print("¿Qué desea editar?")
        print("1. Nombre 2. Tipo 3. Precio")
        a_editar = int(input("Elejir una opcion. El id no es editable"))
        