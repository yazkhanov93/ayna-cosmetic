from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Color
from orders.models import Order, OrderItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from decimal import Decimal

from drf_yasg.utils import swagger_auto_schema

from .serializers import OrderSerializer, OrderItemCreateSerializer, OrderSerializerSwagger


class OrderCreateView(APIView):
    @swagger_auto_schema(request_body=OrderSerializerSwagger)
    def post(self,request):
        try:
            data = request.data
            totalPrice = 0
            for i in data["orderItems"]:
                totalPrice+=i["price"]*i["quantity"]
            data["totalPrice"]=totalPrice
            serializer = OrderSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                for item in data["orderItems"]:
                    item["orderId"] = serializer.data["id"]
                    productId = Product.objects.get(id=item["productId"])
                    color = Color.objects.get(id=item["colorId"])
                    item_serializer = OrderItemCreateSerializer(data=item)
                    if item_serializer.is_valid():
                        item_serializer.save()
                    else:
                        return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)