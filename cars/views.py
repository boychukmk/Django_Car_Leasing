from django.shortcuts import render


def catalog(request):
    return render(request, 'cars/catalog.html')


def auto(request):
    return render(request, 'cars/auto.html')