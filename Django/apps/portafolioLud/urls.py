from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [ 
    path("proyectos/", views.proyectos, name="Proyectos"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)