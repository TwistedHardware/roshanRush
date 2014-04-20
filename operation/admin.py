from django.contrib import admin
#
import models
import forms


class OperationInline(admin.TabularInline):
    model = model = models.Operation
    extra = 0


class OperationParameterInline(admin.TabularInline):
    formset = forms.OperationParameterFormSet
    form = forms.OperationParameterForm
    model = model = models.OperationParameter
    extra = 0


class OperationLinkInline(admin.TabularInline):
    model = model = models.OperationLink
    extra = 0


class LocationAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'parent',
              'help',
              ]
    list_display = [
              'name',
              'parent',
              'help',

                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [OperationInline]


class LinkAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'type',
              'optional',
              ]
    list_display = [
              'name',
              'type',
              'optional',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = []


class OperationAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'location',
              'operation_code',
              ]
    list_display = [
              'name',
              'location',
              'operation_code',
                    ]
    filter_horizontal = []
    list_filter = ['location']
    inlines = [OperationLinkInline, OperationParameterInline]


admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Link, LinkAdmin)
admin.site.register(models.Operation, OperationAdmin)