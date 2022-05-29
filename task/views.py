from django.shortcuts import render, redirect, get_object_or_404
from django import views
from django.contrib import messages
from django.views.generic import ListView, DetailView

from accounts.models import CustomUser
from config.mixins import ManagerRequiredMixin
from task.form import TaskCreateForm, EmployeeRequestChangeTask, AddUserToTeam
from task.models import Task, RequestChangeTask, TeamTask


class TaskListView(ListView):
    model = Task


class TaskDetailView(DetailView):
    model = Task


class RequestTaskListView(ManagerRequiredMixin, ListView):
    model = RequestChangeTask
    template_name = 'task/request_change_list.html'
    ordering = ['-id']


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
            messages.add_message(request, messages.SUCCESS, 'Task created successfully!')
        return redirect('home')


class RequestChangeTaskView(views.View):
    def get(self, request, pk):
        if RequestChangeTask.objects.filter(task_id=pk, status='1').exists():
            messages.add_message(request, messages.ERROR, 'You cannot edit this task, previous request is waiting. '
                                                          'Contact Your manager.')
            return redirect('task:task-list')
        else:
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
            form.instance.task = task
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Request sent')
        return redirect('home')


class RequestChangeApprovalView(views.View):
    def get(self, request, pk):
        waiting_task = get_object_or_404(RequestChangeTask, id=pk)
        task = get_object_or_404(Task, id=waiting_task.task.id)
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
            Task.objects.filter(id=waiting_task.task.id).update(
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
            messages.add_message(request, messages.SUCCESS, 'Changes saved')
            return redirect('task:request-list')

        elif 'deletebtn' in request.POST:
            RequestChangeTask.objects.filter(id=pk).update(
                status='3',
                review_by=self.request.user
            )
            messages.add_message(request, messages.SUCCESS, 'Changes rejected')
            return redirect('task:request-list')


class TeamTaskListView(ListView):
    model = TeamTask
    template_name = 'task/team_task_list.html'

    def get_queryset(self):
        obj_list = []
        teams = TeamTask.objects.values_list('name').distinct()
        for team in teams:
            res = TeamTask.objects.filter(name=team[0]).first()
            obj_list.append(res)
        return obj_list


class TeamTaskAddUsers(views.View):
    def get(self, request, pk):
        team = get_object_or_404(TeamTask, id=pk)
        users = TeamTask.objects.filter(task=team.task, name=team.name)
        users_to_exclude = TeamTask.objects.filter(task=team.task, name=team.name).values_list('user_id_id',
                                                                                               flat=True)
        form = AddUserToTeam()
        form.fields['user_id'].queryset = CustomUser.objects.exclude(id__in=users_to_exclude).exclude(is_superuser=True)
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
                task_id=team.task.id,
                user_id=form.instance.user_id
            )
            messages.add_message(request, messages.SUCCESS, 'User added to a team')
        return redirect('task:team-add', pk=pk)


class TeamUserDeleteView(views.View):
    def get(self, request, pk):
        team = get_object_or_404(TeamTask, id=pk)
        return render(
            request,
            'task/delete_user_from_team.html',
            context={
                'team': team
            }
        )

    def post(self, request, pk):
        team = get_object_or_404(TeamTask, id=pk)
        if 'btnyes' in request.POST:
            team.delete()
            messages.add_message(request, messages.SUCCESS, 'Team deleted')
            return redirect('task:team-list')
        elif 'btnno' in request.POST:
            return redirect('task:team-add', pk)
