from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, FormView
from .models import User, Profile
from .forms import CustomUserCreationForm, ProfileForm, LoginForm, CustomPasswordResetFrom


class LoginUser(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = '/account'

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)

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

    def form_valid(self, form, ):
        user = form.save()
        messages.success(self.request, 'User account was created!')
        login(self.request, user)
        return redirect('/edit-account/'+str(user.profile.id)+'/')

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)


class Profiles(ListView):
    template_name = 'users/profiles.html'
    model = Profile
    context_object_name = 'profiles'


class UserProfile(DetailView):
    template_name = 'users/user-profile.html'
    model = Profile


class UserAccount(LoginRequiredMixin, TemplateView):
    def get(self, request):
        profile = request.user.profile
        context = {'profile': profile}
        return render(request, 'users/account.html', context)


class EditAccount(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile_form.html'
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy('account')

    def get_context_data(self, **kwargs):
        queryset = kwargs.pop('object_list', None)
        if queryset is None:
            self.object_list = self.model.objects.all()
        return super().get_context_data(**kwargs)


# class ResetPassword(UpdateView):
#     model = User
#     fields = '__all__'
#     success_url = reverse_lazy('account')
#     template_name = 'reset.html'
