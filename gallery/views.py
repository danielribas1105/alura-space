from django.shortcuts import get_object_or_404, render
from gallery.models import Fotografia

# Create your views here.



def index(request):
   fotografias = Fotografia.objects.all()
   return render(request, "gallery/index.html", {"cards": fotografias})

def image(request, foto_id):
   fotografia = get_object_or_404(Fotografia, pk=foto_id)
   return render(request, "gallery/image.html", {"fotografia": fotografia})
