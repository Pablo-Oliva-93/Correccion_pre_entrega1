from django.shortcuts import render
from django.http import HttpResponse
from lista_vendedores.models import Vendedor
from lista_vendedores.form import Vendedorformulario
# Create your views here.
def lista_de_vendedores(request):
    if "search" in request.GET:
        var_filto = request.GET["search"]
        var_vendedores = Vendedor.objects.filter(nombre__contains=var_filto)
    else:
        var_vendedores = Vendedor.objects.all()

    context = {
        "vendedores":var_vendedores,
    }
    return render(request, "tem_vendedores/lista_vendedores.html", context=context)
def cargar_los_vendedores (request):
    if request.method == "GET":
        context = {
            "formulario" : Vendedorformulario()
        }
        return render(request, "tem_vendedores/crear_vendedores.html", context=context)
    
    elif request.method == "POST":
        var_form = Vendedorformulario(request.POST)
        if var_form.is_valid():
            Vendedor.objects.create(
                nombre=var_form.cleaned_data["nombre"],
                nivel=var_form.cleaned_data["nivel"],
                activo=var_form.cleaned_data["activo"],
            )
            context = {
                "mensaje_de_ok": "El producto se creo correctamente"
            }
            return render(request, "tem_vendedores/crear_vendedores.html", context=context)
        else:
            context = {
                "error_del_formulario": var_form.errors,
                "formulario" : Vendedorformulario(),
            }
            return render(request, "tem_vendedores/crear_vendedores.html", context=context)
