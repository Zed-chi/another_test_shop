from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, UserRegistrationForm
from .models import UserProfile
from cart.models import Cart


def register(req):
    if req.method == "POST":
        user_form = UserRegistrationForm(req.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            cart = Cart.objects.create(user=new_user)
            return render(
                req, "accounts/register_done.html", {"new_user": new_user}
            )
    else:
        user_form = UserRegistrationForm()
    return render(req, "accounts/register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, email=cd["email"], password=cd["password"]
            )
            print(f"=== {user } ===")

            if user:
                login(request, user)
                return redirect("main:homepage")
            return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


@login_required
def user_detail(req, username):
    user = get_object_or_404(UserProfile, username=username, is_active=True)
    return render(
        req, "accounts/detail.html", {"section": "people", "user": user}
    )
