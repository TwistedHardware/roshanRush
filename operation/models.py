from django.db import models

class Location(models.Model):
    """
    This represents a tree of all operations
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("self", null=True, blank=True)
    help = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.get_path()
    
    def get_path(self):
        if self.parent is None:
            return self.name
        else:
            temp_parent = self.parent
            path = []
            path.append(self.name)
            while not temp_parent is None:
                path.append(temp_parent.name)
                temp_parent = temp_parent.parent
            return "\\".join(path)
        
    """
    Classes
    """
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class Link(models.Model):
    """
    Represents a link between two processes
    """
    
    """
    options
    """
    type_options = (
                    ("input", "Input"),
                    ("output", "Output"),
                    )
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=type_options)
    content_type = models.CharField(max_length=200, default='text/plain')
    optional = models.BooleanField(default=False)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"


class Operation(models.Model):
    """
    Represents an operation that the system can perform
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    operation_code = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Operation"
        verbose_name_plural = "Operations"


class OperationParameter(models.Model):
    """
    Represents a parameter of an operation
    """
    
    """
    Fields
    """
    operation = models.ForeignKey(Operation)
    name = models.CharField(max_length=200)
    default_value = models.CharField(max_length=200, null=True, blank=True)
    help = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.operation.name, self.name)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Operation Parameter"
        verbose_name_plural = "Operation Parameters"


class OperationLink(models.Model):
    """
    Represents a link of an operation like an input or an output
    """
    
    """
    Fields
    """
    operation = models.ForeignKey(Operation)
    link = models.ForeignKey(Link)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.operation.name, self.link.name)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Operation Link"
        verbose_name_plural = "Operation Links"