from django.db import models
from items.utils import image_resize


class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f" {self.name}"

    class Meta:
        verbose_name_plural = "Categories"


class Unit(models.Model):
    unit = models.CharField(max_length=10)
    description = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f" {self.unit}"


class Item(models.Model):

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="item_cat", blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="item_unit", blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    producer = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="items_prod", blank=True, null=True)
    producer_no = models.CharField(max_length=50, unique=True, blank=True)
    supplier = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="items_supp",
                                 blank=True, null=True)
    supplier_no = models.CharField(max_length=50, blank=True)
    minimum_quantity = models.PositiveSmallIntegerField(default=1)
    minimum_order = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='items/', blank=True)

    def __str__(self):
        return f"{self.producer} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.image:
            return ""
        else:
            image_resize(self.image, 1000, 800)
            super().save(*args, **kwargs)


class Company(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, blank=True)
    phone_no = models.CharField(max_length=30, blank=True)
    contact_person = models.CharField(max_length=64, blank=True)
    website = models.CharField(max_length=128, blank=True)
    minimum_order_value = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return f" {self.name}"
