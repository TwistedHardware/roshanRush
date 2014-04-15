from django.db import models
from data_set.models import DataSet,BooleanFeature,DateFeature,ImageFeature,NumberFeature,RecordLinkFeature,TextFeature,Feature

class ImportCSV(models.Model):
    """
    Represents a record of importing data from CSV file
    """
    
    """
    Fields
    """
    file = models.FileField(upload_to="csv")
    create_time = models.DateTimeField(auto_now_add=True)
    data_set = models.ForeignKey(DataSet, null=True, blank=True)
    
    """
    Methods
    """
    def ___unicode__(self):
        return self.file.name
    
    """
    Classes
    """
    class Meta:
        verbose_name = "CSV Import"
        verbose_name_plural = "CSV Imports"


class CSVColumn(models.Model):
    """
    Represents a record of importing data from CSV file
    """
    
    """
    Fields
    """
    import_csv = models.ForeignKey(ImportCSV)
    csv_column = models.CharField(max_length=200)
    feature = models.ForeignKey(Feature, null=True, blank=True)
    
    """
    Methods
    """
    def ___unicode__(self):
        return self.csv_column
    
    """
    Classes
    """
    class Meta:
        verbose_name = "CSV Column"
        verbose_name_plural = "CSV Columns"