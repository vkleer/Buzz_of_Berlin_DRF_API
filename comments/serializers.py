from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    A class for the CommentSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
    creation_date = serializers.SerializerMethodField()
    updated_date = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Sets the is_owner field equal to True if the logged in
        user is the object owner, otherwise it's set to False
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_creation_date(self, obj):
        """
        Sets the creation_date field to a naturaltime, e.g. '4 hours
        ago'
        """
        return naturaltime(obj.creation_date)

    def get_updated_date(self, obj):
        """
        Sets the updated_date field to a naturaltime, e.g. '4 hours
        ago'
        """
        return naturaltime(obj.updated_date)

    class Meta:
        """
        Returns the fields to be displayed from the Comment model
        """
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'post',
            'recommendation', 'creation_date', 'updated_date', 'content',
        ]


class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='owner.post.id')
    recommendation = serializers.ReadOnlyField(
        source='owner.recommendation.id'
    )
