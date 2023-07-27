from django.http import HttpResponseForbidden


class OwnerRequiredMixin:
    """
    Ensures that only the project owner can take action.
    """

    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()
        if project.owner != self.request.user:
            return HttpResponseForbidden()
        return super(OwnerRequiredMixin, self).dispatch(request, *args, **kwargs)
