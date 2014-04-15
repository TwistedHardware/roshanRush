# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'APIParameter'
        db.create_table(u'api_apiparameter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('api', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.API'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('default_value', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'api', ['APIParameter'])

        # Adding model 'APIUsage'
        db.create_table(u'api_apiusage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('api', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.API'])),
            ('token', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.APIToken'], null=True, blank=True)),
            ('parameters', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('request_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('response_code', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('response_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('running_time', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['APIUsage'])

        # Adding model 'APIToken'
        db.create_table(u'api_apitoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('api', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.API'])),
            ('create_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('expiry_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'api', ['APIToken'])

        # Adding field 'API.require_token'
        db.add_column(u'api_api', 'require_token',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'APIParameter'
        db.delete_table(u'api_apiparameter')

        # Deleting model 'APIUsage'
        db.delete_table(u'api_apiusage')

        # Deleting model 'APIToken'
        db.delete_table(u'api_apitoken')

        # Deleting field 'API.require_token'
        db.delete_column(u'api_api', 'require_token')


    models = {
        u'api.api': {
            'Meta': {'object_name': 'API'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'require_token': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'api.apiparameter': {
            'Meta': {'object_name': 'APIParameter'},
            'api': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.API']"}),
            'default_value': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'api.apitoken': {
            'Meta': {'object_name': 'APIToken'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'api': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.API']"}),
            'create_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'api.apiusage': {
            'Meta': {'object_name': 'APIUsage'},
            'api': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.API']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parameters': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'request_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'response_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'response_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'running_time': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.APIToken']", 'null': 'True', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['api']