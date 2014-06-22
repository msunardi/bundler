# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cause.rating'
        db.add_column(u'cause_cause', 'rating',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'Cause.status'
        db.add_column(u'cause_cause', 'status',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cause.rating'
        db.delete_column(u'cause_cause', 'rating')

        # Deleting field 'Cause.status'
        db.delete_column(u'cause_cause', 'status')


    models = {
        u'cause.cause': {
            'Meta': {'object_name': 'Cause'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {}),
            'deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True'}),
            'region': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.PositiveSmallIntegerField', [], {})
        }
    }

    complete_apps = ['cause']