from django.core.urlresolvers import resolve
from django.test import TestCase
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