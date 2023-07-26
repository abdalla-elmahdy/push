from django.urls import path

from .views import ProjectDetailView

app_name = "projects"

urlpatterns = [
    path("<uuid:pk>", ProjectDetailView.as_view(), name="detail"),
]
