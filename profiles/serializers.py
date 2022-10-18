from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    A class for the ProfileSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'creation_date', 'updated_date', 'name',
            'district', 'languages', 'music', 'sports', 'description',
            'image',
        ]
