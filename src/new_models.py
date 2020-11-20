# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    addressid = models.IntegerField(db_column='addressId', primary_key=True)  # Field name made lowercase.
    addressname = models.CharField(db_column='addressName', max_length=55, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Host(models.Model):
    hostid = models.IntegerField(db_column='hostId', primary_key=True)  # Field name made lowercase.
    hostname = models.CharField(db_column='hostName', max_length=60)  # Field name made lowercase.
    hostsince = models.DateTimeField(db_column='hostSince', blank=True, null=True)  # Field name made lowercase.
    hostresponserate = models.FloatField(db_column='hostResponseRate', blank=True, null=True)  # Field name made lowercase.
    hostidentityverified = models.IntegerField(db_column='hostIdentityVerified', blank=True, null=True)  # Field name made lowercase.
    hosthasprofilepic = models.IntegerField(db_column='hostHasProfilePic', blank=True, null=True)  # Field name made lowercase.
    hostlocationid = models.ForeignKey(Address, models.DO_NOTHING, db_column='hostLocationId', blank=True, null=True)  # Field name made lowercase.
    hostabout = models.CharField(db_column='hostAbout', max_length=1050, blank=True, null=True)  # Field name made lowercase.
    hostacceptancerate = models.FloatField(db_column='hostAcceptanceRate', blank=True, null=True)  # Field name made lowercase.
    hostissuperhost = models.IntegerField(db_column='hostIsSuperHost', blank=True, null=True)  # Field name made lowercase.
    hostneighborhoodid = models.ForeignKey(Address, models.DO_NOTHING, db_column='hostNeighborhoodId', blank=True, null=True)  # Field name made lowercase.
    hostctl = models.IntegerField(db_column='hostCTL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Host'


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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
