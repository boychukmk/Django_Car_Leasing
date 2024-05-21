import os
import django

# Налаштування Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

from cars.models import Car

# Перелік автомобілів
cars = [
    {
        "name": "Toyota Camry",
        "price": 25000.00,
        "year": 2021,
        "engine_capacity": 2.5,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 5000,
        "drive_type": "fwd",
        "color": "white",
        "code": "TOYCAM2021",
        "slug": "toyota-camry"
    },
    {
        "name": "Honda Accord",
        "price": 24000.00,
        "year": 2020,
        "engine_capacity": 1.5,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 8000,
        "drive_type": "fwd",
        "color": "black",
        "code": "HONACC2020",
        "slug": "honda-accord"
    },
    {
        "name": "BMW 3 Series",
        "price": 35000.00,
        "year": 2019,
        "engine_capacity": 2.0,
        "fuel_type": "diesel",
        "transmission": "automatic",
        "mileage": 12000,
        "drive_type": "rwd",
        "color": "blue",
        "code": "BMW32019",
        "slug": "bmw-3-series"
    },
    {
        "name": "Audi A4",
        "price": 37000.00,
        "year": 2021,
        "engine_capacity": 2.0,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 7000,
        "drive_type": "awd",
        "color": "red",
        "code": "AUDI42021",
        "slug": "audi-a4"
    },
    {
        "name": "Mercedes-Benz C-Class",
        "price": 40000.00,
        "year": 2021,
        "engine_capacity": 2.0,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 6000,
        "drive_type": "rwd",
        "color": "silver",
        "code": "MBCC2021",
        "slug": "mercedes-benz-c-class"
    },
    {
        "name": "Ford Focus",
        "price": 20000.00,
        "year": 2018,
        "engine_capacity": 1.5,
        "fuel_type": "petrol",
        "transmission": "manual",
        "mileage": 30000,
        "drive_type": "fwd",
        "color": "grey",
        "code": "FORFOC2018",
        "slug": "ford-focus"
    },
    {
        "name": "Chevrolet Malibu",
        "price": 22000.00,
        "year": 2019,
        "engine_capacity": 1.5,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 25000,
        "drive_type": "fwd",
        "color": "black",
        "code": "CHEMAL2019",
        "slug": "chevrolet-malibu"
    },
    {
        "name": "Nissan Altima",
        "price": 23000.00,
        "year": 2020,
        "engine_capacity": 2.5,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 15000,
        "drive_type": "fwd",
        "color": "white",
        "code": "NISALT2020",
        "slug": "nissan-altima"
    },
    {
        "name": "Subaru Impreza",
        "price": 21000.00,
        "year": 2021,
        "engine_capacity": 2.0,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 10000,
        "drive_type": "awd",
        "color": "blue",
        "code": "SUBIMP2021",
        "slug": "subaru-impreza"
    },
    {
        "name": "Volkswagen Passat",
        "price": 27000.00,
        "year": 2021,
        "engine_capacity": 2.0,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 5000,
        "drive_type": "fwd",
        "color": "silver",
        "code": "VWPS2021",
        "slug": "volkswagen-passat"
    },
    {
        "name": "Hyundai Sonata",
        "price": 24000.00,
        "year": 2020,
        "engine_capacity": 2.0,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 12000,
        "drive_type": "fwd",
        "color": "red",
        "code": "HYUSON2020",
        "slug": "hyundai-sonata"
    },
    {
        "name": "Kia Optima",
        "price": 23000.00,
        "year": 2019,
        "engine_capacity": 2.4,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 20000,
        "drive_type": "fwd",
        "color": "white",
        "code": "KIAOPT2019",
        "slug": "kia-optima"
    },
    {
        "name": "Mazda 6",
        "price": 26000.00,
        "year": 2021,
        "engine_capacity": 2.5,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 7000,
        "drive_type": "fwd",
        "color": "grey",
        "code": "MAZ62021",
        "slug": "mazda-6"
    },
    {
        "name": "Lexus ES",
        "price": 42000.00,
        "year": 2020,
        "engine_capacity": 3.5,
        "fuel_type": "petrol",
        "transmission": "automatic",
        "mileage": 10000,
        "drive_type": "fwd",
        "color": "black",
        "code": "LEXES2020",
        "slug": "lexus-es"
    },
    {
        "name": "Tesla Model 3",
        "price": 45000.00,
        "year": 2021,
        "engine_capacity": 0.0,
        "fuel_type": "electric",
        "transmission": "automatic",
        "mileage": 5000,
        "drive_type": "awd",
        "color": "white",
        "code": "TESM32021",
        "slug": "tesla-model-3"
    }
]

# Додавання автомобілів до бази даних
for car_data in cars:
    car = Car(**car_data)
    car.save()

print("Автомобілі успішно додані до бази даних.")
