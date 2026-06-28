
from django.urls import path, include
from . import views

urlpatterns = [
    path('add-task', views.addTask, name='add_task'),
    path('mark-done/<int:pk>', views.markDone, name='mark_done'),
    path('mark-undone<int:pk>', views.markUnDone, name='mark_undone'),
    path('edit-task/<int:pk>', views.editTask, name='edit_task'),
    path('delete-task/<int:pk>', views.deleteTask, name='delete_task'),
]
