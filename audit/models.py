from django.db import models
from django.contrib.auth.models import User


class AuditLog(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action = models.CharField(max_length=100)

    entity_name = models.CharField(max_length=100)

    record_id = models.CharField(
        max_length=100,
        blank=True
    )

    old_value = models.TextField(
        blank=True
    )

    new_value = models.TextField(
        blank=True
    )

    ip_address = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.action} - {self.entity_name}"