import datetime

from django.db import models

from library_practice import settings


class Borrowing(models.Model):
    borrow_date = models.DateField(auto_now=True)
    expected_return_date = models.DateField()
    actual_return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def check_return_date(self):
        if self.actual_return_date == datetime.date.today():
            self.book.inventory += 1
            self.book.save()

    def __str__(self):
        return f"{self.user} borrowed {self.book} ({self.expected_return_date})"
