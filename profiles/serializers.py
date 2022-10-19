from rest_framework import serializers, fields
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    """
    A class for the ProfileSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Sets the is_owner field equal to True if the logged in
        user is the object owner, otherwise it's set to False
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Checks if the logged in user is following any other profiles.
        Sets the following_id field equal to the corresponding Follower
        instance
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """
        Returns the fields to be displayed from the Profile model
        """
        model = Profile
        fields = [
            'id', 'owner', 'creation_date', 'updated_date', 'name',
            'district', 'languages', 'music', 'sports', 'description',
            'image', 'is_owner', 'following_id', 'posts_count',
            'followers_count', 'following_count',
        ]

    languages = fields.MultipleChoiceField(choices=Profile.Languages)
    music = fields.MultipleChoiceField(choices=Profile.Music)
    sports = fields.MultipleChoiceField(choices=Profile.Sports)
