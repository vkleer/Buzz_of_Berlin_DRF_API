from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    """
    A class for the EventList generic API view.
    List events or create an event if logged in.
    """
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
    ]

    def perform_create(self, serializer):
        """
        Asociates the event with the logged in user
        """
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A class for the EventDetail generic API view.
    Retrieve an event and edit or delete it if you own it.
    """
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Event.objects.all()
