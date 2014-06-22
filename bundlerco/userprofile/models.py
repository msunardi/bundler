from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from localflavor.us.models import PhoneNumberField, USStateField


# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	picture = models.ImageField(upload_to='profile_images', blank=True)
	first_name = models.CharField(max_length=30)
	middle_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30)

	street_address = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=50, blank=True)
	state = USStateField(_(u'State'),default='OR', blank=True)
	phone_number = PhoneNumberField(_(u'Phone number'), blank=True)
	email = models.EmailField(_(u'Email'), blank=True)
	dob = models.DateField(_(u'Date of birth'), blank=True, null=True)
	bio = models.TextField(_(u'Profile'), blank=True)
	website = models.CharField(_(u'Website'), max_length=128, blank=True, default="http://www.")

	def __str__(self):
		return "%s, %s" % (self.last_name, self.first_name)

class Candidates(models.Model):
	userprofile = models.OneToOneField(UserProfile)
	affiliation = models.CharField(max_length=50, blank=True)
	