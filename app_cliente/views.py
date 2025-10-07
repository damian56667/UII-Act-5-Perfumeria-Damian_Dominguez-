from django.shortcuts import render
from .models import Cliente

# Create your views here.
def index(request):
    clientes = Cliente.objects.all()  # Usa "objects" en lugar de "object"
    return render(request, "index.html", {"clientes": clientes})  # Pasa "clientes" al contexto
