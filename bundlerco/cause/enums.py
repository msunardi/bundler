from django.utils.translation import ugettext_lazy as _

CAUSE_REGION_CITY = 1
CAUSE_REGION_COUNTY = 2
CAUSE_REGION_STATE = 3
CAUSE_REGION_NATIONAL = 4
CAUSE_REGION_CHOICES = (
	(CAUSE_REGION_CITY, _(u'City')),
	(CAUSE_REGION_COUNTY, _(u'County')),
	(CAUSE_REGION_STATE, _(u'State')),
	(CAUSE_REGION_NATIONAL, _(u'National')),
)

CAUSE_TYPE_FISCAL = 1
CAUSE_TYPE_SOCIAL = 2
CAUSE_TYPE_OTHER = 3
CAUSE_TYPE_CHOICES = (
	(CAUSE_TYPE_FISCAL, _(u'Fiscal')),
	(CAUSE_TYPE_SOCIAL, _(u'Social')),
	(CAUSE_TYPE_OTHER, _(u'Other')),
)