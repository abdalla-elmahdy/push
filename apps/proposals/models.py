from django.contrib.auth import get_user_model
from django.db import models

from apps.projects.models import Project

CustomUser = get_user_model()


class Proposal(models.Model):
    """ """

    sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="proposals_sent",
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="proposals_received",
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="proposals",
    )
    motive = models.TextField(max_length=350)
    skillset = models.TextField(max_length=350)
    created = models.DateTimeField(auto_now_add=True)
    contact_details = models.TextField(max_length=200)

    class Meta:
        ordering = ["-created"]
