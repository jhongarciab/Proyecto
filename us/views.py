from django.shortcuts import render

def home(request):
    """
    Esta función representa la vista de la página de inicio de la aplicación de tareas. 
    Renderiza la plantilla 'home.html' y la  devuelve como respuesta.
    """
    return render(request, 'home.html')

