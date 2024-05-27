from django.utils.translation import gettext_lazy as _
from .models import ServicePackage, Service

def create_service_packages():
    # Create Basic Package
    basic_package = ServicePackage.objects.create(
        name=_("Standard Lease Package"),
        description=_("This package is ideal for customers who need a minimal set of services at a low monthly fee. It includes basic car maintenance and insurance."),
        price=400.00
    )
    basic_services = [
        _("Vehicle maintenance every 10,000 km or once a year, whichever comes first"),
        _("Compulsory Third Party Liability Insurance"),
        _("Oil and filter change"),
        _("24/7 roadside assistance (city towing)")
    ]
    for service in basic_services:
        Service.objects.create(package=basic_package, name=service, description=service)

    # Create Premium Package
    premium_package = ServicePackage.objects.create(
        name=_("Premium Lease Package"),
        description=_("This package provides a wider range of services for customers who want to use the car without worrying about its maintenance and repair. Includes insurance and additional services for convenience."),
        price=550.00
    )
    premium_services = [
        _("Brake pads and discs replacement if needed"),
        _("Tire change twice a year and storage"),
        _("Replacement car during repairs")
    ]
    # Include basic services in premium package
    for service in basic_package.services.all() + premium_services:
        Service.objects.create(package=premium_package, name=service.name, description=service.description)

    # Create Premium Plus Package
    premium_plus_package = ServicePackage.objects.create(
        name=_("Premium Plus Lease Package"),
        description=_("The maximum package of services for the most demanding customers. Includes a full range of maintenance and repair services, as well as additional privileges and services."),
        price=800.00
    )
    premium_plus_services = [
        _("Full check and maintenance of the air conditioning system"),
        _("Concierge service: car delivery for maintenance and return"),
        _("Documents for traveling abroad")
    ]
    # Include basic and premium services in premium plus package
    for service in basic_package.services.all() + premium_package.services.all() + premium_plus_services:
        Service.objects.create(package=premium_plus_package, name=service.name, description=service.description)


