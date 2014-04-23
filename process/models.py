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
        operation_input = {}
        parameters = {}
        for operation in self.processoperation_set.all().order_by("sequence"):
            #Prepare Variables
            parameters[operation.sequence] = {}
            output[operation.sequence] = {}
            operation_input[operation.sequence] = {}
            
            # Load operation_input
            for connection in self.processconnection_set.all().filter(to_operation__operation=operation):
                print connection
                output_sequense = connection.from_operation.operation.sequence
                output_name = connection.from_operation.link.link.name
                operation_input[operation.sequence][connection.to_operation.link.link.name] = output[output_sequense][output_name]
            
            # Load parameters
            for parameter in operation.processoperationparameter_set.all():
                print parameter
                if not parameter.assigned_link is None and parameter.assigned_link.input_connection_set.all().exists():
                    parameters[operation.sequence][parameter.parameter.name] = operation_input[operation.sequence][parameter.assigned_link.link.link.name]
                elif parameter.value in [None, ""]:
                    parameters[operation.sequence][parameter.parameter.name] = eval(parameter.parameter.default_value)
                else:
                    parameters[operation.sequence][parameter.parameter.name] = eval(parameter.value)
            
            # Prepare environment
            i=operation_input[operation.sequence]
            p=parameters[operation.sequence]
            o={}
            
            # Execute Operation
            print p
            exec operation.operation.operation_code
            print "F"
            
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
    name = models.CharField(max_length=200, blank=True, default='')
    process = models.ForeignKey(Process)
    operation = models.ForeignKey(Operation)
    location_x = models.IntegerField(null=True, blank=True)
    location_y = models.IntegerField(null=True, blank=True)
    sequence = models.IntegerField(default=-1)
    
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.process.name, self.operation.name)
    
    def get_parameters(self):
        return ", ".join(["%s:%s" % (parameter.name, parameter.value) for parameter in self.processoperationparameter_set.all()])
    
    def get_new_name(self):
        qs = self.process.processoperation_set.all().filter(operation=self.operation, name__startswith="_%s_" % self.name).order_by("-name")
        if len(qs)==0:
            return "_%s_%05d" % (self.operation.name, int(0))
        else:
            return "_%s_%05d" % (self.operation.name, qs[0].name[:-5])
        
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save to create links and parameters of a new operator
        """ 
        
        # Check if a new operation is being added
        if self.pk is None:
            # Check if the operation is manually named
            if self.name == "":
                self.name = self.get_new_name()
            
            # Call the default save for the operation
            super(ProcessOperation, self).save(*args, **kwargs)
            
            # create Link(s) and Parameter(s) for an operation
            self.prepare_operation()
            
        else:
            # Call the default save for the operation
            super(ProcessOperation, self).save(*args, **kwargs)
    
    def prepare_operation(self):
        """
        Creates Link(s) and Parameter(s) for an operation
        """
        
        # Add links
        for link in self.operation.operationlink_set.all():
            self.processoperationlink_set.all().create(
                                                        operation = self,
                                                        link = link,
                                                        )
            
        # Add links
        for parameter in self.operation.operationparameter_set.all():
            self.processoperationparameter_set.all().create(
                                                            operation=self,
                                                            parameter=parameter,
                                                            value=parameter.default_value,
                                                            assigned_link=self.processoperationlink_set.all().get(link=parameter.assigned_link),
                                                            )
    
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
    
    def connected_to(self):
        return ", ".join([connection for connection in self.processconnection_set.all()])
    
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
    
    def default_value(self):
        return self.parameter.default_value
    
    def help(self):
        return self.parameter.help
    
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