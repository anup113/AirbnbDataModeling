from django.db import models

from address.models import Address
from hosts.models import Host
# Create your models here.

class Listing(models.Model):
    listingid = models.IntegerField(db_column='listingId', primary_key=True)  # Field name made lowercase.
    listingurl = models.CharField(db_column='listingUrl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    pictureurl = models.CharField(db_column='pictureUrl', max_length=150, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    propertytype = models.CharField(db_column='propertyType', max_length=55, blank=True, null=True)  # Field name made lowercase.
    roomtype = models.CharField(db_column='roomType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accommodates = models.IntegerField(blank=True, null=True)
    bedrooms = models.FloatField(blank=True, null=True)
    beds = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    minimumnights = models.IntegerField(db_column='minimumNights', blank=True, null=True)  # Field name made lowercase.
    reviewscoresrating = models.FloatField(db_column='reviewScoresRating', blank=True, null=True)  # Field name made lowercase.
    reviewscoresaccuracy = models.FloatField(db_column='reviewScoresAccuracy', blank=True, null=True)  # Field name made lowercase.
    reviewscoresvalue = models.FloatField(db_column='reviewScoresValue', blank=True, null=True)  # Field name made lowercase.
    instantbookable = models.IntegerField(db_column='instantBookable', blank=True, null=True)  # Field name made lowercase.
    reviewpermonth = models.FloatField(db_column='reviewPerMonth', blank=True, null=True)  # Field name made lowercase.
    hostid = models.ForeignKey(Host, models.DO_NOTHING, db_column='hostId', blank=True, null=True)  # Field name made lowercase.
    neighborhoodcleansedid = models.ForeignKey(Address, models.DO_NOTHING, db_column='neighborhoodCleansedId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Listing'