from django.db import models


class API(models.Model):
    """
    Represents an API for a process
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "API"
        verbose_name_plural = "APIs"