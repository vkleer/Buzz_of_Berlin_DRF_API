# Generated by Django 3.2.16 on 2022-10-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20221018_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.CharField(choices=[('Friedrichshain-Kreuzberg', 'Friedrichshain Kreuzberg'), ('Lichtenberg', 'Lichtenberg'), ('Marzahn-Hellersdorf', 'Marzahn Hellersdorf'), ('Mitte', 'Mitte'), ('Neukölln', 'Neukolln'), ('Pankow', 'Pankow'), ('Reinickendorf', 'Reinickendorf'), ('Spandau', 'Spandau'), ('Steglitz-Zehlendorf', 'Steglitz Zehlendorf'), ('Tempelhof-Schöneberg', 'Tempelhof Schoneberg'), ('Treptow-Köpenick', 'Treptow Kopenick')], default='Mitte', max_length=50),
        ),
    ]