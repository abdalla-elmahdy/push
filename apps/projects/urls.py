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
        "search/",
        views.ProjectSearchView.as_view(),
        name="search",
    ),
    path(
        "update/<uuid:pk>/",
        views.ProjectUpdateView.as_view(),
        name="update",
    ),
    path(
        "delete/<uuid:pk>/",
        views.ProjectDeleteView.as_view(),
        name="delete",
    ),
    path(
        "<uuid:pk>",
        views.ProjectDetailView.as_view(),
        name="detail",
    ),
    path(
        "",
        views.MyProjectsListView.as_view(),
        name="my_projects",
    ),
]
