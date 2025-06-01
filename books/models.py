from django.core.validators import MinValueValidator
from django.db import models

from borrowing.models import Borrowing


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(
        max_length=4,
        choices=[("Hard", "Hard"), ("Soft", "Soft")]
    )
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.inventory} available)"


class Payment(models.Model):
    status = models.CharField(
        max_length=7,
        choices=[("pending", "pending"), ("paid", "paid")]
    )
    type = models.CharField(
        max_length=7,
        choices=[("payment", "payment"), ("fine", "fine")]
    )
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
