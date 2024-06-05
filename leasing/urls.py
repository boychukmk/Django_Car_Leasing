from django.urls import path
from . import views

app_name = 'leasing'

urlpatterns = [
    path('legalentities/', views.legalentities, name='legalentities'),
    path('individual/', views.individuals, name='individuals'),
    path('contract/<str:car_code>/', views.create_contract, name='create_contract'),
    path('get-package-details/<str:package_name>/', views.get_package_details, name='get_package_details'),
    path('contract/success', views.success, name='success'),
    path('services/', views.leasing_services, name='leasing_services'),
]
