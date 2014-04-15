from django.contrib import admin
import models


class APIParameterInline(admin.TabularInline):
    model = models.APIParameter
    extra = 0


class APITokenInline(admin.TabularInline):
    model = models.APIToken
    extra = 0


class APIUsageInline(admin.TabularInline):
    model = models.APIUsage
    extra = 0


class APIAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'require_token'
              ]
    list_display = [
              'name',
              'require_token'
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [
               APIParameterInline,
               APITokenInline,
               APIUsageInline,
               ]


admin.site.register(models.API, APIAdmin)