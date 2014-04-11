from django.contrib import admin
import models

class ProcessOperationInline(admin.TabularInline):
    model = model = models.ProcessOperation
    extra = 0


class ProcessOperationLinkInline(admin.TabularInline):
    model = model = models.ProcessOperationLink
    extra = 0


class ProcessOperationParameterInline(admin.TabularInline):
    model = model = models.ProcessOperationParameter
    extra = 0


class ProcessConnectionInline(admin.TabularInline):
    model = model = models.ProcessConnection
    extra = 0


class ProcessAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'api',
              ]
    list_display = [
              'name',
              'api',

                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [ProcessOperationInline]
    
    
class ProcessOperationAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'process',
              'operation',
              'location_x',
              'location_y',
              ]
    list_display = [
              'process',
              'operation',
              'location_x',
              'location_y',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [
               ProcessOperationLinkInline,
               ProcessOperationParameterInline,
               ProcessConnectionInline,
               ]