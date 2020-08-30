from django.db import models
from login.models import *

# Create your models here.
class TodoManager(models.Manager):
  def validate(self, formData):
    error = {}
    if len(formData['todo']) < 1:
      error['todo'] = 'This field is required'
    if len(formData['todo']) > 50:
      error['todo'] = 'maximum input is 50 characters, Thanks'
    return error

class Todo(models.Model):
  item = models.CharField(max_length=25)
  completed =  models.BooleanField(default= False)
  user = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TodoManager()
