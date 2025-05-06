from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("products/home")

    return render(request, "accounts/login.html")

def logout_view(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            logout(request)
            return redirect("login")

    return render(request, "accounts/logout.html")

def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username=email, email=email, password=password)
        login(request, user)
        return redirect("profile")

    return render(request, "accounts/signup.html")

def profile_view(request):
    return render(request, "accounts/profile.html", {"user": request.user})