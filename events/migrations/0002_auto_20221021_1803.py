# Generated by Django 3.2.16 on 2022-10-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location_name',
            field=models.CharField(default='Location', max_length=255),
            preserve_default=False,
        ),
    ]
