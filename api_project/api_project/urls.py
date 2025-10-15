
from django.contrib import admin
from django.urls import path
from api.urls import urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]

