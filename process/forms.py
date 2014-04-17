from django import forms
import models
from django.contrib import admin
from django.db.models import Q


class ProcessAdminForm(forms.ModelForm):
    """
    Represents a form for a Process in admin interface
    """
    class Meta:
        model = models.Process

    def __init__(self, *args, **kwargs):
        super(ProcessAdminForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            qs = models.ProcessOperationLink.objects.all().filter(operation__process__id=self.instance.id, link__link__type="output")
            self.fields['api_source'].queryset = qs
        else:
            self.fields['api_source'].queryset = models.ProcessOperationLink.objects.all().filter(pk=0)


class ProcessConnectionLine(admin.TabularInline):
    def __init__(self, *args, **kwargs):
        super(ProcessConnectionLine, self).__init__(*args, **kwargs)
        self.can_delete = True


class ProcessConnectionLineForm(forms.ModelForm):
    """
    Represents a form for a Process Connection In-line in admin interface
    """
    class Meta:
        model = models.ProcessConnection

    def __init__(self, *args, **kwargs):
        super(ProcessConnectionLineForm, self).__init__(*args, **kwargs)
        
        if self.instance.id:
            
            qs_from = models.ProcessOperationLink.objects.all().filter(
                                                                  operation__process__id=self.instance.process.id,
                                                                  link__link__type="output"
                                                                  )
            
            qs_to = models.ProcessOperationLink.objects.all().filter(
                                                                  operation__process__id=self.instance.process.id,
                                                                  link__link__type="input"
                                                                  )
            self.fields['from_operation'].queryset = qs_from
            self.fields['to_operation'].queryset = qs_to
        else:
            # print self
            qs_from = models.ProcessOperationLink.objects.all().filter(
                                                                  #operation__process__id=self.instance.process.id,
                                                                  link__link__type="output"
                                                                  )
            
            qs_to = models.ProcessOperationLink.objects.all().filter(
                                                                  #operation__process__id=self.instance.process.id,
                                                                  link__link__type="input"
                                                                  )
            self.fields['from_operation'].queryset = qs_from
            self.fields['to_operation'].queryset = qs_to