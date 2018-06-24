from django.shortcuts import render,redirect
from django.http import HttpResponse
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
from .formulario import Registro, TareaForm

# Create your views here.

def root(request):
    return redirect('tareas')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = Registro
    success_url = reverse_lazy('login')

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
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()
    usuarios = User.objects.all()

    if request.user.username == 'admin':
        return render(request, 'admin.html', { 'usuarios' : usuarios})
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
    tarea.save()
    tareas = Tarea.objects.filter(usuario=request.user)
    tipos = TipoTarea.objects.all()
    estados = EstadoTarea.objects.all()
    return render(request, "tareas.html", { 'tareas' : tareas, 'tipos': tipos, 'estados': estados})



#@login_required()
#def calendario(request):
#    tareas = Tarea.objects.filter(usuario=request.user)
#    return render(request, 'calendario.html', { 'tareas': tareas})

class EliminarTarea(DeleteView):
	model = Tarea
	template_name = 'eliminarTarea.html'
	success_url = reverse_lazy('tareas')


class EditarTarea(UpdateView):
	model = Tarea
	form_class = TareaForm
	template_name = 'formTarea.html'
	success_url = reverse_lazy('tareas')

class DetalleTarea(DetailView):
	model = Tarea
	template_name = 'detalleTarea.html'

"""
CALENDARIO
"""


class CalendarPage(TemplateView):
    template_name = 'calendario.html'
    form_class = TareaForm
    def get_context_data(self, **kwargs):
        context = super(CalendarPage, self).get_context_data(**kwargs)
        context['tareas'] = Tarea.objects.all()
        return context

