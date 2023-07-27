from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from .forms import ProjectForm
from .models import Project


class ProjectDetailView(DetailView):
    """
    Displays details of an individual project instance and its owner
    Context:
        - project: an instance of Project model
    Template used: project/detail.html

    """

    model = Project
    context_object_name = "project"
    template_name = "projects/detail.html"
    template_name = "projects/detail.html"


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """
    Creates a new instance of Project and set its owner to current logged in user
    Context:
        - form: an instance of ProjectForm form
    Template used: project/create.html
    """

    model = Project
    form_class = ProjectForm
    template_name = "projects/create.html"

    def get_success_url(self):
        return reverse("projects:detail", args=[str(self.object.id)])

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
