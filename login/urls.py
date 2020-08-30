from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('register', views.register),
  path('login', views.login),
  path('logout', views.logout),
  path('<int:user_id>/delete', views.delete),
]