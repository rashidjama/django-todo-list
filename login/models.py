from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
  def validate(self, form_data):
    errors = {}
    if len(form_data['first']) < 2:
      errors['first'] = 'First name should be at least 2 letters'
    if len(form_data['last']) < 2:
      errors['last'] = 'Last name should be at least 2 letters'
  
    if not form_data['first'].isalpha() and form_data['first'] != '':
      errors['first'] = "First name must contain only letters"

    if not form_data['last'].isalpha() and form_data['last'] != '':
        errors['last'] = "Last name must contain only letters"
    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(form_data['email']):    # test whether a field matches the pattern            
        errors['email'] = ("Invalid email address!")

    exist_email = self.filter(email=form_data['email'])
    if exist_email:
      errors['email'] = 'Email in use already, choose another one'

    if len(form_data['password']) < 5:
      errors['password'] = "Password must be at least 5 Charactors."
    
    if form_data['cpassword'] != form_data['password']:
      errors['cpassword'] = "Passwords did not match. "
    return errors

  def validate_books(self, postData):
    errors = {}
    if len(postData['title']) < 1:
      errors['title'] = 'Title must be at least 1  character to be valid'
    if len(postData['des']) < 5:
      errors['des'] = 'Description must be at least 5 characters'
    return errors



class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = UserManager()

#trip validations
class TripManager(models.Manager):
  def validate_trips(self, form_data):
      error = {}
      if len(form_data['des']) < 3:
       error['destination'] = 'Destination must be at least 3 charactors!'
      if len(form_data['start_date']) < 1:
        error['start_date'] = 'Start date must be provided'
      if len(form_data['end_date']) < 1:
        error['end_date'] = 'End date must be provided'
      if len(form_data['plan']) < 3:
        error['plan'] = 'Plan must be at least 3 charactors'
      return error

class Trip(models.Model):
  destination = models.CharField(max_length=255)
  start_date = models.DateField()
  end_date = models.DateField()
  plan = models.CharField(max_length=255)
  trip_creator = models.ForeignKey(User, related_name='created_trips', on_delete=models.CASCADE)
  trip_joiners = models.ManyToManyField(User, related_name='joined_trips')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  objects = TripManager()

  