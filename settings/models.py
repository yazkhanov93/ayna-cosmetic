from django.db import models


class Settings(models.Model):
    phone_number = models.CharField(max_length=20, null=True, blank=True, verbose_name="prosent")
    homeDiscountedLimit = models.IntegerField(verbose_name="skidka limit", blank=True, null=True)
    homeRecommendLimit = models.IntegerField(verbose_name="maslahat berilyan limit", blank=True, null=True)

    class Meta:
        verbose_name_plural = "Sazlamalar"

    def __str__(self):
        return str(self.phone_number)