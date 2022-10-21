from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    A class for the EventSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )

    def validate_image(self, value):
        """
        Validates if uploaded images meet the set constraints
        """
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size exceeds 2MB - please upload a smaller image.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height exceeds 4096px - please upload a smaller image.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width exceeds 4096px - please upload a smaller image.'
            )
        return value

    def get_is_owner(self, obj):
        """
        Sets the is_owner field equal to True if the logged in
        user is the object owner, otherwise it's set to False
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Returns the fields to be displayed from the Event model
        """
        model = Event
        fields = [
            'id', 'owner', 'creation_date', 'updated_date', 'title',
            'district', 'date', 'start_time', 'ticket_price', 'location_name',
            'location_mapbox', 'content', 'image', 'is_owner', 'profile_id',
            'profile_image',
        ]
