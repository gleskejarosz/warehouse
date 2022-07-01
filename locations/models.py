from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)
    date_of_placement = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveSmallIntegerField(default=0)
    # maximum_stock = models.PositiveSmallIntegerField(default=999)
    # maksymalna pojemność tego magazynu
    # in_location
    # date_in_location
    # out_location
    # date_out_location

    def __str__(self):
        return f" {self.location}"
