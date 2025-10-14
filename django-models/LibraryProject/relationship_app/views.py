from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Book 
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from .forms import BookForm


# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
"relationship_app/library_detail.html"
# Function-Based View
"relationship_app/list_books.html"
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})
# Create new user
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('book_list')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})
#logout user
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



