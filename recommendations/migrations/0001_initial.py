# Generated by Django 3.2.16 on 2022-10-21 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('location_name', models.CharField(max_length=255, unique=True)),
                ('entry_fee', models.CharField(choices=[('Free', 'Free'), ('€1,00 to €5,00', 'Onetofive'), ('€5,00 to €10,00', 'Fivetoten'), ('€10,00 to €15,00', 'Tentofifteen'), ('€15,00 to €20,00', 'Fifteentotwenty'), ('€20,00 to €30,00', 'Twentytothirty'), ('€30,00 to €50,00', 'Thirtytofifty'), ('€50,00 to €100,00', 'Fiftytohundred'), ('€100,00 or more', 'Overhundred')], max_length=17)),
                ('price', models.CharField(choices=[('Free', 'Free'), ('€', 'Cheap'), ('€€', 'Average'), ('€€€', 'Aboveaverage'), ('€€€€', 'Expensive')], max_length=12)),
                ('district', models.CharField(choices=[('Friedrichshain-Kreuzberg', 'Friedrichshain Kreuzberg'), ('Lichtenberg', 'Lichtenberg'), ('Marzahn-Hellersdorf', 'Marzahn Hellersdorf'), ('Mitte', 'Mitte'), ('Neukölln', 'Neukolln'), ('Pankow', 'Pankow'), ('Reinickendorf', 'Reinickendorf'), ('Spandau', 'Spandau'), ('Steglitz-Zehlendorf', 'Steglitz Zehlendorf'), ('Tempelhof-Schöneberg', 'Tempelhof Schoneberg'), ('Treptow-Köpenick', 'Treptow Kopenick')], max_length=50)),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, default='../default_image-02_ddnubk', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
    ]
