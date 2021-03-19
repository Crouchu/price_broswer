from rest_framework import serializers

from core.models import Product, Watchlist


class ProductSerializer(serializers.ModelSerializer):
    """Serialize a product"""

    class Meta:
        model = Product
        fields = (
            'product_id', 'product_name', 'image', 'link_morele', 'price_morele',
            'link_xkom', 'price_xkom', 'category', 'created_at', 'updated_at'
        )
        read_only_fields = ('product_id',)


class WatchlistSerializer(serializers.ModelSerializer):
    """Serialize a watchlist"""

    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())

    class Meta:
        model = Watchlist
        fields = ('watchlist_id', 'title', 'products')
        read_only_fields = ('watchlist_id',)