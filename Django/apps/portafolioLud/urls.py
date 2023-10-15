from django.urls import path
from . import views
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path("proyectos/", views.proyectos, name="Proyectos"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]