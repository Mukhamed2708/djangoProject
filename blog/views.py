from django.http import HttpResponse
from django.shortcuts import render
from . import models

def hello_world(request):
    return HttpResponse('Hello World')


def blog_all(reqeuest):
    post = models.Post.objects.all()
    return render(reqeuest, 'post_list.html', {'post': post})
