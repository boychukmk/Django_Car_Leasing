from django.shortcuts import render
from .models import Car

# def catalog(request):
#     return render(request, 'cars/catalog.html')


# def auto(request):
#     return render(request, 'cars/auto.html')

def auto(request, car_code):
    car = Car.objects.get(code=car_code)
    return render(request, 'auto.html', {'car': car})

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



