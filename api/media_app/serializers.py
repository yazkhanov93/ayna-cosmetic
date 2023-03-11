from rest_framework import serializers
from api.products.serializers import ProductSerializer
from media_app.models import Post, PostImage, PostVideo


class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ["id", "videoCover", "blurhash", "video"]

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "image", "blurhash"]


class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)
    videos = PostVideoSerializer(many=True)
    class Meta:
        model = Post
        fields = ["id", "title", "images", "videos"]

class PostDetailSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)
    videos = PostVideoSerializer(many=False)
    products = ProductSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"