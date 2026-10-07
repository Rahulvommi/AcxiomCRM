from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer


class Opportunity(models.Model):

    STAGE_CHOICES = [
        ('Qualification', 'Qualification'),
        ('Proposal', 'Proposal'),
        ('Negotiation', 'Negotiation'),
        ('Won', 'Won'),
        ('Lost', 'Lost'),
    ]

    name = models.CharField(max_length=150)

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='opportunities'
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='owned_opportunities'
    )

    stage = models.CharField(
        max_length=30,
        choices=STAGE_CHOICES,
        default='Qualification'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    probability = models.PositiveIntegerField(
        default=0
    )

    expected_close_date = models.DateField()

    source = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def weighted_value(self):
        return self.amount * self.probability / 100

    def __str__(self):
        return self.name