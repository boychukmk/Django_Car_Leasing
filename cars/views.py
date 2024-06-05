from django.shortcuts import render

from leasing.models import ServicePackage
from .models import Car

# def catalog(request):
#     return render(request, 'cars/catalog.html')


# def auto(request):
#     return render(request, 'cars/auto.html')

def auto(request, car_code):
    car = Car.objects.get(code=car_code)
    service_packages = ServicePackage.objects.all()
    base_leasing = ServicePackage.objects.filter(name="Base Leasing").first()
    base_services_count = base_leasing.services.count() if base_leasing else 0

    for package in service_packages:
        package.base_services_count = base_services_count
        package.premium_services_count = package.services.count() - base_services_count if package.name != "Base Leasing" else 0

    return render(request, 'auto.html', {'car': car,'service_packages': service_packages})

def catalog(request):
    order_by = request.GET.get('order_by', 'default')
    discount_filter = request.GET.get('discount', 'false') == 'true'

    cars = Car.objects.all()

    if discount_filter:
        cars = cars.filter(discount__isnull=False, discount__gt=0)

    if order_by == 'price':
        cars = cars.order_by('price')
    elif order_by == '-price':
        cars = cars.order_by('-price')

    context = {
        'cars': cars,
        'order_by': order_by,
        'discount_filter': discount_filter,
    }
    return render(request, 'catalog.html', context)



