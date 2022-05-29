from django.urls import path

from task import views

app_name = 'task'

urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('list/', views.TaskListView.as_view(), name='task-list'),
    path('detail/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('update/<int:pk>/', views.RequestChangeTaskView.as_view(), name='task-update'),
    path('request/list/', views.RequestTaskListView.as_view(), name='request-list'),
    path('request/approval/<int:pk>/', views.RequestChangeApprovalView.as_view(), name='request-approval'),
    path('team/list/', views.TeamTaskListView.as_view(), name='team-list'),
    path('team/add/<int:pk>/', views.TeamTaskAddUsers.as_view(), name='team-add'),
    path('team/delete/user/<int:pk>/', views.TeamUserDeleteView.as_view(), name='team-delete-user'),

]
