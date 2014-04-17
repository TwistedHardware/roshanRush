from django.contrib import admin
import models
import forms

class ProcessOperationInline(admin.TabularInline):
    model = models.ProcessOperation
    extra = 0


class ProcessOperationLinkInline(admin.TabularInline):
    model = models.ProcessOperationLink
    extra = 0


class ProcessOperationParameterInline(admin.TabularInline):
    model = models.ProcessOperationParameter
    extra = 0


class ProcessConnectionInline(forms.ProcessConnectionLine):
    form = forms.ProcessConnectionLineForm
    model = models.ProcessConnection
    extra = 0


class ProcessAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    form = forms.ProcessAdminForm
    list_per_page = 100
    fields = [
              'name',
              'api',
              'api_source',
              ]
    list_display = [
              'name',
              'api',
              'api_source',

                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [
               ProcessOperationInline,
               ProcessConnectionInline
               ]
    
    
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
              'sequence',
              ]
    list_display = [
              'operation',
              'process',
              'location_x',
              'location_y',
              'sequence',
                    ]
    filter_horizontal = []
    list_filter = ['process']
    inlines = [
               ProcessOperationLinkInline,
               ProcessOperationParameterInline,
               ]


admin.site.register(models.Process, ProcessAdmin)
admin.site.register(models.ProcessOperation, ProcessOperationAdmin)