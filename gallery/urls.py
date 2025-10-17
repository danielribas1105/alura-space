from django.urls import path
from gallery.views import buscar, index, image

urlpatterns = [
   path('', index, name='index'),
   path('image/<int:foto_id>', image, name='image'),
   path('buscar', buscar, name='buscar')
]