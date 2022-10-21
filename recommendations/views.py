from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Recommendation
from .serializers import RecommendationSerializer


class RecommendationList(generics.ListCreateAPIView):
    """
    A class for the RecommendationList generic API view.
    List recommendations or create a recommendation if logged in.
    """
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recommendation.objects.all()

    def perform_create(self, serializer):
        """
        Asociates the post with the logged in user
        """
        serializer.save(owner=self.request.user)


class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for the RecommendationDetail generic API view.
    Retrieve a recommendation and edit or delete it if you own it.
    """
    serializer_class = RecommendationSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recommendation.objects.all()
