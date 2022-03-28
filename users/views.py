from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, FormView
from .models import User, Profile
from .forms import CustomUserCreationForm, ProfileForm, LoginForm


class LoginUser(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/account'

    def form_valid(self, form):

        user = authenticate(email=self.request.POST['email'], password=self.request.POST['password'])

        if user is not None:
            login(self.request, user)
            return super(LoginUser, self).form_valid(form)
        else:
            messages.error(self.request, 'Email OR password is incorrect')
            return super(LoginUser, self).form_valid(form)


class LogoutUser(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'User was logged out!')
        return redirect('login')


class RegisterUser(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/account'


class Profiles(ListView):
    template_name = 'users/profiles.html'
    model = Profile
    context_object_name = 'profiles'


class UserProfile(DetailView):
    template_name = 'users/user-profile.html'
    model = Profile


@method_decorator(login_required, name='dispatch')
class UserAccount(TemplateView):
    def get(self, request):
        profile = request.user.profile
        context = {'profile': profile}
        return render(request, 'users/account.html', context)


@method_decorator(login_required, name='dispatch')
class EditAccount(UpdateView):
    template_name = 'users/profile_form.html'
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('profiles')