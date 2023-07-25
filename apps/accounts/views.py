from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import ProfileUpdateForm

CustomUser = get_user_model()


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileUpdateForm
    template_name = "account/update_profile.html"
    success_url = reverse_lazy("accounts:update")

    def get_object(self):
        return CustomUser.objects.get(pk=self.request.user.id)
