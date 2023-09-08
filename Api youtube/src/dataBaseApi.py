import mysql.connector

def conexionDatabase():
  conex = mysql.connector.connect(
      host="sql3.freesqldatabase.com",
      user = "sql3645200",
      password = "7qHv6dRJDS",
      database ="sql3645200",
      port ="3306")