import datetime

from rest_framework import serializers

from books.models import Book
from books.serializers import BookSerializer
from borrowings.models import Borrowing


class BorrowingSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = (
            "id",
            "borrow_date",
            "expected_return_date",
            "actual_return_date",
            "book",
            "user",
        )


class BorrowingCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Borrowing
        fields = ("id", "book", "expected_return_date")

    def validate(self, data):
        book = data.get("book")
        if not book:
            raise serializers.ValidationError("Please select a book")

        if book.inventory <= 0:
            raise serializers.ValidationError("This book isn't available.")
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        if not request:
            raise serializers.ValidationError("You need to specify a request")

        user = request.user
        book = validated_data.get("book")

        borrowing = Borrowing.objects.create(user=user, **validated_data)

        book.inventory -= 1
        book.save()

        return borrowing


class BorrowingReturnSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Borrowing
        fields = ("id", "book", "actual_return_date")

    def validate_return_date(self, value):
        today = datetime.date.today()
        if value < today:
            raise serializers.ValidationError("Choose either today's date or future's date.")
        return value

    def update(self, instance, validated_data):
        instance.actual_return_date = validated_data["actual_return_date"]
        instance.save()

        instance.check_return_date()
        instance.delete()

        return instance
