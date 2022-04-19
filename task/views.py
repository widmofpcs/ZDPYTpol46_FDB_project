from django.shortcuts import render, redirect, get_object_or_404
from django import views
from django.views.generic import ListView

from task.form import TaskCreateForm, EmployeeRequestChangeTask
from task.models import Task


class TaskListView(ListView):
    model = Task


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
        form = EmployeeRequestChangeTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
