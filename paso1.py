"""Paso 1: 
Pedir el nombre del libro (Nombre-escuela-grado)
Preguntar cuantas hojas son simple faz:
Preguntar cuantas hojas son doble faz:
Preguntar cuantas hojas son simple faz color:
Preguntar cuantas hojas son doble faz color:      

Agregar una descripcion que te muestre cuantas hojas tenes de cada tipo y te muestre el numero que se le asigno:
Asigna 1 hojas son simple faz:
Asigna 2 hojas son doble faz:
Asigna 3 hojas son simple faz color:
Asigna 4 cuantas hojas son doble faz color:
Asigna 5 si es mixto
"""
#la lista que contenga el diccionario
lista = []
def agregar_libro():
    nombre = input("¿Cómo se llama el libro? ") #Pedir el nombre del libro (Nombre-escuela-grado)
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

    print(f"Libro agregado con exito. El precio es ${precio_libro}")
    #mostrar libros
    print("\nLista de libros:")
    for libro in lista:
        print(f"Nombre: {libro['Nombre']}, Tipo: {libro['Tipo']}, Precio: ${libro['Precio']}")





