from django.contrib import admin
from .models import ServicePackage, LeasingContract, Service


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1

class ServicePackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    inlines = [ServiceInline]

admin.site.register(ServicePackage, ServicePackageAdmin)

class LeasingContractAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'service_package', 'total_price', 'monthly_payment')
    search_fields = ('user__username', 'car__name')
    list_filter = ('start_date', 'end_date', 'service_package')

admin.site.register(LeasingContract, LeasingContractAdmin)
