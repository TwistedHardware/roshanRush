# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'operation_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operation.Location'])),
            ('help', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'operation', ['Location'])

        # Adding model 'Operation'
        db.create_table(u'operation_operation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operation.Location'])),
            ('operation_code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'operation', ['Operation'])

        # Adding model 'OperationLink'
        db.create_table(u'operation_operationlink', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operation.Operation'])),
            ('link', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operation.Link'])),
        ))
        db.send_create_signal(u'operation', ['OperationLink'])

        # Adding model 'Link'
        db.create_table(u'operation_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('optional', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'operation', ['Link'])

        # Adding model 'OperationParameter'
        db.create_table(u'operation_operationparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('operation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operation.Operation'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('help', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'operation', ['OperationParameter'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'operation_location')

        # Deleting model 'Operation'
        db.delete_table(u'operation_operation')

        # Deleting model 'OperationLink'
        db.delete_table(u'operation_operationlink')

        # Deleting model 'Link'
        db.delete_table(u'operation_link')

        # Deleting model 'OperationParameter'
        db.delete_table(u'operation_operationparameter')


    models = {
        u'operation.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'optional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'operation.location': {
            'Meta': {'object_name': 'Location'},
            'help': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Location']"})
        },
        u'operation.operation': {
            'Meta': {'object_name': 'Operation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Location']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'operation_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'operation.operationlink': {
            'Meta': {'object_name': 'OperationLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Link']"}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Operation']"})
        },
        u'operation.operationparameter': {
            'Meta': {'object_name': 'OperationParameter'},
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'help': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Operation']"})
        }
    }

    complete_apps = ['operation']