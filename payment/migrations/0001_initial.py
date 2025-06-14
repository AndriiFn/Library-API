# Generated by Django 5.1 on 2025-06-07 07:32

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("borrowings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("PENDING", "Pending"), ("PAID", "Paid")], max_length=7
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("PAYMENT", "Payment"), ("FINE", "Fine")], max_length=7
                    ),
                ),
                ("session_url", models.URLField()),
                ("session_id", models.IntegerField(unique=True)),
                (
                    "money_to_pay",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[django.core.validators.MinValueValidator(0.01)],
                    ),
                ),
                (
                    "borrowing_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="borrowings.borrowing",
                    ),
                ),
            ],
        ),
    ]
