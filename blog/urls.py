from django.urls import path
from . import views

urlpatterns = [
    path('', views.todos, name='todos'),
    path('add', views.add_todo, name='add'),
    path('delete/<int:pk>', views.delete_one, name='delete'),
    path('edit/<int:pk>', views.edit_todo, name='edit'),
    path('complete/<int:pk>', views.complete_todo, name='complete'),
    path('completed', views.delete_completed, name='delete_completed'),
    path('delete_all', views.delete_all, name='delete_all'),
]
