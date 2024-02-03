from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('add', views.add_todo, name='add'),
    path('completed', views.delete_completed, name='delete_completed'),
    path('delete_all', views.delete_all, name='delete_all'),
]
