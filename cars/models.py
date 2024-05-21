from django.db import models
from django.utils.text import slugify

class Car(models.Model):
    FUEL_TYPES = [
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
        ('hybrid', 'Hybrid'),
    ]

    TRANSMISSION_TYPES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('semi-automatic', 'Semi-Automatic'),
    ]

    DRIVE_TYPES = [
        ('fwd', 'Front-Wheel Drive'),
        ('rwd', 'Rear-Wheel Drive'),
        ('awd', 'All-Wheel Drive'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField()
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, help_text="Обʼєм двигуна в літрах")
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    transmission = models.CharField(max_length=15, choices=TRANSMISSION_TYPES)
    mileage = models.PositiveIntegerField(help_text="Пробіг у кілометрах")
    drive_type = models.CharField(max_length=10, choices=DRIVE_TYPES)
    color = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} ({self.year})'

    class Meta:
        verbose_name = "Авто"
        verbose_name_plural = "Автомобілі"

