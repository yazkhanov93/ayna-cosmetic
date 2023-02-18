from rest_framework import serializers

from products.models import Category, SubCategory, Brand, Product, ProductImage, Color, Banner


class SubCategorySerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ["id", "title", "image", "blurhash"]

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["id", "title", "image","blurhash", "discount","recommend","brand","subcategory", "product"]


class BrandSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True)
    class Meta:
        model = Brand
        fields = ["id", "title", "logo", "blurhash"]

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "title", "hexCode"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "url", "urlMini", "blurhash"]


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    color = ColorSerializer(many=False)
    brand = BrandSerializer(many=False)
    subcategory = SubCategorySerializer(many=False)
    class Meta:
        model = Product
        fields = ["id", "title", "price","discount", "description", "color", "brand", "subcategory","images",]

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    images = serializers.SerializerMethodField()
    color = ColorSerializer(many=False)
    class Meta:
        model = Product
        fields = ["id", "title","price", "discount", "brand", "color", "images"]

    def get_images(self, obj):
        images = ProductImage.objects.filter(product=obj)
        return ProductImageSerializer([images[0],],many=True).data

class BrandDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = Brand
        fields = ["id", "title", "logo", "blurhash", "product"]


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = SubCategory
        fields = ["id", "title", "image", "product", "blurhash"]


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ["id","title","image", "blurhash", "subcategory"]

