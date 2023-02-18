from rest_framework import serializers

from media_app.models import Post, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["id", "image", "blurhash"]


class PostSerializer(serializers.ModelSerializer):
    # images = PostImageSerializer(many=True)[:0]
    class Meta:
        model = Post
        fields = ["id", "title", "image"]

    # def get_image(self, obj):
    #     try:
    #         images = PostImage.objects.filter(post=obj)
    #         return PostImageSerializer([images[0]], many=True).data
    #     except:
    #         pass

class PostDetailSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True)
    class Meta:
        model = Post
        fields = "__all__"