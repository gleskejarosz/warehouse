from django.test import TestCase

from orders.models import OrderDetail


class OrderDetailModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        OrderDetail.objects.create(item="0034.5228", quantity=10)

    def test(self):
        assert 1 == 1

    def test_item_label(self):
        order_detail = OrderDetail.objects.get(id=1)
        field_label = order_detail._meta.get_field("item").verbose_name
        self.assertEqual(field_label, "item")

    def test_quantity_label(self):
        order_detail = OrderDetail.objects.get(id=1)
        field_label = order_detail._meta.get_field("quantity").verbose_name
        self.assertEqual(field_label, "quantity")

    def test_user_label(self):
        order_detail = OrderDetail.objects.get(id=1)
        field_label = order_detail._meta.get_field("user").verbose_name
        self.assertEqual(field_label, "user")

    def test_ordered_label(self):
        order_detail = OrderDetail.objects.get(id=1)
        field_label = order_detail._meta.get_field("ordered").verbose_name
        self.assertEqual(field_label, "ordered")

    def test_object_name_is_item_producer_no_x_quantity(self):
        order_detail = OrderDetail.objects.get(id=1)
        expected_object_name = f'{order_detail.item.producer_no} x {order_detail.quantity}'
        self.assertEqual(str(order_detail), expected_object_name)
