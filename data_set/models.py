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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Data Group"
        verbose_name_plural = "Data Groups"


class DataSetType(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    columns = models.ManyToManyField("Feature", limit_choices_to={"parent": None})
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Data Set Type"
        verbose_name_plural = "Data Set Types"


class DataSet(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    data_group = models.ForeignKey(DataGroup)
    type = models.ForeignKey(DataSetType)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Data Set"
        verbose_name_plural = "Data Sets"
    

class FeatureType(models.Model):
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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Feature Type"
        verbose_name_plural = "Feature Types"


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
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Feature"
        verbose_name_plural = "Features"


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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Record"
        verbose_name_plural = "Records"
    

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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Date Feature"
        verbose_name_plural = "Date Features"
    

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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Number Feature"
        verbose_name_plural = "Number Features"
    

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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Boolean Feature"
        verbose_name_plural = "Boolean Features"


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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Text Feature"
        verbose_name_plural = "Text Features"


class ImageFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.ImageField(upload_to="images", null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Image Feature"
        verbose_name_plural = "Image Features"


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
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Record Link Feature"
        verbose_name_plural = "Record Link Features"