import datetime
import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from books.models import Book
from borrowings.models import Borrowing
from borrowings.serializer import BorrowingSerializer


BORROWING_URL = reverse("borrowings:borrowings-list")

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


def sample_borrowing(user=None, **params):
    book = sample_book()

    if user is None:
        user = get_user_model().objects.create_user(
            f"user1@{uuid.uuid4()}test.com",
            "password123",
        )

    defaults = {
        "borrow_date": datetime.date.today(),
        "expected_return_date": datetime.date.today(),
        "actual_return_date": None,
        "book": book,
        "user": user,
    }
    defaults.update(params)

    return Borrowing.objects.create(**defaults)

def detail_url(borrowing_id):
    return reverse("library:borrowing-detail", args=[borrowing_id])


class UnauthenticatedBorrowingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(BORROWING_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthenticatedBorrowingApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            f"user1415{uuid.uuid4()}@test.com",
            "password123",
        )
        self.client.force_authenticate(self.user)

    def test_list_borrowings(self):
        sample_borrowing(user=self.user)
        sample_borrowing(user=self.user)

        res = self.client.get(BORROWING_URL)

        borrowings = Borrowing.objects.order_by("id")
        serializer = BorrowingSerializer(borrowings, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
