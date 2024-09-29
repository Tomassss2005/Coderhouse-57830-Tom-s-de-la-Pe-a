from django.contrib import admin
from .models import Perfil, Pedido, RegistroUsuarioForm, PerfilForm, PedidoForm, Servicio, ServicioForm

# Registro del modelo Perfil

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'celular', 'fecha_nacimiento')  # Muestra estos campos en la lista de perfiles
    search_fields = ('nombre', 'apellido', 'celular')  # Barra de búsqueda por nombre, apellido, celular
    list_filter = ('fecha_nacimiento',)  # Filtros por fecha de nacimiento

# Registro del modelo Pedido
    
class PedidoAdmin(admin.ModelAdmin):
    form = PedidoForm  # Aquí se asigna el formulario personalizado
    list_display = ['perfil', 'descripcion_pedido', 'precio_pagar', 'fecha_entregadoz', 'estado']
    search_fields = ['perfil__nombre', 'descripcion_pedido']
    list_filter = ['estado', 'fecha_pedido']
    ordering = ['fecha_pedido']


# Registro del modelo registro
    
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'celular', 'fecha_nacimiento')
    search_fields = ('nombre', 'apellido')
    list_filter = ('fecha_nacimiento',)
    ordering = ('-fecha_nacimiento',)


class ServicioAdmin(admin.ModelAdmin):
    form = ServicioForm
    
    list_display = ['producto', 'precio', 'estado']
    search_fields = ['producto']
    list_filter = ['estado']