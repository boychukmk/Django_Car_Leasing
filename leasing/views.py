from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ServicePackage, LeasingContract
from .forms import LeasingContractForm
from django.contrib.auth.decorators import login_required
from cars.models import Car
from decimal import Decimal

def legalentities(request):
    return render(request, 'legalentities.html')

def individuals(request):
    return render(request, 'individuals.html')
def get_package_details(request, package_name):
    package = get_object_or_404(ServicePackage, name=package_name)
    services = package.services.all()
    services_list = [service.name for service in services]
    data = {
        'name': package.name,
        'description': package.description,
        'price': str(package.price),
        'services': services_list
    }
    return JsonResponse(data)

@login_required
def create_contract(request, car_code):
    car = get_object_or_404(Car, code=car_code)
    service_packages = ServicePackage.objects.all()

    if request.method == 'POST':
        form = LeasingContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.user = request.user
            contract.car = car
            contract.total_price = contract.service_package.price * ((contract.end_date - contract.start_date).days // 30)
            contract.monthly_payment = contract.total_price / ((contract.end_date - contract.start_date).days // 30)
            contract.save()
            return redirect('leasing:success')  # Замініть на вашу фактичну URL-адресу успіху
    else:
        form = LeasingContractForm()

    return render(request, 'create_contract.html', {'form': form, 'car': car, 'service_packages': service_packages})


def success(request):
    return render(request, 'success.html')





def leasing_services(request):
    service_packages = ServicePackage.objects.all()
    base_leasing = ServicePackage.objects.filter(name="Base Leasing").first()
    base_services_count = base_leasing.services.count() if base_leasing else 0

    for package in service_packages:
        package.base_services_count = base_services_count
        package.premium_services_count = package.services.count() - base_services_count if package.name != "Base Leasing" else 0

    return render(request, 'leasing_services.html', {'service_packages': service_packages})
