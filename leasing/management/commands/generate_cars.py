import os
import django
from django.core.files import File
from leasing.models import Service, ServicePackage
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Налаштування Django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
# settings.configure()
# django.setup()
# from cars.models import Car
#
# path = "/Users/boychukmaksim/Documents/Університет/3.2/курсова/cars/"
# # Перелік автомобілів
# cars = [
#     {
#         "name": "Toyota Camry",
#         "price": 25000.00,
#         "year": 2021,
#         "engine_capacity": 2.5,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 5000,
#         "drive_type": "fwd",
#         "color": "white",
#         "code": "TOYCAM2021",
#         "slug": "toyota-camry",
#         "photo_filename": "toyota-camry.jpeg"
#     },
#     {
#         "name": "Honda Accord",
#         "price": 24000.00,
#         "year": 2020,
#         "engine_capacity": 1.5,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 8000,
#         "drive_type": "fwd",
#         "color": "black",
#         "code": "HONACC2020",
#         "slug": "honda-accord",
#         "photo_filename": "honda-accord.jpeg"
#     },
#     {
#         "name": "BMW 3 Series",
#         "price": 35000.00,
#         "year": 2019,
#         "engine_capacity": 2.0,
#         "fuel_type": "diesel",
#         "transmission": "automatic",
#         "mileage": 12000,
#         "drive_type": "rwd",
#         "color": "blue",
#         "code": "BMW32019",
#         "slug": "bmw-3-series",
#         "photo_filename": "bmw-3-series.jpeg"
#     },
#     {
#         "name": "Audi A4",
#         "price": 37000.00,
#         "year": 2021,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 7000,
#         "drive_type": "awd",
#         "color": "red",
#         "code": "AUDI42021",
#         "slug": "audi-a4",
#         "photo_filename": "audi-a4.jpeg"
#     },
#     {
#         "name": "Mercedes-Benz C-Class",
#         "price": 40000.00,
#         "year": 2021,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 6000,
#         "drive_type": "rwd",
#         "color": "silver",
#         "code": "MBCC2021",
#         "slug": "mercedes-benz-c-class",
#         "photo_filename": "mercedes-benz-c-class.jpeg"
#     },
#     {
#         "name": "Ford Focus",
#         "price": 20000.00,
#         "year": 2018,
#         "engine_capacity": 1.5,
#         "fuel_type": "petrol",
#         "transmission": "manual",
#         "mileage": 30000,
#         "drive_type": "fwd",
#         "color": "grey",
#         "code": "FORFOC2018",
#         "slug": "ford-focus",
#         "photo_filename": "ford-focus.jpeg"
#     },
#     {
#         "name": "Chevrolet Malibu",
#         "price": 22000.00,
#         "year": 2019,
#         "engine_capacity": 1.5,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 25000,
#         "drive_type": "fwd",
#         "color": "black",
#         "code": "CHEMAL2019",
#         "slug": "chevrolet-malibu",
#         "photo_filename": "chevrolet-malibu.jpeg"
#     },
#     {
#         "name": "Nissan Altima",
#         "price": 23000.00,
#         "year": 2020,
#         "engine_capacity": 2.5,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 15000,
#         "drive_type": "fwd",
#         "color": "white",
#         "code": "NISALT2020",
#         "slug": "nissan-altima",
#         "photo_filename": "nissan-altima.jpeg"
#     },
#     {
#         "name": "Subaru Impreza",
#         "price": 21000.00,
#         "year": 2021,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 10000,
#         "drive_type": "awd",
#         "color": "blue",
#         "code": "SUBIMP2021",
#         "slug": "subaru-impreza",
#         "photo_filename": "subaru-impreza.jpeg",
#         "discount": 9,
#     },
#     {
#         "name": "Volkswagen Passat",
#         "price": 27000.00,
#         "year": 2021,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 5000,
#         "drive_type": "fwd",
#         "color": "silver",
#         "code": "VWPS2021",
#         "slug": "volkswagen-passat",
#         "photo_filename": "volkswagen-passat.jpeg"
#     },
#     {
#         "name": "Hyundai Sonata",
#         "price": 24000.00,
#         "year": 2020,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 12000,
#         "drive_type": "fwd",
#         "color": "red",
#         "code": "HYNSON2020",
#         "slug": "hyundai-sonata",
#         "photo_filename": "hyundai-sonata.jpeg",
#         "discount": 5
#     },
#     {
#         "name": "Kia Optima",
#         "price": 23000.00,
#         "year": 2019,
#         "engine_capacity": 2.4,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 20000,
#         "drive_type": "fwd",
#         "color": "white",
#         "code": "KIAOPT2019",
#         "slug": "kia-optima",
#         "photo_filename": "kia-optima.jpeg"
#     },
#     {
#         "name": "Mazda 6",
#         "price": 26000.00,
#         "year": 2021,
#         "engine_capacity": 2.5,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 7000,
#         "drive_type": "fwd",
#         "color": "grey",
#         "code": "MAZ62021",
#         "slug": "mazda-6",
#         "photo_filename": "mazda-6.jpeg"
#     },
#     {
#         "name": "Lexus ES",
#         "price": 42000.00,
#         "year": 2020,
#         "engine_capacity": 3.5,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 10000,
#         "drive_type": "fwd",
#         "color": "black",
#         "code": "LEXES2020",
#         "slug": "lexus-es",
#         "photo_filename": "lexus-es.jpeg"
#     },
#     {
#         "name": "Tesla Model 3",
#         "price": 45000.00,
#         "year": 2021,
#         "engine_capacity": 0.0,
#         "fuel_type": "electric",
#         "transmission": "automatic",
#         "mileage": 5000,
#         "drive_type": "awd",
#         "color": "white",
#         "code": "TESM32021",
#         "slug": "tesla-model-3",
#         "photo_filename": "tesla-model-3.jpeg"
#     },
#     {
#         "name": "Volvo S60",
#         "price": 30000.00,
#         "year": 2022,
#         "engine_capacity": 2.0,
#         "fuel_type": "hybrid",
#         "transmission": "automatic",
#         "mileage": 4000,
#         "drive_type": "awd",
#         "color": "white",
#         "code": "VOLVS602022",
#         "slug": "volvo-s60",
#         "photo_filename": "volvo-s60.jpeg",
#         "discount": 10,
#     },
#     {
#         "name": "Jaguar XE",
#         "price": 35000.00,
#         "year": 2020,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 15000,
#         "drive_type": "awd",
#         "color": "black",
#         "code": "JAGXE2020",
#         "slug": "jaguar-xe",
#         "photo_filename": "jaguar-xe.jpeg",
#         "discount": 4,
#     },
#     {
#         "name": "Alfa Romeo Giulia",
#         "price": 37000.00,
#         "year": 2021,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 7000,
#         "drive_type": "rwd",
#         "color": "black",
#         "code": "ARGR2021",
#         "slug": "alfa-romeo-giulia",
#         "photo_filename": "alfa-romeo-giulia.jpeg"
#     },
#     {
#         "name": "Infiniti Q50",
#         "price": 38000.00,
#         "year": 2020,
#         "engine_capacity": 3.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 12000,
#         "drive_type": "awd",
#         "color": "white",
#         "code": "INQ502020",
#         "slug": "infiniti-q50",
#         "photo_filename": "infiniti-q50.jpeg",
#         "discount": 5,
#
#     },
#     {
#         "name": "Cadillac CT5",
#         "price": 42000.00,
#         "year": 2022,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 5000,
#         "drive_type": "rwd",
#         "color": "blue",
#         "code": "CADCT52022",
#         "slug": "cadillac-ct5",
#         "photo_filename": "cadillac-ct5.jpeg"
#     },
#     {
#         "name": "Genesis G70",
#         "price": 39000.00,
#         "year": 2021,
#         "engine_capacity": 3.3,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 10000,
#         "drive_type": "awd",
#         "color": "grey",
#         "code": "GENG702021",
#         "slug": "genesis-g70",
#         "photo_filename": "genesis-g70.jpeg"
#     },
#     {
#         "name": "Acura TLX",
#         "price": 36000.00,
#         "year": 2021,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 8000,
#         "drive_type": "awd",
#         "color": "black",
#         "code": "ACTLX2021",
#         "slug": "acura-tlx",
#         "photo_filename": "acura-tlx.jpeg"
#     },
#     {
#         "name": "Lincoln MKZ",
#         "price": 34000.00,
#         "year": 2020,
#         "engine_capacity": 2.0,
#         "fuel_type": "hybrid",
#         "transmission": "automatic",
#         "mileage": 9000,
#         "drive_type": "awd",
#         "color": "black",
#         "code": "LINMKZ2020",
#         "slug": "lincoln-mkz",
#         "photo_filename": "lincoln-mkz.jpeg"
#     },
#     {
#         "name": "Buick Regal",
#         "price": 31000.00,
#         "year": 2019,
#         "engine_capacity": 2.0,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 15000,
#         "drive_type": "fwd",
#         "color": "red",
#         "code": "BUIREG2019",
#         "slug": "buick-regal",
#         "photo_filename": "buick-regal.jpeg",
#         "discount": 6,
#     },
#     {
#         "name": "Chrysler 300",
#         "price": 35000.00,
#         "year": 2021,
#         "engine_capacity": 3.6,
#         "fuel_type": "petrol",
#         "transmission": "automatic",
#         "mileage": 11000,
#         "drive_type": "rwd",
#         "color": "black",
#         "code": "CHR3002021",
#         "slug": "chrysler-300",
#         "photo_filename": "chrysler-300.jpeg"
#     }
# ]
#
# # Додавання автомобілів до бази даних
# for car_data in cars:
#     photo_filename = car_data.pop('photo_filename', None)
#     car = Car(**car_data)
#     if photo_filename:
#         photo_path = os.path.join(path, photo_filename)
#         with open(photo_path, 'rb') as photo_file:
#             car.photo.save(photo_filename, File(photo_file), save=False)
#     car.save()
#
# print("Автомобілі успішно додані до бази даних.")
#



# Створення послуг
services_data = [
    {"name": "Car maintenance every 10,000 km or once a year", "description": "Regular car maintenance every 10,000 km or once a year, whichever comes first."},
    {"name": "OSAGO Insurance", "description": "Basic liability insurance."},
    {"name": "Full insurance (OSAGO + KASKO with zero deductible)", "description": "Full insurance without deductible."},
    {"name": "Oil and filter change", "description": "Changing the car's oil and filters."},
    {"name": "Brake pads and discs replacement as needed", "description": "Replacement of brake pads and discs as needed."},
    {"name": "Tire change twice a year and storage", "description": "Changing tires twice a year and storing them."},
    {"name": "Full check and maintenance of the air conditioning system", "description": "Full check and maintenance of the car's air conditioning system."},
    {"name": "24/7 Roadside assistance (city towing)", "description": "24/7 roadside assistance, including city towing."},
    {"name": "24/7 Roadside assistance (towing, tire change, fuel delivery)", "description": "24/7 roadside assistance, including towing, tire change, and fuel delivery."},
    {"name": "Provision of a replacement car during repair", "description": "Provision of a replacement car during the repair period."},
    {"name": "Concierge service: car delivery for maintenance and return", "description": "Concierge service: delivery of the car for maintenance and its return."},
    {"name": "Documents for traveling abroad", "description": "Documents necessary for traveling abroad by car."},
]

for data in services_data:
    service = Service.objects.create(name=data["name"], description=data["description"])
    service.save()

print("Послуги успішно додані до бази даних.")

# Створення та додавання пакетів послуг
service_packages_data = [
    {
        "name": "Standard Lease Package",
        "description": "This package is perfect for customers who need a minimal set of services at a low monthly fee. It includes basic car maintenance and insurance services.",
        "price": 450.00,
        "service_ids": [1, 2, 4, 7]  # Список ідентифікаторів послуг для цього пакету
    },
    {
        "name": "Premium Lease Package",
        "description": "This package offers a wider range of services for customers who want to use the car without worrying about its maintenance and repair. Includes insurance and additional convenience services.",
        "price": 600.00,
        "service_ids": [1, 3, 4, 5, 6, 8, 10]  # Список ідентифікаторів послуг для цього пакету
    },
    {
        "name": "Premium Plus Lease Package",
        "description": "The maximum service package for the most demanding customers. Includes a full range of car maintenance and repair services, as well as additional privileges and services.",
        "price": 800.00,
        "service_ids": list(range(1, len(services_data) + 1))  # Список ідентифікаторів всіх послуг
    },
]

for package_data in service_packages_data:
    package = ServicePackage.objects.create(
        name=package_data["name"],
        description=package_data["description"],
        price=package_data["price"]
    )
    package.services.add(*Service.objects.filter(pk__in=package_data["service_ids"]))
    package.save()

print("Пакети послуг успішно додані до бази даних.")

# # Описи для предметів Service
# services_data = [
#     (_("Car maintenance every 10,000 km or once a year"), _("Regular car maintenance every 10,000 km or once a year, whichever comes first.")),
#     (_("OSAGO Insurance"), _("Basic liability insurance.")),
#     (_("Full insurance (OSAGO + KASKO with zero deductible)"), _("Full insurance without deductible.")),
#     (_("Oil and filter change"), _("Changing the car's oil and filters.")),
#     (_("Brake pads and discs replacement as needed"), _("Replacement of brake pads and discs as needed.")),
#     (_("Tire change twice a year and storage"), _("Changing tires twice a year and storing them.")),
#     (_("Full check and maintenance of the air conditioning system"), _("Full check and maintenance of the car's air conditioning system.")),
#     (_("24/7 Roadside assistance (city towing)"), _("24/7 roadside assistance, including city towing.")),
#     (_("24/7 Roadside assistance (towing, tire change, fuel delivery)"), _("24/7 roadside assistance, including towing, tire change, and fuel delivery.")),
#     (_("Provision of a replacement car during repair"), _("Provision of a replacement car during the repair period.")),
#     (_("Concierge service: car delivery for maintenance and return"), _("Concierge service: delivery of the car for maintenance and its return.")),
#     (_("Documents for traveling abroad"), _("Documents necessary for traveling abroad by car.")),
# ]
#
# # Додавання предметів Service до бази даних
# for name, description in services_data:
#     service = Service.objects.create(name=name, description=description)
#     service.save()
#
# print(_("Предмети Service успішно додані до бази даних."))
#
# # Створення та додавання пакетів ServicePackage до бази даних
# standard_lease = ServicePackage.objects.create(
#     name=_("Standard Lease Package"),
#     description=_("This package is perfect for customers who need a minimal set of services at a low monthly fee. It includes basic car maintenance and insurance services."),
#     price=450.00
# )
# standard_lease.services.set(Service.objects.filter(name__in=[_("Car maintenance every 10,000 km or once a year"), _("OSAGO Insurance"), _("Oil and filter change"), _("24/7 Roadside assistance (city towing)")]))
# standard_lease.save()
#
# premium_lease = ServicePackage.objects.create(
#     name=_("Premium Lease Package"),
#     description=_("This package offers a wider range of services for customers who want to use the car without worrying about its maintenance and repair. Includes insurance and additional convenience services."),
#     price=600.00
# )
# premium_lease.services.set(Service.objects.filter(name__in=[_("Car maintenance every 10,000 km or once a year"), _("Full insurance (OSAGO + KASKO with zero deductible)"), _("Oil and filter change"), _("Brake pads and discs replacement as needed"), _("Tire change twice a year and storage"), _("24/7 Roadside assistance (towing, tire change, fuel delivery)"), _("Provision of a replacement car during repair")]))
# premium_lease.save()
#
# premium_plus_lease = ServicePackage.objects.create(
#     name=_("Premium Plus Lease Package"),
#     description=_("The maximum service package for the most demanding customers. Includes a full range of car maintenance and repair services, as well as additional privileges and services."),
#     price=800.00
# )
# premium_plus_lease.services.set(Service.objects.all())
# premium_plus_lease.save()
#
# print(_("Пакети ServicePackage успішно додані до бази даних."))

