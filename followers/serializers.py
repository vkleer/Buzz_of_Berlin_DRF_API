from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowSerializer(serializers.ModelSerializer):
    """
    A class for the FollowSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        """
        Returns the fields to be displayed from the Follower model
        """
        model = Follower
        fields = [
            'id', 'owner', 'creation_date', 'followed',
            'followed_name',
        ]

    def create(self, validated_data):
        """
        Handles the unique constraint on 'owner' and 'followed'
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplicate follower'
            })
