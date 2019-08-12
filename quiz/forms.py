from django import forms

from .models import SensorData

class SensorForm(forms.ModelForm):
    class Meta:
        model = SensorData
        # fields = ('soilTemp', 'soilHumid', 'waterTemp', 'PH', 'voltage',)
        fields = ('AT', 'H', 'WT', 'PH', 'V',)
