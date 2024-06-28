
from django.urls import path

from  .import views

app_name = 'payment'

urlpatterns = [
   path('process/', views.payment_process, name='payment_process'),
   path('completed/', views.payment_completed, name='payment_completed'),
   path('canseled/', views.payment_canceled, name='payment_canceled'),
   path('checkout/', views.checkout, name='checkout'),


]
