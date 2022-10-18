from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile


class Post(models.Model):
    """
    A class for the Post model, which is related to its owner (User instance)
    """
    Districts = Profile.Districts

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
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
        Orders profiles by creation date
        """
        ordering = ['-creation_date']

    def __str__(self):
        """
        Overrides default name of Post objects to the Post id and title
        """
        return f'{self.id} {self.title}'
