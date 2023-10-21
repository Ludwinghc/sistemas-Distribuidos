from django.shortcuts import render
from .models import sites
import folium
from folium.plugins import FastMarkerCluster

# Create your views here.
def location(request):
  #Get my locations
  locations = sites.objects.all()
  #Define the initial map
  initialMap = folium.Map(location=[4.705775,-74.065426], zoom_start=11)
  #Creating the markets
  latitudes = [location.lat for location in locations]
  longitudes = [location.long for location in locations]
  popups = [location.name for location in locations]
  FastMarkerCluster(data=list(zip(latitudes, longitudes, popups))).add_to(initialMap)
  
  # context = {'map':initialMap._repr_html_()}
  context = {'map':initialMap._repr_html_(), 'locations':locations}

  return render(request, 'pages/locations.html', context)