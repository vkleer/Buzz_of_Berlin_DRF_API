from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """
        Orders Comment objects by creation date
        """
        ordering = ['-creation_date']

    def __str__(self):
        """
        Overrides default name of Comment objects to the Comment content
        """
        return self.content