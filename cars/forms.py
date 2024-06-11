from django import forms
from cars.models import Car

class CarSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Name')
    fuel_type = forms.ChoiceField(choices=[('', 'Any')] + Car.FUEL_TYPES, required=False, label='Fuel Type')
    transmission = forms.ChoiceField(choices=[('', 'Any')] + Car.TRANSMISSION_TYPES, required=False, label='Transmission')
    drive_type = forms.ChoiceField(choices=[('', 'Any')] + Car.DRIVE_TYPES, required=False, label='Drive Type')
    color = forms.ChoiceField(choices=[('', 'Any')] + Car.COLORS, required=False, label='Color')
    min_price = forms.DecimalField(required=False, min_value=0, label='Min Price')
    max_price = forms.DecimalField(required=False, min_value=0, label='Max Price')

