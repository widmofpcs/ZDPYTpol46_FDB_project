from django.urls import path

from task.views import TaskCreateView, TaskListView, RequestChangeTaskView, RequestTaskListView, \
    RequestChangeApprovalView, TeamTaskListView, TeamTaskAddUsers, TaskDetailView, TeamUserDeleteView

app_name = 'task'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('update/<int:pk>/', RequestChangeTaskView.as_view(), name='task-update'),
    path('request/list/', RequestTaskListView.as_view(), name='request-list'),
    path('request/approval/<int:pk>/', RequestChangeApprovalView.as_view(), name='request-approval'),
    path('team/list/', TeamTaskListView.as_view(), name='team-list'),
    path('team/add/<int:pk>/', TeamTaskAddUsers.as_view(), name='team-add'),
    path('team/delete/user/<int:pk>/', TeamUserDeleteView.as_view(), name='team-delete-user'),

]
