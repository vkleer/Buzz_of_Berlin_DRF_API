from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    """
    A class for the PostList API view
    """
    def get(self, request):
        profiles = Post.objects.all()
        serializer = PostSerializer()(
            profiles, many=True, context={'request': request}
        )
        return Response(serializer.data)
