from django import forms


class FavoriteForm(forms.Form):
    """
    This form is used to validate the uuidfield
    in the form submitted from FavoriteCreateView
    """

    id = forms.UUIDField()
