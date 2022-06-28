from django.db import models
from django_currentuser.db.models import CurrentUserField

from items.models import Item


class TransactionType(models.Model):
    name = models.CharField(max_length=16, null=False)
    description = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f" {self.name} -- {self.description}"


class TransactionArchive(models.Model):
    transaction = models.ForeignKey(
        TransactionType,
        on_delete=models.PROTECT,
        related_name="transactions",
        blank=False,
        null=False)
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name="trans_archive",
        blank=False,
        null=False
    )
    quantity = models.FloatField()
    quantity_after = models.FloatField(blank=True, null=True)
    who = CurrentUserField()
    when = models.DateTimeField(auto_now_add=True)






