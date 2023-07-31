from django.views.generic import FormView

from .forms import SearchForm


class HomePageView(FormView):
    """
    Displays an intro section about the platform and search form for projects
    Context:
        - form: an instance of SearchForm
    """

    template_name = "pages/home.html"
    form_class = SearchForm
