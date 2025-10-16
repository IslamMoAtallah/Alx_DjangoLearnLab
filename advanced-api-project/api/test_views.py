from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.author = Author.objects.create(name='Ahmed Khaled')
        self.book = Book.objects.create(title='Python Basics', publication_year=2022, author=self.author)

      
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.id})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.id})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.id})

    def test_list_books(self):
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Python Basics', str(response.data))

    def test_retrieve_book_detail(self):
        
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Python Basics')

    def test_create_book_requires_authentication(self):
        
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        
        self.client.login(username='testuser', password='testpass')
        data = {
            'title': 'Updated Title',
            'publication_year': 2021,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    
    def test_delete_book_requires_authentication(self):
    
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
    
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_year(self):
        
        response = self.client.get(self.list_url, {'publication_year': 2022})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
       
        response = self.client.get(self.list_url, {'search': 'Python'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Python Basics', str(response.data))

    def test_order_books_by_title(self):
    
        Book.objects.create(title='A Book', publication_year=2020, author=self.author)
        Book.objects.create(title='Z Book', publication_year=2024, author=self.author)

        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))
