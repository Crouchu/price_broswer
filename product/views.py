from rest_framework import viewsets, mixins, authentication, permissions, generics

from core.models import Product, Watchlist
from .serializers import ProductSerializer, WatchlistSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """Manage products in the database"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class WatchlistViewSet(viewsets.ModelViewSet):
    """Manage watchlists in the database"""
    serializer_class = WatchlistSerializer
    queryset = Watchlist.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """retrieve watchlists for the authenticated user"""
        return self.queryset.filter(user=self.request.user)