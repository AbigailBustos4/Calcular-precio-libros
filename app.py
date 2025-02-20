from nicegui import ui
from agregarlibro import agregar_libro_ui
from consultas import consulta_especifica, consultas
from editar import editar
from eliminar import eliminar

# Función para mostrar la pantalla de agregar libro
def mostrar_agregar_libro():
    menu_container.visible = False  # Ocultar el menú principal
    agregar_libro_container.visible = True  # Mostrar la interfaz de agregar libros

# Función para volver al menú principal desde cualquier pantalla
def volver_al_menu():
    agregar_libro_container.visible = False  # Ocultar la interfaz de agregar libros
    menu_container.visible = True  # Mostrar el menú principal

# Función para mostrar el menú principal
def mostrar_menu():
    menu_container.visible = True

# Contenedores para cada sección
with ui.column().style("width: 100%; align-items: center;") as menu_container:
    with ui.card().style("width: 300px; margin: auto;"):
        ui.label("*** Venta de libros ***").style("font-size: 18px; font-weight: bold;")
        ui.button("1. Agregar un libro nuevo", on_click=mostrar_agregar_libro)
        ui.button("2. Mostrar la lista completa de libros", on_click=consultas)
        ui.button("3. Editar algún libro", on_click=editar)
        ui.button("4. Eliminar libro", on_click=eliminar)
        ui.button("5. Realizar una consulta específica", on_click=lambda: consulta_especifica(input_consulta.value))
        ui.button("6. Salir", on_click=lambda: ui.notify("¡Gracias por usar la aplicación! Nos vemos ☺"))

        # Campo de entrada para la consulta específica
        input_consulta = ui.input("Ingresa el nombre del libro para consulta específica")

with ui.column().style("width: 100%; align-items: center; display: none;") as agregar_libro_container:
    ui.label("Agregar un libro nuevo").style("font-size: 18px; font-weight: bold;")
    agregar_libro_ui()
    ui.button("Volver al menú principal", on_click=volver_al_menu)

# Iniciar la interfaz gráfica
ui.run()
