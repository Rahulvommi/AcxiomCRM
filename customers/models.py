from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20, unique=True)

    address = models.TextField(blank=True)

    status = models.CharField(
        max_length=30,
        default="Active"
    )

    assigned_sales_executive = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_customers"
    )

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name