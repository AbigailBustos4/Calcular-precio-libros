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


#Eliminar libro
def eliminar():
    from paso1 import lista
    print("\nLista de libros:")
    for libro in lista:
        print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}, ID: {libro['ID']}")

    try:
        eliminar_id = int(input("Para seleccionar el libro a eliminar, debe poner el ID correspondiente"))
        libro_a_eliminar = next((libro for libro in list if libro['ID'] == eliminar_id), None)
        if libro_a_eliminar:
            lista.remove(libro_a_eliminar)
            print(f"Libro eliminado {libro_a_eliminar['Nombre']} ")
        else:
            print("Libro no encontrado")
    except ValueError:
        print("Por favor, ingrese un ID valido")