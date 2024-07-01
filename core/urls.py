from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product.urls', namespace='product')),
    path('accounts/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('coupons/', include('coupons.urls', namespace='coupons')),
    # path('accounts/', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)