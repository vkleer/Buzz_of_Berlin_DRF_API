from rest_framework import serializers, fields
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

    languages = fields.MultipleChoiceField(choices=Profile.Languages)
    music = fields.MultipleChoiceField(choices=Profile.Music)
    sports = fields.MultipleChoiceField(choices=Profile.Sports)
