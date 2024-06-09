from django.urls import path, include
from cars import views

app_name = 'cars'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('page/<int:page>/', views.catalog, name='index'),
    path('search/', views.catalog, name='search'),
    path('cars/', views.auto, name='auto'),
    path('cars/<str:car_code>/', views.auto, name='auto'),

]