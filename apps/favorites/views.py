from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View

from apps.projects.models import Project

from .forms import FavoriteForm
from .models import Favorite


class FavoriteCreateView(LoginRequiredMixin, View):
    """
    Creates an instance of Favorite and sends back success response if
    it doesn't actually exist, otherwise sends a response that the instance already exists
    """

    def post(self, request):
        try:
            form = FavoriteForm(request.POST)
            if form.is_valid():
                project = get_object_or_404(Project, id=form.cleaned_data["id"])
                Favorite(
                    project=project,
                    owner=request.user,
                ).save()
                return HttpResponse("Added to favorites")
        # IntegrityError is thrown if the instance already exists
        # because of the unique_together constraint in Favorite model
        except IntegrityError:
            return HttpResponse("Already added to your favorites")
