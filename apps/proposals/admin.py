from django.contrib import admin

from .models import Proposal


class ProposalAdmin(admin.ModelAdmin):
    model = Proposal
    list_display = [
        "project",
        "sender",
        "created",
    ]


admin.site.register(Proposal, ProposalAdmin)
