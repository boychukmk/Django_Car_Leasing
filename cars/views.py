from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from leasing.models import ServicePackage
from .models import Car
from .utils import q_search


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
    query = request.GET.get('q', None)
    cars = Car.objects.all()

    if discount_filter:
        cars = cars.filter(discount__isnull=False, discount__gt=0)

    if order_by == 'price':
        cars = cars.order_by('price')
    elif order_by == '-price':
        cars = cars.order_by('-price')
    elif query:
        cars = q_search(query)

    paginator = Paginator(cars, 9)  # Show 12 cars per page
    page = request.GET.get('page', 1)

    try:
        cars_page = paginator.page(page)
    except PageNotAnInteger:
        cars_page = paginator.page(1)
    except EmptyPage:
        cars_page = paginator.page(paginator.num_pages)

    context = {
        'cars': cars_page,  # Pass the paginated page object to the context
        'order_by': order_by,
        'discount_filter': discount_filter,
    }
    return render(request, 'catalog.html', context)

def search(request):
    query = request.GET.get('q', '')
    cars = Car.objects.filter(name__icontains=query) if query else Car.objects.all()
    context = {
        'cars': cars,
        'query': query,
    }
    return render(request, 'base.html', context)