
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.root),
    path('login/',auth_views.LoginView.as_view(), name="login"),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.register, name='register'),
    path('home/', views.index, name= "home"),
    path('tareas/', views.tareas, name= "tareas"),
    path('crear_tarea/', views.crear_tarea, name= "crear_tarea"),
    path('detalleTarea/', views.detalleTarea, name="detalleTarea"),
    path('editarTarea/<int:pk>', views.EditarTarea.as_view(), name="editarTarea"),
    path('eliminarTarea/', views.eliminarTarea, name="eliminarTarea"),
    path('calendario/', views.calendario, name= "calendario"),
    path('admin', views.admin, name= "admin"),





]
