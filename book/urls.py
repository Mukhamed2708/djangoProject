from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello'),
    path('genres/', views.book_all, name='genres'),
    path('genres/<int:id>/update/', views.book_update, name='books_update'),
    path('genres/<int:id>/delete/', views.book_delete, name='books_delete'),
    path('genres/<int:id>/', views.book_detail, name='book_detail'),
    path('add-book/', views.add_book, name='add_book'),
]