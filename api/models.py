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
    require_token = models.BooleanField(default=False)
    
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


class APIToken(models.Model):
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


class APIUsage(models.Model):
    """
    Represents a log for API access using a token
    """
    
    """
    Options
    """
    response_code_options = (
                             ("success", "Success"),
                             ("decline", "Decline"),
                             ("fail", "Fail"),
                             )
    
    """
    Fields
    """
    api = models.ForeignKey(API)
    token = models.ForeignKey(APIToken, null=True, blank=True)
    parameters = models.TextField(null=True, blank=True)
    request_time = models.DateTimeField(auto_now_add=True)
    response_code = models.CharField(max_length=20, choices=response_code_options, null=True, blank=True)
    response_time = models.DateTimeField(null=True, blank=True)
    running_time = models.FloatField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s" % self.request_time