from nicegui import ui

from agregarlibro import agregar_libro
from consultas import consulta_especifica, consultas
from editar import editar
from eliminar import eliminar

def agregarlibro():
    agregar_libro()
    ui.notify("Libro agregado")

def mostrar_lista_libros():
    consultas()
    ui.notify("Lista de libros")

def editar_libro():
    editar()
    ui.notify("Libro editado")

def eliminar_libro():
    eliminar()
    ui.notify("Libro eliminado")

def consultaespecifica(nombre_libro):
    consulta_especifica()
    ui.notify(f"Consulta específica para: {nombre_libro}")

# Función para mostrar el menú principal
def mostrar_menu():
    with ui.card().style("width: 300px; margin: auto;"):
        ui.label("*** Venta de libros ***").style("font-size: 18px; font-weight: bold;")
        ui.button("1. Agregar un libro nuevo", on_click=agregar_libro)
        ui.button("2. Mostrar la lista completa de libros", on_click=mostrar_lista_libros)
        ui.button("3. Editar algún libro", on_click=editar_libro)
        ui.button("4. Eliminar libro", on_click=eliminar_libro)
        ui.button("5. Realizar una consulta específica", on_click=lambda: consulta_especifica(input_consulta.value))
        ui.button("6. Salir", on_click=salir)

        # Campo de entrada para la consulta específica
        global input_consulta
        input_consulta = ui.input("Ingresa el nombre del libro para consulta específica")

def salir():
    ui.notify("¡Gracias por usar la aplicación! Nos vemos ☺")
    # Ocultar el menú
    menu_container.visible = False

# Contenedor para el menú
with ui.column().style("width: 100%; align-items: center;") as menu_container:
    mostrar_menu()

# Iniciar la interfaz gráfica
ui.run()