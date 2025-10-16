from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, default='untitled' )
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200 )
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='books')
    publication_year = models.IntegerField(null=True, blank=True)
    def __str__(self):
     return self.title
   
   


# Create your models here.
