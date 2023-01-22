from django.shortcuts import render
from django.http import HttpResponse
from lista_usuarios.models import Usuario
from lista_usuarios.form import Usuarioformulario
# Create your views here.
def lista_de_usuarios(request):
    if "search" in request.GET:
        var_filto = request.GET["search"]
        var_usuarios = Usuario.objects.filter(usuario__contains=var_filto)
    else:
        var_usuarios = Usuario.objects.all()

    context = {
        "usuarios":var_usuarios,
    }
    return render(request, "tem_usuarios/lista_usuarios.html", context=context)
    
def cargar_los_usuarios (request):
    if request.method == "GET":
        context = {
            "formulario" : Usuarioformulario()
        }
        return render(request, "tem_usuarios/crear_usuarios.html", context=context)
   
    elif request.method == "POST":
        var_form = Usuarioformulario(request.POST)
        if var_form.is_valid():
            Usuario.objects.create(
                usuario=var_form.cleaned_data["usuario"],
                nombre=var_form.cleaned_data["nombre"],
                edad=var_form.cleaned_data["edad"],
            )
            context = {
                "mensaje_de_ok": "Vienvenido/a, te registraste correctamente"
            }
            return render(request, "tem_usuarios/crear_usuarios.html", context=context)
        else:
            context = {
                "error_del_formulario": var_form.errors,
                "formulario" : Usuarioformulario(),
            }
            return render(request, "tem_usuarios/crear_usuarios.html", context=context)