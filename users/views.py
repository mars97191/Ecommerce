from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from product.models import CartOrder, Address
from users.forms import UserLoginForm, UserRegisterForm


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')


def dashboard(request):
    orders = CartOrder.objects.filter(user=request.user)
    address = Address.objects.filter(user=request.user)
    context = {'orders': orders, 'address': address}
    return render(request, 'accounts/profile.html', context)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('product:index')
