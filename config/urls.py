"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from proyecto import views


app_name = 'proyecto'

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('iniciar/sesion/', LoginView.as_view(template_name='base/iniciar-sesion.html'), name='iniciar-sesion'),
    path('cerrar/sesion', LogoutView.as_view(template_name='base/cerrar-sesion.html'), name='cerrar-sesion'),

    path('registro', views.registro, name='registro'),

    path('pedidos', views.listar_pedido, name='listar_pedido'),
    path('crear/pedido', views.crear_pedido, name='crear_pedido'),
    path('listar/pedido', views.listar_pedido, name='listar_pedido'),
    path('actualizar/pedido/<int:pedido_id>', views.actualizar_pedido, name='actualizar_pedido'),
    path('eliminar/pedido/<int:pedido_id>', views.eliminar_pedido, name='eliminar_pedido'),

    path('perfiles', views.perfiles, name='listar_perfil'),
    path('crear/perfil', views.crear_perfil, name='crear_perfil'),
    path('listar/perfil', views.listar_perfil, name='listar_perfil'),
    path('actualizar/perfil/<int:pk>/', views.actualizar_perfil, name='actualizar_perfil'),
    path('eliminar/perfil/<int:pk>/', views.eliminar_perfil, name='eliminar_perfil'),

    path('servicio/', views.listar_servicio, name='listar_servicio'),
    path('crear/servicio/', views.crear_servicio, name='crear_servicio'),
    path('listar/servicio/', views.listar_servicio, name='listar_servicio'),
    path('actualizar/servicio/<int:pk>/', views.actualizar_servicio, name='actualizar_servicio'),
    path('eliminar/servicio/<int:pk>/', views.eliminar_servicio, name='eliminar_servicio'),
]