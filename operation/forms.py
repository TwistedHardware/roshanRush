from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
#
import models


class OperationParameterFormSet(BaseInlineFormSet):
    """
    Represents an In-line FormSet for a connection in a Process Form
    """ 
    def __init__(self, *args, **kwargs):
        super(OperationParameterFormSet, self).__init__(*args, **kwargs)
        
        
    @property
    def empty_form(self, *args, **kwargs):
        #super(OperationParameterFormSet, self).empty_form(*args, **kwargs)
        # Add operation_id to Form __init__ method in kwargs 
        form = self.form(
                         auto_id=self.auto_id,
                         prefix=self.add_prefix('__prefix__'),
                         empty_permitted=True,
                         operation_id=self.instance.id
                         )

        self.add_fields(form, None)

        return form


class OperationParameterForm(forms.ModelForm):
    """
    Represents a form for a Process Connection In-line in admin interface
    """
    class Meta:
        model = models.OperationParameter

    def __init__(self, *args, **kwargs):
        operation_id = kwargs.get('operation_id',0)
        try:
            del kwargs['operation_id']
        except:
            pass
        super(OperationParameterForm, self).__init__(*args, **kwargs)

        if self.instance.id:
            qs_assigned_link = models.OperationLink.objects.all().filter(
                                                                operation__id=self.instance.operation.id,
                                                                link__type="input",
                                                                )
            
            self.fields['assigned_link'].queryset = qs_assigned_link
        else:
            qs_assigned_link = models.OperationLink.objects.all().filter(
                                                                operation__id=operation_id,
                                                                link__type="input",
                                                                )
            
            self.fields['assigned_link'].queryset = qs_assigned_link