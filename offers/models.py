# offers/models.py
from django.db import models
from User.models import User
from property.models import Property
from django.utils import timezone


class Status(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name


class Offers(models.Model):
    offer_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_price = models.FloatField()
    create_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)  # Assuming 1 is "Pending"

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return f"Offer #{self.offer_id} for {self.property_id} by {self.buyer_id}"