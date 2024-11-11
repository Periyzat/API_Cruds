from django.urls import path
from . import views
from django.urls import get_resolver


urlpatterns = [
    path('', views.task_list, name='task_list'),                # '' (home page) links to task_list, which shows all tasks and allows adding new tasks.
    path('create/', views.create_task, name='create_task'),  
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]
