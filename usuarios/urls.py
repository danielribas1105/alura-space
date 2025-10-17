from django.urls import path
from usuarios.views import login, cadastro
from gallery.views import buscar, index, image

urlpatterns = [
   path("login", login, name="login"),
   path("cadastro", cadastro, name="cadastro"),
]