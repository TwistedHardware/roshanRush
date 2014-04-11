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


class ProcessOperationLink(models.Model):
    """
    Represents an operation link that can connect it to other operations
    """
    
    """
    Fields
    """
    operation = models.ForeignKey(ProcessOperation)
    link = models.ForeignKey(OperationLink)


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