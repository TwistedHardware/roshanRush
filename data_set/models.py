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
    Options
    """
    feature_db_type_options = (
                               ("date", "Date Time"),
                               ("number", "Number"),
                               ("boolean", "Boolean"),
                               ("text", "Text"),
                               ("file", "File"),
                               ("relation", "Relation"),
                               )
    
    """
    Fields
    """
    name = models.CharField(max_length=200)
    feature_type = models.CharField(max_length=20, choices=feature_db_type_options)
    
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
    related_to = models.ForeignKey(DataSet, null=True, blank=True, help_text="Use only for Relation Features")
    
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
    name = models.CharField(max_length=200, null=True, blank=True)
    original_id = models.BigIntegerField(null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save to insert features for new DataSets
        """
        
        # Check if it is a new DataSet
        if self.pk is None:
            # Call Parent Save
            super(Record, self).save(*args, **kwargs)
            for feature in self.data_set.type.columns.all():
                if feature.type.feature_type == "date":
                    self.datefeature_set.all().create(
                                                      record=self,
                                                      feature=feature,
                                                      )
                elif feature.type.feature_type == "number":
                    self.numberfeature_set.all().create(
                                                      record=self,
                                                      feature=feature,
                                                      )
                elif feature.type.feature_type == "boolean":
                    self.booleanfeature_set.all().create(
                                                      record=self,
                                                      feature=feature,
                                                      )
                elif feature.type.feature_type == "text":
                    self.textfeature_set.all().create(
                                                      record=self,
                                                      feature=feature,
                                                      )
                elif feature.type.feature_type == "file":
                    self.textfeature_set.all().create(
                                                      record=self,
                                                      feature=feature,
                                                      )
                elif feature.type.feature_type == "relation":
                    self.recordlinkfeature_set.all().create(
                                                      record=self,
                                                      feature=feature,
                                                      data_set=feature.related_to,
                                                      )
        else:
            super(Record, self).save(*args, **kwargs)
    
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


class FileFeature(models.Model):
    """
    Represents a type of records
    """
    
    """
    Fields
    """
    record = models.ForeignKey(Record)
    feature = models.ForeignKey(Feature)
    value = models.FileField(upload_to="files", null=True, blank=True)
    
    """
    Methods
    """
    def __unicode__(self):
        return "%s: %s" % (self.feature.name, self.value)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "File Feature"
        verbose_name_plural = "File Features"


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