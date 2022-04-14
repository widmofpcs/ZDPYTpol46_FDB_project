from django.urls import path

from customer.views import TaskCreateView, TaskListView, RequestChangeTaskView

app_name = 'task'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('update/<int:pk>/', RequestChangeTaskView.as_view(), name='task-update'),

]
