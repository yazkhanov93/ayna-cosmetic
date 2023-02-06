from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from media_app.models import Post

from .serializers import PostSerializer, PostDetailSerializer


class PostDetailView(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostDetailSerializer(post, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostListView(APIView):
    def get(self, request):
        try:
            post = Post.objects.filter(active=True)
            serializer = PostSerializer(post, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)