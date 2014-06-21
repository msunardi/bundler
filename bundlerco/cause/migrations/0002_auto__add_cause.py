# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cause'
        db.create_table(u'cause_cause', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('region', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('deadline', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cause', ['Cause'])


    def backwards(self, orm):
        # Deleting model 'Cause'
        db.delete_table(u'cause_cause')


    models = {
        u'cause.cause': {
            'Meta': {'object_name': 'Cause'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['cause']