from rest_framework import serializers
from .models import Recommendation
from likes.models import Like


class RecommendationSerializer(serializers.ModelSerializer):
    """
    A class for the RecommendationSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

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

    def get_like_id(self, obj):
        """
        Checks if the logged in user has liked any recommendations.
        Sets the like_id field equal to the corresponding Like
        instance
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, recommendation=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        """
        Returns the fields to be displayed from the Recommendation model
        """
        model = Recommendation
        fields = [
            'id', 'owner', 'creation_date', 'updated_date', 'title',
            'district', 'location_name', 'location_mapbox', 'entry_fee',
            'price', 'content', 'image', 'is_owner', 'like_id',
            'likes_count', 'comments_count', 'profile_id', 'profile_image',
        ]
