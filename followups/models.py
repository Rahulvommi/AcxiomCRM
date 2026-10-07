from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from leads.models import Lead
from opportunities.models import Opportunity


class FollowUp(models.Model):

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Completed', 'Completed'),
        ('Missed', 'Missed'),
        ('Cancelled', 'Cancelled'),
    ]

    TYPE_CHOICES = [
        ('Call', 'Call'),
        ('Email', 'Email'),
        ('Meeting', 'Meeting'),
        ('Other', 'Other'),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='followups'
    )

    lead = models.ForeignKey(
        Lead,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='followups'
    )

    opportunity = models.ForeignKey(
        Opportunity,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='followups'
    )

    date = models.DateField()

    subject = models.CharField(max_length=150)

    type = models.CharField(
        max_length=30,
        choices=TYPE_CHOICES,
        default='Call'
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Planned'
    )

    notes = models.TextField(blank=True)

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_followups'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject