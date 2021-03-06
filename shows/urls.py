from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('shows/', views.shows_all, name='shows_all'),
    path('shows/<int:id>/', views.shows_detail, name='shows_detail'),
    path('shows/<int:id>/update/', views.show_update, name='shows_update'),
    path('shows/<int:id>/delete/', views.show_delete, name='shows_delete'),
    path('add-shows/', views.add_show, name='add_shows'),
]
