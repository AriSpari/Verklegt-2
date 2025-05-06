from django.db import models

# Create your models here.

class Property(models.Model):
    propertyId = models.IntegerField()
    PropertyAddress = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postalCode = models.IntegerField()
    propertyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    propertyType = models.CharField(max_length=100)
    description = models.TextField()
    roomCount = models.IntegerField()
    bedroomCount = models.IntegerField()
    bathroomCount = models.IntegerField()
    isSold = models.BooleanField()
    listingDate = models.DateField()
    squareMeters = models.IntegerField()
    propertyValuation = models.DecimalField(max_digits=100, decimal_places=2)
    sellerId = models.IntegerField() #get from user
    image = models.ImageField()

class PropertyImage(models.Model):
    image = models.ImageField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
