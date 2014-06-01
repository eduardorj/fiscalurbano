# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Relato'
        db.create_table(u'fiscalizacao_relato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('anonymous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('incidentTitle', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'fiscalizacao', ['Relato'])


    def backwards(self, orm):
        # Deleting model 'Relato'
        db.delete_table(u'fiscalizacao_relato')


    models = {
        u'fiscalizacao.relato': {
            'Meta': {'object_name': 'Relato'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidentTitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['fiscalizacao']