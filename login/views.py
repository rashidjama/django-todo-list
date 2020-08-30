from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Trip
import bcrypt


# Create your views here.
def index(request):
  context = {
    'users': User.objects.all(),
  }
  return render(request, 'index.html', context)


def register(request):
  errors = User.objects.validate(request.POST)

  if errors:
    for values in errors.values():
      messages.error(request, values)
    return redirect('/')
  else:

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    current_user = User.objects.create(
      first_name = request.POST['first'],
      last_name = request.POST['last'],
      email = request.POST['email'],
      password = pw_hash,
    )
    request.session['user_id'] = current_user.id
    messages.success(request, 'You have successfully registered!')
    return redirect('/todo')


def login(request):
  if request.method == 'POST':
    results = User.objects.filter(email=request.POST['email'])
    if len(results) > 0:
        if bcrypt.checkpw(request.POST['password'].encode(), results[0].password.encode()):
            request.session['user_id'] = results[0].id
            request.session["name"] = (f"{results[0].first_name}")
            return redirect('/todo')
            
        else:
            messages.error(request, "Email or passwort did not match.")
            return redirect("/")
    else:
        messages.error(request, "Email or passwort did not match.")
        return redirect("/")



def logout(request):
  request.session.flush()
  return redirect('/')
# delete user
def delete(request, user_id):
  user_to_delete = User.objects.get(id=user_id)
  user_to_delete.delete()
  return redirect('/')



