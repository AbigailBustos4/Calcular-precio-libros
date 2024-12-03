#la idea aca es editar algun libro. Lo que tengo que hacer es encontrar la posicion de mi elemento en la lista, traerlo y decirle que esa posicion es igual a.... 
def editar():
    from paso1 import lista
    print("\nLista de libros:")
    for libro in lista:
        print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}, ID: {libro['ID']}")

    editar = int(input("\nPara seleccionar el libro a editar debe poner el ID correspondiente: "))
    encontrado = next((libro for libro in lista if libro['ID'] == editar), None) #Se utiliza next() con un generador para buscar un libro cuyo ID coincida con el valor ingresado. None si no hay coincidencia

    if encontrado:
        print("\n*** Libros encontrados ***")
        print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")
        
        print("¿Qué desea editar?")
        print("1. Nombre\n2. Tipo\n3. Precio")
        a_editar = int(input("Elejir una opcion. (El id no es editable): "))
        if a_editar == 1:
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            encontrado['Nombre'] = nuevo_nombre
        elif a_editar == 2:
            #PARA ADITAR EL TIPO HAY QUE CONSULTAR CUANTAS HOJAS TIENE
            simple_faz = int(input("¿Cuantas hojas simple ByN tiene? "))
            doble_faz = int(input("¿Cuantas hojas doble ByN tiene? "))
            color_simple = int(input("¿Cuantas hojas simple COLOR tiene? "))
            color_doble = int(input("¿Cuantas hojas doble COLOR tiene? "))

            if simple_faz >= 1 and doble_faz == 0 and color_doble == 0 and color_simple == 0:
                tipo = 1
            elif simple_faz >= 0 and doble_faz == 1 and color_doble == 0 and color_simple == 0:
                tipo = 2
            elif simple_faz >= 0 and doble_faz == 0 and color_doble == 0 and color_simple == 1:
                tipo = 3
            elif simple_faz >= 0 and doble_faz == 0 and color_doble == 1 and color_simple == 0:
                tipo = 4
            else:
                tipo = 5
            encontrado['Tipo'] = tipo
        elif a_editar == 3:
            #PARA EDITAR EL PRECIO HAY QUE CONSULTAR CUANTAS HOJAS TIENE
            simple_faz = int(input("¿Cuantas hojas simple ByN tiene? "))
            doble_faz = int(input("¿Cuantas hojas doble ByN tiene? "))
            color_simple = int(input("¿Cuantas hojas simple COLOR tiene? "))
            color_doble = int(input("¿Cuantas hojas doble COLOR tiene? "))
            precio_hojas = simple_faz * 60 + doble_faz * 80 + color_doble * 230 + color_simple * 150
            cantidad_hojas = simple_faz + doble_faz + color_doble + color_simple
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

            precio_libro = precio_anillado + precio_hojas
            encontrado['Precio'] = precio_libro
        else:
            print("Opción invalida")
        
        print("Libro actualizado")
        print(f"Nombre: {encontrado['Nombre']}, Tipo: {encontrado['Tipo']}, Precio: ${encontrado['Precio']}")
    else:
        print("No se encontró un libro con ese ID")