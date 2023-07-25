from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Status(models.TextChoices):
        STUDENT = "ST", "Student"
        HOBBYIST = "HB", "Hobbyist"
        PROFESSIONAL = "PR", "Professional"

    first_name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=150,
        blank=False,
        null=False,
    )
    bio = models.TextField(max_length=350)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.STUDENT,
    )
