from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    A class for the LikeSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_is_owner(self, obj):
        """
        Sets the is_owner field equal to True if the logged in
        user is the object owner, otherwise it's set to False
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Returns the fields to be displayed from the Like model
        """
        model = Like
        fields = [
            'id', 'owner', 'created_at', 'post',
        ]

    def create(self, validated_data):
        """
        Handles the unique constraint on 'owner' and 'post'
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'Duplicate like'
            })
