from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Perfil(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True, default=None, verbose_name="Fecha de Nacimiento", help_text="Introduce tu fecha de nacimiento.")
    imagen_usuario = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.apellido})"
    

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'celular', 'fecha_nacimiento', 'imagen_usuario']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'imagen_usuario': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'celular': 'Celular',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'imagen_usuario': 'Imagen de Usuario',
        }
        help_texts = {
            'nombre': 'Introduce el nombre del usuario.',
            'apellido': 'Introduce el apellido del usuario.',
            'celular': 'Introduce el número de celular.',
            'fecha_nacimiento': 'Introduce la fecha de nacimiento.',
            'imagen_usuario': 'Opcional: Carga una imagen de usuario.',
        }
    

class Pedido(models.Model):
    class Estado(models.TextChoices):
        PENDIENTE = "PENDIENTE", "Pendiente",
        EN_PROGRESO = "EN_PROGRESO", "En progreso",
        TERMINADO = "TERMINADO", "Terminado",
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    descripcion_pedido = models.TextField(blank=True, null=True)
    precio_pagar = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entregado = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=Estado.choices, default=Estado.PENDIENTE)
    imagen_producto = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    
def __str__(self) -> str:
        return f"Pedido de {self.servicio.nombre} para {self.perfil.nombre}"

class PedidoForm(forms.ModelForm):
     class Meta:
          model = Pedido
          fields = ['perfil', 'descripcion_pedido', 'precio_pagar', 'fecha_entregado', 'estado', 'imagen_producto']
          widgets = {
               'estado': forms.Select(choices=Pedido.Estado.choices),    #Selección del estado
          }

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Servicio(models.Model):
    producto = models.CharField(max_length=50, unique=True)
    descripcion_producto = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.producto

    

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['producto', 'descripcion_producto', 'precio', 'estado']


from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),  # Reemplaza con el nombre de tu migración inicial
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50, unique=True)),
                ('descripcion_producto', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
