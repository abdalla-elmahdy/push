from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import ProjectForm
from .mixins import OwnerRequiredMixin
from .models import Project

CustomUser = get_user_model()


class ProjectDetailView(generic.DetailView):
    """
    Displays details of an individual project instance and its owner
    Context:
        - project: an instance of Project model
    Template used: projects/detail.html

    """

    model = Project
    context_object_name = "project"
    template_name = "projects/detail.html"
    template_name = "projects/detail.html"


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    """
    Creates a new instance of Project and set its owner to current logged in user
    Context:
        - form: an instance of ProjectForm form
    Template used: projects/create.html
    """

    model = Project
    form_class = ProjectForm
    template_name = "projects/create.html"

    def get_success_url(self):
        return reverse("projects:detail", args=[str(self.object.id)])

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MyProjectsListView(LoginRequiredMixin, generic.ListView):
    """
    Displays a list of the logged-in user's created projects
    Context:
        - project_list: iterable of the logged-in user's created projects
    Template name: projects/my_projects.html
    """

    context_object_name = "project_list"
    template_name = "projects/my_projects.html"

    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id).projects.all()


class ProjectUpdateView(OwnerRequiredMixin, LoginRequiredMixin, generic.UpdateView):
    """
    Updates an instance of Project model using ProjectForm that has the current user as owner
    Uses the instance's pk passed in the url path to retrieve it from DB
    Context:
        - project: the instance of project the user wants to update
        - form: an instance of ProjectForm
    Template used: projects/update.html
    """

    model = Project
    form_class = ProjectForm
    template_name = "projects/update.html"
    context_object_name = "project"

    def get_success_url(self):
        return reverse("projects:detail", args=[str(self.object.id)])


class ProjectDeleteView(OwnerRequiredMixin, LoginRequiredMixin, generic.DeleteView):
    model = Project
    context_object_name = "project"
    template_name = "projects/delete.html"
    success_url = reverse_lazy("projects:my_projects")
