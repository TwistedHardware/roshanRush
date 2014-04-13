from django.db import models
from django.contrib.auth.models import User


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


class APIParameter(models.Model):
    """
    Represents a parameter for an API
    """
    
    """
    Fields
    """
    api = models.ForeignKey(API)
    name = models.CharField(max_length=200)
    default_value = models.CharField(max_length=200)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name


class APITokens(models.Model):
    """
    Represents a token to be used for API authentication
    """
    
    """
    Fields
    """
    user = models.ForeignKey(User)
    api = models.ForeignKey(API)
    create_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.token