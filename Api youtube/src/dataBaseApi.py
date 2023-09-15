import mysql.connector
host = 'ludwingengine.mysql.pythonanywhere-services.com'
user = 'ludwingengine'
passkey = '020916lAU'
database = 'ludwingengine$default'
puerto = '3306'
def conexionDatabase():
    try:
        conex = mysql.connector.connect(
            host=host,
            user= user,   
            password=passkey,
            database=database,
            port= puerto
        )
        return conex
    except mysql.connector.Error as err:
        print(f"Error de conexión a la base de datos: {err}")
        return None
