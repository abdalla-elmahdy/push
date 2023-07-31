from django import forms

from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "title",
            "open_for",
            "time_estimate",
            "description",
            "repo_url",
        )
