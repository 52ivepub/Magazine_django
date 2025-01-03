from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from users.models import Users

class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        label = 'Имя',
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите имя пользователя'
                                                             }))
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 
                                        'class': 'form-control',
                                        'placeholder': 'Введите пароль'
                                          }),
    )
    class Meta:
        model = Users
        fields = ['username','password']