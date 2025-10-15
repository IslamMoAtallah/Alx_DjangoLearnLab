from django.shortcuts import render
from rest_framework import generics
from api.models import Book
from .serializers import BookSerializer
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
