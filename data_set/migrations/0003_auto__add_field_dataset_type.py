# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DataSet.type'
        db.add_column(u'data_set_dataset', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['data_set.DataSetType']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DataSet.type'
        db.delete_column(u'data_set_dataset', 'type_id')


    models = {
        u'data_set.booleanfeature': {
            'Meta': {'object_name': 'BooleanFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data_set.datagroup': {
            'Meta': {'object_name': 'DataGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data_set.dataset': {
            'Meta': {'object_name': 'DataSet'},
            'data_group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataSetType']"})
        },
        u'data_set.datasettype': {
            'Meta': {'object_name': 'DataSetType'},
            'columns': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['data_set.Feature']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data_set.datefeature': {
            'Meta': {'object_name': 'DateFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data_set.feature': {
            'Meta': {'object_name': 'Feature'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'formula': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.FeatureType']"})
        },
        u'data_set.featuretype': {
            'Meta': {'object_name': 'FeatureType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data_set.imagefeature': {
            'Meta': {'object_name': 'ImageFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'data_set.numberfeature': {
            'Meta': {'object_name': 'NumberFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data_set.record': {
            'Meta': {'object_name': 'Record'},
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataSet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'<django.db.models.fields.DateTimeField>'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'original_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data_set.recordlinkfeature': {
            'Meta': {'object_name': 'RecordLinkFeature'},
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataSet']"}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data_set.textfeature': {
            'Meta': {'object_name': 'TextFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data_set']
