from datetime import datetime
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import marca, categoria, proveedor, producto, empleado, cliente, pedido, tipoUsuario, estadoPedido, estadoPago, pedidoSinRegistrar
from .apiMonedas import dolar, euro
import requests
import json
from django.db.models import Q

from django.conf import settings
from django.http import JsonResponse
from transbank.webpay.webpay_plus.transaction import Transaction, WebpayOptions, IntegrationCommerceCodes, IntegrationApiKeys
from transbank.common.integration_type import IntegrationType

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def Nosotros(request):
    return render(request, "core/Nosotros.html")


def Contacto(request):
    return render(request, "core/Contacto.html")


def crud_cuentas(request):
    if request.method == "POST":
        nombre_empleado = request.POST["nombre_empleado"]
        nombre_completo = request.POST["nombre_completo"]
        correo = request.POST["correo_empleado"]
        edad = request.POST["edad_empleado"]
        contraseña = request.POST["contraseña_empleado"]
        IdCar = request.POST["cargo"]
        tipo = 2

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        Emp = empleado.objects.create(
            nombreEmpleado=nombre_empleado,
            nombreCompleto=nombre_completo,
            correo=correo,
            edad=edad,
            contraseña=contraseña,
            tipoUsuario=objTipo
        )

        Emp.save()
        return redirect("crud_cuentas")

    else:
        tipo = tipoUsuario.objects.all()
        Empleados = empleado.objects.all()

        context = {
            "tipo": tipo, 
            "cuenta": Empleados
            }
        return render(request, "core/crud_cuentas.html", context)


def crud_productos(request):
    if request.method != "POST":
        mar = marca.objects.all()
        cat = categoria.objects.all()
        pro = proveedor.objects.all()
        produ = producto.objects.all()

        context = {
            "marca": mar,
            "categoria": cat,
            "proveedor": pro,
            "productos": produ
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


def Pedido(request):
    valorDolar = dolar()
    valorEuro = euro()

    context = {
        'dolar' : valorDolar,
        'euro' : valorEuro
    }

    return render(request, "core/pedido.html", context)


def Login(request):
    if request.method == "POST":
        runCliente = request.POST["runCliente"]
        contraseña = request.POST["contraseña"]
        try:
            cli = cliente.objects.get(
                        runCliente=runCliente, contraseña=contraseña
                    )
        except cliente.DoesNotExist:
            cli = None
        if cli is not None:
            request.session["nombreCliente"] = cli.nombreCompleto
            request.session["runCliente"] = cli.runCliente
            return render(request, "core/index.html")
        
    return render(
        request,
        "core/Login.html",
    )


def login_empleados(request):
    if request.method == "POST":
        runEmp = request.POST["runEmpleado"]
        contraseña = request.POST["contraseña"]
        try:
            emp = empleado.objects.get(
                        runEmpleado=runEmp, contraseña=contraseña
                    )
        except empleado.DoesNotExist:
            emp = None
            return redirect("index")
        if emp.tipoUsuario.idTipoUsuario == 2:
            request.session["nombreEmpleado"] = emp.nombreCompleto
            request.session["runEmpleado"] = emp.runEmpleado
            request.session["tipoUsuario"] = emp.tipoUsuario.idTipoUsuario
            return redirect("administrador")
        elif emp.tipoUsuario.idTipoUsuario == 3:
            request.session["nombreEmpleado"] = emp.nombreCompleto
            request.session["runEmpleado"] = emp.runEmpleado
            request.session["tipoUsuario"] = emp.tipoUsuario.idTipoUsuario
            return redirect("vendedor")
        elif emp.tipoUsuario.idTipoUsuario == 4:
            request.session["nombreEmpleado"] = emp.nombreCompleto
            request.session["runEmpleado"] = emp.runEmpleado
            request.session["tipoUsuario"] = emp.tipoUsuario.idTipoUsuario
            return redirect("bodeguero")
        elif emp.tipoUsuario.idTipoUsuario == 5:
            request.session["nombreEmpleado"] = emp.nombreCompleto
            request.session["runEmpleado"] = emp.runEmpleado
            request.session["tipoUsuario"] = emp.tipoUsuario.idTipoUsuario
            return redirect("contador")
        
    return render(request, "core/login_empleados.html",
    )


def registro(request):
    if request.method == "POST":
        run_cliente = request.POST["runCliente"]
        nombre_completo = request.POST["nombreCompleto"]
        correo = request.POST["correo"]
        contraseña1 = request.POST["contraseña1"]
        contraseña2 = request.POST["contraseña2"]
        tipo = 1

        objTipo = tipoUsuario.objects.get(idTipoUsuario=tipo)

        if contraseña1 == contraseña2:
            usu = cliente.objects.create(
                runCliente=run_cliente,
                nombreCompleto=nombre_completo,
                correo=correo,
                contraseña=contraseña1,
                tipoUsuario=objTipo
            )
            usu.save()
            return render(request, "core/Login.html")

        else:
            return render(request, "core/registro.html")

    context = {}
    return render(request, "core/registro.html", context)


def pago(request):
    runCli = request.session.get("runCliente")
    cli = cliente.objects.get(runCliente=runCli)

    nOrder = request.POST["ordenCompra"]
    idSesion = request.POST["idSesion"]
    direccion = request.POST["direccion"]
    fecha = datetime.now()
    total = request.POST["monto"]
    estPedido = 1
    estPago = 1

    objEstadoPedido = estadoPedido.objects.get(idEstadoPedido=estPedido)
    objEstadoPago = estadoPago.objects.get(idEstadoPago=estPago)

    objPedido = pedido.objects.create(
        idOrden=nOrder,
        idSesion=idSesion,
        direccionPedido=direccion,
        fechaPedido=fecha,
        totalPedido=total,
        estadoPedido=objEstadoPedido,
        estadoPago=objEstadoPago,
        cliente=cli,
    )
    objPedido.save()

    buy_order = request.POST["ordenCompra"]
    session_id = request.POST["idSesion"]
    amount = request.POST["monto"]
    return_url = 'http://127.0.0.1:8000/retorno_pago'

    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))
    
    response = transaction.create(buy_order, session_id, amount, return_url)
    token = response['token']
    url = response['url']
    
    return render(request, 'core/pago.html', {'url': url, 'token': token})


def pago_invitado(request):
    nombre = request.POST["nombre"]
    run = request.POST["run"]
    correo = request.POST["correo"]
    direccion = request.POST["direccionSinRegistro"]

    nOrder = request.POST["ordenCompra"]
    idSesion = request.POST["idSesion"]
    fecha = datetime.now()
    total = request.POST["monto"]
    estPedido = 1
    estPago = 1

    objEstadoPedido = estadoPedido.objects.get(idEstadoPedido=estPedido)
    objEstadoPago = estadoPago.objects.get(idEstadoPago=estPago)

    objPedido = pedidoSinRegistrar.objects.create(
        idOrden=nOrder,
        idSesion=idSesion,
        runCliente=run,
        nombreCompleto=nombre,
        direccionPedido=direccion,
        correo=correo,
        fechaPedido=fecha,
        totalPedido=total,
        estadoPedido=objEstadoPedido,
        estadoPago=objEstadoPago,
    )
    objPedido.save()

    buy_order = request.POST["ordenCompra"]
    session_id = request.POST["idSesion"]
    amount = request.POST["monto"]
    return_url = 'http://127.0.0.1:8000/retorno_pago'

    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))
    
    response = transaction.create(buy_order, session_id, amount, return_url)
    token = response['token']
    url = response['url']
    
    return render(request, 'core/pago_invitado.html', {'url': url, 'token': token})


def retorno_pago(request):
    token = request.GET.get('token_ws')
    
    transaction = Transaction(WebpayOptions(
        IntegrationCommerceCodes.WEBPAY_PLUS, 
        IntegrationApiKeys.WEBPAY, 
        IntegrationType.TEST))

    response = transaction.commit(token)
    
    status = response['status']
    amount = response['amount']
    buy_order = response['buy_order']
    
    context = {
        'status': status,
        'amount': amount,
        'buy_order': buy_order,
    }
    
    return render(request, 'core/retorno_pago.html', context)


def productos(request):
    datos = producto.objects.all()
    
    context = {
        'productos': datos
    }
    
    return render(request, 'core/productos.html', context)


def eliminarProducto(request, pk):
    prod = producto.objects.get(idProducto = pk)
    prod.delete()

    return redirect("crud_productos")



def edicion_producto(request, pk):
    if request.method != "POST":
        
        prod = producto.objects.get(idProducto = pk)
        mar = marca.objects.all()
        cat = categoria.objects.all()
        prov = proveedor.objects.all()
        context = {
            'producto': prod,
            'marca': mar,
            'categoria': cat,
            'proveedor': prov
        } 
        return render(request, 'core/edicion_producto.html', context)
    else:
        id_producto = request.POST["id_Producto"]
        nombre_producto = request.POST["txtNombre_Producto"]
        sotck_producto = request.POST["txtstock_Producto"]
        descripcion_producto = request.POST["txtdescripcion_Producto"]
        precio_producto = request.POST["txtPrecio_Producto"]
        id_marca = request.POST["marca"]
        id_categoria = request.POST["categoria"]
        id_proveedor = request.POST["proveedor"]

        objMarca = marca.objects.get(idMarca=id_marca)
        objCategoria = categoria.objects.get(idCategoria=id_categoria)
        objProveedor = proveedor.objects.get(idProveedor=id_proveedor)

        prod = producto.objects.get(idProducto = id_producto)
    
        prod.nombreProducto=nombre_producto
        prod.stockProducto=sotck_producto
        prod.descripcionProducto=descripcion_producto
        prod.precioProducto=precio_producto
        if 'imagen_producto' in request.FILES:
            prod.imagenProducto = request.FILES["imagen_producto"]
        prod.categoria=objCategoria
        prod.marca=objMarca
        prod.proveedor=objProveedor

        prod.save()

        return redirect("crud_productos")


def administrador(request):
    tipo = request.session.get("tipoUsuario")
    if tipo != 2 or tipo is None:
        return redirect("index")
    else:
        return render(request, "core/administrador.html")


def boletas(request):
    tipo = request.session.get("tipoUsuario")
    if tipo != 2 or tipo is None:
        return redirect("index")
    else:
        ped = pedido.objects.all()
        pedInvitado = pedidoSinRegistrar.objects.all()

        context = {
            "pedidos": ped,
            "pedidos_invitados": pedInvitado
        }
        return render(request, "core/boletas.html", context)


def boletas_registrados(request):
    ped = pedido.objects.all()

    context = {
        "pedidos" : ped
    }
    return render(request, "core/boletas_registrados.html", context)


def boletas_invitados(request):
    pedInvitados = pedidoSinRegistrar.objects.all()

    context = {
        "pedidos_invitados" : pedInvitados
    }
    return render(request, "core/boletas_invitados.html", context)


def detalle_registrado(request, pk):
    ped = pedido.objects.get(idPedido=pk)
    context = {
        "pedido" : ped
    }
    return render(request, "core/detalle_registrado.html", context)


def detalle_invitado(request, pk):
    ped = pedidoSinRegistrar.objects.get(idPedido=pk)
    context = {
        "pedido" : ped
    }
    return render(request, "core/detalle_invitado.html", context)


def vendedor(request):
    tipo = request.session.get("tipoUsuario")
    if tipo != 3 or tipo is None:
        return redirect("index")
    else:
        ped = pedido.objects.filter(Q(estadoPedido=1) | Q(estadoPedido=3))
        pedInvitado = pedidoSinRegistrar.objects.filter(Q(estadoPedido=1) | Q(estadoPedido=3))
        context = {
            "pedidos" : ped,
            "pedidos_invitados": pedInvitado,
        }
        return render(request, "core/vendedor.html", context)


def bodeguero(request):
    tipo = request.session.get("tipoUsuario")
    if tipo != 4 or tipo is None:
        return redirect("index")
    else:
        ped = pedido.objects.filter(Q(estadoPedido=2) | Q(estadoPedido=4) | Q(estadoPedido=5))
        pedInvitado = pedidoSinRegistrar.objects.filter(Q(estadoPedido=2) | Q(estadoPedido=4) | Q(estadoPedido=5))
        context = {
            "pedidos" : ped,
            "pedidos_invitados": pedInvitado,
        }
        return render(request, "core/bodeguero.html", context)


def cambiarEstadoPedido(request):
    if request.method == "POST":
        idPed = request.POST["idPedido"]
        idEstado = request.POST["idEstado"]
        redirect_url = request.POST.get("redirect_url")

        objPedido = pedido.objects.get(idPedido=idPed)
        objEstado = estadoPedido.objects.get(idEstadoPedido=idEstado)

        objPedido.estadoPedido = objEstado
        objPedido.save()
        return redirect(redirect_url)


def cambiarEstadoPedidoInvitado(request):
    if request.method == "POST":
        idPed = request.POST["idPedido"]
        idEstado = request.POST["idEstado"]
        redirect_url = request.POST.get("redirect_url")

        objPedido = pedidoSinRegistrar.objects.get(idPedido=idPed)
        objEstado = estadoPedido.objects.get(idEstadoPedido=idEstado)

        objPedido.estadoPedido = objEstado
        objPedido.save()
        return redirect(redirect_url)


def contador(request):
    tipo = request.session.get("tipoUsuario")
    if tipo != 5 or tipo is None:
        return redirect("index")
    else:
        ped = pedido.objects.all()
        ped_invitado = pedidoSinRegistrar.objects.all()
        context = {
            "pedidos" : ped,
            "pedidos_invitados" : ped_invitado,
        }
        return render(request, "core/contador.html", context)


def cambiarEstadoPago(request):
    if request.method == "POST":
        idPed = request.POST["idPedido"]
        idEstado = request.POST["idEstado"]
        redirect_url = request.POST.get("redirect_url")

        objPedido = pedido.objects.get(idPedido=idPed)
        objEstado = estadoPago.objects.get(idEstadoPago=idEstado)

        objPedido.estadoPago = objEstado
        objPedido.save()
        return redirect(redirect_url)


def cambiarEstadoPagoInvitado(request):
    if request.method == "POST":
        idPed = request.POST["idPedido"]
        idEstado = request.POST["idEstado"]
        redirect_url = request.POST.get("redirect_url")

        objPedido = pedidoSinRegistrar.objects.get(idPedido=idPed)
        objEstado = estadoPago.objects.get(idEstadoPago=idEstado)

        objPedido.estadoPago = objEstado
        objPedido.save()
        return redirect(redirect_url)


def Logout(request):
    del request.session["runCliente"]
    del request.session["nombreCliente"]
    return redirect("index")


def logout_empleado(request):
    del request.session["runEmpleado"]
    del request.session["nombreEmpleado"]
    return redirect("index")


def EliminarCuenta(request, pk):
    Emp = empleado.objects.get(idEmpleado=pk)
    Emp.delete()

    return redirect("crud_cuentas")