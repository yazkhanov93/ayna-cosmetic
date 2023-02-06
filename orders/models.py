from django.db import models
from products.models import Product, Color


class Order(models.Model):
    STATUS = (
        ("SARGYT EDILDI", "SARGYT EDILDI"),
        ("TASSYKLANDY", "TASSYKLANDY"),
        ("GOWŞURYLDY", "GOWŞURYLDY"),
        ("BES EDILDI","BES EDILDI")
    )
    name = models.CharField(max_length=255, verbose_name="ady")
    phone = models.CharField(max_length=255, verbose_name="telefon belgisi")
    address = models.CharField(max_length=255, verbose_name="öý aglysy")
    orderStatus = models.CharField(choices=STATUS, max_length=255, verbose_name="statusy", default="SARGYT EDILDI")
    totalPrice = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="jemi bahasy")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="sargyt edilen wagty")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="üýtgeşme girizilen wagty")


    class Meta:
        verbose_name_plural = "Sargytlar"
        ordering = ("orderStatus",)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="sargyt", related_name="orderItems")
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="haryt", related_name="product")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="bahasy")
    quantity = models.PositiveIntegerField(default=1, verbose_name="sany")
    colorId = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="orderColors", verbose_name="reňki")

    class Meta:
        verbose_name_plural = "Sargyt edilen Harytlar"

    def __str__(self):
        return str(self.productId.title)