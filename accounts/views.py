import os

from django import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.forms import CustomUserCreationForm, CustomUserProfileChangeForm, CustomUserChangeForm, \
    CustomUserCreationFormFirst
from accounts.formset import CustomUserProfileFormSet
from accounts.models import CustomUserProfile, CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationFormFirst
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


""""
class ProfileUpdateView(UpdateView):
    form_class = CustomUserProfileChangeForm
    success_url = reverse_lazy("home")
    template_name = 'accounts/profile_update.html'
"""


@login_required
def profile_list_view(request):
    model_user = CustomUser.objects.all()
    model_user_profile = CustomUserProfile.objects.all()

    return render(
        request,
        'accounts/profile_list.html',
        context={
            'model_user': model_user,
            'model_user_profile': model_user_profile,
        }
    )


class UserCreateView(views.View):

    def get(self, request):
        form1 = CustomUserCreationForm
        return render(
            request,
            'accounts/profile_form.html',
            context={
                'form1': form1,
            }
        )

    def post(self, request):
        password = CustomUser.objects.make_random_password(10)
        form1 = CustomUserCreationForm(request.POST)

        form1.fields['password1'].initial = password
        form1.fields['password2'].initial = password

        if form1.is_valid():
            form1.save()

        return redirect('accounts:list-profile')


#

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
    user = get_object_or_404(CustomUser, pk=pk)
    profile = get_object_or_404(CustomUserProfile, pk=user.profile.id)
    return render(
        request,
        'accounts/profile_detail.html',
        context={
            'user': user,
            'profile': profile,
        }
    )


class UserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('accounts:list-profile')
    template_name = 'accounts/profile_confirm_delete.html'
