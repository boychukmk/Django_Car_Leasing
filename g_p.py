# Импортируем настройки Django
import os
import django

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ваш_проект.settings')

# Загружаем настройки Django
django.setup()

# Вставляем код для генерации базы данных
from leasing.models  import Service, ServicePackage

# Ваш скрипт для создания и заполнения базы данных


# # Створення послуг
# services_data = [
#     {"id": 1,"name": "Технічне обслуговування автомобіля кожні 10 000 км або раз на рік", "description": "Регулярне технічне обслуговування автомобіля кожні 10 000 км або раз на рік, залежно від того, що настане раніше."},
#     {"id": 2,"name": "Страхування ОСЦПВ", "description": "Основне страхування цивільної відповідальності."},
#     {"id": 3,"name": "Повне страхування (ОСЦПВ + КАСКО з нульовими франшизами)", "description": "Повне страхування без франшизи."},
#     {"id": 4,"name": "Заміна масла та фільтрів", "description": "Заміна масла та фільтрів автомобіля."},
#     {"id": 5,"name": "Заміна гальмівних колодок і дисків за потребою", "description": "Заміна гальмівних колодок і дисків за потребою."},
#     {"id": 6,"name": "Заміна шин двічі на рік та їх зберігання", "description": "Заміна шин двічі на рік та їх зберігання."},
#     {"id": 7,"name": "Повна перевірка та обслуговування системи кондиціонування повітря", "description": "Повна перевірка та обслуговування системи кондиціонування повітря в автомобілі."},
#     {"id": 8,"name": "Круглодобова допомога на дорогах (міське буксирування)", "description": "Круглодобова допомога на дорогах, включаючи міське буксирування."},
#     {"id": 9,"name": "Круглодобова допомога на дорогах (буксирування, заміна шин, доставка палива)", "description": "Круглодобова допомога на дорогах, включаючи буксирування, заміну шин та доставку палива."},
#     {"id": 10,"name": "Надання замінного автомобіля під час ремонту", "description": "Надання замінного автомобіля на час ремонту."},
#     {"id": 11,"name": "Консьєрж-сервіс: доставка автомобіля на обслуговування та повернення", "description": "Консьєрж-сервіс: доставка автомобіля на обслуговування та повернення його власнику."},
#     {"id": 12,"name": "Документи для поїздки за кордон", "description": "Документи, необхідні для поїздки за кордон на автомобілі."},
# ]
#
# # Створення послуг
# for data in services_data:
#     service = Service.objects.create(id=data["id"],name=data["name"], description=data["description"])
#     service.save()
#
# print("Послуги успішно додані до бази даних.")
service_packages_data = [
    {
        "name": "Base Leasing",
        "description": "Цей пакет ідеально підходить для клієнтів, яким потрібен мінімальний набір послуг за низькою щомісячною ставкою. Включає в себе основне технічне обслуговування автомобіля та страхові послуги.",
        "price": 450.00,
        "service_names": ["Технічне обслуговування автомобіля кожні 10 000 км або раз на рік", "Страхування ОСЦПВ", "Заміна масла та фільтрів", "Круглодобова допомога на дорогах (міське буксирування)"]
    },
    {
        "name": "Premium Leasing",
        "description": "Цей пакет пропонує більший спектр послуг для клієнтів, які хочуть користуватися автомобілем, не турбуючись про його технічне обслуговування та ремонт. Включає страхування та додаткові зручності.",
        "price": 600.00,
        "service_names": ["Технічне обслуговування автомобіля кожні 10 000 км або раз на рік", "Повне страхування (ОСЦПВ + КАСКО з нульовими франшизами)", "Заміна масла та фільтрів", "Заміна гальмівних колодок і дисків за потребою", "Заміна шин двічі на рік та їх зберігання", "Круглодобова допомога на дорогах (буксирування, заміна шин, доставка палива)", "Надання замінного автомобіля під час ремонту"]
    },
    {
        "name": "All in clusive",
        "description": "Максимальний пакет послуг для найвимогливіших клієнтів. Включає повний спектр технічного обслуговування та ремонту автомобіля, а також додаткові привілеї та послуги.",
        "price": 800.00,
        "service_names": ["Технічне обслуговування автомобіля кожні 10 000 км або раз на рік", "Страхування ОСЦПВ", "Повне страхування (ОСЦПВ + КАСКО з нульовими франшизами)"]
    },
]

# Запис об'єктів ServicePackage в базу даних
for package_data in service_packages_data:
    # Створення пакету послуг
    package = ServicePackage.objects.create(
        name=package_data["name"],
        description=package_data["description"],
        price=package_data["price"]
    )
    # Отримання послуг за їх назвами
    package_services = Service.objects.filter(name__in=package_data["service_names"])
    # Додавання отриманих послуг до пакету
    package.services.set(package_services)
    package.save()

print("Дані про пакети послуг успішно додано до бази даних.")



