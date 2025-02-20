import datetime
from django import forms
from .models import LeasingContract
from django.utils.translation import gettext_lazy as _

class LeasingContractForm(forms.ModelForm):
    class Meta:
        model = LeasingContract
        fields = ['start_date', 'end_date', 'service_package']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].required = True
        self.fields['end_date'].required = True
        self.fields['service_package'].required = True

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

