from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


class Profile(models.Model):
    """
    A class for the Profile model
    """

    class Languages(models.TextChoices):
        """
        A class for the Languages model
        Contains all the language options users can pick from
        """
        ENGLISH = 'English'
        GERMAN = 'German'
        FRENCH = 'French'
        DUTCH = 'Dutch'
        TURKISH = 'Turkish'
        POLISH = 'Polish'
        SPANISH = 'Spanish'
        ITALIAN = 'Italian'
        PORTUGESE = 'Portugese'
        UKRAINIAN = 'Ukrainian'
        RUSSIAN = 'Russian'
        ARABIC = 'Arabic'
        CHINESE = 'Chinese'
        JAPANESE = 'Japanese'
        KOREAN = 'Korean'
        ROMANIAN = 'Romanian'
        SWEDISH = 'Swedish'
        NORWEGIAN = 'Norwegian'
        DANISH = 'Danish'
        FINNISH = 'Finnish'
        HUNGARIAN = 'Hungarian'
        SLOVENIAN = 'Slovenian'
        ESTONIAN = 'Estonian'
        BULGARIAN = 'Bulgarian'
        LATVIAN = 'Latvian'
        CROATIAN = 'Croatian'
        GREEK = 'Greek'
        URDU = 'Urdu'
        HINDI = 'Hindi'
        OTHER = 'Other'

    class Districts(models.TextChoices):
        """
        A class for the Districts model
        Contains all the district options users can pick from
        """
        FRIEDRICHSHAINKREUZBERG = 'Friedrichshain-Kreuzberg'
        LICHTENBERG = 'Lichtenberg'
        MARZAHNHELLERSDORF = 'Marzahn-Hellersdorf'
        MITTE = 'Mitte'
        NEUKOLLN = 'Neukölln'
        PANKOW = 'Pankow'
        REINICKENDORF = 'Reinickendorf'
        SPANDAU = 'Spandau'
        STEGLITZZEHLENDORF = 'Steglitz-Zehlendorf'
        TEMPELHOFSCHONEBERG = 'Tempelhof-Schöneberg'
        TREPTOWKOPENICK = 'Treptow-Köpenick'

    class Music(models.TextChoices):
        """
        A class for the Music model
        Contains all the music options users can pick from
        """
        SIXTIES = '60s'
        SEVENTIES = '70s'
        EIGHTIES = '80s'
        NINETIES = '90s'
        POP = 'Pop'
        SYNTHPOP = 'Synthpop'
        DISCO = 'Disco'
        NEWWAVE = 'New Wave'
        DARKWAVE = 'Dark Wave'
        INDUSTRIAL = 'Industrial'
        PUNK = 'Punk'
        ROCK = 'Rock'
        INDIE = 'Indie'
        EMO = 'Emo'
        GRUNGE = 'Grunge'
        METAL = 'Metal'
        BLUES = 'Blues'
        JAZZ = 'Jazz'
        CLASSICAL = 'Classical'
        COUNTRY = 'Country'
        FOLK = 'Folk'
        HIPHOP = 'Hip-hop'
        TRIPHOP = 'Trip-hop'
        TRAP = 'Trap'
        REGGAE = 'Reggae'
        SOUL = 'Soul'
        RNB = 'R&B'
        TECHNO = 'Techno'
        HOUSE = 'House'
        TRANCE = 'Trance'
        DRUMANDBASS = 'Drum & Bass'
        EDM = 'EDM'
        EBM = 'EBM'
        KPOP = 'K-Pop'
        JPOP = 'J-Pop'
        LATIN = 'Latin'
        NONE = 'None'
        OTHER = 'Other'

    class Sports(models.TextChoices):
        """
        A class for the Sports model
        Contains all the sports options users can pick from
        """
        FOOTBALL = 'Football'
        BASKETBALL = 'Basketball'
        TENNIS = 'Tennis'
        VOLLEYBALL = 'Volleyball'
        HANDBALL = 'Handball'
        BADMINTON = 'Badminton'
        SWIMMING = 'Swimming'
        BOXING = 'Boxing'
        TABLETENNIS = 'Tabletennis'
        SKIING = 'Skiing'
        ICESKATING = 'Ice skating'
        ROLLERSKATING = 'Roller skating'
        CRICKET = 'Cricket'
        RUGBY = 'Rugby'
        DARTS = 'Darts'
        BOWLING = 'Bowling'
        HOCKEY = 'Hockey'
        ICEHOCKEY = 'Ice hockey'
        KARATE = 'Karate'
        HORSERIDING = 'Horse riding'
        SNOWBOARDING = 'Snowboarding'
        SKATEBOARDING = 'Skateboarding'
        CYCLING = 'Cycling'
        ARCHERY = 'Archery'
        GYMNASTICS = 'Gymnastics'
        FIGURESKATING = 'Figureskating'
        ROCKCLIMBING = 'Rockclimbing'
        BOULDERING = 'Bouldering'
        JUDO = 'Judo'
        KICKBOXING = 'Kickboxing'
        WRESTLING = 'Wrestling'
        JUJUTSU = 'Jujutsu'
        MMA = 'MMA'
        TAEKWONDO = 'Taekwondo'
        AIKIDO = 'Aikido'
        FENCING = 'Fencing'
        GOLF = 'Golf'
        DANCING = 'Dancing'
        FISHING = 'Fishing'
        ROWING = 'Rowing'
        FITNESS = 'Fitness'
        NONE = 'None'
        OTHER = 'Other'

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=75, blank=True)
    district = models.CharField(
        max_length=50,
        choices=Districts.choices,
        default=Districts.MITTE,
    )
    languages = MultiSelectField(
        max_length=20,
        choices=Languages.choices,
        default=Languages.ENGLISH,
    )
    music = MultiSelectField(
        max_length=20,
        choices=Music.choices,
        default=Music.NONE
    )
    sports = MultiSelectField(
        max_length=20,
        choices=Sports.choices,
        default=Sports.NONE,
    )
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_image-01_iotmha'
    )

    class Meta:
        """
        Orders profiles by creation date
        """
        ordering = ['-creation_date']

    def __str__(self):
        """
        Overrides default name of Profile objects to the users' username
        """
        return f"{self.owner.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Created a new Profile object on user creation
    """
    if created:
        Profile.objects.create(owner=instance)


# Calls the create_profile function on user creation
post_save.connect(create_profile, sender=User)
