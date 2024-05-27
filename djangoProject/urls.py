from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib import admin
from django.views.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('cars.urls', namespace='catalog')),
    path('leasing/', include('leasing.urls', namespace='leasing')),
    path('set-language/', set_language, name='set_language'),
    path('accounts/', include('django.contrib.auth.urls')),  # Додано для аутентифікації

]

