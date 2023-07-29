from django.urls import path

from .views import FavoriteCreateView

app_name = "favorites"

urlpatterns = [
    path(
        "create/",
        FavoriteCreateView.as_view(),
        name="create",
    )
]
