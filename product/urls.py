
from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
   path('', views.index, name='index'),
   path('shop/', views.products, name='products')
]
