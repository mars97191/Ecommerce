from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'checkout__input--field border-radius-5', 'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'checkout__input--field border-radius-5', 'placeholder': 'Введите ваше имя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'checkout__input--field border-radius-5', 'placeholder': 'Введите адрес эл. почты'}))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'checkout__input--field border-radius-5', 'placeholder': 'Введите ваш адрес'}))
    postal_code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'checkout__input--field border-radius-5', 'placeholder': 'Введите ваш почтовый код'}))
    city = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'checkout__input--field border-radius-5', 'placeholder': 'Введите ваш город'}))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', ]
