from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Book
from books.serializers import BookSerializer

BOOK_URL = reverse("library:book-list")

def sample_book(**params):
    defaults = {
        "title": "Sample Book",
        "author": "sample",
        "cover": "HARD",
        "inventory": 5,
        "daily_fee": 1
    }
    defaults.update(params)

    return Book.objects.create(**defaults)

def detail_url(book_id):
    return reverse("library:book-detail", args=[book_id])


class AuthenticatedBookApiTEsts(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "user@test.com",
            "password123",
        )
        self.client.force_authenticate(self.user)

    def test_list_books(self):
        sample_book()
        sample_book()

        res = self.client.get(BOOK_URL)

        books = Book.objects.order_by("id")
        serializer = BookSerializer(books, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_book_detail(self):
        book = sample_book()

        url = detail_url(book.id)
        res = self.client.get(url)

        serializer = BookSerializer(book)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_book_forbidden(self):
        payload = {
            "title": "Sample Book",
            "author": "sample",
            "cover": "HARD",
            "inventory": 5,
            "daily_fee": 1
        }
        res = self.client.post(BOOK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)


class AdminBookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "admin@test.com"
            "password123",
            is_staff=True,
        )
        self.client.force_authenticate(self.user)

    def test_create_book_admin(self):
        payload = {
            "title": "Sample Book",
            "author": "sample",
            "cover": "HARD",
            "inventory": 5,
            "daily_fee": 1
        }
        res = self.client.post(BOOK_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        book = Book.objects.get(id=res.data["id"])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(book, key))
