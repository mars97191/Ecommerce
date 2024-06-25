from django.contrib import admin

from users.models import User, ShippingAddress

admin.site.register(User)
admin.site.register(ShippingAddress)