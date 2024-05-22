from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('cars/', views.auto, name='auto'),
    path('catalog/cars/<str:car_code>/', views.auto, name='auto')

]