from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("tags/", views.tag_list, name="tag_list"),
    path("create-task/", views.create_task, name="create_task"),
    path("create-tag/", views.create_tag, name="create_tag"),
    path("update-task/<int:task_id>/", views.update_task, name="update_task"),
    path("delete-task/<int:task_id>/", views.delete_task, name="delete_task"),
    path("toggle-task-status/<int:task_id>/", views.toggle_task_status, name="toggle_task_status"),
]
