from django.urls import path
from . import views


urlpatterns = [
  path('', views.index),
  path('create_todo', views.create_todo),
  path('<int:item_id>/delete', views.delete_item),
  path('<int:item_id>/done', views.done),
  path('<int:item_id>/uncross', views.uncross),
  path('<int:item_id>/confirm', views.confirm),
  path('completed', views.completed)
]