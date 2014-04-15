# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TrainedModel'
        db.create_table(u'algorithm_trainedmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('algorithm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Algorithm'])),
            ('dataset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.DataSet'])),
            ('accumulative_training', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('result', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'], null=True, blank=True)),
            ('result_offest', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('import_code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('feature_loader', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('feature_preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('result_preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('training', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('predection', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('test_accuracy', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['TrainedModel'])

        # Adding model 'Algorithm'
        db.create_table(u'algorithm_algorithm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.AlgorithmType'])),
            ('library', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.Library'], null=True, blank=True)),
            ('import_code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('feature_loader', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('feature_preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('result_preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('training', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('predection', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('test_accuracy', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['Algorithm'])

        # Adding model 'TrainedModelParameter'
        db.create_table(u'algorithm_trainedmodelparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.AlgorithmParameter'])),
            ('trained_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.TrainedModel'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'algorithm', ['TrainedModelParameter'])

        # Adding model 'AlgorithmType'
        db.create_table(u'algorithm_algorithmtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('feature_loader', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('feature_preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('result_preparation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('training', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('predection', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('test_accuracy', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['AlgorithmType'])

        # Adding model 'AlgorithmParameter'
        db.create_table(u'algorithm_algorithmparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['AlgorithmParameter'])

        # Adding model 'TrainedModelSession'
        db.create_table(u'algorithm_trainedmodelsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trained_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.TrainedModel'])),
            ('parameters', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('features', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('finish_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('output', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('accuracy_score', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['TrainedModelSession'])

        # Adding model 'ProgrammingLanguage'
        db.create_table(u'algorithm_programminglanguage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'algorithm', ['ProgrammingLanguage'])

        # Adding model 'TrainedModelFeature'
        db.create_table(u'algorithm_trainedmodelfeature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_set.Feature'])),
            ('trained_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.TrainedModel'])),
            ('normalize', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pre_process', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.DataProcess'])),
        ))
        db.send_create_signal(u'algorithm', ['TrainedModelFeature'])

        # Adding model 'DataProcess'
        db.create_table(u'algorithm_dataprocess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('process_code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['DataProcess'])

        # Adding model 'ParameterValue'
        db.create_table(u'algorithm_parametervalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.AlgorithmParameter'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('help', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'algorithm', ['ParameterValue'])

        # Adding model 'Library'
        db.create_table(u'algorithm_library', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.ProgrammingLanguage'])),
        ))
        db.send_create_signal(u'algorithm', ['Library'])

        # Adding model 'TrainedModelProcess'
        db.create_table(u'algorithm_trainedmodelprocess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trained_model', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.TrainedModel'])),
            ('process', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['algorithm.DataProcess'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'algorithm', ['TrainedModelProcess'])


    def backwards(self, orm):
        # Deleting model 'TrainedModel'
        db.delete_table(u'algorithm_trainedmodel')

        # Deleting model 'Algorithm'
        db.delete_table(u'algorithm_algorithm')

        # Deleting model 'TrainedModelParameter'
        db.delete_table(u'algorithm_trainedmodelparameter')

        # Deleting model 'AlgorithmType'
        db.delete_table(u'algorithm_algorithmtype')

        # Deleting model 'AlgorithmParameter'
        db.delete_table(u'algorithm_algorithmparameter')

        # Deleting model 'TrainedModelSession'
        db.delete_table(u'algorithm_trainedmodelsession')

        # Deleting model 'ProgrammingLanguage'
        db.delete_table(u'algorithm_programminglanguage')

        # Deleting model 'TrainedModelFeature'
        db.delete_table(u'algorithm_trainedmodelfeature')

        # Deleting model 'DataProcess'
        db.delete_table(u'algorithm_dataprocess')

        # Deleting model 'ParameterValue'
        db.delete_table(u'algorithm_parametervalue')

        # Deleting model 'Library'
        db.delete_table(u'algorithm_library')

        # Deleting model 'TrainedModelProcess'
        db.delete_table(u'algorithm_trainedmodelprocess')


    models = {
        u'algorithm.algorithm': {
            'Meta': {'object_name': 'Algorithm'},
            'feature_loader': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feature_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'library': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.Library']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'predection': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'test_accuracy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.AlgorithmType']"})
        },
        u'algorithm.algorithmparameter': {
            'Meta': {'object_name': 'AlgorithmParameter'},
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'help': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'predection': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']", 'null': 'True', 'blank': 'True'}),
            'result_offest': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'result_preparation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'test_accuracy': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'training': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'algorithm.trainedmodelfeature': {
            'Meta': {'object_name': 'TrainedModelFeature'},
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'normalize': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pre_process': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['algorithm.DataProcess']"}),
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
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data_set.FeatureType']"})
        },
        u'data_set.featuretype': {
            'Meta': {'object_name': 'FeatureType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['algorithm']