import django.contrib.auth.decorators
import django.contrib.auth.views
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views.decorators.cache import cache_control
from django.urls import reverse_lazy
from django.contrib.auth.password_validation import (
    CommonPasswordValidator,
    NumericPasswordValidator,
    UserAttributeSimilarityValidator,
    MinimumLengthValidator,
)
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required()
def home(request):
    return render(request, "app/home.html")


# -------- login and register views -------------


def validate_password(password):
    validators = [
        CommonPasswordValidator(),
        NumericPasswordValidator(),
        UserAttributeSimilarityValidator(),
        MinimumLengthValidator(min_length=8),
    ]
    errors = []

    for validator in validators:
        try:
            validator.validate(password)
        except ValidationError as e:
            errors.extend(e.messages)

    return errors


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get("password1")
            password_errors = validate_password(password)

            if password_errors:
                for error in password_errors:
                    form.add_error("password1", error)
            else:
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
