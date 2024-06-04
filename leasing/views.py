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
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .forms import LeasingContractForm
# from cars.models import Car
# from leasing.models import ServicePackage

@login_required
def create_contract(request, car_code):
    car = get_object_or_404(Car, code=car_code)
    package_name = request.GET.get('package')
    package = get_object_or_404(ServicePackage, name=package_name) if package_name else None

    if request.method == 'POST':
        form = LeasingContractForm(request.POST, car=car, package=package)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if car.is_available(start_date, end_date):
                contract = form.save(commit=False)
                contract.user = request.user
                contract.car = car
                contract.total_price = contract.service_package.price * ((contract.end_date - contract.start_date).days // 30)
                contract.monthly_payment = contract.total_price / ((contract.end_date - contract.start_date).days // 30)
                contract.save()
                return redirect('leasing:success')  # Замініть на вашу фактичну URL-адресу успіху
            else:
                form.add_error(None, 'Цей автомобіль недоступний на обраний період.')
    else:
        form = LeasingContractForm(car=car, package=package)

    return render(request, 'create_contract.html', {'form': form, 'car': car})


def success(request):
    return render(request, 'success.html')