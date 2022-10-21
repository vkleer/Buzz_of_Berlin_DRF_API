import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from profiles.models import Profile
from recommendations.models import Recommendation


class Event(models.Model):
    """
    A class for the Event model, which is related to its owner (User instance).
    Uses MinValueValidator on start_time to only allow the current date or
    future dates to prevent users from creating events in the past.
    Uses MinValueValidator and MaxValueValidator on ticket_price to allow
    positive integers only with a maximum price of 100 to prevent unrealistic
    ticket prices.
    """
    Districts = Profile.Districts
    EntryFees = Recommendation.EntryFees

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    date = models.DateField()
    start_time = models.TimeField(validators=[
        MinValueValidator(datetime.date.today)
    ])
    ticket_price = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100)
    ])
    district = models.CharField(
        max_length=50,
        choices=Districts.choices
    )
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_image-02_ddnubk', blank=True
    )

    class Meta:
        """
        Orders Event objects by creation date
        """
        ordering = ['-creation_date']

    def __str__(self):
        """
        Overrides default name of Event objects to the Event id and title
        """
        return f'{self.id} {self.title}'
