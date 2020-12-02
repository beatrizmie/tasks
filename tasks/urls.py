from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_tasks', views.get_all_tasks, name='all_tasks'),
    path("<int:task_id>", views.get_task_by_id, name="task"),
    path("create_task", views.create_task, name="create_task"),
    path("update_task_title/<int:task_id>", views.update_task_title, name="update_task_title"),
    path("update_task_pub_date/<int:task_id>", views.update_task_pub_date, name="update_task_pub_date"),
    path("update_task_description/<int:task_id>", views.update_task_description, name="update_task_description"),
    path("delete_task/<int:task_id>", views.delete_task, name="delete_task"),
    path("delete_all_tasks", views.delete_all_tasks, name="delete_all_tasks"),
]
