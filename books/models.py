from django.core.validators import MinValueValidator
from django.db import models

from borrowings.models import Borrowing


class Book(models.Model):
    class Cover(models.TextChoices):
        HARD = "HARD"
        SOFT = "SOFT"

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=4, choices=Cover.choices)
    inventory = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    daily_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.inventory} available)"


class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        PAID = "PAID"


    class Type(models.TextChoices):
        PAYMENT = "PAYMENT"
        FINE = "FINE"

    status = models.CharField(max_length=7, choices=Status.choices)
    type = models.CharField(max_length=7, choices=Type.choices)
    borrowing_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField()
    session_id = models.IntegerField(unique=True)
    money_to_pay = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return f"{self.money_to_pay} ({self.status})"
