from django import forms

from .models import Proposal


class NoInput(forms.Widget):
    """
    A widget to render nothing but still keep the field
    in the form class for validation, this helps when we
    need to put the field manually in the form
    """

    input_type = "hidden"
    template_name = ""

    def render(self, name, value, attrs=None, renderer=None):
        return ""


class ProposalForm(forms.ModelForm):
    project_id = forms.UUIDField(widget=NoInput)

    class Meta:
        model = Proposal
        fields = (
            "project_id",
            "motive",
            "skillset",
            "contact_details",
        )
        labels = {
            "motive": "Why do you want to join this project?",
            "skillset": "Tell me about your skills",
            "contact_details": "How can I contact you?",
        }
