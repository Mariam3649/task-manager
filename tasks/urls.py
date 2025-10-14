from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('create/', views.create_task, name='create-task'),
    path('<int:pk>/update/', views.update_task, name='update-task'),
    path('<int:pk>/delete/', views.delete_task, name='delete-task'),
    path('<int:pk>/complete/', views.complete_task, name='complete-task'),
]

