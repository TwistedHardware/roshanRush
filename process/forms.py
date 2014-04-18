from django import forms
from django.contrib import admin
from django.db.models import Q
from django.forms.models import BaseInlineFormSet
#
import models


class ProcessConnectionFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(ProcessConnectionFormSet, self).__init__(*args, **kwargs)
        #self.queryset = Author.objects.filter(name__startswith='O')
        
        
    @property
    def empty_form(self, *args, **kwargs):
        form = self.form(
                         auto_id=self.auto_id,
                         prefix=self.add_prefix('__prefix__'),
                         empty_permitted=True,
                         process_id=self.instance.id
                         )

        self.add_fields(form, None)

        return form
        #super(ProcessConnectionFormSet, self).empty_form(*args, **kwargs)


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


class ProcessOperationLine(admin.TabularInline):
    def __init__(self, *args, **kwargs):
        super(ProcessOperationLine, self).__init__(*args, **kwargs)
        self.can_delete = True


class ProcessConnectionLineForm(forms.ModelForm):
    """
    Represents a form for a Process Connection In-line in admin interface
    """
    class Meta:
        model = models.ProcessConnection

    def __init__(self, *args, **kwargs):
        process_id = kwargs.get('process_id',0)
        try:
            del kwargs['process_id']
        except:
            pass
        super(ProcessConnectionLineForm, self).__init__(*args, **kwargs)

        if self.instance.id:
            qs_from = models.ProcessOperationLink.objects.all().filter(
                                                                  operation__process__id=self.instance.process.id,
                                                                  link__link__type="output",
                                                                  )
            
            qs_to = models.ProcessOperationLink.objects.all().filter(
                                                                  operation__process__id=self.instance.process.id,
                                                                  link__link__type="input",
                                                                  )
            self.fields['from_operation'].queryset = qs_from
            self.fields['to_operation'].queryset = qs_to
        else:
            qs_from = models.ProcessOperationLink.objects.all().filter(
                                                                  operation__process__id=process_id,
                                                                  link__link__type="output",
                                                                  )
            
            qs_to = models.ProcessOperationLink.objects.all().filter(
                                                                  operation__process__id=process_id,
                                                                  link__link__type="input",
                                                                  )
            self.fields['from_operation'].queryset = qs_from
            self.fields['to_operation'].queryset = qs_to