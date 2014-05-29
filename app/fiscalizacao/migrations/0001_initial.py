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
            ('text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('lon', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('data', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'fiscalizacao', ['Relato'])


    def backwards(self, orm):
        # Deleting model 'Relato'
        db.delete_table(u'fiscalizacao_relato')


    models = {
        u'fiscalizacao.relato': {
            'Meta': {'object_name': 'Relato'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'data': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'lon': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['fiscalizacao']