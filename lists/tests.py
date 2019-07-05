from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.


class SmokeTest(TestCase):

    def test_root_url_resolvers_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

