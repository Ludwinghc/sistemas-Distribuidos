import mysql.connector

def conexionDatabase():
  conex = mysql.connector.connect(
      host="ludwingengine.mysql.pythonanywhere-services.com",
      user = "ludwingengine",
      password = "150102Br",
      database ="ludwingengine$apiYoutube",
      port ="3306")
  return conex