from django import forms
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
#
import models


class ProcessConnectionFormSet(BaseInlineFormSet):
    """
    Represents an In-line FormSet for a connection in a Process Form
    """ 
    def __init__(self, *args, **kwargs):
        super(ProcessConnectionFormSet, self).__init__(*args, **kwargs)
        
    
    def _construct_form(self, i, **kwargs):
        if self.instance.id:
            val_process_id =  self.instance.id
        else:
            val_process_id = 0
        kwargs['val_process_id'] = val_process_id
        form = super(BaseInlineFormSet, self)._construct_form(i, **kwargs)
        if self.save_as_new:
            # Remove the primary key from the form's data, we are only
            # creating new instances
            form.data[form.add_prefix(self._pk_field.name)] = None

            # Remove the foreign key from the form's data
            form.data[form.add_prefix(self.fk.name)] = None

        # Set the fk value here so that the form can do its validation.
        setattr(form.instance, self.fk.get_attname(), self.instance.pk)
        return form
    
    @property
    def empty_form(self, *args, **kwargs):
        # super(ProcessConnectionFormSet, self).empty_form(*args, **kwargs)
        # Add process_id to Form __init__ method in kwargs
        if self.instance.id:
            val_process_id =  self.instance.id
        else:
            val_process_id = 0
        form = self.form(
                         auto_id=self.auto_id,
                         prefix=self.add_prefix('__prefix__'),
                         empty_permitted=True,
                         val_process_id=val_process_id,
                         )

        self.add_fields(form, None)

        return form


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
        process_id = kwargs['val_process_id'] #kwargs.get('val_process_id',0)
        try:
            del kwargs['val_process_id']
        except:
            pass
        super(ProcessConnectionLineForm, self).__init__(*args, **kwargs)


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