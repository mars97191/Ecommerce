
from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
   path('', views.index, name='index'),
   path('shop/', views.products, name='products'),
   path('child-categories/<int:id>/', views.child_categories, name='child_categories'),
   path('products/<slug:slug>/', views.products_by_category, name='products_by_category'),
   path('<slug:slug>', views.product_detail, name='product_detail'),

   # add review
   path('ajax-add-review/<int:id>/', views.ajax_add_review, name='ajax_add_review'),

   # search
   path('search/', views.search_view, name='search'),
   path('wishlist/', views.wishlist, name='wishlist'),
   path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
   path('wishlist/remove/<int:product_id>/', views.remove_wishlist, name='remove_wishlist'),
]
