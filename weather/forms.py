from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import City, TemperatureRecord


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        labels = {
            'name': 'Название города'
        }


class TemperatureRecordForm(forms.ModelForm):
    date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = TemperatureRecord
        fields = ['date', 'temperature_c']
        labels = {
            'date': 'Дата',
            'temperature_c': 'Температура'
        }