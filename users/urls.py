
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include

from users import views


app_name = 'users'

urlpatterns = [
   path('login/', views.CustomLoginView.as_view(), name='login'),
   path('register/', views.RegisterView.as_view(), name='register'),
   path('', include('django.contrib.auth.urls')),
   path('profile/', views.dashboard, name='dashboard'),
]
