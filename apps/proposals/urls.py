from django.urls import path

from .views import ProposalCreateView, ProposalDeleteView, ProposalListView

app_name = "proposals"

urlpatterns = [
    path(
        "create/",
        ProposalCreateView.as_view(),
        name="create",
    ),
    path(
        "delete/<int:pk>",
        ProposalDeleteView.as_view(),
        name="delete",
    ),
    path(
        "",
        ProposalListView.as_view(),
        name="list",
    ),
]
