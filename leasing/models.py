from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from cars.models import Car

class ServicePackage(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        previous_package = ServicePackage.objects.filter(pk__lt=self.pk).order_by('-pk').first()
        if previous_package:
            for service in previous_package.services.all():
                self.services.add(service)


class Service(models.Model):
    package = models.ForeignKey(ServicePackage, on_delete=models.CASCADE, related_name='services', verbose_name=_("Package"))
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.name


class LeasingContract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("User"))
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name=_("Car"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    service_package = models.ForeignKey(ServicePackage, on_delete=models.CASCADE, verbose_name=_("Service Package"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Monthly Payment"))

    def __str__(self):
        return f"{self.user} - {self.car.name} ({self.car.code})"

    class Meta:
        verbose_name = _("Leasing Contract")
        verbose_name_plural = _("Leasing Contracts")
