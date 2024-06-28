
from django.urls import path

from  .import views

app_name = 'payment'

urlpatterns = [
   path('process/', views.payment_process, name='process'),
   path('completed/', views.payment_completed, name='completed'),
   path('canseled/', views.payment_canceled, name='canceled'),



]
