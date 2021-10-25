from django.shortcuts import render

from store.models import Category, Product


def index(request):
    context = {
        'title': 'Добро пожаловать!',
        'products': Product.objects.all(),
    }
    return render(request, 'index.html', context)
