from django.shortcuts import render, redirect, get_object_or_404
from django import views
from django.views.generic import ListView

from accounts.models import CustomUser
from task.form import TaskCreateForm, EmployeeRequestChangeTask, AddUserToTeam
from task.models import Task, RequestChangeTask, TeamTask


class TaskListView(ListView):
    model = Task


class RequestTaskListView(ListView):
    model = RequestChangeTask
    template_name = 'task/request_change_list.html'


class TaskCreateView(views.View):
    def get(self, request):
        form = TaskCreateForm()
        return render(
            request,
            'task/create_task.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = TaskCreateForm(request.POST)

        if form.is_valid():
            form.instance.created_by = self.request.user
            form.save()
        return redirect('home')


class RequestChangeTaskView(views.View):
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = EmployeeRequestChangeTask(
            initial={
                'title': task.title,
                'description': task.description,
                'consumed_time': task.consumed_time,
                'rate': task.rate,
                'is_active': task.is_active,
            })
        return render(
            request,
            'task/create_task.html',
            context={
                'form': form
            }
        )

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = EmployeeRequestChangeTask(request.POST)
        if form.is_valid():
            form.instance.requested_by = self.request.user
            form.instance.task_id = task
            form.save()
        return redirect('home')


class RequestChangeApprovalView(views.View):
    def get(self, request, pk):
        waiting_task = get_object_or_404(RequestChangeTask, id=pk)
        task = get_object_or_404(Task, id=waiting_task.task_id.id)
        return render(
            request,
            'task/approval_change.html',
            context={
                'waiting_task': waiting_task,
                'task': task,
            }
        )

    def post(self, request, pk):
        waiting_task = get_object_or_404(RequestChangeTask, id=pk)
        if 'applybtn' in request.POST:
            Task.objects.filter(id=waiting_task.task_id.id).update(
                title=waiting_task.title,
                description=waiting_task.description,
                consumed_time=waiting_task.consumed_time,
                rate=waiting_task.rate,
                is_active=waiting_task.is_active
            )
            RequestChangeTask.objects.filter(id=pk).update(
                status='2',
                review_by=self.request.user
            )
            return redirect('task:request-list')

        elif 'deletebtn' in request.POST:
            RequestChangeTask.objects.filter(id=pk).update(
                status='3',
                review_by=self.request.user
            )
            return redirect('task:request-list')


class TeamTaskListView(ListView):
    model = TeamTask
    template_name = 'task/team_task_list.html'

    def get_queryset(self):
        name_list = []
        obj_list = []
        teams = TeamTask.objects.all()
        for team in teams:
            if team.name not in name_list:
                name_list.append(team.name)
                obj_list.append(team)
        return obj_list


# class TeamTaskListView(views.View):
#     def get(self, request):
#         object_list = TeamTask.objects.values('name').distinct()
#         return render(
#             request,
#             'task/team_task_list.html',
#             context={
#                 'object_list': object_list,
#             }
#         )


class TeamTaskAddUsers(views.View):
    def get(self, request, pk):
        team = get_object_or_404(TeamTask, id=pk)
        users = TeamTask.objects.filter(task_id=team.task_id, name=team.name)
        excludes = []
        for user in users:
            excludes.append(user.user_id.id)

        form = AddUserToTeam()
        form.fields['user_id'].queryset = CustomUser.not_super.exclude(id__in=excludes)
        # form.fields['user_id'].queryset = CustomUser.not_super.filter(users)
        return render(
            request,
            'task/add_user_to_team.html',
            context={
                'team': team,
                'form': form,
                'users': users,
            })

    def post(self, request, pk):
        team = get_object_or_404(TeamTask, id=pk)
        form = AddUserToTeam(request.POST)
        if form.is_valid():
            TeamTask.objects.create(
                name=team.name,
                task_id=team.task_id,
                user_id=form.instance.user_id
            )
        return redirect('task:team-add', pk=pk)
