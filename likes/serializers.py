from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    A class for the LikeSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Returns the fields to be displayed from the Like model
        """
        model = Like
        fields = [
            'id', 'owner', 'creation_date', 'post', 'recommendation',
        ]

    def create(self, validated_data):
        """
        Handles the unique constraint on 'owner', 'post' and 'recommendation'
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplicate like'
            })
