from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    path("", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.sign_up, name='signup'), # Update URL Path
]
