
# Create your tests here.

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser1", password="password123")
        # Create an author
        self.author = Author.objects.create(name="Test Author")
        # Create some books
        self.book1 = Book.objects.create(title="Book 1", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book 2", publication_year=2021, author=self.author)
        # Authentication token
        self.client.login(username="testuser1", password="password123")

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_retrieve_book(self):
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book 1")

    def test_update_book(self):
        data = {
            "title": "Updated Book 1",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.put(f'/api/books/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book 1")

    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get('/api/books/?title=Book 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book 1")

    def test_order_books_by_publication_year(self):
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.post('/api/books/', {"title": "Unauthorized"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

