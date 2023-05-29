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
            personalized_fact = form.cleaned_data["personalized_fact"]
            value_creation = form.cleaned_data["value_creation"]
            passion_motivation = form.cleaned_data["passion_motivation"]

            module_dir = os.path.dirname(__file__)
            file_path = os.path.join(module_dir, "teste.txt")
            bio_samples = read_file_text(file_path)

            bio = generate_lk_bio(
                bio_samples=bio_samples,
                professional_title=professional_title,
                personalized_fact=personalized_fact,
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
