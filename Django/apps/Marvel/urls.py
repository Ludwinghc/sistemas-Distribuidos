from django.urls import path
from . import views

urlpatterns = [
  path("Characters/", views.Characters, name="Characters"),
]