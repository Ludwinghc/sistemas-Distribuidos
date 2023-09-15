import mysql.connector

def conexionDatabase():
    try:
        conex = mysql.connector.connect(
            host="ludwingengine.mysql.pythonanywhere-services.com",
            user="ludwingengine",
            password="020916lAU",
            database="ludwingengine$apiYoutube",
            port="3306"
        )
        return conex
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        return None
