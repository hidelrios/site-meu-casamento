from django.urls import path
from . import views

urlpatterns = [
    path("", views.confirmar_presenca, name="confirmar_presenca"),
    path("confirmar/", views.confirmar_presenca, name="confirmar_presenca"),
]
