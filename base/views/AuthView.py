from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def authLogin(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user is not None:
                auth_user = authenticate(request, username=username, password=password)
                if auth_user is not None:
                    login(request, auth_user)
                    messages.success(
                        request,
                        " Hey " + username.upper() + ", welcome to the Studybuddy!",
                    )
                    return redirect("home")
                else:
                    messages.error(request, "User dose not exist!")
            else:
                messages.error(request, "User dose not exist!")
        except Exception as e:
            print(e)
    context = {}
    return render(request, "base/pages/login.html", context)


def authSignup(request):
    form = UserCreationForm()
    try:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                messages.success(
                    request,
                    " Hey " + user.username.upper() + ", welcome to the Studybuddy!",
                )
                return redirect("home")
            else:
                messages.error(request, "An error occurred during registration")
    except Exception as e:
        print(e)
    context = {"form": form}
    return render(request, "base/pages/signup.html", context)


def authLogout(request):
    logout(request)
    messages.error(request, "You have been  logged out!")
    return redirect("home")
