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


@login_required()
def generate_bio(request):
    if request.method == "POST":
        form = BioGenForm(request.POST)
        if form.is_valid():
            creator = request.user

            request.session["creator"] = creator.id

            professional_experience = form.cleaned_data["professional_experience"]
            personalized_fact = form.cleaned_data["personalized_fact"]
            skills = form.cleaned_data["skills"]

            bio = generate_lk_bio(
                professional_experience=professional_experience,
                personalized_fact=personalized_fact,
                skills=skills,
            )

            return render(request, "app/generatebio.html", {"bio": bio})
    else:
        form = BioGenForm()

    return render(request, "app/generatebio.html", {"form": form})


def send_email(request):
    if request.method == "POST":
        bio = request.POST.get("textarea_content")

        subject = "Your Bio and Professional Title"
        message = f"Hello {request.user.username},\n\nHere is your generated bio:\n\nBio: {bio}"
        from_email = os.getenv("HOST_EMAIL")
        send_mail(subject, message, from_email, recipient_list=[request.user.email])

        return redirect(generate_bio)

    return render(request, "app/generatebio.html")


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
