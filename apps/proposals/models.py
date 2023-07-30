from django.contrib.auth import get_user_model
from django.db import models

from apps.projects.models import Project

CustomUser = get_user_model()


class Proposal(models.Model):
    """
    Stores a single entry of a proposl
    Has a many to one relationships with CustomUser and Project
    """

    sender = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="proposals_sent",
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

    @property
    def owner(self):
        # This exist so we can use OwnerRequiredMixin
        # for views that lets users manage proposals they receive
        return self.project.owner
