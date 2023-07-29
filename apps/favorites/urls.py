from django.urls import path

from .views import FavoriteCreateView, FavoriteListView

app_name = "favorites"

urlpatterns = [
    path(
        "create/",
        FavoriteCreateView.as_view(),
        name="create",
    ),
    path(
        "",
        FavoriteListView.as_view(),
        name="list",
    ),
]
