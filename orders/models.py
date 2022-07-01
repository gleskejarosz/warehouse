from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from items.models import Item


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField("OrderDetail")

    def __str__(self):
        return f"{self.user.username}"


class OrderDetail(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item")
    quantity = models.PositiveSmallIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.item.producer_no} x {self.quantity}"


def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile = UserProfile.objects.create(user=instance)


post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

