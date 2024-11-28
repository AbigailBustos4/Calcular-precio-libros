lista = []
while True:
    print("\n *** Venta de libros ***")
    print("1. Agregar un libro nuevo")
    print("2. Consultar precio de un libro")
    print("3. Editar algun libro")
    print("4. Eliminar libro")
    print("5. Salir")

    opcion = int(input("Elige una opcion del 1 al 5: "))
    if opcion == 1: #paso 1
        #Pedir el nombre del libro (Nombre-escuela-grado)
        nombre = input("¿Cómo se llama el libro? ")
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
#precio de las hojas
        precio_hojas = simple_faz * 60 + doble_faz * 80 + color_doble * 230 + color_simple * 150
#precio del anillado
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

#precio total del libro
        precio_libro = precio_anillado + precio_hojas

#Creo mi diccionario con el libro y sus datos
        libro = {
            "Nombre": nombre,
            "Tipo": tipo,
            "Precio": precio_libro
        }

        lista.append(libro)

        print("Libro agregado con exito")
    elif opcion == 2: 
        #Tengo que poder hacer consultas en toda la lista de libros
        pass
    elif opcion == 3:
        #edito algun dato del libro
        pass
    elif opcion == 4:
        #elimino algun libro que ya no se use
        pass
    elif opcion == 5:
        #guardar lista y diccionario
        print("¡Segui trabajando así, lo haces genial! Nos vemos ☺")
        break
    else:
        print("Opción no válida. Por favor elige entre 1 y 5.")

        
