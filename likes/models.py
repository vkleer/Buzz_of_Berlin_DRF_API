from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from recommendations.models import Recommendation


class Like(models.Model):
    """
    A class for the Like model.
    The model is related to User, Post and Recommendation.
    'unique_together' ensures a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes',
        default=None, null=True
    )
    recommendation = models.ForeignKey(
        Recommendation, on_delete=models.CASCADE, related_name='likes',
        default=None, null=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders Like objects by creation date
        """
        ordering = ['-creation_date']
        unique_together = ['owner', 'post'], ['owner', 'recommendation']

    def __str__(self):
        """
        Overrides default name of Like objects to the Like owner and
        related Post and Recommendation objects
        """
        return f'${self.owner} ${self.post} ${self.recommendation}'
