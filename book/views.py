from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models


def hello_world(request):
    return HttpResponse('Hello World')


def book_all(request):
    genre = models.Genre.objects.all()
    return render(request, 'genre_list.html', {'genre': genre})


def book_detail(request, id):
    show = get_object_or_404(models.Book, id=id)
    return render(request, 'book.detail.html',
                  {'book': book})