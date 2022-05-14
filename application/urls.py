from django.urls import path
from . import views
from user.views import login_view

urlpatterns = [
    path("", views.index, name = "index" ),
    path("AddTask", views.AddTask, name = "AddTask"),
    path("edit/<int:task_id>/", views.edit, name = "edit"),
    path("delete/<int:task_id>/", views.delete, name = "delete"),
    path("mark/<int:task_id>", views.mark, name = "mark"),
    path("restore/<int:task_id>/", views.restore, name = "restore"),
    path("logout/", views.logout_view, name = "logout" ),
    path("loggout/" , login_view, name = "loggout" )
]
