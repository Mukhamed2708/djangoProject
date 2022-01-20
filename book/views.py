from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from book import models, forms


def hello_world(request):
    return HttpResponse('Hello World')


def book_all(request):
    genres = models.Genre.objects.all()
    return render(request, 'genre_list.html', {'genres': genres})


def book_detail(request, id):
    genre = get_object_or_404(models.Genre, id=id)
    return render(request, 'book_detail.html',
                  {'genre': genre})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Book created')
    else:
        form = forms.BookForm()
    return render(request, 'add_book.html', {'form': form})


def book_update(request, id):
    book_object = get_object_or_404(models.Genre, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_object, data=request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Show Updated Successfully')
            return redirect(reverse("genres:genre_all"))
    else:
        form = forms.BookForm(instance=book_object)
    return render(request, 'book_update.html', {'form': form, 'object': book_object})


def book_delete(request, id):
    book_object = get_object_or_404(models.Genre, id=id)
    book_object.delete()
    return HttpResponse('Show Deleted')