#Eliminar libro
def eliminar():
    from paso1 import lista
    print("\nLista de libros:")
    for libro in lista:
        print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}, ID: {libro['ID']}")

    eliminar = int(input("Para seleccionar el libro a editar debe poner el ID correspondiente: "))
    posicion = eliminar -1 #El menos uno es porqu el ID empieza en uno, pero las ubicaciones en 0
    encontrado = [libro for libro in lista if libro['ID'].lower() == posicion]
    lista.remove(posicion)
    if encontrado:
        print("Libro eliminado")
        for libro in encontrado:
            lista.remove(posicion)
            print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")
    else:
        print("libro no encontrado")