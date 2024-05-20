from django.urls import path
from cars import views

app_name = 'cars'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.auto, name='auto'),
]