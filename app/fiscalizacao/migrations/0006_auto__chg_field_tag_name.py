# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.name'
        db.alter_column(u'fiscalizacao_tag', 'name', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=20))

    def backwards(self, orm):

        # Changing field 'Tag.name'
        db.alter_column(u'fiscalizacao_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True))

    models = {
        u'fiscalizacao.relato': {
            'Meta': {'object_name': 'Relato'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incidentTitle': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['fiscalizacao.Tag']", 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'fiscalizacao.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '20'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['fiscalizacao']