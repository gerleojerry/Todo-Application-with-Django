from django.forms import ModelForm
from django.db import models
from . models import Tasks

class UpdateForm(ModelForm):
  class Meta:
    model = Tasks
    fields = ["task"]