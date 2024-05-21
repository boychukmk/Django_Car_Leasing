from django.shortcuts import render
from .models import Car

# def catalog(request):
#     return render(request, 'cars/catalog.html')


def auto(request):
    return render(request, 'cars/auto.html')
def catalog(request):

    order_by = request.GET.get('order_by', 'default')

    if order_by == 'price':
        cars = Car.objects.order_by('price')
    elif order_by == '-price':
        cars = Car.objects.order_by('-price')
    else:
        cars = Car.objects.all()

    context = {
        'cars': cars,
        'order_by': order_by,
    }
    return render(request, 'catalog.html', context)

