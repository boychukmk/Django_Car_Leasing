# admin.py

from django.contrib import admin
from .models import Service, ServicePackage, LeasingContract

class ServiceInline(admin.TabularInline):
    model = ServicePackage.services.through
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(ServicePackage)
class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    inlines = [ServiceInline]

@admin.register(LeasingContract)
class LeasingContractAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'service_package', 'total_price', 'monthly_payment')

admin.site.register(ServicePackage.services.through)
