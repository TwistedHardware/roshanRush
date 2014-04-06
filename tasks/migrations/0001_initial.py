# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Worker'
        db.create_table(u'tasks_worker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15)),
            ('concurrency', self.gf('django.db.models.fields.IntegerField')(default=8)),
            ('online', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'tasks', ['Worker'])

        # Adding model 'Task'
        db.create_table(u'tasks_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('output', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('progress', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('progress_details', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('estimated_finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('celery_id', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('worker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Worker'], null=True, blank=True)),
        ))
        db.send_create_signal(u'tasks', ['Task'])

        # Adding model 'TaskParameter'
        db.create_table(u'tasks_taskparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tasks.Task'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'tasks', ['TaskParameter'])


    def backwards(self, orm):
        # Deleting model 'Worker'
        db.delete_table(u'tasks_worker')

        # Deleting model 'Task'
        db.delete_table(u'tasks_task')

        # Deleting model 'TaskParameter'
        db.delete_table(u'tasks_taskparameter')


    models = {
        u'tasks.task': {
            'Meta': {'object_name': 'Task'},
            'celery_id': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'estimated_finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'output': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'progress': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'progress_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'worker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Worker']", 'null': 'True', 'blank': 'True'})
        },
        u'tasks.taskparameter': {
            'Meta': {'object_name': 'TaskParameter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['tasks.Task']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'tasks.worker': {
            'Meta': {'object_name': 'Worker'},
            'concurrency': ('django.db.models.fields.IntegerField', [], {'default': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15'}),
            'online': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['tasks']