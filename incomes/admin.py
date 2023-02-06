from django.contrib import admin
from .models import Income
from rangefilter.filters import DateRangeFilter

@admin.register(Income)
class Incomeadmin(admin.ModelAdmin):
    list_display = ["productId", "quantity", "price", "created_at"]
    list_filter = [("created_at", DateRangeFilter)]