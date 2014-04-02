# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RecordLinkFeature'
        db.create_table(u'data_set_recordlinkfeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Record'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('data_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.DataSet'])),
            ('value', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['RecordLinkFeature'])

        # Adding model 'DataSetType'
        db.create_table(u'data_set_datasettype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'data_set', ['DataSetType'])

        # Adding M2M table for field columns on 'DataSetType'
        m2m_table_name = db.shorten_name(u'data_set_datasettype_columns')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datasettype', models.ForeignKey(orm[u'data_set.datasettype'], null=False)),
            ('feature', models.ForeignKey(orm[u'data_set.feature'], null=False))
        ))
        db.create_unique(m2m_table_name, ['datasettype_id', 'feature_id'])

        # Adding model 'BooleanFeature'
        db.create_table(u'data_set_booleanfeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Record'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('value', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['BooleanFeature'])

        # Adding model 'ImageFeature'
        db.create_table(u'data_set_imagefeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Record'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('value', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['ImageFeature'])

        # Adding model 'TextFeature'
        db.create_table(u'data_set_textfeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Record'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['TextFeature'])

        # Adding model 'DataGroup'
        db.create_table(u'data_set_datagroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'data_set', ['DataGroup'])

        # Adding model 'FeatureType'
        db.create_table(u'data_set_featuretype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'data_set', ['FeatureType'])

        # Adding model 'DataSet'
        db.create_table(u'data_set_dataset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.DataGroup'])),
        ))
        db.send_create_signal(u'data_set', ['DataSet'])

        # Adding model 'DateFeature'
        db.create_table(u'data_set_datefeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Record'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('value', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['DateFeature'])

        # Adding model 'Feature'
        db.create_table(u'data_set_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('formula', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.FeatureType'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'], null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['Feature'])

        # Adding model 'NumberFeature'
        db.create_table(u'data_set_numberfeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Record'])),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['NumberFeature'])

        # Adding model 'Record'
        db.create_table(u'data_set_record', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_set', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.DataSet'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='<django.db.models.fields.DateTimeField>', max_length=200, null=True, blank=True)),
            ('original_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'data_set', ['Record'])


    def backwards(self, orm):
        # Deleting model 'RecordLinkFeature'
        db.delete_table(u'data_set_recordlinkfeature')

        # Deleting model 'DataSetType'
        db.delete_table(u'data_set_datasettype')

        # Removing M2M table for field columns on 'DataSetType'
        db.delete_table(db.shorten_name(u'data_set_datasettype_columns'))

        # Deleting model 'BooleanFeature'
        db.delete_table(u'data_set_booleanfeature')

        # Deleting model 'ImageFeature'
        db.delete_table(u'data_set_imagefeature')

        # Deleting model 'TextFeature'
        db.delete_table(u'data_set_textfeature')

        # Deleting model 'DataGroup'
        db.delete_table(u'data_set_datagroup')

        # Deleting model 'FeatureType'
        db.delete_table(u'data_set_featuretype')

        # Deleting model 'DataSet'
        db.delete_table(u'data_set_dataset')

        # Deleting model 'DateFeature'
        db.delete_table(u'data_set_datefeature')

        # Deleting model 'Feature'
        db.delete_table(u'data_set_feature')

        # Deleting model 'NumberFeature'
        db.delete_table(u'data_set_numberfeature')

        # Deleting model 'Record'
        db.delete_table(u'data_set_record')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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