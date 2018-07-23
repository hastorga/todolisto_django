# Taller: Todo Listo en Django

Respecto a los requerimientos:

  * Es necesario tener instalar:
    * Framework Django en su version 2.0
    * XAMPP en su version 3.2.2
    * Anaconda
    * Python 3

  * Sistema Operativo:
    * Windows 10

Respecto a la instalacion:

  * Mediante la consola de Anaconda (Anaconda Prompt):

    * Se debe crear un ambiente exclusivo para el proyecto:
      > conda create -n todolisto python=3

    * Se debe instalar el framework Django
      > pip install django
    
    * Es necesario instalar un cliente MySQL para usar la BD desde Python:
      > pip install mysqlclient


Respecto a la ejecucion:

  * Iniciar, en XAMPP, los siguiente modulos:
    - `Apache`
    - `MySQL`

  * Se debe activar el proyecto en la consola de anaconda (Anaconda Prompt):
    - source activate todolisto
    - cd todolisto
    - python manage.py runserver
  
  * Se debe crear obligatoriamente un usuario con username: 'admin', quien será el administrador del sistema

Respecto a los controladores:

  * COMPLETAR

Respecto a los modelos:

  * El sistema cuenta con tres modelos:
    - Tarea
    - EstadoTarea
    - TipoTarea

Respecto a las vistas:

  * Se tienen las siguientes vistas:
    - 'registro': Registro de nuevos usuarios
    - 'login': Iniciar sesión 
    - 'home': Inicio
    - 'tareas': Tareas de un usuario
    - 'tareasAdmin': Tareas de todos los usuarios
    - 'borrarTarea': Eliminar tarea
    - 'detalleTarea': Detalle de tarea
    - 'editarTarea': Edición de tarea
    - 'calendario': Calendario de tareas de un usuario



Respecto a la base de datos:

  * Debe crear una base de datos denomidada 'todolisto'. Para esto es necesario aplicar los siguientes comandos en la consola (shell) de XAMPP:

    > mysql -u root -p

    > CREATE DATABASE todolisto;

    > CREATE USER ‘todo’@’%’ IDENTIFIED BY ‘listo’;

    > GRANT ALL PRIVILEGES ON todolisto.* TO ‘todo’@’%’;

    > FLUSH PRIVILEGES;
  
  * Es necesario ingresar los nombres de los host y la cuenta de usuario por defecto con la contraseña en el archivo 'php.ini' (C:\xampp\php), en el nivel siguiente:

    ; Default host for mysql_connect() (doesn't apply in safe mode).
    ; http://php.net/mysqli.default-host
    mysqli.default_host='localhost'

    ; Default user for mysql_connect() (doesn't apply in safe mode).
    ; http://php.net/mysqli.default-user
    mysqli.default_user='todo'

    ; Default password for mysqli_connect() (doesn't apply in safe mode).
    ; Note that this is generally a *bad* idea to store passwords in this file.
    ; *Any* user with PHP access can run 'echo get_cfg_var("mysqli.default_pw")
    ; and reveal this password!  And of course, any users with read access to this
    ; file will be able to reveal the password as well.
    ; http://php.net/mysqli.default-pw
    mysqli.default_pw='listo'




Respecto de las funciones del sistema:

1. Para registrarse en el sistema debe acceder a la URL `/todolisto/register`. Dentro de esta vista se deben completar los campos requeridos. Para confirmar debe presionar el boton "Sign In".

2. Para ingresar al sistema debe acceder a la URL `/todolisto/login`. Dentro de esta vista se deben completar los campos requeridos. Para confirmar debe presionar el boton "Login".

3. Para crear una tarea o ver el listado de tareas del usuario se debe acceder a la URL `/todolisto/tareas`
Dentro de esta vista, en caso de querer crear una tarea, debe completar los campos solicitados y luego. presionar el boton "Crear". Ademas, esta vista ofrece tres opciones para cada tarea: Detalle, Editar y Eliminar l

4. Para ver el detalle una tarea de el listado de tareas del usuario se debe acceder a la URL `/todolisto/detalleTarea/"id"`.
Dentro de esta vista se puede modificar la tarea seleccionada tras presionar el boton "Editar".

5. Para modificar una tarea de el listado de tareas del usuario se debe acceder a la URL `/todolisto/editarTarea/"id"`. Dentro de esta vista se deben completar los campos requeridos. Para confirmar debe presionar el boton "Guardar".

5. Para eliminar una tarea de el listado de tareas del usuario se debe acceder a la URL `/todolisto/eliminarTarea/"id"`
Dentro de esta vista debe presionar el boton "Aceptar" para completar la accion.

6. Para ver el calendario que contiene todas las tareas del usuario se debe acceder a la URL `/todolisto/calendario`.

7. Para ver las tareas de todos los usuarios del sistema es necesario loguearse como administrador, es decir, entrar bajo el username 'admin'. 
 