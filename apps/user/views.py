from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.views import LoginView, LogoutView

from apps.user.forms import CustomUserCreationForm


class CustomLoginView(LoginView):

    def get_success_url(self):
        return reverse_lazy('home')


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('user:login')
    template_name = 'registration/signup.html'


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('user:login')
