from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    A class for the PostSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )

    def get_is_owner(self, obj):
        """
        Sets the is_owner field equal to True if the logged in
        user is the object owner, otherwise it's set to False
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image', 'post',
            'created_at', 'updated_at', 'content',
        ]
