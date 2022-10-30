from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    A class for the ProfileList generic API view.
    List all profiles.
    No create view required since profile creation is handled by
    Django signals.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        recommendations_count=Count('owner__recommendation', distinct=True),
        events_count=Count('owner__event', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-creation_date')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__following__followed__profile',
        'owner__followed__owner__profile'
    ]
    ordering_fields = [
        'posts_count',
        'recommendations_count',
        'events_count',
        'followers_count',
        'following_count',
        'owner__following__creation_date',
        'owner__followed__creation_date',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    A class for the ProfileDetail generic API view.
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        recommendations_count=Count('owner__recommendation', distinct=True),
        events_count=Count('owner__event', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-creation_date')
    serializer_class = ProfileSerializer
