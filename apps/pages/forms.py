from django import forms

from apps.projects.models import Project


class SearchForm(forms.Form):
    """
    Creates a form used to search for projects available
    Fields:
        - query: CharField submitted to target project
                title and description in the search view
        - open_for: ChoiceField that maps directly to
                    the open_for field in the Project model
        - time_estimate: ChoiceField that maps directly to
                    the time_estimate field in the Project model
    """

    query = forms.CharField(max_length=150, label='Search all projects')
    open_for = forms.ChoiceField(choices=Project.OpenForChoices.choices)
    time_estimate = forms.ChoiceField(choices=Project.TimeEstimateChoices.choices)
