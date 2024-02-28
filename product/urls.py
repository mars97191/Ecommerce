
from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
   path('', views.index, name='index'),
   path('shop/', views.products, name='products'),
   path('child-categories/<int:id>/', views.child_categories, name='child_categories'),
   path('products/<slug:slug>/', views.products_by_category, name='products_by_category'),
   path('<slug:slug>', views.product_detail, name='product_detail'),

]
