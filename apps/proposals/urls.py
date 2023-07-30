from django.urls import path

from .views import ProposalCreateView, ProposalListView

app_name = "proposals"

urlpatterns = [
    path(
        "create/",
        ProposalCreateView.as_view(),
        name="create",
    ),
    path(
        "",
        ProposalListView.as_view(),
        name="list",
    ),
]
