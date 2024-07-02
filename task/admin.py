from django.contrib import admin

# Register your models here.
from task.models import Task, RequestChangeTask, TeamTask

admin.site.register(Task)
admin.site.register(RequestChangeTask)
admin.site.register(TeamTask)