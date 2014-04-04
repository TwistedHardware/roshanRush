from django.contrib import admin
import models


class CSVColumnInline(admin.TabularInline):
    model = model = models.CSVColumn
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


admin.site.register(models.ImportCSV, ImportCSVAdmin)