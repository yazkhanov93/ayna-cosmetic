from django.db import models
from products.models import Product


class Income(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="haryt")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="girdeji")
    quantity = models.IntegerField(verbose_name="satylan sany")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="satylan guni")

    class Meta:
        verbose_name_plural = "Arassa Girdejiler"
        ordering = ("created_at",)


    def __str__(self):
        return str(self.productId.title)