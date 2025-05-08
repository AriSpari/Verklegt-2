from django.db import models
from User.models import User
from property.models import Property
# Create your models here.


class Status(models.Model):
    status_name = models.CharField(max_length=100)


class Offers(models.Model):
    offer_id = models.AutoField(primary_key=True)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_price = models.FloatField()
    expire_date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)