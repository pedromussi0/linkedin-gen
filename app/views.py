from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import BioGenForm
from .langchain import *
from django.core.mail import send_mail


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
            personalized_fact = form.cleaned_data["personalized_fact"]
            background = form.cleaned_data["background"]
            current_role = form.cleaned_data["current_role"]
            relevant_skills = form.cleaned_data["relevant_skills"]

            bio = generate_lk_bio(
                professional_title=professional_title,
                personalized_fact=personalized_fact,
                background=background,
                current_role=current_role,
                relevant_skills=relevant_skills,
            )

            # Send email to the current user
            subject = "Your Bio and Professional Title"
            message = f"Hello {creator.username},\n\nHere is your generated bio and professional title:\n\nBio: {bio}\nProfessional Title: {professional_title}"
            from_email = os.getenv("HOST_EMAIL")
            send_mail(subject, message, from_email, recipient_list=[creator.email])

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
