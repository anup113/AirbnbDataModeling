from django.db import models

# Create your models here.
class Address(models.Model):
    addressid = models.IntegerField(db_column='addressId', primary_key=True)  # Field name made lowercase.
    addressname = models.CharField(db_column='addressName', max_length=55, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'