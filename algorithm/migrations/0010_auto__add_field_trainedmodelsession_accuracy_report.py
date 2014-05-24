# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TrainedModelSession.accuracy_report'
        db.add_column(u'algorithm_trainedmodelsession', 'accuracy_report',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TrainedModelSession.accuracy_report'
        db.delete_column(u'algorithm_trainedmodelsession', 'accuracy_report')


    models = {
        u'algorithm.algorithm': {
            'Meta': {'object_name': 'Algorithm'},
            'feature_loader': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feature_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'library': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Library']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prediction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'test_accuracy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.AlgorithmType']"})
        },
        u'algorithm.algorithmparameter': {
            'Meta': {'object_name': 'AlgorithmParameter'},
            'algorithm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Algorithm']"}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'algorithm.algorithmtype': {
            'Meta': {'object_name': 'AlgorithmType'},
            'feature_loader': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feature_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'predection': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'test_accuracy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'algorithm.dataprocess': {
            'Meta': {'object_name': 'DataProcess'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'process_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'algorithm.library': {
            'Meta': {'object_name': 'Library'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.ProgrammingLanguage']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'algorithm.parametervalue': {
            'Meta': {'object_name': 'ParameterValue'},
            'help': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.AlgorithmParameter']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'algorithm.programminglanguage': {
            'Meta': {'object_name': 'ProgrammingLanguage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'algorithm.trainedmodel': {
            'Meta': {'object_name': 'TrainedModel'},
            'accumulative_training': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'algorithm': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Algorithm']"}),
            'dataset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.DataSet']"}),
            'feature_loader': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feature_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'prediction': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']", 'null': 'True', 'blank': 'True'}),
            'result_offest': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'result_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'not-ready'", 'max_length': '20'}),
            'test_accuracy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training_percentage': ('django.db.models.fields.FloatField', [], {'default': '0.5'})
        },
        u'algorithm.trainedmodelfeature': {
            'Meta': {'object_name': 'TrainedModelFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'normalize': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pre_process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.DataProcess']", 'null': 'True', 'blank': 'True'}),
            'trained_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.TrainedModel']"})
        },
        u'algorithm.trainedmodelparameter': {
            'Meta': {'object_name': 'TrainedModelParameter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.AlgorithmParameter']"}),
            'trained_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.TrainedModel']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'algorithm.trainedmodelprocess': {
            'Meta': {'object_name': 'TrainedModelProcess'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.DataProcess']"}),
            'trained_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.TrainedModel']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'algorithm.trainedmodelsession': {
            'Meta': {'object_name': 'TrainedModelSession'},
            'accuracy_report': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'accuracy_score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'finish_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'output': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'parameters': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'trained_model': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.TrainedModel']"})
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
        }
    }

    complete_apps = ['algorithm']