from django.core.validators import MinValueValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=10,
        choices=[("Hard", "Soft")]
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


class Payment(models.Model):
    status = models.CharField()
    type = models.CharField()
    borrowing_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField()
    session_id = models.IntegerField(unique=True)
    money_to_pay = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
