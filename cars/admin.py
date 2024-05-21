from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name', 'year', 'price', 'fuel_type', 'transmission', 'mileage', 'drive_type', 'color', 'code')
    search_fields = ('name', 'code', 'color')

