from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories



def index(request):

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели Home',

    }
    return render(request, 'main/index.html', context)


def  about(request):
    context = {
        'title': 'Home - О Нас',
        'content': 'О нас',
        'text_on_page': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Tenetur corrupti minus inventore sed, debitis a libero, reprehenderit, quam corporis nisi ipsa culpa dolores tempore ad adipisci sit facilis magni est.',

    }
    return render(request, 'main/about.html', context)



