from django.db import models


class TVShow(models.Model):
    GENRE_CHOICE = (
        ('Detective', 'Detective'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romantic', 'Romantic'),
        ('Anime', 'Anime')
    )
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='', null=True)
    quantity = models.IntegerField(null=True)
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100, null=True)
    date_filmed = models.DateField(auto_now_add=True, null=True)
