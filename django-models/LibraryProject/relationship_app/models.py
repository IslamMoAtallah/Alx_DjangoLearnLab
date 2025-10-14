from django.db import models
from django.apps import AppConfig 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class RelationshipConfig(AppConfig):
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
class Librarian(models.Model):
    name = models.CharField(max_length=100, default='unnamed librarian')
    library = models.OneToOneField('library', on_delete=models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=100, default='untitled')
    books = models.ManyToManyField(Book, related_name='libraries', blank=True)
    def __str__(self):
        return self.name
class UserProfile(models.Model):
    ROLE_CHOICES = [ 
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')  
    def __str__(self):
        return f"{self.user.username} - {self.role}"
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else :
        instance.userprofile.save()



# Create your models here.

# Create your models here.



