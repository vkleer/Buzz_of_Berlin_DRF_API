# Generated by Django 3.2.16 on 2022-10-31 14:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_languages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('English', 'English'), ('German', 'German'), ('French', 'French'), ('Dutch', 'Dutch'), ('Turkish', 'Turkish'), ('Polish', 'Polish'), ('Spanish', 'Spanish'), ('Italian', 'Italian'), ('Portugese', 'Portugese'), ('Ukrainian', 'Ukrainian'), ('Russian', 'Russian'), ('Arabic', 'Arabic'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese'), ('Korean', 'Korean'), ('Romanian', 'Romanian'), ('Swedish', 'Swedish'), ('Norwegian', 'Norwegian'), ('Danish', 'Danish'), ('Finnish', 'Finnish'), ('Hungarian', 'Hungarian'), ('Slovenian', 'Slovenian'), ('Estonian', 'Estonian'), ('Bulgarian', 'Bulgarian'), ('Latvian', 'Latvian'), ('Croatian', 'Croatian'), ('Greek', 'Greek'), ('Urdu', 'Urdu'), ('Hindi', 'Hindi'), ('Other', 'Other')], max_length=238),
        ),
        migrations.AlterField(
            model_name='event',
            name='music',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('60s', 'Sixties'), ('70s', 'Seventies'), ('80s', 'Eighties'), ('90s', 'Nineties'), ('Pop', 'Pop'), ('Synthpop', 'Synthpop'), ('Disco', 'Disco'), ('New Wave', 'Newwave'), ('Dark Wave', 'Darkwave'), ('Industrial', 'Industrial'), ('Punk', 'Punk'), ('Rock', 'Rock'), ('Indie', 'Indie'), ('Emo', 'Emo'), ('Grunge', 'Grunge'), ('Metal', 'Metal'), ('Blues', 'Blues'), ('Jazz', 'Jazz'), ('Classical', 'Classical'), ('Country', 'Country'), ('Folk', 'Folk'), ('Hip-hop', 'Hiphop'), ('Trip-hop', 'Triphop'), ('Trap', 'Trap'), ('Reggae', 'Reggae'), ('Soul', 'Soul'), ('R&B', 'Rnb'), ('Techno', 'Techno'), ('House', 'House'), ('Trance', 'Trance'), ('Drum & Bass', 'Drumandbass'), ('EDM', 'Edm'), ('EBM', 'Ebm'), ('K-Pop', 'Kpop'), ('J-Pop', 'Jpop'), ('Latin', 'Latin'), ('None', 'None'), ('Other', 'Other')], max_length=238),
        ),
        migrations.AlterField(
            model_name='event',
            name='sports',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Football', 'Football'), ('Basketball', 'Basketball'), ('Tennis', 'Tennis'), ('Volleyball', 'Volleyball'), ('Handball', 'Handball'), ('Badminton', 'Badminton'), ('Swimming', 'Swimming'), ('Boxing', 'Boxing'), ('Tabletennis', 'Tabletennis'), ('Skiing', 'Skiing'), ('Ice skating', 'Iceskating'), ('Roller skating', 'Rollerskating'), ('Cricket', 'Cricket'), ('Rugby', 'Rugby'), ('Darts', 'Darts'), ('Bowling', 'Bowling'), ('Hockey', 'Hockey'), ('Ice hockey', 'Icehockey'), ('Karate', 'Karate'), ('Horse riding', 'Horseriding'), ('Snowboarding', 'Snowboarding'), ('Skateboarding', 'Skateboarding'), ('Cycling', 'Cycling'), ('Archery', 'Archery'), ('Gymnastics', 'Gymnastics'), ('Figureskating', 'Figureskating'), ('Rockclimbing', 'Rockclimbing'), ('Bouldering', 'Bouldering'), ('Judo', 'Judo'), ('Kickboxing', 'Kickboxing'), ('Wrestling', 'Wrestling'), ('Jujutsu', 'Jujutsu'), ('MMA', 'Mma'), ('Taekwondo', 'Taekwondo'), ('Aikido', 'Aikido'), ('Fencing', 'Fencing'), ('Golf', 'Golf'), ('Dancing', 'Dancing'), ('Fishing', 'Fishing'), ('Rowing', 'Rowing'), ('Fitness', 'Fitness'), ('None', 'None'), ('Other', 'Other')], max_length=386),
        ),
    ]
