from rest_framework import serializers

from media_app.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "image", "blurHash"]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "image", "video", "blurHash"]


class PostDetailSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"