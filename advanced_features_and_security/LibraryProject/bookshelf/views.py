from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all()
    return HttpResponse("Hello,World From Views, welcome to the Bookshelf app!")
    # return render(request, 'bookshelf/index.html', {'books': books}),  
