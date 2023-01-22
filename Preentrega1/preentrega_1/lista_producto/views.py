from django.shortcuts import render
from django.http import HttpResponse
from lista_producto.models import Producto
from lista_producto.form import Produtoformulario
# Create your views here.
def lista_de_productos(request):
    if "search" in request.GET:
        var_filto = request.GET["search"]
        var_productos = Producto.objects.filter(name__contains=var_filto)
    else:
        var_productos = Producto.objects.all()

    context = {
        "productos":var_productos,
    }
    return render(request, "tem_productos/lista_productos.html", context=context)

def cargar_los_productos (request):
    if request.method == "GET":
        context = {
            "formulario" : Produtoformulario()
        }
        return render(request, "tem_productos/crear_productos.html", context=context)

    elif request.method == "POST":
        var_form = Produtoformulario(request.POST)
        if var_form.is_valid():
            Producto.objects.create(
                name=var_form.cleaned_data["name"],
                precio=var_form.cleaned_data["precio"],
                stock=var_form.cleaned_data["stock"],
            )
            context = {
                "mensaje_de_ok": "El producto se creo correctamente"
            }
            return render(request, "tem_productos/crear_productos.html", context=context)
        else:
            context = {
                "error_del_formulario": var_form.errors,
                "formulario" : Produtoformulario(),
            }
            return render(request, "tem_productos/crear_productos.html", context=context)
