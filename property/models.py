from django.db import models
from User.models import User
# Create your models here.


class Property(models.Model):
    property_id = models.IntegerField()
    property_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postalcode = models.IntegerField()
    property_price = models.DecimalField(max_digits=100, decimal_places=2)
    property_type = models.CharField(max_length=100)
    description = models.TextField()
    roomcount = models.IntegerField()
    bedroomcount = models.IntegerField()
    bathroomcount = models.IntegerField()
    is_sold = models.BooleanField()
    listing_date = models.DateField()
    squaremeters = models.IntegerField()
    property_valuation = models.DecimalField(max_digits=100, decimal_places=2)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image_cover = models.CharField(max_length=4096)

class PropertyImage(models.Model):
    image = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')
