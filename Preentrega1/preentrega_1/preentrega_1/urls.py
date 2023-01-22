"""preentrega_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from preentrega_1.views import index
from lista_producto.views import lista_de_productos,cargar_los_productos
from lista_usuarios.views import lista_de_usuarios,cargar_los_usuarios
from lista_vendedores.views import lista_de_vendedores,cargar_los_vendedores

urlpatterns = [
    path("",index, name="index"),
    path('admin/', admin.site.urls),

    #url de lista_producto
    path("lista_producto/", lista_de_productos),
    path("cargar_producto/", cargar_los_productos),
    path("lista_usuario/", lista_de_usuarios),
    path("cargar_usuario/", cargar_los_usuarios),
    path("lista_vendedores/", lista_de_vendedores),
    path("cargar_vendedores/", cargar_los_vendedores),
]
