import mysql.connector

def obtener_conexion():
    """Crea y retorna una conexión a la base de datos MySQL."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",       # Cambia si el host es diferente
            user="root",            # Reemplaza con tu usuario de MySQL
            password="root",        # Reemplaza con tu contraseña de MySQL
            database="gestion_libros"  # Nombre de la base de datos
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

