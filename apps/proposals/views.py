from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import ListView

from apps.projects.models import Project

from .forms import ProposalForm
from .models import Proposal


class ProposalCreateView(LoginRequiredMixin, View):
    """
    Post:
        Creates a new proposal instance for the current logged-in
        user and project instance which its id passed in the form
    """

    def post(self, request):
        form = ProposalForm(request.POST)
        if form.is_valid():
            project = get_object_or_404(Project, id=form.cleaned_data["project_id"])
            Proposal(
                sender=request.user,
                project=project,
                motive=form.cleaned_data["motive"],
                skillset=form.cleaned_data["skillset"],
                contact_details=form.cleaned_data["contact_details"],
            ).save()
            return HttpResponse("Proposal sent successfully")

        return HttpResponse("Something went wrong, try again.")


class ProposalListView(ListView):
    """
    Displays a list of proposals received for the logged-in user
    """

    model = Proposal
    context_object_name = "proposal_list"
    template_name = "proposals/partials/list.html"

    def get_queryset(self):
        return Proposal.objects.filter(project__owner=self.request.user)
