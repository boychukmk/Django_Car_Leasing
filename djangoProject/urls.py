from django.urls import path, include
from django.views.generic import RedirectView

from django.views.i18n import set_language

urlpatterns = [
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('cars.urls', namespace='catalog')),
    path('set-language/', set_language, name='set_language'),  # URL для переключения языка
    # Другие URL-адреса вашего приложения...
]

