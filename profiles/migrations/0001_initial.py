# Generated by Django 3.2.16 on 2022-10-16 12:32

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(blank=True, max_length=75)),
                ('name', models.CharField(blank=True, max_length=75)),
                ('district', models.CharField(choices=[('Friedrichshain-Kreuzberg', 'Friedrichshainkreuzberg'), ('Lichtenberg', 'Lichtenberg'), ('Marzahn-Hellersdorf', 'Marzahnhellersdorf'), ('Mitte', 'Mitte'), ('Neukölln', 'Neukolln'), ('Pankow', 'Pankow'), ('Reinickendorf', 'Reinickendorf'), ('Spandau', 'Spandau'), ('Steglitz-Zehlendorf', 'Steglitzzehlendorf'), ('Tempelhof-Schöneberg', 'Tempelhofschoneberg'), ('Treptow-Köpenick', 'Treptowkopenick')], default='Mitte', max_length=50)),
                ('languages', models.CharField(choices=[('English', 'English'), ('German', 'German'), ('French', 'French'), ('Dutch', 'Dutch'), ('Turkish', 'Turkish'), ('Polish', 'Polish'), ('Spanish', 'Spanish'), ('Italian', 'Italian'), ('Portugese', 'Portugese'), ('Ukrainian', 'Ukrainian'), ('Russian', 'Russian'), ('Arabic', 'Arabic'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Romanian', 'Romanian'), ('Swedish', 'Swedish'), ('Norwegian', 'Norwegian'), ('Danish', 'Danish'), ('Finnish', 'Finnish'), ('Hungarian', 'Hungarian'), ('Slovenian', 'Slovenian'), ('Estonian', 'Estonian'), ('Bulgarian', 'Bulgarian'), ('Latvian', 'Latvian'), ('Croatian', 'Croatian'), ('Greek', 'Greek'), ('Urdu', 'Urdu'), ('Hindi', 'Hindi'), ('Other', 'Other')], default='English', max_length=20)),
                ('music', models.CharField(choices=[('60s', 'Sixties'), ('70s', 'Seventies'), ('80s', 'Eighties'), ('90s', 'Nineties'), ('Pop', 'Pop'), ('Synthpop', 'Synthpop'), ('Disco', 'Disco'), ('New Wave', 'Newwave'), ('Dark Wave', 'Darkwave'), ('Industrial', 'Industrial'), ('Punk', 'Punk'), ('Rock', 'Rock'), ('Indie', 'Indie'), ('Emo', 'Emo'), ('Grunge', 'Grunge'), ('Metal', 'Metal'), ('Blues', 'Blues'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Country', 'Country'), ('Folk', 'Folk'), ('Hip-hop', 'Hiphop'), ('Trip-hop', 'Triphop'), ('Trap', 'Trap'), ('Reggae', 'Reggae'), ('Soul', 'Soul'), ('R&B', 'Rnb'), ('Techno', 'Techno'), ('House', 'House'), ('Trance', 'Trance'), ('Drum & Bass', 'Drumandbass'), ('EDM', 'Edm'), ('EBM', 'Ebm'), ('K-Pop', 'Kpop'), ('J-Pop', 'Jpop'), ('Latin', 'Latin'), ('None', 'None'), ('Other', 'Other')], default='None', max_length=20)),
                ('sports', models.CharField(choices=[('Football', 'Football'), ('Basketball', 'Basketball'), ('Tennis', 'Tennis'), ('Volleyball', 'Volleyball'), ('Handball', 'Handball'), ('Badminton', 'Badminton'), ('Swimming', 'Swimming'), ('Boxing', 'Boxing'), ('Tabletennis', 'Tabletennis'), ('Skiing', 'Skiing'), ('Ice skating', 'Iceskating'), ('Roller skating', 'Rollerskating'), ('Cricket', 'Cricket'), ('Rugby', 'Rugby'), ('Darts', 'Darts'), ('Bowling', 'Bowling'), ('Hockey', 'Hockey'), ('Ice hockey', 'Icehockey'), ('Karate', 'Karate'), ('Horse riding', 'Horseriding'), ('Snowboarding', 'Snowboarding'), ('Skateboarding', 'Skateboarding'), ('Cycling', 'Cycling'), ('Archery', 'Archery'), ('Gymnastics', 'Gymnastics'), ('Figureskating', 'Figureskating'), ('Rockclimbing', 'Rockclimbing'), ('Bouldering', 'Bouldering'), ('Judo', 'Judo'), ('Kickboxing', 'Kickboxing'), ('Wrestling', 'Wrestling'), ('Jujutsu', 'Jujutsu'), ('MMA', 'Mma'), ('Taekwondo', 'Taekwondo'), ('Aikido', 'Aikido'), ('Fencing', 'Fencing'), ('Golf', 'Golf'), ('Dancing', 'Dancing'), ('Fishing', 'Fishing'), ('Rowing', 'Rowing'), ('Fitness', 'Fitness'), ('None', 'None'), ('Other', 'Other')], default='None', max_length=20)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(default='../default_profile_image-01_iotmha', upload_to='images/')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creation_date'],
            },
        ),
    ]
