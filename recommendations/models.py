from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile
from mapbox_location_field.models import LocationField


class Recommendation(models.Model):
    """
    A class for the Recommendation model, which is related to its owner
    (User instance)
    """

    class EntryFees(models.TextChoices):
        """
        A class for the EntryFees model
        Contains all the entry fee options users can pick from
        """
        FREE = 'Free',
        ONETOFIVE = '€1,00 to €5,00',
        FIVETOTEN = '€5,00 to €10,00',
        TENTOFIFTEEN = '€10,00 to €15,00',
        FIFTEENTOTWENTY = '€15,00 to €20,00',
        TWENTYTOTHIRTY = '€20,00 to €30,00',
        THIRTYTOFIFTY = '€30,00 to €50,00',
        FIFTYTOHUNDRED = '€50,00 to €100,00',
        OVERHUNDRED = '€100,00 or more',

    class Prices(models.TextChoices):
        """
        A class for the Prices model
        Contains all the price options users can pick from
        """
        FREE = 'Free',
        CHEAP = '€',
        AVERAGE = '€€',
        ABOVEAVERAGE = '€€€',
        EXPENSIVE = '€€€€',

    # Reference to Districts subclass in Profile model
    Districts = Profile.Districts

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    location_name = models.CharField(max_length=255, unique=True)
    entry_fee = models.CharField(
        max_length=17,
        choices=EntryFees.choices,
    )
    price = models.CharField(
        max_length=12,
        choices=Prices.choices,
    )
    district = models.CharField(
        max_length=50,
        choices=Districts.choices,
    )
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_image-02_ddnubk', blank=True
    )

    class Meta:
        """
        Orders Recommendation objects by creation date
        """
        ordering = ['-creation_date']

    def __str__(self):
        """
        Overrides default name of Recommendation objects to the Recommendation
        id and title
        """
        return f'{self.id} {self.title}'
