from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from django_dynamic_fixture import G

from cause.models import Cause
from cause.views import home

# Create your tests here.
class CauseBaseTestCase(TestCase):
	def setUp(self):
		super(CauseBaseTestCase, self).setUp()
		self.clause = G(Cause)

class HomeTest(TestCase):
	def test_home_url(self):
		found = resolve('/')
		self.assertEqual(found.func, home)

	def test_home_html(self):
		request = HttpRequest()
		response = home(request)
		expected_html = render_to_string('home.html')
		self.assertEqual(response.content.decode(), expected_html)