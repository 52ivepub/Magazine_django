from django import forms 
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from users.models import Users

class UserLoginForm(AuthenticationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True,
                                      'class': 'form-control',
                                      'placeholder': 'Введите имя пользователя'
                                                             }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 
                                        'class': 'form-control',
                                        'placeholder': 'Введите пароль'
                                          }),
    )
    class Meta:
        model = Users
        fields = ['username','password']