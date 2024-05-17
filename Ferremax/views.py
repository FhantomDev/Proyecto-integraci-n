from django.shortcuts import render, redirect
from django.urls import reverse
from .models import marca, categoria, proveedor, producto, cargo, empleado


# Create your views here.
def index(request):
    return render(request, "core/index.html")


def Nosotros(request):
    return render(request, "core/Nosotros.html")


def Contacto(request):
    return render(request, "core/Contacto.html")


def crud_cuentas(request):
    if request.method != "POST":
        carg = cargo.objects.all()

        context = {
            "cargo": carg,
        }
        return render(request, "core/crud_cuentas.html", context)
    else:
        p_nombre_empleado = request.POST["txtPrimer_nombre_Empleado"]
        s_nombre_empleado = request.POST["txtSegundo_nombre_Empleado"]
        p_apellido_empleado = request.POST["txtPrimer_Apellido"]
        s_apellido_empleado = request.POST["txtSegundo_Apellido"]
        direccion_empleado = request.POST["txtDireccion"]
        edad_empleado = request.POST["txtEdad"]
        id_cargo = request.POST["cargo"]

        objCargo = cargo.objects.get(idCargo=id_cargo)

        emp = empleado.objects.create(
            pNombreEmpleado=p_nombre_empleado,
            sNombreEmpleado=s_nombre_empleado,
            pApellidoEmpleado=p_apellido_empleado,
            sApellidoEmpleado=s_apellido_empleado,
            direccionEmpleado=direccion_empleado,
            edad=edad_empleado,
            cargo=objCargo,
        )
        emp.save()

        context = {
            "mensaje": "Exito"

        }
        return render(request, "core/resultado.html", context)


def crud_productos(request):
    if request.method != "POST":
        mar = marca.objects.all()
        cat = categoria.objects.all()
        pro = proveedor.objects.all()

        context = {
            "marca": mar,
            "categoria": cat,
            "proveedor": pro,
        }
        return render(request, "core/crud_productos.html", context)

    else:
        nombre_producto = request.POST["txtNombre_Producto"]
        sotck_producto = request.POST["txtstock_Producto"]
        descripcion_producto = request.POST["txtdescripcion_Producto"]
        precio_producto = request.POST["txtPrecio_Producto"]
        imagen_producto = request.FILES["imagen_producto"]
        id_marca = request.POST["marca"]
        id_categoria = request.POST["categoria"]
        id_proveedor = request.POST["proveedor"]

        objMarca = marca.objects.get(idMarca=id_marca)
        objCategoria = categoria.objects.get(idCategoria=id_categoria)
        objProveedor = proveedor.objects.get(idProveedor=id_proveedor)

        cli = producto.objects.create(
            nombreProducto=nombre_producto,
            stockProducto=sotck_producto,
            descripcionProducto=descripcion_producto,
            precioProducto=precio_producto,
            imagenProducto = imagen_producto,
            categoria=objCategoria,
            marca=objMarca,
            proveedor=objProveedor,
        )
        cli.save()

        context = {
            "mensaje": "Exito"

        }
        return render(request, "core/resultado.html", context)


def resultado(request):
    context = {

    }
    return render(request, "core/resultado.html", context)


def pago(request):
    context = {

    }
    return render(request, "core/pago.html", context)