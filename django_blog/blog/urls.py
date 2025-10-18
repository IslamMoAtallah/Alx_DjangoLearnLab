from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),  # for password reset and other
    path('comment/<int:pk>/update/', include('blog.urls')),  # for comments
    path('comment/<int:pk>/delete/', include('blog.urls')),  # for comments
    path('comment/new/', include('blog.urls')),
    path('post/<int:pk>/comments/new/', include('blog.urls')),  # for comments# for comments
]






