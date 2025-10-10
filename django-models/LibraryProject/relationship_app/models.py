from django.db import models
from django.apps import AppConfig 
class relationshipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship'
class Author(models.Model):
    name = models.CharField(max_length=100, default='untitled' )
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100, default='Untitled book' )
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    def __str__(self):
        return self.title
class librarian(models.Model):
    name = models.CharField(max_length=100, default='unnamed librarian')
    library = models.OneToOneField('library', on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name
class library(models.Model):
    name = models.CharField(max_length=100, default='untitled')
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)
    def __str__(self):
        return self.name


# Create your models here.

# Create your models here.

