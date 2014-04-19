# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'FileFeature.value'
        db.alter_column(u'data_set_filefeature', 'value', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True))
        # Adding field 'Feature.related_to'
        db.add_column(u'data_set_feature', 'related_to',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.DataSet'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'FileFeature.value'
        db.alter_column(u'data_set_filefeature', 'value', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))
        # Deleting field 'Feature.related_to'
        db.delete_column(u'data_set_feature', 'related_to_id')


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
            'related_to': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataSet']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.FeatureType']"})
        },
        u'data_set.featuretype': {
            'Meta': {'object_name': 'FeatureType'},
            'feature_type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'data_set.filefeature': {
            'Meta': {'object_name': 'FileFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Record']"}),
            'value': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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