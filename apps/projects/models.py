import uuid

from django.contrib.auth import get_user_model
from django.db import models

CustomUser = get_user_model()


class Project(models.Model):
    """
    stores a single project entry.
    has a many to one relationship to the user model.
    """

    class OpenForChoices(models.TextChoices):
        STUDY_PARTNERS = "ST", "Study Partners"
        PAIR_PROGRAMMING = "PP", "Pair Programming Partners"
        CODE_REVIEWERS = "CR", "Code Reviewers"
        CONTRIBUTORS = "CT", "Contributors"

    class TimeEstimateChoices(models.TextChoices):
        DAYS = "DY", "Days"
        WEEKS = "WK", "Weeks"
        MONTHS = "MT", "Months"
        YEARS = "YR", "Years"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="projects",
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    open_for = models.CharField(
        max_length=2,
        choices=OpenForChoices.choices,
        default=OpenForChoices.CONTRIBUTORS,
    )
    time_estimate = models.CharField(
        max_length=2,
        choices=TimeEstimateChoices.choices,
        default=TimeEstimateChoices.DAYS,
    )
    repo_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['-updated']),
        ]

    def __str__(self):
        return self.title
