from django.db import models
from items.models import Item


class TransactionType(models.Model):
    name = models.CharField(max_length=16, null=False)
    description = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f" {self.name} -- {self.description}"


class TransactionArchive(models.Model):
    transaction = models.CharField(max_length=32, blank=False, null=False)
    item = models.ForeignKey(
        Item,
        on_delete=models.PROTECT,
        related_name="trans_archive",
        blank=False,
        null=False
    )
    quantity = models.FloatField()
    quantity_after = models.FloatField(blank=True, null=True)
    who = models.CharField( max_length=64, null=False)
    when = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):

        return f"{self.id}__ {self.transaction}/Item: {self.item.name}"





