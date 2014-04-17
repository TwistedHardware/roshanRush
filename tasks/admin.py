from django.contrib import admin
import models


class TaskInline(admin.TabularInline):
    model = model = models.Task
    extra = 0


class TaskParameterInline(admin.TabularInline):
    model = model = models.TaskParameter
    extra = 0

class WorkerAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'ip',
              'concurrency',
              'online',
              ]
    list_display = [
              'ip',
              'concurrency',
              'online',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [TaskInline]


class TaskAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'type',
              'status',
              'start_time',
              'finish_time',
              'output',
              'progress',
              'progress_details',
              'estimated_finish_time',
              'celery_id',
              'worker',
              ]
    list_display = [
              'type',
              'status',
              'start_time',
              'finish_time',
              'progress',
              'progress_details',
              'estimated_finish_time',
              'worker',
                    ]
    filter_horizontal = []
    list_filter = [
              'type',
              'status',
              'worker',
                   ]
    inlines = [TaskParameterInline]
    

admin.site.register(models.Worker, WorkerAdmin)
admin.site.register(models.Task, TaskAdmin)
