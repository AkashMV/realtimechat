from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *

def profile_view(req):
    profile = req.user.profile
    print(profile)
    return render(req, 'a_users/profile.html', {'profile': profile})

@login_required
def profile_edit_view(req):
    form = ProfileForm(instance = req.user.profile)
    if req.method == 'POST':
        form = ProfileForm(req.POST, req.FILES, instance=req.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    print(req)
    return render(req, 'a_users/profile_edit.html', {'form':form}) 