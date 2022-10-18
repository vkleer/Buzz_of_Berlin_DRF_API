from rest_framework import serializers, fields
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    A class for the PostSerializer model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source='owner.profile.id')
    profile_image = serializers.SerializerMethodField(
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
            'id', 'owner', 'creation_date', 'updated_date', 'title',
            'district', 'content', 'is_owner',
        ]

    district = fields.MultipleChoiceField(choices=Profile.Districts)
