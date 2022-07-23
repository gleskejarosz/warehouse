from django.db import models


class Location(models.Model):
    location = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return f" {self.location}"


class LocationDetail(models.Model):
    warehouse = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="warehouse")
    loc_section = models.IntegerField(blank=True, null=True)
    loc_shelf = models.CharField(max_length=4, blank=True, null=True)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.warehouse}"

