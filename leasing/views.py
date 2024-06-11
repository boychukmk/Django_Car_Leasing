from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import ServicePackage, LeasingContract
from .forms import LeasingContractForm
from django.contrib.auth.decorators import login_required
from cars.models import Car
from django.utils.translation import gettext_lazy as _
from decimal import Decimal
from datetime import datetime


def legalentities(request):
    return render(request, 'legalentities.html')

def individuals(request):
    return render(request, 'individuals.html')




from datetime import datetime
from datetime import datetime

@login_required
def create_contract(request, car_code):
    car = get_object_or_404(Car, code=car_code)
    service_packages = ServicePackage.objects.all()
    selected_package = None
    error_message = None
    car_part = (car.price / 100) * 2
    calculated_prices = []
    for package in service_packages:
        package_price = package.price
        total_price = package_price * 12 + car_part
        monthly_payment = total_price / 12
        calculated_prices.append({
            'package': package,
            'total_price': round(total_price,2),
            'monthly_payment': round(monthly_payment,2),
        })
    if request.method == 'POST':
        form = LeasingContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.user = request.user
            contract.car = car
            overlapping_contracts = LeasingContract.objects.filter(
                car=car,
                start_date__lt=contract.end_date,
                end_date__gt=contract.start_date
            )
            if overlapping_contracts.exists():
                error_message = _("This car is already booked during the selected dates. "
                                  "Available after " +
                                  str(contract.end_date))
            else:
                contract.total_price = contract.service_package.price * ((contract.end_date - contract.start_date).days // 30) + car_part
                contract.monthly_payment = contract.total_price / ((contract.end_date - contract.start_date).days // 30)
                contract.save()
                return redirect('leasing:success')


    else:
        form = LeasingContractForm()

    package_id = request.GET.get('package')
    if package_id:
        selected_package = get_object_or_404(ServicePackage, id=package_id)
        form.fields['service_package'].initial = selected_package

    return render(request, 'create_contract.html', {
        'form': form,
        'car': car,
        'service_packages': service_packages,
        'selected_package': selected_package,
        'error_message': error_message,
        'calculated_prices': calculated_prices,
    })


def success(request):
    return render(request, 'success.html')





def leasing_services(request):
    service_packages = ServicePackage.objects.all()
    base_leasing = ServicePackage.objects.filter(name="Base Leasing").first()
    base_services_count = base_leasing.services.count() if base_leasing else 0

    for package in service_packages:
        package.base_services_count = base_services_count
        package.premium_services_count = package.services.count() - base_services_count \
            if package.name != "Base Leasing" else 0

    return render(request, 'leasing_services.html', {'service_packages': service_packages})
