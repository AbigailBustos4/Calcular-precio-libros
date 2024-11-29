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

        
