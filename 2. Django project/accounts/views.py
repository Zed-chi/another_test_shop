from cart.models import Cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import LoginForm, UserRegistrationForm, ProfileForm
from .models import UserProfile, ProfileInfo


def register(req):
    if req.method == "POST":
        user_form = UserRegistrationForm(req.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            Cart.objects.create(user=new_user)
            ProfileInfo.objects.create(user=new_user)
            return render(req, "accounts/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(req, "accounts/register.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd["email"], password=cd["password"])
            if user:
                login(request, user)
                return redirect("main:homepage")
            return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})


@login_required
def user_detail(request):
    form = ProfileForm()
    if request.method == "GET":
        form = ProfileForm()
        return render(request, "accounts/detail.html", {"form": form})
    form = ProfileForm(date=request.POST)
    if not form.is_valid():
        form.save()

    return redirect(reverse("accounts:detail"))
