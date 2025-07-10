# dashboard/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import SignupForm

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.groups.filter(name="Coach").exists():
                return redirect("/dashboard/coach/planning")
            return redirect("/dashboard/client/planning")
        return render(request, "account/login.html", {"error": "Identifiants invalides."})
    return render(request, "account/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()
            group_name = form.cleaned_data["group"]
            group = Group.objects.get(name=group_name)
            user.groups.add(group)
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "account/signup.html", {"form": form})
