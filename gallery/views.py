from django.shortcuts import get_object_or_404, render
from gallery.models import Fotografia

# Create your views here.



def index(request):
   fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
   return render(request, "gallery/index.html", {"cards": fotografias})

def image(request, foto_id):
   fotografia = get_object_or_404(Fotografia, pk=foto_id)
   return render(request, "gallery/image.html", {"fotografia": fotografia})

def buscar(request):
   fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

   if "buscar" in request.GET:
      nome_buscar = request.GET['buscar']
      if nome_buscar:
         fotografias = fotografias.filter(nome__icontains=nome_buscar)

   return render(request, "gallery/buscar.html", {"cards": fotografias})