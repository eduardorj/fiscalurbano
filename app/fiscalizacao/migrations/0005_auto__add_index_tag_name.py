# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field tags on 'Relato'
        m2m_table_name = db.shorten_name(u'fiscalizacao_relato_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('relato', models.ForeignKey(orm[u'fiscalizacao.relato'], null=False)),
            ('tag', models.ForeignKey(orm[u'fiscalizacao.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['relato_id', 'tag_id'])

        # Adding index on 'Tag', fields ['name']
        db.create_index(u'fiscalizacao_tag', ['name'])


    def backwards(self, orm):
        # Removing index on 'Tag', fields ['name']
        db.delete_index(u'fiscalizacao_tag', ['name'])

        # Removing M2M table for field tags on 'Relato'
        db.delete_table(db.shorten_name(u'fiscalizacao_relato_tags'))


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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['fiscalizacao']