from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_presentes, name="lista_presentes"),
    path("reservar/<int:presente_id>/", views.reservar_presente, name="reservar_presente"),
    path("agradecimento/", views.pagina_agradecimento, name="pagina_agradecimento"),

]
