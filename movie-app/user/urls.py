from django.urls import path
from django.contrib.auth import views as auth_views

from .views import RegisterView

app_name = 'user'

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]