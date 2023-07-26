from django.views.generic import DetailView

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
