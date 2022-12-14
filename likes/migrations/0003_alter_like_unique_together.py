# Generated by Django 3.2.16 on 2022-10-21 13:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_post_district'),
        ('recommendations', '0001_initial'),
        ('likes', '0002_auto_20221021_1010'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('owner', 'post'), ('owner', 'recommendation')},
        ),
    ]
