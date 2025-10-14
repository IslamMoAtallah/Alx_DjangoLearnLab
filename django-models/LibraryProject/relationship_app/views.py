from django.shortcuts import render , get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Class-Based View
"relationship_app/library_detail.html"
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
# Function-Based View
"relationship_app/list_books.html"
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
