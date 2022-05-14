from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Tasks(models.Model):
  task = models.CharField(max_length = 250)
  user_id = models.ForeignKey(User, on_delete= models.CASCADE, default = 1)
  created_time = models.CharField(max_length = 255, default = datetime.now().strftime("%d/%m/%y | %H: %M"))
  completed = models.IntegerField(default = 0)