from django.shortcuts import get_object_or_404, redirect, render
from gallery.models import Fotografia
from django.contrib import messages

# Create your views here.

def index(request):
   if not request.user.is_authenticated:
      messages.error(request, "Usuário não logado!")
      return redirect('login')
   fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
   return render(request, "gallery/index.html", {"cards": fotografias})

def image(request, foto_id):
   fotografia = get_object_or_404(Fotografia, pk=foto_id)
   return render(request, "gallery/image.html", {"fotografia": fotografia})

def buscar(request):
   if not request.user.is_authenticated:
      messages.error(request, "Usuário não logado!")
      return redirect('login')
   fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

   if "buscar" in request.GET:
      nome_buscar = request.GET['buscar']
      if nome_buscar:
         fotografias = fotografias.filter(nome__icontains=nome_buscar)

   return render(request, "gallery/buscar.html", {"cards": fotografias})