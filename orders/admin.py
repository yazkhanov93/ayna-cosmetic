from django.contrib import admin
from .models import Order, OrderItem
import requests, json
from service.income import addIncome


class OrderItemsInline(admin.StackedInline):
    fields = ["productId", "price", "quantity", "colorId"]
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    list_display = ["id", "name", "phone", "orderStatus",
                    "totalPrice", "created_at", "updated_at"]
    list_editable = ["orderStatus"]
    list_filter = ["orderStatus"]

    def save_model(self, request, obj, form, change):
        if obj.orderStatus == "GOWŞURYLDY":
            items = OrderItem.objects.filter(orderId=obj.id)
            k = []
            for i in items:
                k.append({"productId": i.productId.id,
                     "quantity": i.quantity, "price": i.price})
            addIncome(k)
            obj.save()
        else:
            obj.save()