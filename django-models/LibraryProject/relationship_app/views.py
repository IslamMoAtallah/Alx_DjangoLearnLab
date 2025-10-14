from django.shortcuts import render , get_object_or_404
from .models import Book
from .models import Library
from django.views.generic import DetailView

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
# Function-Based View
def list_books(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})