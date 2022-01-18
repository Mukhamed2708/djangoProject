from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('genres/', views.book_all, name='genres'),
    path('genres/<int:id>/', views.book_detail, name='book_detail'),
    path('add-book/', views.add_book, name='add_book'),
]