from django.test import TestCase
from django_dynamic_fixture import G
from cause.models import Cause

# Create your tests here.
class CauseBaseTestCase(TestCase):
	def setUp(self):
		super(CauseBaseTestCase, self).setUp()
		self.clause = G(Cause)