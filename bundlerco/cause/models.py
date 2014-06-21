from django.db import models
from django.utils.translation import ugettext_lazy as _
from cause import enums

class Cause(models.Model):
	title = models.CharField(max_length=200)
	created_date =models.DateTimeField(_(u'Date Established'))
	type = models.PositiveSmallIntegerField(_(u'type'),
											choices=enums.CAUSE_TYPE_CHOICES)
	region = models.PositiveSmallIntegerField(_(u'region'),
											  choices=enums.CAUSE_REGION_CHOICES)
	deadline = models.DateTimeField(_(u'Deadline date'))
	description = models.TextField(_(u'Description'))

	def __str__(self):
		return self.title