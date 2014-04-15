# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Location.parent'
        db.alter_column(u'operation_location', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['operation.Location'], null=True))

    def backwards(self, orm):

        # Changing field 'Location.parent'
        db.alter_column(u'operation_location', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['operation.Location']))

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
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'help': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'operation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['operation.Operation']"})
        }
    }

    complete_apps = ['operation']