from django import forms

from payment.models import ShippingAddress


# class ShippingAddressForm(forms.ModelForm):
#     class Meta:
#         model = ShippingAddress
#         fields = ['full_name', 'street_address', 'city', 'email']
#         exclude = ['user',]