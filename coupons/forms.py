from django import forms
from .models import Coupon


class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = ['code']

    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'checkout__discount--code__input--field border-radius-5', 'placeholder': 'Gift card or discount code'}))
