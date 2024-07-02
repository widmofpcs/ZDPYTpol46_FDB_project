from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from task.models import Task, TeamTask


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        teams = TeamTask.objects.filter(user_id=request.user.id)
        task = teams.values_list('task_id_id')
        context["tasks"] = Task.objects.filter(id__in=task).exclude(is_active=False)
        context['teams'] = teams
        return self.render_to_response(context)

    def post(self, request):
        task_id = request.POST.get('task')
        time = request.POST.get('consumed_time')
        task = get_object_or_404(Task, id=task_id)
        res = float(task.consumed_time) + float(time)
        task.consumed_time = res
        task.save()
        return redirect('home')
