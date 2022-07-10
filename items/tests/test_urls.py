from django.test import SimpleTestCase
from django.urls import reverse, resolve
from items.views import UnitCreateView


class TestUrls(SimpleTestCase):

    def test_units_create_view_resolved(self):
        url = reverse('items_app:units-create-view')
        print(resolve(url))
        self.assertEqual(resolve(url).func.view_class, UnitCreateView)
