from django.shortcuts import render, redirect
from django.contrib import messages
from todo.models import Todo, TodoManager
from login.models import User

# Create your todos views here.
def index(request):
  if 'user_id' not in request.session:
    return redirect('/')
  else:
    context = {
      'items': Todo.objects.all(),
      }
    return render(request, 'todos/index.html', context)

def completed(request):
  context = {
     'items': Todo.objects.all()
  }
  return render(request, 'todos/completed.html', context)

def create_todo(request):
  errors = Todo.objects.validate(request.POST)

  if errors:
    for value in errors.values():
      messages.error(request, value)
    return redirect('/todo')
  else:
    new_item = Todo.objects.create(item = request.POST['todo'], 
    user = User.objects.get(id= request.session['user_id']))
    return redirect('/todo')

def delete_item(request, item_id):
  item_to_delete = Todo.objects.get(id=item_id)
  item_to_delete.delete()
  return redirect('/todo/completed')

def done(request, item_id):
  item_to_cross = Todo.objects.get(id=item_id)
  item_to_cross.completed = True
  item_to_cross.save()
  print(item_to_cross.completed)
  return redirect('/todo')

def uncross(request, item_id):
  item_to_uncross = Todo.objects.get(id=item_id)
  item_to_uncross.completed = False
  item_to_uncross.save()
  print(item_to_uncross.completed)
  return redirect('/todo/completed')

def confirm(request, item_id):
  current_item = Todo.objects.get(id= item_id)
  context = {
    'todo': current_item
  }

  return render(request, 'todos/confirm.html', context)