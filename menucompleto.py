while True:
    print("\n *** Venta de libros ***")
    print("1. Agregar un libro nuevo")
    print("2. Mostrar la lista completa de libros")
    print("3. Editar algún libro")
    print("4. Eliminar libro")
    print("5. Realizar una consulta específica")
    print("6. Salir")
    opcion = int(input("Elige una opcion del 1 al 6: "))
    """    try:  
        opcion = int(input("Elige una opcion del 1 al 5: "))
    except ValueError:
        print("ERROR: Escribe un número")
        break"""

    if opcion == 1: #paso 1
        from paso1 import agregar_libro
        agregar_libro()
        while True:
            print("¿Qué deseas hacer ahora?")
            print("1. Agregar otro libro")
            print("2. Volver al menú")
            opcion2 = int(input("elige una opción "))
            if opcion2 == 2:
                break
            elif opcion2 == 1:
                agregar_libro()
            else:
                print("Opcion no valida. Volviendo al menú")
                break
    elif opcion == 2: #paso 2
        from paso2 import consultas
        consultas()
    elif opcion == 3: #paso 3
        #edito algun dato del libro
        from paso3 import editar
        editar()
    elif opcion == 4: #paso 4
        from paso4 import eliminar
        eliminar()
    elif opcion == 5: #paso 2
        #Realizo un consulta especifica
        from paso2 import consulta_especifica
        consulta_especifica()
    elif opcion == 6:
        #guardar lista y diccionario
        print("¡Segui trabajando así, lo haces genial! Nos vemos ☺")
        break
    else:
        print("Opción no válida. Por favor elige entre 1 y 5.")

        