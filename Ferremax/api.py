from .models import producto, categoria
from rest_framework import viewsets, permissions, generics
from .serializers import ProductoSerializer, CategoriaSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductoFilter

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoFilter
    permission_classes = [permissions.AllowAny]


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny] 