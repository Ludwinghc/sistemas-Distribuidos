from django.shortcuts import render
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import sys
from pprint import pprint
# Create your views here.
# Vista de personajes spotify
def Characters(request):
  client_id = 'a11b5936163d40319d65243dc2faeaae'
  client_secret = 'c781300fd01a459db7cd605e2fd36608'
  list_author = ['Avicii', 'Linkin Park', 'Fonseca']
  playlist = []
  # autentica mi cuenta de spotify
  sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
  # Busca el autor que desea uno 
  for i in list_author:
    result = sp.search(i)
    # Clase canciones
    class Cancion:
      def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
    
    for i in range(0, len(result["tracks"]["items"])):
      name_song = result["tracks"]["items"][i]["name"]
      link_song = result["tracks"]["items"][i]["external_urls"]["spotify"]
      nueva_cancion = Cancion(name_song,link_song)
      playlist.append(nueva_cancion)
    # print(result)
  return render(request, 'pages/Characters.html', {'playlist': playlist})
