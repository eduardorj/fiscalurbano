# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Relato'
        db.create_table('fiscalizacao_relato', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('data', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('fiscalizacao', ['Relato'])


    def backwards(self, orm):
        # Deleting model 'Relato'
        db.delete_table('fiscalizacao_relato')


    models = {
        'fiscalizacao.relato': {
            'Meta': {'object_name': 'Relato'},
            'data': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['fiscalizacao']