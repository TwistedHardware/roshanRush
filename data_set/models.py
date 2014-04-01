from django.db import models

class DateSet(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    
    
class RecordType(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    

class Record(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    type = models.ForeignKey(RecordType)
    create_date = models.DateTimeField(auto_now_add=True)
    