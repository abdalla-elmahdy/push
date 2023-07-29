from django.urls import path

from .views import FavoriteCreateView, FavoriteDeleteView, FavoriteListView

app_name = "favorites"

urlpatterns = [
    path(
        "create/",
        FavoriteCreateView.as_view(),
        name="create",
    ),
    path(
        "delete/<int:pk>",
        FavoriteDeleteView.as_view(),
        name="delete",
    ),
    path(
        "",
        FavoriteListView.as_view(),
        name="list",
    ),
]
