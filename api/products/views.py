from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from products.models import Category, SubCategory, Brand, Product, Banner, ProductImage
from settings.models import Settings
from drf_yasg.utils import swagger_auto_schema
from django.db.models import Q

from .serializers import (CategorySerializer, SubCategorySerializer, SubCategoryDetailSerializer,
                          BrandSerializer, BrandDetailSerializer, ProductSerializer,
                          ProductDetailSerializer, BannerSerializer)
from .service import diffColors


class HomeListView(APIView):
    def get(self, request):
        try:
            settings = Settings.objects.first()
            products = Product.objects.filter(active=True)
            banners = Banner.objects.filter(active=True)
            recommend_products = products.filter(
                recommend=True)[:settings.homeRecommendLimit]
            discounted_products = products.filter(
                discount__gt=0)[:settings.homeDiscountedLimit]
            banner_serializer = BannerSerializer(banners, many=True)
            recommend_serializer = ProductSerializer(
                recommend_products, many=True)
            discounted_serializer = ProductSerializer(
                discounted_products, many=True)
            return Response({"banners": banner_serializer.data, "recommended": recommend_serializer.data,
            "discounted": discounted_serializer.data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CategoryListView(APIView):
    def get(self, request):
        try:
            category = Category.objects.filter(active=True)
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProductListView(APIView):
    # @swagger_auto_schema(request_body=ProductSerializer)
    def get(self, request):
        limit = 10
        try:
            products = Product.objects.filter(active=True)
            if request.query_params.get("limit", None):
                limit = request.query_params.get("limit", None)
            if request.query_params.get("brandId", None):
                brandId = request.query_params.get("brandId", None)
                products = products.filter(brand=brandId)
            if request.query_params.get("subcategoryId", None):
                subcategoryId = request.query_params.get("subcategoryId", None)
                products = products.filter(subcategory=subcategoryId)
            if request.query_params.get("recommend", None):
                recommend = request.query_params.get("recommend", None)
                products = products.filter(recommend=recommend.title())
            if request.query_params.get("discount", None):
                discount = request.query_params.get("discount", None)
                products = products.filter(discount__gt=0)
            if request.query_params.get("query", None):
                query = request.query_params.get("query", None)
                products = products.filter(Q(brand__title__icontains=query.strip().lower()) | Q(title__icontains=query.strip().lower()))
            # if request.query_params.get("sortTo", None):
            #     sortTo = request.query_params.get("sortTo", None)
            #     products = products.filter(Q(price__gte=sortTo.split(
            #         "-")[0]) | Q(price__lte=sortTo.split("-")[-1]))
            if request.query_params.get("sortTo", None):
                sortTo = request.query_params.get("sortTo", None)
                products = products.order_by(sortTo)
            if request.query_params.get("date", None):
                date = request.query_params.get("date", None)
                products = products.order_by(date)
            paginator = PageNumberPagination()
            paginator.page_size = limit
            result = paginator.paginate_queryset(products, request)
            serializer = ProductSerializer(result, many=True)
            return paginator.get_paginated_response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProductDetailView(APIView):
    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
            diffColor = diffColors(product.title, product.id)
            serializer = ProductDetailSerializer(product, many=False)
            diffColorsSerializer = ProductSerializer(diffColor, many=True)
            return Response({"product":serializer.data, "diffColors":diffColorsSerializer.data})
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
