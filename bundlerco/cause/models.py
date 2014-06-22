from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from cause import enums
from userprofile.models import UserProfile

class Cause(models.Model):
	title = models.CharField(max_length=200)
	created_date =models.DateTimeField(_(u'Date Established'))
	type = models.PositiveSmallIntegerField(_(u'type'),
											choices=enums.CAUSE_TYPE_CHOICES)
	region = models.PositiveSmallIntegerField(_(u'region'),
											  choices=enums.CAUSE_REGION_CHOICES)
	deadline = models.DateTimeField(_(u'Deadline date'))
	description = models.TextField(_(u'Description'))
	rating = models.PositiveSmallIntegerField(_(u'Rating'), blank=True)
	status = models.PositiveSmallIntegerField(_(u'Status'),
											  choices=enums.CAUSE_STATUS_CHOICES)
	manager = models.ForeignKey(UserProfile, null=True)

	def __str__(self):
		return self.title

class CauseForm(ModelForm):
	class Meta:
		model = Cause
		localized_fields = ('created_date', 'deadline',)