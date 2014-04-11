from django.contrib import admin
import models

class APIAdmin(admin.ModelAdmin):
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
    inlines = []


admin.site.register(models.API, APIAdmin)