from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateInput, EmailInput, DateTimeInput, forms
from django import forms
from .models import Clients, Sotrudnik, Bank, Credit, Dolzhnost, Count


class ClientsForm(ModelForm):
    class Meta:
        model = Clients
        fields=['surname', 'name', 'data_birth', 'email']

        widgets={
            "surname": TextInput(attrs={
                'class': 'input'
            }),
            "name": TextInput(attrs={
                'class': 'input'
            }),
            "data_birth": DateInput(attrs={
                'class': 'input'
            }),
            "email": EmailInput(attrs={
                'class': 'input'
            })
        }

class SotrudnikiForm(ModelForm):
    class Meta:
        model = Sotrudnik
        fields = ['surname', 'name', 'data_birth', 'stazh']

        widgets = {
            "surname": TextInput(attrs={
                'class': 'input'
            }),
            "name": TextInput(attrs={
                'class': 'input'
            }),
            "data_birth": DateInput(attrs={
                'class': 'input'
            }),
            "stazh": TextInput(attrs={
                'class': 'input'
            })
        }

class PoseschenieForm(ModelForm):
    class Meta:
        model = Bank
        fields=['surname', 'name', 'date_and_time', 'service', 'sotrudnik']

        widgets={
            "surname": TextInput(attrs={
                'class':'input'
            }),
            "name": TextInput(attrs={
                'class': 'input'
            }),
            "date_and_time": DateTimeInput(attrs={
                'class': 'input'
            }),
            "service": TextInput(attrs={
                'class': 'input'
            }),
            "sotrudnik": TextInput(attrs={
                'class': 'input'
            })
        }

class CreditForm(ModelForm):
    class Meta:
        model = Credit
        fields = ['client', 'summa', 'procent', 'years']

        widgets = {
            "client": TextInput(attrs={
                'class': 'input'
            }),
            "summa": TextInput(attrs={
                'class': 'input'
            }),
            "procent": DateInput(attrs={
                'class': 'input'
            }),
            "years": TextInput(attrs={
                'class': 'input'
            })
        }


class CountForm(ModelForm):
    class Meta:
        model = Count
        fields = ['client', 'summa']

        widgets = {
            "client": TextInput(attrs={
                'class': 'input'
            }),
            "summa": TextInput(attrs={
                'class': 'input'
            })
        }

class DolzhnostForm(ModelForm):
    class Meta:
        model = Dolzhnost
        fields = ['name', 'sotrudnik']

        widgets = {
            "name": TextInput(attrs={
                'class': 'input'
            }),
            "sotrudnik": TextInput(attrs={
                'class': 'input'
            })
        }
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length = 50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', max_length = 50, widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', max_length = 50, widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-input'}),
            "password1": forms.PasswordInput(attrs={'class': 'form-input'}),
            "password2": forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=50, widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-input'}))