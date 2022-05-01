from django import views
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from accounts.forms import CustomUserCreationForm, CustomUserProfileChangeForm, CustomUserCreationFormFirst, \
    CustomUserChangeForm
from accounts.models import CustomUserProfile, CustomUser
from config.mixins import ManagerRequiredMixin


class SignUpView(CreateView):
    form_class = CustomUserCreationFormFirst
    success_url = reverse_lazy("login")
    template_name = "user_registration/signup.html"


""""
class ProfileUpdateView(UpdateView):
    form_class = CustomUserProfileChangeForm
    success_url = reverse_lazy("home")
    template_name = 'accounts/profile_update.html'
"""


class ProfileListView(ManagerRequiredMixin, views.View):

    def get(self, request):
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
            username = form1.instance.username
            email = form1.instance.email
            protocol = request.get_host
            domain = 'accounts/password_reset/'
            res = {
                'username': username,
                'email' : email,
                'protocol': protocol,
                'domain': domain,
            }
            body = render_to_string('user_registration/profile_reset.txt', res)
            send_mail(
                'Hello new user',
                body,
                'FDBteam@sda.com',
                [email],
                fail_silently=False,
            )

        return redirect('accounts:list-profile')


class ProfileUpdateView(views.View):

    def get(self, request):
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = CustomUserProfileChangeForm(instance=request.user.profile)

        return render(
            request,
            'accounts/profile_update.html',
            {'user_form': user_form,
             'profile_form': profile_form},
        )

    def post(self, request):
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = CustomUserProfileChangeForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to='accounts:list-profile')


class ProfileDetailView(views.View):
    def get(self, request, pk):
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
