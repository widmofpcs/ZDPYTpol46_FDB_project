from django.contrib import admin

# Register your models here.
from task.models import Task, RequestChangeTask

admin.site.register(Task)
admin.site.register(RequestChangeTask)
