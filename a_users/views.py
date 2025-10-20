from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.contrib.auth.models import User


def profile_view(req, username=None):
    print(username)
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = req.user.profile
        except:
            return redirect("account_login")
    return render(req, "a_users/profile.html", {"profile": profile})


@login_required
def profile_edit_view(req):
    form = ProfileForm(instance=req.user.profile)
    if req.method == "POST":
        form = ProfileForm(req.POST, req.FILES, instance=req.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    if req.path == reverse("profile-onboarding"):
        onboarding = True
    else:
        onboarding = False
    print(req)
    return render(
        req, "a_users/profile_edit.html", {"form": form, "onboarding": onboarding}
    )


@login_required
def profile_settings_view(req):
    return render(req, "a_users/profile_settings.html")
