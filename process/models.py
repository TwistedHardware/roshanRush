from django.db import models
from api.models import API
from operation.models import Operation, OperationLink, OperationParameter

class Process(models.Model):
    """
    Represents a process that executes operation(s)
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    api = models.ForeignKey(API, null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Process"
        verbose_name_plural = "Processes"

class ProcessOperation(models.Model):
    """
    Represents an operation inside a process
    """
    
    """
    Fields
    """
    process = models.ForeignKey(Process)
    operation = models.ForeignKey(Operation)
    location_x = models.IntegerField()
    location_y = models.IntegerField()
    
    """
    Methods
    """
    def __unicode__(self):
        return self.process.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Process Operation"
        verbose_name_plural = "Process Operations"


class ProcessOperationLink(models.Model):
    """
    Represents an operation link that connects it to other operations
    """
    
    """
    Fields
    """
    operation = models.ForeignKey(ProcessOperation)
    link = models.ForeignKey(OperationLink)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s" % self.operation
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Process Operation Link"
        verbose_name_plural = "Process Operation Links"



class ProcessOperationParameter(models.Model):
    """
    Represent a parameter of an operation
    """
    
    """
    Fields
    """
    operation = models.ForeignKey(ProcessOperation)
    parameter = models.ForeignKey(OperationParameter)
    value = models.CharField(max_length=200)
    assigned_link = models.ForeignKey(ProcessOperationLink, null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.parameter.name, self.value)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Process Operation Parameter"
        verbose_name_plural = "Process Operation Parameters"


class ProcessConnection(models.Model):
    """
    Represents an operation inside a process
    """
    
    """
    Fields
    """
    process = models.ForeignKey(Process)
    from_operation = models.ForeignKey(OperationLink, related_name="output_connection_set")
    to_operation = models.ForeignKey(OperationLink, related_name="input_connection_set")
    
    """
    Methods
    """
    def __unicode__(self):
        return "FROM:%s - TO:%s" % (self.from_operation.process.name, self.to_operation.process.name)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Process Connection"
        verbose_name_plural = "Process Connections"