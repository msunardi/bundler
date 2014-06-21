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
	state = USStateField(_(u'state'),default='OR', blank=True)
	phone_number = PhoneNumberField(_(u'phone number'), blank=True)
	email = models.EmailField(_(u'email'), blank=True)
	dob = models.DateField(_(u'date of birth'), blank=True, null=True)