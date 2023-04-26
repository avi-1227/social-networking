from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html", {"section": "dashboard"})



class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name= 'registration/signup.html'