from django.urls import path

from task.views import TaskCreateView, TaskListView, RequestChangeTaskView, RequestTaskListView, \
    RequestChangeApprovalView

app_name = 'task'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('update/<int:pk>/', RequestChangeTaskView.as_view(), name='task-update'),
    path('request/list', RequestTaskListView.as_view(), name='request-list'),
    path('request/approval/<int:pk>', RequestChangeApprovalView.as_view(), name='request-approval'),

]
