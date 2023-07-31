from django.contrib import admin

from .models import Favorite


class FavoriteInline(admin.TabularInline):
    model = Favorite
