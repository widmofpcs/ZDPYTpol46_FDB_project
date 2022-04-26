import os

from login_required import LoginNotRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from accounts.forms import CustomUserCreationForm, CustomUserProfileChangeForm, CustomUserChangeForm
from accounts.models import CustomUserProfile


class SignUpView(LoginNotRequiredMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


""""
class ProfileUpdateView(UpdateView):
    form_class = CustomUserProfileChangeForm
    success_url = reverse_lazy("home")
    template_name = 'accounts/profile_update.html'
"""


@login_required
def profile_update_view(request):
    if request.method == 'POST':
        profile_form = CustomUserProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            return redirect(to='home')
    else:
        profile_form = CustomUserProfileChangeForm(instance=request.user.profile)

    return render(
        request,
        'accounts/profile_update.html',
        {'profile_form': profile_form}
    )


@login_required
def profile_detail_view(request, pk):
    profile = get_object_or_404(CustomUserProfile, pk=pk)
    return render(
        request,
        'accounts/profile_detail.html',
        context={
            'profile': profile,
        }
    )
