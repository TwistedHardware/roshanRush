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
    api_source = models.ForeignKey("ProcessOperationLink", null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    def execute_process(self):
        """
        Executes a process by running all operations inside
        """
        
        # Run Each Operation
        output = {}
        input = {}
        parameters = {}
        for operation in self.processoperation_set.all().order_by("sequence"):
            #Prepare Variables
            parameters[operation.sequence] = {}
            output[operation.sequence] = {}
            input[operation.sequence] = {}
            
            # Load input
            for connection in self.processconnection_set.all().filter(to_operation__operation=operation):
                output_sequense = connection.from_operation.operation.sequence
                output_name = connection.from_operation.link.link.name
                input[operation.sequence][connection.to_operation.link.link.name] = output[output_sequense][output_name]
            
            # Load parameters
            for parameter in operation.processoperationparameter_set.all():
                if not parameter.assigned_link is None and parameter.assigned_link.input_connection_set.all().exists():
                    parameters[operation.sequence][parameter.parameter.name] = input[operation.sequence][parameter.assigned_link.link.link.name]
                elif parameter.value in [None, ""]:
                    parameters[operation.sequence][parameter.parameter.name] = eval(parameter.parameter.default_value)
                else:
                    parameters[operation.sequence][parameter.parameter.name] = eval(parameter.value)
            
            # Prepare environment
            i=input[operation.sequence]
            p=parameters[operation.sequence]
            o={}
            
            # Execute Operation
            exec operation.operation.operation_code
            
            # Store Output
            output[operation.sequence] = o
        
        if not self.api_source is None:
            return output[self.api_source.operation.sequence][self.api_source.link.link.name], 'text/plain'
            
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
    sequence = models.IntegerField(default=-1)

    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.process.name, self.operation.name)
    
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
        return "%s: %s" % (self.operation.operation.name, self.link.link.name)
    
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
    value = models.CharField(max_length=200, null=True, blank=True)
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
    from_operation = models.ForeignKey(ProcessOperationLink, related_name="output_connection_set")
    to_operation = models.ForeignKey(ProcessOperationLink, related_name="input_connection_set")
    
    """
    Methods
    """
    def __unicode__(self):
        return "FROM:%s - TO:%s" % (self.from_operation.operation.operation.name, self.to_operation.operation.operation.name)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Process Connection"
        verbose_name_plural = "Process Connections"