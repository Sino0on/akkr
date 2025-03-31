# forms.py
from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'phone', 'message']
        labels = {
            'name': 'Имя',
            'email': 'Электронная почта',
            'phone': 'Телефон',
            'message': 'Сообщение',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ваша почта'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ваш номер телефона'}),
            'message': forms.Textarea(attrs={'placeholder': 'Ваше сообщение'}),
        }
