from rest_framework import serializers
from .models import producto, categoria

class ProductoSerializer(serializers.ModelSerializer):
  class Meta():
    model = producto
    fields = ('idProducto', 'nombreProducto', 'stockProducto', 'descripcionProducto', 'precioProducto',
              'imagenProducto', 'categoria', 'marca', 'proveedor')

class CategoriaSerializer(serializers.ModelSerializer):
  class Meta():  
    model = categoria
    fields = ('idCategoria', 'nombreCategoria')