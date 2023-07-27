from django.urls import path

from . import views

app_name = "projects"

urlpatterns = [
    path(
        "create/",
        views.ProjectCreateView.as_view(),
        name="create",
    ),
    path(
        "<uuid:pk>",
        views.ProjectDetailView.as_view(),
        name="detail",
    ),
]
