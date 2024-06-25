from django.shortcuts import redirect, render
from .models import empleado, usuario, tipoUsuario


def autorizadoEmpleado(view_func):
    def _wrapped_view(request, *args, **kwargs):
        nUsuario = request.session.get("nombreUsuario")
        tipo = 0
        if nUsuario:
            try:
                emp = empleado.objects.get(nombreEmpleado=nUsuario)
                tipo = 1 
            except empleado.DoesNotExist:
                pass

        if tipo == 0:
            return redirect('Login')
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view

def autorizadoTotal(view_func):
    def _wrapped_view(request, *args, **kwargs):
        nUsuario = request.session.get("nombreUsuario")
        tipo = 0

        if nUsuario:
            try:
                cli = usuario.objects.get(nombreUsuario=nUsuario)
                tipo = 2
            except usuario.DoesNotExist:
                pass

            try:
                emp = empleado.objects.get(nombreEmpleado=nUsuario)
                tipo = 1 
            except empleado.DoesNotExist:
                pass

        if tipo == 0:
            return redirect('Login')
        
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view