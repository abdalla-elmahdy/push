from django.contrib.auth import get_user_model
from django.db import models

from apps.projects.models import Project

CustomUser = get_user_model()


class Favorite(models.Model):
    """
    Stores a single Favorite entry.
    Has a many to one relationships with CustomUser and Project models
    """

    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
