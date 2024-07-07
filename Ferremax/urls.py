from django.urls import path, include
from rest_framework import routers
from .api import ProductoViewSet, CategoriaViewSet

from .views import (
    index,
    Nosotros,
    Contacto,
    crud_cuentas,
    crud_productos,
    resultado,
    Pedido,
    pago,
    retorno_pago,
    productos,
    Login,
    registro,
    eliminarProducto,
    edicion_producto,
    administrador,
    Logout,
    EliminarCuenta,
    pago_invitado,
    cambiarEstadoPedido,
    bodeguero,
    cambiarEstadoPedidoInvitado,
    contador,
    cambiarEstadoPago,
    cambiarEstadoPagoInvitado,
    login_empleados,
    logout_empleado,
    vendedor
)

router = routers.DefaultRouter()
router.register('api/v1/productos', ProductoViewSet, 'productos')
router.register('api/v1/categorias', CategoriaViewSet, 'categorias')

urlpatterns = [
    path("", index, name="index"),
    path("Nosotros", Nosotros, name="Nosotros"),
    path("Contacto", Contacto, name="Contacto"),
    path("crud_cuentas", crud_cuentas, name="crud_cuentas"),
    path("crud_productos", crud_productos, name="crud_productos"),
    path("resultado", resultado, name="resultado"),
    path("pedido", Pedido, name="pedido"),
    path("pago", pago, name="pago"),
    path("pago_invitado", pago_invitado, name="pago_invitado"),
    path("retorno_pago", retorno_pago, name="retorno_pago"),
    path("productos", productos, name="productos"),
    path("Login", Login, name="Login"),
    path("registro", registro, name="registro"),
    path("edicion_producto/<str:pk>", edicion_producto, name="edicion_producto"),
    path("eliminarProducto/<str:pk>", eliminarProducto, name="eliminarProducto"),
    path("administrador", administrador, name="administrador"),
    path("Logout", Logout, name="Logout"),
    path("EliminarCuenta/<str:pk>", EliminarCuenta, name="EliminarCuenta"),
    path("vendedor", vendedor, name="vendedor"),
    path("cambiarEstadoPedido", cambiarEstadoPedido, name="cambiarEstadoPedido"),
    path("bodeguero", bodeguero, name="bodeguero"),
    path("cambiarEstadoPedidoInvitado", cambiarEstadoPedidoInvitado, name="cambiarEstadoPedidoInvitado"),
    path("contador", contador, name="contador"),
    path("cambiarEstadoPago", cambiarEstadoPago, name="cambiarEstadoPago"),
    path("cambiarEstadoPagoInvitado", cambiarEstadoPagoInvitado, name="cambiarEstadoPagoInvitado"),
    path("login_empleados", login_empleados, name="login_empleados"),
    path("logout_empleado", logout_empleado, name="logout_empleado"),
    path('', include(router.urls)),
]
