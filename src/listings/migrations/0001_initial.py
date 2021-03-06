# Generated by Django 2.0.7 on 2020-11-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('listingid', models.IntegerField(db_column='listingId', primary_key=True, serialize=False)),
                ('listingurl', models.CharField(blank=True, db_column='listingUrl', max_length=150, null=True)),
                ('pictureurl', models.CharField(blank=True, db_column='pictureUrl', max_length=150, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('propertytype', models.CharField(blank=True, db_column='propertyType', max_length=55, null=True)),
                ('roomtype', models.CharField(blank=True, db_column='roomType', max_length=50, null=True)),
                ('accommodates', models.IntegerField(blank=True, null=True)),
                ('bedroom', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('minimumnights', models.IntegerField(blank=True, db_column='minimumNights', null=True)),
                ('reviewscoresrating', models.FloatField(blank=True, db_column='reviewScoresRating', null=True)),
                ('reviewscoresaccuracy', models.FloatField(blank=True, db_column='reviewScoresAccuracy', null=True)),
                ('reviewscoresvalue', models.FloatField(blank=True, db_column='reviewScoresValue', null=True)),
                ('instantbookable', models.IntegerField(blank=True, db_column='instantBookable', null=True)),
                ('reviewpermonth', models.FloatField(blank=True, db_column='reviewPerMonth', null=True)),
            ],
            options={
                'db_table': 'Listing',
                'managed': False,
            },
        ),
    ]
