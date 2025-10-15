from django.shortcuts import render
from rest_framework import generics
from api.models import Book
from api.serializers import BookSerializer
class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create your views here.
