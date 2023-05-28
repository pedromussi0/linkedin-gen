from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import BioGenForm
from .langchain import *


# Create your views here.


@login_required()
def home(request):
    return render(request, "app/home.html")


def generate_bio(request):
    if request.method == "POST":
        form = BioGenForm(request.POST)
        if form.is_valid():
            creator = request.user

            request.session["creator"] = creator.id

            professional_title = form.cleaned_data["professional_title"]
            years_of_experience = form.cleaned_data["years_of_experience"]
            professional_values = form.cleaned_data["professional_values"]
            problem_solving = form.cleaned_data["problem_solving"]
            emotional_intelligence = form.cleaned_data["emotional_intelligence"]
            personal_growth_mindset = form.cleaned_data["personal_growth_mindset"]
            teamwork_collaboration = form.cleaned_data["teamwork_collaboration"]
            communication_skills = form.cleaned_data["communication_skills"]
            initiative_proactivity = form.cleaned_data["initiative_proactivity"]
            adaptability_resilience = form.cleaned_data["adaptability_resilience"]
            value_creation = form.cleaned_data["value_creation"]
            passion_motivation = form.cleaned_data["passion_motivation"]

            bio = generate_lk_bio(
                professional_title=professional_title,
                years_of_experience=years_of_experience,
                professional_values=professional_values,
                problem_solving=problem_solving,
                emotional_intelligence=emotional_intelligence,
                personal_growth_mindset=personal_growth_mindset,
                teamwork_collaboration=teamwork_collaboration,
                communication_skills=communication_skills,
                initiative_proactivity=initiative_proactivity,
                adaptability_resilience=adaptability_resilience,
                value_creation=value_creation,
                passion_motivation=passion_motivation,
            )

            return render(request, "app/generatebio.html", {"bio": bio})
    else:
        form = BioGenForm()

    return render(request, "app/generatebio.html", {"form": form})


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
