from django.shortcuts import render, redirect
from .models import Tasks
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from . forms import UpdateForm


# Create your views here.
def index(request):
  if(request.user.is_authenticated):    
    completed = Tasks.objects.filter(user_id = request.user , completed = 1)
    uncompleted = Tasks.objects.filter(user_id =  request.user, completed = 0)
    return render(request, "index.html", {"completed" : completed, "uncompleted" :  uncompleted})

  
  return redirect("login")


#This is the view to add task to the todo application.
def AddTask(request):
  if(request.user.is_authenticated):
    if(request.method == "POST"): 
      input_task = request.POST["task"]
      if(input_task != ""): 
        task = Tasks(user_id = request.user, task= input_task)
        task.save()
        return redirect("index")

      return redirect("index")
  return redirect("login")

# this is the view to edit the task 
def edit(request, task_id):
  if(request.user.is_authenticated):
    if (request.method == "POST"):
      initial_task = Tasks.objects.get(id = task_id )
      task = UpdateForm(request.POST, instance = initial_task)
      task.save()
      return redirect("index")

    id = task_id
    task = Tasks.objects.get(pk = task_id)
    form = UpdateForm(instance=task)
    
    return render(request, "edit.html", {"id" : id, "form": form })
  return redirect("login")

#This is the view that delete tasks from the todo application.
def delete(request, task_id):
  element = Tasks.objects.get(id = task_id)
  element.delete()
  return redirect("index")


#This is the views that marks the tasks that are completed.
def mark(request, task_id):
  task = Tasks.objects.get(id = task_id)
  task.completed = 1
  task.save()
  return redirect("index")


#This is the view that marks completed task as uncompleted.
def restore(request, task_id): 
  task = Tasks.objects.get(id = task_id)
  task.completed = 0
  task.save()
  return redirect("index")

#This is the view that helps you to logout
def logout_view(request):
  logout(request)
  form = AuthenticationForm()
  context = {"form" : form}
  return redirect("loggout")