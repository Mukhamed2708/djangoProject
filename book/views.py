from django.http import HttpResponse
from django.shortcuts import render
from . import models


def hello_world(request):
    return HttpResponse('Hello World')


def book_all(request):
    genre = models.Genre.objects.all()
    return render(request, 'genre_list.html', {'genre': genre})