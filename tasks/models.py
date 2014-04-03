from django.db import models

class Task(models.Model):
    """
    Represents a task that the system executes
    """
    
    """
    Options
    """
    task_status_options = (
                   ("Received","Received"),
                   ("Started","Started"),
                   ("Success","Success"),
                   ("Failed","Failed")
                   )

    
    """
    Fields
    """
    type = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=task_status_options)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(null=True, blank=True)
    output = models.TextField(null=True, blank=True)
    progress = models.FloatField(default=0)
    progress_details = models.TextField(null=True, blank=True)
    estimated_finish_time = models.DateTimeField(null=True, blank=True)
    celery_id = models.CharField(max_length=200)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.type
    
    def parameters_text(self):
        return ", ".join([item.__unicode__() for item in  self.taskparameter_set.all()])
    

class TaskParameter(models.Model):
    """
    Represents a parameter of a task
    """
    
    """
    Options
    """
    parameter_type_options = (
                              ("value","value"),
                              ("reference","reference"),
                              )
    
    """
    Fields
    """
    task = models.ForeignKey(Task)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    value = models.FloatField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.name, self.value)
    