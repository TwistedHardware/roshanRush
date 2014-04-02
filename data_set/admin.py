from django.contrib import admin
from .models import DataGroup, DataSetType, DataSet, FeatureType, Feature, Record

class DataGroupAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = []
    list_filter = []


class DataSetTypeAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = []
    list_filter = []

class DataSetAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = []
    list_filter = []


class FeatureTypeAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = []
    list_filter = []


class FeatureAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = []
    list_filter = []


class RecordAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = []
    list_filter = []


admin.site.register(DataGroup, DataGroupAdmin)
admin.site.register(DataSetType, DataSetTypeAdmin)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(FeatureType, FeatureTypeAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Record, RecordAdmin)
