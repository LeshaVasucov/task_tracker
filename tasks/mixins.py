from django.core.exceptions import PermissionDenied


class UserIsOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if self.request.user != instance.creator :
            raise PermissionDenied
        return super().dispatch(request , *args, **kwargs)