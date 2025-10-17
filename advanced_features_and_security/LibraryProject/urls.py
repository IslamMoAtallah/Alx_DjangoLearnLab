from django.contrib import admin
from django.urls import path , include
from relationship_app import views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.list_books, name='home'),
        path('', include('relationship_app.urls')),
        # path('library/<int:pk>/', include('LibraryProject.urls')),
        
]