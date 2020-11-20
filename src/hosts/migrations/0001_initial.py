# Generated by Django 2.0.7 on 2020-11-15 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('hostid', models.IntegerField(db_column='hostId', primary_key=True, serialize=False)),
                ('hostname', models.CharField(db_column='hostName', max_length=60)),
                ('hostsince', models.DateTimeField(blank=True, db_column='hostSince', null=True)),
                ('hostresponserate', models.FloatField(blank=True, db_column='hostResponseRate', null=True)),
                ('hostidentityverified', models.IntegerField(blank=True, db_column='hostIdentityVerified', null=True)),
                ('hosthasprofilepic', models.IntegerField(blank=True, db_column='hostHasProfilePic', null=True)),
                ('hostabout', models.CharField(blank=True, db_column='hostAbout', max_length=1050, null=True)),
                ('hostacceptancerate', models.FloatField(blank=True, db_column='hostAcceptanceRate', null=True)),
                ('hostissuperhost', models.IntegerField(blank=True, db_column='hostIsSuperHost', null=True)),
                ('hostctl', models.IntegerField(blank=True, db_column='hostCTL', null=True)),
            ],
            options={
                'db_table': 'Host',
                'managed': False,
            },
        ),
    ]
