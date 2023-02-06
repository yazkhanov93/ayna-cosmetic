from rest_framework import serializers

from orders.models import Order, OrderItem
from products.models import Product, ProductImage, Color


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializerSwagger(serializers.ModelSerializer):
    orderItems = OrderItemsSerializer(many=True)
    class Meta:
        model = Order
        fields = ["id", "name", "phone","address","totalPrice","orderStatus","orderItems"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"