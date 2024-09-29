from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfil, PerfilForm, Pedido, PedidoForm, RegistroUsuarioForm, Servicio, ServicioForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def index(request):
    return render(request, 'base/index.html', {'perfil': request.user})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sesión iniciada correctamente')
            return redirect('index')
        else:
            messages.error(request, 'Datos incorrectos')
    return render(request, 'iniciar_sesion.html')



def perfiles(request):
    return render(request, 'perfiles/listar_perfil.html')

def crear_perfil(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_perfil')
    else:
        form = PerfilForm()
    return render(request, 'perfiles/crear_perfil.html', {'form': form})

def listar_perfil(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfiles/listar_perfil.html', {'perfiles': perfiles})

def actualizar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('listar_perfil')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfiles/actualizar_perfil.html', {'form': form})

def eliminar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if request.method == "POST":
        perfil.delete()
        return redirect(listar_perfil)
    return render(request, 'perfiles/eliminar_perfil.html', {'perfil': perfil})




def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_pedido')
    else:
        form = PedidoForm()
    return render(request, 'pedidos/crear_pedido.html', {'form': form})


def listar_pedido(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/listar_pedido.html', {'pedidos': pedidos})

def actualizar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('listar_pedido')
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedidos/actualizar_pedido.html', {'form': form})

def eliminar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        pedido.delete()
        return redirect('listar_pedido')

    return render(request, 'pedidos/eliminar_pedido.html', {'pedido': pedido})



def registro(request):
    if request.method == 'POST':
        form_usuario = RegistroUsuarioForm(request.POST)
        form_perfil = PerfilForm(request.POST, request.FILES)
        if form_usuario.is_valid() and form_perfil.is_valid():
            usuario = form_usuario.save()
            perfil = form_perfil.save(commit=False)
            perfil.usuario = usuario
            perfil.save()
            login(request, usuario)
            return redirect('index')
    else:
        form_usuario = RegistroUsuarioForm()
        form_perfil = PerfilForm()
    return render(request, 'registros/registro.html', {'form_usuario': form_usuario, 'form_perfil': form_perfil})



def crear_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_servicio')  # Redirige a la vista de lista de servicios después de guardar
    else:
        form = ServicioForm()
    return render(request, 'servicios/crear_servicio.html', {'form': form})

def listar_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/listar_servicio.html', {'servicios': servicios})


def actualizar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('listar_servicio')  # Redirige a la lista después de actualizar
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicios/actualizar_servicio.html', {'form': form})


def eliminar_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('listar_servicio')  # Redirige a la lista después de eliminar
    return render(request, 'servicios/eliminar_servicio.html', {'servicio': servicio})
