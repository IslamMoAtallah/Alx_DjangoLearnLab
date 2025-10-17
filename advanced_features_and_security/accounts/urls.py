from django.urls import path
from .views import RegisterView, login_view, ProfileView, follow_toggle
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login_view, name='login'),  # returns token + user
    # you could also expose /api-token-auth/ using DRF's built-in view:
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/<str:username>/follow/', follow_toggle, name='follow-toggle'),
]
