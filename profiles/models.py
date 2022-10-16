from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    A class for the Profile model
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=75, blank=True)
    name = models.CharField(max_length=75, blank=True)
    district = models.CharField(
        max_length=2,
        choices=Districts.choices,
        default=Districts.MITTE,
    )
    languages = models.CharField(
        max_length=2,
        choices=Languages.choices,
        default=Languages.ENGLISH,
    )
    interests = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_image-01_iotmha'
    )

    class Meta:
        """
        Orders profiles by creation date
        """
        ordering = ['-creation_date']

    class Languages(models.TextChoices):
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

    class Districts(models.TextChoices):
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

    def __str__(self):
        """
        Overrides default name of Profile objects to the users' username
        """
        return f"{self.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
