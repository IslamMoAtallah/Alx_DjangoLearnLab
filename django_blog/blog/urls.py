from django.urls import path, include   
from django.conf import settings
from . import views
from . views import CustomLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]
