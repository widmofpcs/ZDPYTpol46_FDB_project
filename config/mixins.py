from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.contrib import messages


class ManagerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_manager

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            message = messages.error(request, message='Access denied. Managers only.')
            return render(request,
                          'home.html',
                          context={
                              'message': message
                          })
        return super().dispatch(request, *args, **kwargs)
