import os
import mysql.connector


def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST', '192.168.20.12'),  # IP de alpine-2 (MySQL)
        port=int(os.getenv('DB_PORT', 3306)),         # Puerto estándar de MySQL
        user=os.getenv('DB_USER', 'root'),            # Usuario
        password=os.getenv('DB_PASSWORD', ''),        # Contraseña (vacía si no tiene)
        database=os.getenv('DB_NAME', 'veterinaria_db')
    )

    return connection
