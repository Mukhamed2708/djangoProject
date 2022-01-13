from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('genres/', views.book_all, name='genres'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
]