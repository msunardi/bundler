from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from cause import enums
from userprofile.models import UserProfile

import datetime as dt
from dateutil.relativedelta import relativedelta

class Cause(models.Model):
	title = models.CharField(max_length=200)
	created_date =models.DateField(_(u'Date Established'), default=dt.date.today())
	type = models.PositiveSmallIntegerField(_(u'type'),
											choices=enums.CAUSE_TYPE_CHOICES)
	region = models.PositiveSmallIntegerField(_(u'region'),
											  choices=enums.CAUSE_REGION_CHOICES)
	deadline = models.DateTimeField(_(u'Deadline date'), default=dt.date.today() + relativedelta(months=1))
	description = models.TextField(_(u'Description'))
	rating = models.PositiveSmallIntegerField(_(u'Rating'), blank=True)
	status = models.PositiveSmallIntegerField(_(u'Status'),
											  choices=enums.CAUSE_STATUS_CHOICES,
											  default=enums.CAUSE_STATUS_OPEN)
	manager = models.ForeignKey(UserProfile, null=True)

	def __str__(self):
		return self.title

class CauseForm(ModelForm):
	class Meta:
		model = Cause
		localized_fields = ('created_date', 'deadline',)

class Pledge(models.Model):
	userprofile = models.ForeignKey(UserProfile)
	cause = models.ForeignKey(Cause)
	amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
	payment_method = models.PositiveSmallIntegerField(_(u'Payment method'),
													  choices=enums.PLEDGE_PAYMENT_CHOICES,
													  default=enums.PLEDGE_PAYMENT_VISA)
	is_verified = models.BooleanField(default=False)
	processed = models.PositiveSmallIntegerField(_(u'Status'),
												 choices=enums.PLEDGE_STATUS_CHOICES,
												 default=enums.PLEDGE_STATUS_PENDING)