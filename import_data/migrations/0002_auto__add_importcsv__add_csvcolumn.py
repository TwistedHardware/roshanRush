# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImportCSV'
        db.create_table(u'import_data_importcsv', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('data_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.DataSet'])),
        ))
        db.send_create_signal(u'import_data', ['ImportCSV'])

        # Adding model 'CSVColumn'
        db.create_table(u'import_data_csvcolumn', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('import_csv', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['import_data.ImportCSV'])),
            ('csv_column', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'], null=True, blank=True)),
        ))
        db.send_create_signal(u'import_data', ['CSVColumn'])


    def backwards(self, orm):
        # Deleting model 'ImportCSV'
        db.delete_table(u'import_data_importcsv')

        # Deleting model 'CSVColumn'
        db.delete_table(u'import_data_csvcolumn')


    models = {
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
        u'import_data.csvcolumn': {
            'Meta': {'object_name': 'CSVColumn'},
            'csv_column': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_csv': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['import_data.ImportCSV']"})
        },
        u'import_data.importcsv': {
            'Meta': {'object_name': 'ImportCSV'},
            'create_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataSet']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['import_data']