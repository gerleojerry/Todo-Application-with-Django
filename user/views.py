from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . forms import RegisterationForm
from application.models import Tasks

# Create your views here.

# this is the login view of the application 
def login_view(request):
  if(request.method == "POST"):
    form = AuthenticationForm(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username = username, password = password)
    if(user is not None): 
      login(request, user)
      return redirect("homepage")
    else: 
      messages.error(request, "User is not authenticated, please try again later!!!")
      return redirect("homepage")
  
  form = AuthenticationForm()
  return render(request, "login.html", {"form" : form})


# this is the signup  view of the application 
def signup(request):

  if(request.method == "POST"):
    user_form = RegisterationForm(request.POST)
    if(user_form.is_valid()) :
      user_form.save()
      return redirect("login")
    # messages.error(request, "Registeration Failed, Please try again later!!! ")
    return render(request, "signup.html", {"form" : user_form})
  else:
    form = RegisterationForm
    return render(request, "signup.html", {"form" : form })


def homepage(request):
  if(request.user.is_authenticated) :
    completed = Tasks.objects.filter(user_id =  request.user, completed = 1)
    uncompleted = Tasks.objects.filter(user_id = request.user, completed = 0)
    return render(request, "index.html", {"completed" : completed, "uncompleted" :  uncompleted})
  else: 
    form = AuthenticationForm()
    return render(request,"login.html", {"form" : form} )