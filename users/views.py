from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import ShippingAddress
from users.forms import UserLoginForm, UserRegisterForm, ShippingAddressForm


class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'registration/login.html'


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('users:login')


@login_required(login_url='users:login')
def dashboard(request):
    try:
        shipping_address = ShippingAddress.objects.get(user=request.user)
    except ShippingAddress.DoesNotExist:
        shipping_address = None

    form = ShippingAddressForm(instance=shipping_address)

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.save()
            return redirect('users:dashboard')
    return render(request, 'accounts/profile.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('product:index')
