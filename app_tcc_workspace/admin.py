from django.contrib import admin
from app_tcc_workspace.models import Task
from .models import Message

admin.site.register(Task)
admin.site.register(Message)



