from django.contrib import admin
import models


class LibraryInline(admin.TabularInline):
    model = model = models.Library
    extra = 0


class AlgorithmInline(admin.TabularInline):
    model = model = models.Algorithm
    extra = 0

class AlgorithmTypeAdmin(admin.ModelAdmin):
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


class ProgrammingLanguageAdmin(admin.ModelAdmin):
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
    inlines = [LibraryInline]


class LibraryAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'language',

              ]
    list_display = [
              'name',
              'language',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [AlgorithmInline]


class DataProcessAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',
              'description',
              'process_code',

              ]
    list_display = [
              'name',
              'description',
              'process_code',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = []


class AlgorithmAdmin(admin.ModelAdmin):
    """
    Manages admin interface for data groups
    """
    list_per_page = 100
    fields = [
              'name',

              ]
    list_display = [
              'ip',

                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [LibraryInline]