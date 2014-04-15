from django.contrib import admin
import models


class LibraryInline(admin.TabularInline):
    model = model = models.Library
    extra = 0


class AlgorithmInline(admin.TabularInline):
    model = model = models.Algorithm
    extra = 0


class AlgorithmParameterInline(admin.TabularInline):
    model = model = models.AlgorithmParameter
    extra = 0


class ParameterValueInline(admin.TabularInline):
    model = model = models.ParameterValue
    extra = 0


class TrainedModelParameterInline(admin.TabularInline):
    model = model = models.TrainedModelParameter
    extra = 0


class TrainedModelFeatureInline(admin.TabularInline):
    model = model = models.TrainedModelFeature
    extra = 0


class TrainedModelSessionInline(admin.TabularInline):
    model = model = models.TrainedModelSession
    extra = 0


class TrainedModelProcessInline(admin.TabularInline):
    model = model = models.TrainedModelProcess
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
              'type',
              'library',
              'import_code',
              'feature_loader',
              'feature_preparation',
              'result_preparation',
              'training',
              'prediction',
              'test_accuracy',
              ]
    list_display = [
              'name',
              'type',
              'library',
              'import_code',
              'feature_loader',
              'feature_preparation',
              'result_preparation',
              'training',
              'prediction',
              'test_accuracy',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [AlgorithmParameterInline]


class AlgorithmParameterAdmin(admin.ModelAdmin):
    """
    Manages admin interface for Algorithms Parameters
    """
    list_per_page = 100
    fields = [
              'name',
              'default_value',
              'help',
              'min_value',
              'max_value',
              ]
    list_display = [
              'name',
              'default_value',
              'help',
              'min_value',
              'max_value',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [ParameterValueInline]


class TrainedModelAdmin(admin.ModelAdmin):
    """
    Manages admin interface for Algorithms Parameters
    """
    list_per_page = 100
    fields = [
              'name',
              'algorithm',
              'dataset',
              'accumulative_training',
              'result',
              'result_offest',
              'status',
              'import_code',
              'feature_loader',
              'feature_preparation',
              'result_preparation',
              'training',
              'prediction',
              'test_accuracy',
              ]
    list_display = [
              'name',
              'algorithm',
              'dataset',
              'accumulative_training',
              'result',
              'result_offest',
              'status',
              'import_code',
              'feature_loader',
              'feature_preparation',
              'result_preparation',
              'training',
              'prediction',
              'test_accuracy',
                    ]
    filter_horizontal = []
    list_filter = []
    inlines = [TrainedModelParameterInline,TrainedModelFeatureInline,TrainedModelProcessInline,TrainedModelSessionInline]


admin.site.register(models.AlgorithmType, AlgorithmTypeAdmin)
admin.site.register(models.ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(models.Library, LibraryAdmin)
admin.site.register(models.DataProcess, DataProcessAdmin)
admin.site.register(models.Algorithm, AlgorithmAdmin)
admin.site.register(models.AlgorithmParameter, AlgorithmParameterAdmin)
admin.site.register(models.TrainedModel, TrainedModelAdmin)