# Generated by Django 3.2.16 on 2022-10-29 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20221021_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location_mapbox',
        ),
    ]
