from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls.conf import include

from users import views


app_name = 'users'

urlpatterns = [
   path('login/', views.CustomLoginView.as_view(), name='login'),
   path('register/', views.RegisterView.as_view(), name='register'),
   path('logout/', views.CustomLogoutView.as_view(), name='logout'),
   path('password_reset/', auth_views.PasswordResetView.as_view(template_name ="accounts/profile.html"), name='password_reset'),
   path('profile/', views.dashboard, name='dashboard'),

]
