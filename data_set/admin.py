from django.contrib import admin
import models


class DateFeatureInline(admin.TabularInline):
    model = models.DateFeature
    extra = 0


class NumberFeatureInline(admin.TabularInline):
    model = model = models.NumberFeature
    extra = 0


class TextFeatureInline(admin.TabularInline):
    model = model = models.TextFeature
    extra = 0
    

class ImageFeatureInline(admin.TabularInline):
    model = model = models.ImageFeature
    extra = 0
    

class RecordLinkFeatureInline(admin.TabularInline):
    model = model = models.RecordLinkFeature
    extra = 0
    

class BooleanFeatureInline(admin.TabularInline):
    model = model = models.BooleanFeature
    extra = 0


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


admin.site.register(models.DataGroup, DataGroupAdmin)
admin.site.register(models.DataSetType, DataSetTypeAdmin)
admin.site.register(models.DataSet, DataSetAdmin)
admin.site.register(models.FeatureType, FeatureTypeAdmin)
admin.site.register(models.Feature, FeatureAdmin)
admin.site.register(models.Record, RecordAdmin)
