
from django.urls import path

from  .import views

app_name = 'payment'

urlpatterns = [
   path('payment-success/', views.payment_success, name='payment_success'),
   path('payment-fail/', views.payment_fail, name='payment_fail'),
   path('shipping/', views.shipping, name='shipping'),
   path('checkout/', views.checkout, name='checkout'),
   path('complete-order/', views.complete_order, name='complete_order')

]
