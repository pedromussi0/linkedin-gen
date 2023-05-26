import django.contrib.auth.views
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.decorators.cache import cache_control
from django.urls import reverse_lazy


# Create your views here.


def home(request):
    return render(request, "app/home.html")


# -------- login and register views -------------


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "app/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "app/login.html"  # Specify the path to your login template
    redirect_authenticated_user = True  # Redirect authenticated users to home page

    def get_success_url(self):
        return reverse_lazy("home")
