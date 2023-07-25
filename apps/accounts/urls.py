from django.urls import path

from .views import ProfileUpdateView

app_name = "accounts"

urlpatterns = [
    path("update/", ProfileUpdateView.as_view(), name="update"),
]
