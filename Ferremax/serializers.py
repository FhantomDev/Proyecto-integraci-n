from rest_framework import serializers
from .models import producto

class ProductoSerializer(serializers.ModelSerializer):
  class Meta():
    model = producto
    fields = ('idProducto', 'nombreProducto', 'stockProducto', 'descripcionProducto', 'precioProducto',
              'imagenProducto', 'categoria', 'marca', 'proveedor')