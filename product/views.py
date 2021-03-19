from rest_framework import viewsets, mixins, authentication, permissions, generics

from core.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage products in the database"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
