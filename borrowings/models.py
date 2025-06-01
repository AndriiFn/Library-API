from django.db import models
from django.contrib.auth import get_user_model


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} borrowed {self.book} ({self.expected_return_date})"
