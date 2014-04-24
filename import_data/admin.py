from django.contrib import admin
import models


class CSVColumnInline(admin.TabularInline):
    model = model = models.CSVColumn
    extra = 0


class DICOMFileInline(admin.TabularInline):
    model = model = models.DICOMFile
    extra = 0


class ImportCSVAdmin(admin.ModelAdmin):
    """
    Manages admin interface for Import CSV
    """
    list_per_page = 100
    fields = [
              'file',
              'data_set',
              ]
    list_display = [
              'file',
              'data_set',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [CSVColumnInline]


class ImportDICOMAdmin(admin.ModelAdmin):
    """
    Manages admin interface for Import DICOM
    """
    list_per_page = 100
    fields = [
              'data_set',
              ]
    list_display = [
              'data_set',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [DICOMFileInline]


admin.site.register(models.ImportCSV, ImportCSVAdmin)
admin.site.register(models.ImportDICOM, ImportDICOMAdmin)