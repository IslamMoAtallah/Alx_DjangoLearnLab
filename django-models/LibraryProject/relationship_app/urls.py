from django.urls import path 
from . import views
from .views import list_books, LibraryDetailView
urlpatterns = [
    path(LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path(LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
]
    



