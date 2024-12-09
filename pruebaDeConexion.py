import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root"
    )
    print("¡Conexión exitosa!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
