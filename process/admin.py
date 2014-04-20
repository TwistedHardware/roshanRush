from django.contrib import admin
import models
import forms

class ProcessOperationInline(forms.ProcessOperationLine):
    model = models.ProcessOperation
    extra = 0
    
    fields = ['operation', 'name', 'sequence']


class ProcessOperationLinkInline(admin.TabularInline):
    model = models.ProcessOperationLink
    extra = 0
    max_num=0
    can_delete = False
    readonly_fields = ['link', 'connected_to']


class ProcessOperationParameterInline(admin.TabularInline):
    model = models.ProcessOperationParameter
    extra = 0
    max_num=0
    can_delete = False
    #fields = ['parameter', 'value', 'assigned_link']
    readonly_fields = ['parameter', 'default_value', 'help', 'assigned_link']


class ProcessConnectionInline(forms.ProcessConnectionLine):
    formset = forms.ProcessConnectionFormSet
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
              'name',
              'process',
              'operation',
              'location_x',
              'location_y',
              'sequence',
              ]
    list_display = [
              'name',
              'operation',
              'process',
              'location_x',
              'location_y',
              'sequence',
                    ]
    filter_horizontal = []
    list_filter = ['process']
    inlines = [
               ProcessOperationParameterInline,
               ProcessOperationLinkInline,
               ]


admin.site.register(models.Process, ProcessAdmin)
admin.site.register(models.ProcessOperation, ProcessOperationAdmin)