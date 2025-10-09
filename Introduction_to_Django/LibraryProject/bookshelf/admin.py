from .models import Book
from django.contrib import admin
admin.ModelAdmin
list_filter = ('author', 'publication_year')
search_fields = ('title', 'author')
admin.site.register(Book)



# Register your models here.


