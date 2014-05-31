import pandas as pd
import zipfile
import os.path
import os
#
from django.db import models
from roshanRush import settings
#
from data_set.models import DataSet,Feature#BooleanFeature,DateFeature,FileFeature,NumberFeature,RecordLinkFeature,TextFeature,


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
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save to process the uploaded file and create CSVColumn(s) for a new Import
        """
        
        # Check if the ImportCSV is being added
        if self.pk is None:
            # Call the default save for the operation
            super(ImportCSV, self).save(*args, **kwargs)
            
            # Create column(s)
            self.create_columns()
        else:
            # Call the default save for the operation
            super(ImportCSV, self).save(*args, **kwargs)
            
    def create_columns(self):
        """
        Creates columns for a new CSV Import
        """
        # Read the CSV File
        raw_data = pd.read_csv(self.file, nrows=20)
        print raw_data.columns
        
        # Add CSVColumns
        for column in raw_data.columns:
            self.csvcolumn_set.all().create(
                                            import_csv=self,
                                            csv_column=column
                                            )
    
    """
    Classes
    """
    class Meta:
        verbose_name = "CSV Import"
        verbose_name_plural = "CSV Imports"


class CSVColumn(models.Model):
    """
    Represents a CSV file column and mapping to a feature
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


class ImportDICOM(models.Model):
    """
    Represents a record of importing a DICOM Sequence
    """
    
    """
    Fields
    """
    create_time = models.DateTimeField(auto_now_add=True)
    data_set = models.ForeignKey(DataSet, null=True, blank=True)
    comppressed_file = models.FileField(upload_to="DICOM", null=True, blank=True)
    
    """
    Methods
    """
    def ___unicode__(self):
        return self.file.name
    
    def save(self, *args, **kwargs):
        """
        Override the default save to unzip the compressed file (if exists) and add all files inside
        """
        if self.pk is None:
            super(ImportDICOM, self).save(*args, **kwargs)
            files_list = self.unzip_file()
            for name, dirname in files_list:
                if not name in [None, ""] and name.lower().endswith("dcm"):
                    self.dicomfile_set.all().create(
                                                import_dicom = self,
                                                file = "%s/%s" % (dirname, name)
                                                )
            
    
    def unzip_file(self):
        """
        unzips a file and adds all files inside it as DICOMFile(s)
        """ 
        files_list = []
        if not self.comppressed_file is None:
            zfile = zipfile.ZipFile("%s/%s" % (settings.MEDIA_ROOT, self.comppressed_file.name))
            for name in zfile.namelist():
                (dirname, filename) = os.path.split(name)
                rel_dirname = "DICOM/%s" % (dirname)
                dirname = "%s/DICOM/" % (settings.MEDIA_ROOT)
                files_list.append([filename, rel_dirname])
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                zfile.extract(name, dirname)
        return files_list

    """
    Classes
    """
    class Meta:
        verbose_name = "DICOM Import"
        verbose_name_plural = "DICOM Imports"


class DICOMFile(models.Model):
    """
    Represents a single DICOM File
    """
    
    """
    Fields
    """
    import_dicom = models.ForeignKey(ImportDICOM)
    file = models.FileField(upload_to="DICOM")
    
    """
    Methods
    """
    def ___unicode__(self):
        return self.csv_column
    
    """
    Classes
    """
    class Meta:
        verbose_name = "DICOM File"
        verbose_name_plural = "DICOM Files"

