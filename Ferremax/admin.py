from django.contrib import admin
from .models import categoria, marca, proveedor, producto, empleado, cliente, pedido, detallePedido, tipoUsuario, pedidoSinRegistrar, estadoPedido, estadoPago
# Register your models here.

admin.site.register(categoria) 
admin.site.register(marca) 
admin.site.register(proveedor) 
admin.site.register(producto)
admin.site.register(empleado)
admin.site.register(cliente)
admin.site.register(pedido)
admin.site.register(detallePedido)
admin.site.register(tipoUsuario)
admin.site.register(pedidoSinRegistrar)
admin.site.register(estadoPedido)
admin.site.register(estadoPago)
