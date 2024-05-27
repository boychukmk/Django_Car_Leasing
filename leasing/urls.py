from django.urls import path
from . import views

app_name = 'leasing'

urlpatterns = [
    path('legalentities/', views.legalentities, name='legalentities'),
    path('individual/', views.individuals, name='individuals'),
    path('contract/<str:car_code>/', views.create_contract, name='create_contract'),
    path('contract/success', views.success, name='success'),
]
