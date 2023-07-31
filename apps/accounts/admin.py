from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.favorites.admin import FavoriteInline

from .forms import CustomUserChangeForm, CustomUserCreationForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    inlines = [
        FavoriteInline,
    ]
    list_display = [
        "username",
        "email",
        "status",
        "is_superuser",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
