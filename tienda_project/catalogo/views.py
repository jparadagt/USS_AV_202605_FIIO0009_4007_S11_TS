from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()

    contexto = {
        'productos': productos
    }

    return render(
        request,
        'catalogo/lista_productos.html',
        contexto
    )