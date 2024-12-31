from django.shortcuts import render

from users.forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'Home - Авторизация',
        'form': form,
         
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Home - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Home - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {
        'title': 'Home - Выход'
    }
    return render(request, 'users/logout.html', context)


