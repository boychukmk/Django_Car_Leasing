from django.utils import timezone
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from leasing.models import LeasingContract
from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы вошли в аккаунт")

                if request.POST.get('next', None):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Ви успішно створили аккаунт")
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Home - Регістрація',
        'form': form
    }
    return render(request, 'users/registration.html', context)

# @login_required
# def profile(request):
#
#     context = {
#         'title': 'Home - Кабинет',
#         'form': form
#     }
#     return render(request, 'users/profile.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Профіль успішно оновлено")
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    user = request.user
    contracts = LeasingContract.objects.filter(user=user)

    today_date = timezone.now().date()
    monthly_payments = []
    for contract in contracts:
        end_date = contract.end_date
        start_date = contract.start_date
        days_difference = (end_date - start_date).days
        monthly_payment = contract.total_price / Decimal(days_difference / 30)
        if start_date > today_date:
            payment_info = {
                'contract': contract,
                'message': f"Перша оплата: {start_date} - {round(monthly_payment, 2)} $"
            }
        else:
            payment_info = {
                'contract': contract,
                'message': f"Сума до сплати за цей місяць: {round(monthly_payment, 2)} $"
            }
        monthly_payments.append(payment_info)
        contract.monthly_payment = round(monthly_payment, 2)  # Add this field to pass to the template


    context = {
            'user': user,
            'contracts': contracts,
            'monthly_payments': monthly_payments,
            'today_date': today_date,
            'form': form
        }

    return render(request, 'users/profile.html', context)
@login_required
def logout(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('catalog:index'))