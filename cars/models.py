from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Car(models.Model):
    FUEL_TYPES = [
        ('petrol', _('Petrol')),
        ('diesel', _('Diesel')),
        ('electric', _('Electric')),
        ('hybrid', _('Hybrid')),
    ]

    TRANSMISSION_TYPES = [
        ('manual', _('Manual')),
        ('automatic', _('Automatic')),
        ('semi-automatic', _('Semi-Automatic')),
    ]

    DRIVE_TYPES = [
        ('fwd', _('Front-Wheel Drive')),
        ('rwd', _('Rear-Wheel Drive')),
        ('awd', _('All-Wheel Drive')),
    ]

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    year = models.PositiveIntegerField(verbose_name=_("Year"))
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, verbose_name=_("Engine Capacity"), help_text=_("Engine capacity in liters"))
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES, verbose_name=_("Fuel Type"))
    transmission = models.CharField(max_length=15, choices=TRANSMISSION_TYPES, verbose_name=_("Transmission"))
    mileage = models.PositiveIntegerField(verbose_name=_("Mileage"), help_text=_("Mileage in kilometers"))
    drive_type = models.CharField(max_length=10, choices=DRIVE_TYPES, verbose_name=_("Drive Type"))
    color = models.CharField(max_length=50, verbose_name=_("Color"))
    code = models.CharField(max_length=50, unique=True, verbose_name=_("Code"))
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True, verbose_name=_("Photo"))
    slug = models.SlugField(unique=True, blank=True, verbose_name=_("Slug"))

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.year})'

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")


