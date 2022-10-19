from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    A class for the Follower model.
    The model is related to 'owner' and 'followed'.
    'owner' is a User that is following another User.
    'followed' is a User that is followed by 'owner'.
    The related_name attribute is used to differentiate between
    'owner' and 'followed' which are both User model instances.
    'unique_together' ensures a user can't follow the same user
    twice.
    """
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following'
    )
    followed = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followed'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders Follower objects by creation date
        """
        ordering = ['-creation_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        Overrides default name of Follower objects to the owner and 
        followed
        """
        return f'${self.owner} ${self.followed}'
