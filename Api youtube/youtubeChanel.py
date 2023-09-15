# Este Documento contiene la logica de los end-points de la api de canales de youtube
# Desarrollado por ludwing.engine y por Bryan.engine

# Inicio de importacion de librerias
import os
from functools import wraps
from flask import Flask, jsonify, request
import requests
import re
from bs4 import BeautifulSoup
from src import dataBaseApi as dataBase
# Fin de importacion de librerias

# Inicio de la funcion para realizar el web Scrapping a youtube
def obtener_descripcion_y_url_imagen_canal_youtube(nombre_canal):
    try:
        # Componemos la URL completa del canal
        url_canal = f"https://www.youtube.com/{nombre_canal}"

        # Realizamos una solicitud HTTP para obtener el contenido de la página del canal
        response = requests.get(url_canal)
        response.raise_for_status()

        # Extraemos la URL de la imagen de perfil del canal directamente del código fuente
        match = re.search(r'"avatar":{"thumbnails":\[{"url":"(https:\/\/[^"]+)","width":', response.text)
        
        if match:
            url_imagen_perfil = match.group(1)
        else:
            url_imagen_perfil = "No se encontró una imagen de perfil para este canal."

        # Analizamos el contenido HTML de la página
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos la etiqueta <meta> con el nombre "description"
        meta_description = soup.find('meta', {'name': 'description'})

        if meta_description:
            # Extraemos el contenido de la descripción del canal
            descripcion = meta_description['content'].strip()
        else:
            descripcion = "No se encontró una descripción para este canal."

        return descripcion, url_imagen_perfil
    except Exception as e:
        return str(e), "No se pudo obtener la descripción ni la URL de la imagen."

# Fin de la funcion para el web Scrapping en youtube

# Declaracion del nombre de como se van a manejar los endpoints de la api
api = Flask(__name__)

# Inicio de la 
# Definicion del primer endpoint para la api el cual solo tiene la funcion de mostrar que la api esta activa
@api.route('/')
def index():
    return jsonify({
      "Esta es la api de canales de youtube": "Bienvenido a nuestra api" 
    })
# Fin de la 
# Definicion del primer endpoint para la api el cual solo tiene la funcion de mostrar que la api esta activa

# Inicio de la declaracion de
# Definicion del segundo endpoint para la api donde se genera el codigo para guardar la informacion en la base de datos 
@api.route('/consult', methods=['POST'])
def consult():
    try:
      # definimos una variable en la cual se albergara el nombre del canal que los usuarios busquen
      nameChannel = request.form['channel_name'] 
      # Enviamos a la funcion que creamos para el scrapping
      # y guardamos en una variable la descripción que retorna la funcion
      descriptionChannel, imagenChannel = obtener_descripcion_y_url_imagen_canal_youtube(nombre_canal=nameChannel)
      print(descriptionChannel)
      print(imagenChannel)
      # Realizamos el llamado para realizar la conexion a la base de datos
      newConex = dataBase.conexionDatabase()
      print(newConex)
      cursor = newConex.cursor()
      sentencia = "INSERT INTO History (nameChannel, description, imagenChannel) VALUES ($s, %s, %s);"
      cursor.execute(sentencia,(nameChannel, descriptionChannel, imagenChannel))

      return jsonify({
          "Canal" : nameChannel,
          "description" : descriptionChannel,
          "imagenChannel" : imagenChannel
      })
    except Exception as e:
        return jsonify({
            "Message": "Error. "+ str(e) 
        })    
# Inicio de la declaracion de
# Definicion del segundo endpoint para la api donde se genera el codigo para guardar la informacion en la base de datos 


if __name__ == '__main__':
    api.run(debug=True, port=os.getenv("PORT", default=5000))