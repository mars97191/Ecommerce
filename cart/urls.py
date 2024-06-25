from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),

    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('update/', views.update_cart_quantity, name='update-cart-quantity'),


]
