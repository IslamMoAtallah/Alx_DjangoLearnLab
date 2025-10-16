from django.shortcuts import render

from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # بس الادمن يقدر يعمل CRUD

from rest_framework import generics
from api.models import Book

# Create your views here.

