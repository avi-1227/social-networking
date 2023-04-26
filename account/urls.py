from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import SignUpView
from . import views


urlpatterns = [
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", SignUpView.as_view(), name='signup'),
]
