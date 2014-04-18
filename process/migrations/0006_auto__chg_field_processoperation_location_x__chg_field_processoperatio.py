# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ProcessOperation.location_x'
        db.alter_column(u'process_processoperation', 'location_x', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'ProcessOperation.location_y'
        db.alter_column(u'process_processoperation', 'location_y', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'ProcessOperation.location_x'
        db.alter_column(u'process_processoperation', 'location_x', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'ProcessOperation.location_y'
        db.alter_column(u'process_processoperation', 'location_y', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'api.api': {
            'Meta': {'object_name': 'API'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'require_token': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'operation.link': {
            'Meta': {'object_name': 'Link'},
            'content_type': ('django.db.models.fields.CharField', [], {'default': "'text/plain'", 'max_length': '200'}),
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Location']", 'null': 'True', 'blank': 'True'})
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
            'assigned_link': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['operation.OperationLink']", 'null': 'True', 'blank': 'True'}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'help': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Operation']"})
        },
        u'process.process': {
            'Meta': {'object_name': 'Process'},
            'api': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.API']", 'null': 'True', 'blank': 'True'}),
            'api_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['process.ProcessOperationLink']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'process.processconnection': {
            'Meta': {'object_name': 'ProcessConnection'},
            'from_operation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'output_connection_set'", 'to': u"orm['process.ProcessOperationLink']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['process.Process']"}),
            'to_operation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'input_connection_set'", 'to': u"orm['process.ProcessOperationLink']"})
        },
        u'process.processoperation': {
            'Meta': {'object_name': 'ProcessOperation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_x': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'location_y': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Operation']"}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['process.Process']"}),
            'sequence': ('django.db.models.fields.IntegerField', [], {'default': '-1'})
        },
        u'process.processoperationlink': {
            'Meta': {'object_name': 'ProcessOperationLink'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.OperationLink']"}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['process.ProcessOperation']"})
        },
        u'process.processoperationparameter': {
            'Meta': {'object_name': 'ProcessOperationParameter'},
            'assigned_link': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['process.ProcessOperationLink']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['process.ProcessOperation']"}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.OperationParameter']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['process']