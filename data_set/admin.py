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


class RecordInline(admin.TabularInline):
    model = model = models.Record
    extra = 0


class DataSetInline(admin.TabularInline):
    model = model = models.DataSet
    extra = 0


class FeatureInline(admin.TabularInline):
    model = model = models.Feature
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
    inlines = [DataSetInline]


class DataSetTypeAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'columns'
              ]
    list_display = [
                    'name',
                    ]
    filter_horizontal = ['columns']
    list_filter = []
    inlines = [DataSetInline]

class DataSetAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'data_group',
              'type',
              ]
    list_display = [
                    'name',
                    'data_group',
                    'type',
                    ]
    filter_horizontal = []
    list_filter = [
              'data_group',
              'type',
                   ]
    inlines = [RecordInline]


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
    inlines = [FeatureInline]


class FeatureAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'description',
              'formula',
              'type',
              'parent',
              ]
    list_display = [
              'name',
              'description',
              'formula',
              'type',
              'parent',
                    ]
    filter_horizontal = []
    list_filter = []


class RecordAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'create_date',
              'name',
              'data_set',
              'original_id',
              ]
    list_display = [
              'create_date',
              'name',
              'data_set',
              'original_id',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [
               NumberFeatureInline,
               DateFeatureInline,
               TextFeatureInline,
               ImageFeatureInline,
               RecordLinkFeatureInline,
               BooleanFeatureInline,
               
               ]


admin.site.register(models.DataGroup, DataGroupAdmin)
admin.site.register(models.DataSetType, DataSetTypeAdmin)
admin.site.register(models.DataSet, DataSetAdmin)
admin.site.register(models.FeatureType, FeatureTypeAdmin)
admin.site.register(models.Feature, FeatureAdmin)
admin.site.register(models.Record, RecordAdmin)
