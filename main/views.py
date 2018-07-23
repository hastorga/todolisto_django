from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST
from .models import Tarea, TipoTarea, EstadoTarea
from .formulario import RegistrationForm, TareaForm

#decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def root(request):
    return redirect('tareas')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario Creado Satisfactoriamente")
            success_url = reverse_lazy('login')
    else:
        form = RegistrationForm()
        args = {'form': RegistrationForm}
        return render(request, 'registration/signup.html', args)

    return HttpResponseRedirect(reverse_lazy('login'))

@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def admin(request):
    usuarios = User.objects.all()
    #cantidad = Tarea.objects.filter(usuario='1').count()

    if request.user.username == 'admin':
        return render(request, 'admin.html', { 'usuarios' : usuarios})
    else:
        return redirect('tareas')

@login_required()
@require_GET
def tareas(request):

    tareas = Tarea.objects.filter(usuario=request.user)
    tareasAdmin = Tarea.objects.all()
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()
    usuarios = User.objects.all()

    if request.user.username == 'admin':
        return render(request, 'admin.html', { 'usuarios' : usuarios , 'tareasAdmin' : tareasAdmin})
    else:
        return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})

"""
CRUD
"""

@login_required()
@require_POST
def crear_tarea(request):
    tarea = Tarea()
    tarea.titulo = request.POST.get('titulo')
    tarea.descripcion = request.POST.get('descripcion')
    tarea.tipo = TipoTarea.objects.get(id=(request.POST.get('tipo')))
    tarea.estado = EstadoTarea.objects.get(id=(request.POST.get('estado')))
    tarea.usuario = request.user
    tarea.fechaInicio = request.POST.get('fechaInicio')
    tarea.fechaTermino = request.POST.get('fechaTermino')
    tareas = Tarea.objects.filter(usuario=request.user)
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()

    if(tarea.fechaInicio <= tarea.fechaTermino):
        tarea.save()
        messages.success(request, "Tarea creada con éxito!")
        return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})
    else:
        messages.error(request,'La fecha de término debe ser posterior a la fecha de inicio!')
        return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})

@login_required
@require_GET
def eliminarTarea(request):
    tarea = Tarea.objects.get(pk=request.GET.get("id"))
    if tarea.usuario == request.user:
        tarea.delete()
        return render(request,'eliminarTarea.html')
    else:
        return HttpResponse("El elemento no existe o no tiene permiso")

@method_decorator(login_required, name='get')
class EditarTarea(UpdateView):
	model = Tarea
	form_class = TareaForm
	template_name = 'formTarea.html'
	success_url = reverse_lazy('tareas')

@login_required
@require_GET
def detalleTarea(request):
    estados = EstadoTarea.objects.all().order_by('nombre')
    tipos = TipoTarea.objects.all().order_by('nombre')
    tarea = Tarea.objects.get(pk=request.GET.get("id"))
    if request.user == tarea.usuario:
        return render(request, 'detalleTarea.html', { 'tarea': tarea, 'estados': estados, 'tipos': tipos })
    else:
        return HttpResponse("El elemento no existe o no tiene permiso")

@login_required()
def calendario(request):
    tareas = Tarea.objects.filter(usuario=request.user)
    return render(request, "calendario.html", { 'tareas' : tareas })
