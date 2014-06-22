from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from django_dynamic_fixture import G

from cause.models import Cause
from cause.views import home, MainPageView

from userprofile.models import UserProfile

# Create your tests here.
class CauseBaseTestCase(TestCase):
	def setUp(self):
		super(CauseBaseTestCase, self).setUp()
		self.profile = G(UserProfile)
		self.cause = G(Cause, manager=self.profile)
		print self.cause

	def test_cause(self):
		print self.cause

class HomeTest(TestCase):
	"""def test_home_url(self):
		found = resolve('/')
		print found.url_name
		self.assertEqual(found.func, MainPageView.as_view())"""

	def test_home_html(self):
		request = HttpRequest()
		response = MainPageView.as_view()
		print response
		#expected_html = render_to_string('index.html')
		#self.assertEqual(response.content.decode(), expected_html)