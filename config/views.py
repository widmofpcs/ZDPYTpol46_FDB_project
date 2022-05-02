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
