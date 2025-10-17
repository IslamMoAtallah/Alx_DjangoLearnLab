from django.db import models
from django.apps import AppConfig 
class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    published_date = models.DateField()

    def __str__(self):
        return self.title
# Create your models here.

