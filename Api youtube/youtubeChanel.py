# Inicio de importacion de librerias
import os
from functools import wraps
from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from src import dataBaseApi as dataBase

def scrapingYoutubeDescription(nombre_canal):
    try:
        # Componemos la URL completa del canal
        url_canal = f"https://www.youtube.com/{nombre_canal}"

        # Realizamos una solicitud HTTP para obtener el contenido de la página del canal
        response = requests.get(url_canal)
        response.raise_for_status()

        # Analizamos el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos la etiqueta <meta> con el nombre "description"
        meta_description = soup.find('meta', {'name': 'description'})

        if meta_description:
            # Extraemos el contenido de la descripción del canal
            descripcion = meta_description['content'].strip()
            return descripcion
        else:
            return "No se encontró una descripción para este canal."

    except Exception as e:
        return str(e)


api = Flask(__name__)


@api.route('/')
def index():
    return jsonify({
      "Esta es la api de canales de youtube": "Bienvenido a nuestra api"
    })
print(dataBase.conexionDatabase)

@api.route('/consult', methods=['POST'])
def consult():
    try:
      nameChannel = request.form['channel_name'] 
      print(nameChannel)
      descriptionChannel = scrapingYoutubeDescription(nombre_canal=nameChannel)
      print(descriptionChannel)
      newConex = dataBase.conexionDatabase()
      print(newConex)
      cursor = newConex.cursor()
      sentencia = "INSERT INTO History (nameChannel, description) VALUES ('"+nameChannel+"', '"+descriptionChannel+"');"
      cursor.execute(sentencia)
    except Exception as e:
        return jsonify({
            "Message": "Error. "+ str(e) 
        })
    



if __name__ == '__main__':
    api.run(debug=True, port=os.getenv("PORT", default=5000))