from django.db import models
from User.models import User
from django.conf import settings


class Property(models.Model):
    property_id = models.IntegerField()
    property_address = models.CharField(max_length=4096)
    city = models.CharField(max_length=4096)
    postalcode = models.IntegerField()
    property_price = models.DecimalField(max_digits=100, decimal_places=2)
    property_type = models.CharField(max_length=4096)
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


    def get_image_url(self):
        """Return the appropriate image URL regardless of source"""
        if self.image_cover.startswith('http'):
            # External URL - use as is
            return self.image_cover
        else:
            # Local file - prepend with MEDIA_URL if not already included
            if settings.MEDIA_URL in self.image_cover:
                return self.image_cover
            else:
                return f"{settings.MEDIA_URL}{self.image_cover}"


class PropertyImage(models.Model):
    image = models.CharField(max_length=4096)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


    def get_image_url(self):
        """Return the appropriate image URL regardless of source"""
        if self.image.startswith('http'):
            # External URL - use as is
            return self.image
        else:
            # Local file - prepend with MEDIA_URL if not already included
            if settings.MEDIA_URL in self.image:
                return self.image
            else:
                return f"{settings.MEDIA_URL}{self.image}"


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'property')