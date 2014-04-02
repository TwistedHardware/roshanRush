from django.db import models

class DataGroup(models.Model):
    """
    Represents a type of records
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


class DataSetType(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    columns = models.ManyToManyField("Feature", limit_choices_to={'parent': None})
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name


class DataSet(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    data_group = models.ForeignKey(DataGroup)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    

class FeatureType(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)


class Feature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    formula = models.TextField(null=True, blank=True)
    type = models.ForeignKey(FeatureType)
    parent = models.ForeignKey("self", null=True, blank=True)


class Record(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    data_set = models.ForeignKey(DataSet)
    create_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, null=True, blank=True, default=str(create_date))
    original_id = models.BigIntegerField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    

class DateFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.DateTimeField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)
    

class NumberFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.FloatField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)
    

class BooleanFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.NullBooleanField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)


class TextFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.TextField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)


class ImageFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.ImageField(upload_to='images', null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)


class RecordLinkFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    data_set = models.ForeignKey(DataSet)
    value = models.BigIntegerField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)