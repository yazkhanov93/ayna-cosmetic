from django.contrib import admin
from .models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ["phone_number","homeDiscountedLimit", "homeRecommendLimit"]