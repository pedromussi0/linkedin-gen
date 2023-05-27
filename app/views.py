
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required()
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
    template_name = "app/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")
