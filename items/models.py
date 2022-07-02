from django.db import models
from items.utils import image_resize
from django.core.validators import MinValueValidator


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
    quantity = models.FloatField(default=0, validators=[MinValueValidator(0.0)])
    producer = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="items_prod", blank=True, null=True)
    producer_no = models.CharField(max_length=50, unique=True, blank=True)
    supplier = models.ForeignKey("Company", on_delete=models.CASCADE, related_name="items_supp",
                                 blank=True, null=True)
    supplier_no = models.CharField(max_length=50, blank=True)
    minimum_quantity = models.PositiveSmallIntegerField(default=1)
    minimum_order = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='items/', default="items/default.png", blank=True)

    def __str__(self):
        return f"{self.producer} - {self.name}"

    def save(self, *args, **kwargs):
        image_resize(self.image, 1000, 800)
        super().save(*args, **kwargs)

    ''' Operations on items for warehouse workers and managers.'''


def input_to_stock(self, amount: float):
    if amount > 0:
        self.quantity += amount


def withdraw(self, amount: float):
    if amount > 0:
        self.quantity -= amount


def total_scrap(self):
    self.quantity = 0


def scrap(self, amount: float):
    if amount > 0:
        self.quantity -= amount


def return_to_stock(self, amount: float):
    if amount > 0:
        self.quantity += amount



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
