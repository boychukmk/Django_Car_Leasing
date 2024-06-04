import datetime
from django.utils.translation import gettext_lazy as _
# from .models import LeasingContract, ServicePackage
# # class LeasingContractForm(forms.ModelForm):
# #     class Meta:
# #         model = LeasingContract
# #         fields = ['user', 'car', 'start_date', 'end_date', 'service_package', 'total_price', 'monthly_payment']
#
# class LeasingContractForm(forms.ModelForm):
#     car_info = forms.CharField(label=_("Selected Car"), required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#     package_info = forms.CharField(label=_("Selected Package"), required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
#
#     class Meta:
#         model = LeasingContract
#         fields = ['start_date', 'end_date', 'service_package']
#
#     def clean_start_date(self):
#         start_date = self.cleaned_data.get('start_date')
#         if start_date <= datetime.date.today():
#             raise forms.ValidationError(_("Start date must be from tomorrow onwards."))
#         return start_date
#
#     def clean_end_date(self):
#         end_date = self.cleaned_data.get('end_date')
#         start_date = self.cleaned_data.get('start_date')
#
#         if end_date is None:
#             raise forms.ValidationError(_("End date cannot be empty."))
#         if start_date is None:
#             raise forms.ValidationError(_("Start date cannot be empty."))
#
#         if end_date <= start_date + datetime.timedelta(days=30):
#             raise forms.ValidationError(_("End date must be at least 30 days ahead of start date."))
#         return end_date
#
#     def clean_service_package(self):
#         service_package = self.cleaned_data.get('service_package')
#         if not service_package:
#             raise forms.ValidationError(_("Please select a service package."))
#         return service_package
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['start_date'].widget.attrs.update({'type': 'date'})
#         self.fields['end_date'].widget.attrs.update({'type': 'date'})
#         self.fields['service_package'].widget = forms.Select(choices=[(package.pk, package.name) for package in ServicePackage.objects.all()])
#
#         # Add buttons for car and package details
#         self.fields['car_info'].widget.attrs.update({'class': 'form-control', 'onclick': 'show_car_details()'})
#         self.fields['package_info'].widget.attrs.update({'class': 'form-control', 'onclick': 'show_package_details()'})


# Форма
from django import forms
from .models import LeasingContract

class LeasingContractForm(forms.ModelForm):
    car_info = forms.CharField(label=_("Selected Car"), required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    package_info = forms.CharField(label=_("Selected Package"), required=True, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = LeasingContract
        fields = ['start_date', 'end_date', 'service_package']

    def __init__(self, *args, car=None, package=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({'type': 'date'})
        self.fields['end_date'].widget.attrs.update({'type': 'date'})
        if car:
            self.fields['car_info'].initial = \
                f"{car.name}, Price: {car.price}, Year: {car.year}, Fuel Type: {car.get_fuel_type_display()}," \
                f" Transmission: {car.get_transmission_display()}, Mileage: {car.mileage}, " \
                f"Drive Type: {car.get_drive_type_display()}, Color: {car.get_color_display()}, " \
                f"Engine Capacity: {car.engine_capacity}L"
            self.fields['car_info'].widget.attrs.update({'class': 'form-control col-md-7'})

        if package:
            self.fields['package_info'].initial = f"{package.name}: {package.description}, Price: {package.price}"

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date <= datetime.date.today():
            raise forms.ValidationError(_("Start date must be from tomorrow onwards."))
        return start_date

    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        start_date = self.cleaned_data.get('start_date')

        if end_date is None:
            raise forms.ValidationError(_("End date cannot be empty."))
        if start_date is None:
            raise forms.ValidationError(_("Start date cannot be empty."))

        if end_date <= start_date + datetime.timedelta(days=30):
            raise forms.ValidationError(_("End date must be at least 30 days ahead of start date."))
        return end_date

    def clean_service_package(self):
        service_package = self.cleaned_data.get('service_package')
        if not service_package:
            raise forms.ValidationError(_("Please select a service package."))
        return service_package
