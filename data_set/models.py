from datetime import datetime
import pandas as pd
#
from django.db import models

class DataGroup(models.Model):
    """
    Represents a group an Data Sets
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
    Represents a schema for a Data Set
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
    Represents a Data Set which is basically a table of data that has the same schema
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
    
    def to_DataFrame(self, truncate=False, filter_features=None):
        """
        Returns a dataframe representing the dataset
        """
        # Load all features
        if filter_features:
            records = NumberFeature.objects.all().filter(feature__name=filter_features[0], value=filter_features[1]).values_list("record__id")
            records = [item[0] for item in records]
        else:
            records = [item[0] for item in self.record_set.all().values_list("id")]
        date_features = list(DateFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        numerical_features = list(NumberFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        boolean_features = list(BooleanFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        text_features = list(TextFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        file_features = list(FileFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value"))
        record_link_features = list(RecordLinkFeature.objects.all().filter(record__id__in=records).values("record__id", "feature__name", "value", "data_set__id"))
        
        # Create dataset with record__id as index
        dataset = pd.DataFrame({"record__id": records})
        dataset.set_index("record__id", inplace=True)
        
        # Process date features
        if len(date_features) <> 0:
            date_df = pd.DataFrame(date_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            date_df = pd.DataFrame()
        
        # Process number features
        if len(numerical_features) <> 0:
            numerical_df = pd.DataFrame(numerical_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            numerical_df = pd.DataFrame()
        
        # Process boolean features
        if len(boolean_features) <> 0:
            boolean_df = pd.DataFrame(boolean_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            boolean_df = pd.DataFrame()
        
        # Process text features
        if len(text_features) <> 0:
            text_df = pd.DataFrame(text_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            text_df = pd.DataFrame()
        
        # Process file features
        if len(file_features) <> 0:
            file_df = pd.DataFrame(file_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            file_df = pd.DataFrame()
        
        # Process record link features
        if len(record_link_features) <> 0:
            record_link_df = pd.DataFrame(record_link_features).pivot(index="record__id", columns="feature__name", values="value")
        else:
            record_link_df = pd.DataFrame()
        
        if truncate:
            tr = lambda x: [str(item)[:100] for item in x]
            return pd.concat([dataset, date_df, numerical_df, boolean_df, text_df, file_df, record_link_df], axis=1).apply(tr)
        
        # Concatenate all features DataFrames to the Main IDs DataFrame and return it
        return pd.concat([dataset, date_df, numerical_df, boolean_df, text_df, file_df, record_link_df], axis=1)
    
    """
    Classes
    """
    class Meta:
        verbose_name = "Data Set"
        verbose_name_plural = "Data Sets"
    

class FeatureType(models.Model):
    """
    Represents a type of features
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
    Represents a feature which is basically a column in a Data Set
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
    Represents a record in a Data Set
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
        return "%s" % self.create_date
    
    def feature(self, feature, value=None, date_format="%Y%m%d"):
        """
        Sets or get the value of a feature
        """
        # Check the faeture_type
        if feature.type.feature_type == "date":
            value = datetime.strptime(str(value), date_format)
            record_feature = self.datefeature_set.all().get(
                                                record=self,
                                                feature=feature,
                                                )
        elif feature.type.feature_type == "number":
            record_feature = self.numberfeature_set.all().get(
                                                record=self,
                                                feature=feature,
                                                )
        elif feature.type.feature_type == "boolean":
            record_feature =  self.booleanfeature_set.all().get(
                                                record=self,
                                                feature=feature,
                                                )
        elif feature.type.feature_type == "text":
            record_feature =  self.textfeature_set.all().get(
                                              record=self,
                                              feature=feature,
                                              )
        elif feature.type.feature_type == "file":
            record_feature =  self.textfeature_set.all().get(
                                              record=self,
                                              feature=feature,
                                              )
        elif feature.type.feature_type == "relation":
            record_feature =  self.recordlinkfeature_set.all().get(
                                                record=self,
                                                feature=feature,
                                                )
        
        # Check if a value is set
        if not value is None:
            record_feature.value = value
            record_feature.save()
        
        return record_feature
    
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
    Represents a Feature of type Date
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
    Represents a Feature of type Number
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
    Represents a Feature of type Boolean
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
    Represents a Feature of type Text
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
    Represents a Feature of type File
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
    Represents a Feature of type Record Link which links one Data Set
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