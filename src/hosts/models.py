from django.db import models

from address.models import Address
# Create your models here.
class Host(models.Model):
    hostid = models.IntegerField(db_column='hostId', primary_key=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='hostName', max_length=60)  # Field name made lowercase.
    hostsince = models.DateTimeField(db_column='hostSince', blank=True, null=True)  # Field name made lowercase.
    hostresponserate = models.FloatField(db_column='hostResponseRate', blank=True, null=True)  # Field name made lowercase.
    hostidentityverified = models.IntegerField(db_column='hostIdentityVerified', blank=True, null=True)  # Field name made lowercase.
    hosthasprofilepic = models.IntegerField(db_column='hostHasProfilePic', blank=True, null=True)  # Field name made lowercase.
    hostlocationid = models.ForeignKey(Address, models.DO_NOTHING, db_column='hostLocationId', blank=True, null=True, related_name="hostLocaion")  # Field name made lowercase.
    hostabout = models.CharField(db_column='hostAbout', max_length=1050, blank=True, null=True)  # Field name made lowercase.
    hostacceptancerate = models.FloatField(db_column='hostAcceptanceRate', blank=True, null=True)  # Field name made lowercase.
    hostissuperhost = models.IntegerField(db_column='hostIsSuperHost', blank=True, null=True)  # Field name made lowercase.
    hostneighborhoodid = models.ForeignKey(Address, models.DO_NOTHING, db_column='hostNeighborhoodId', blank=True, null=True, related_name="hostneighborhood")  # Field name made lowercase.
    hostctl = models.IntegerField(db_column='hostCTL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Host'
