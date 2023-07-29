from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView, ListView

from apps.projects.models import Project
from utils.mixins import OwnerRequiredMixin

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


class FavoriteListView(LoginRequiredMixin, ListView):
    """
    Displays a list of all projects in a user's favorites
    Context:
        - favorite_list: iterable of favorite instances
    """

    model = Favorite
    template_name = "favorites/partials/list.html"
    context_object_name = "favorite_list"

    def get_queryset(self):
        return Favorite.objects.filter(owner=self.request.user)


class FavoriteDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    """
    Uses the instance's pk passed in the url path to retrieve it from DB
    Get:
        Displays a confirmation form to delete the instance or cancel
    Post:
        Deletes the instance if the current user as owner, otherwise returns 403 response
    """

    model = Favorite
    context_object_name = "favorite"
    template_name = "favorites/partials/delete.html"
    success_url = reverse_lazy("projects:my_projects")
