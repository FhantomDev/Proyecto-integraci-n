from django.urls import path
from .views import (
    index,
    Nosotros,
    Contacto,
    crud_cuentas,
    crud_productos,
    resultado,
    pago
)

urlpatterns = [
    path("", index, name="index"),
    path("Nosotros", Nosotros, name="Nosotros"),
    path("Contacto", Contacto, name="Contacto"),
    path("crud_cuentas", crud_cuentas, name="crud_cuentas"),
    path("crud_productos", crud_productos, name="crud_productos"),
    path("resultado", resultado, name="resultado"),
    path("pago", pago, name="pago"),
]
