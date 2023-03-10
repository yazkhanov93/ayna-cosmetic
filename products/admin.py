from django.contrib import admin
from .models import Category, SubCategory, Brand, Color, Product, ProductGroup, ProductImage, Banner
import numpy
import blurhash
from PIL import Image as IMG
from service.blurhash import blurCatImage, blurSubCatImage, blurBrandImage, blurProdImage, blurBannerImage


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "brand", "product","subcategory","discount","recommend", "index", "active", "createdAt"]
    list_editable = ["active", "index", "recommend","discount"]
    list_filter = ["active", "recommend", "discount"]
    readonly_fields = ["image_tag",]

    def save_model(self, request, obj, form, change):
        obj.save()
        blurBannerImage()



class ProductGroupInline(admin.TabularInline):
    model = ProductGroup
    fields = ["price","quantity","total_quantity","note","createdAt"]
    extra = 0

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
   

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductGroupInline, ProductImageInline]
    list_display = ["title", "image_tag","discount", "price", "brand", "active","recommend"]
    list_editable = ["discount", "active","recommend"]
    list_filter = ["active","discount","color", "recommend"]
    search_fields = ["title",]
    readonly_fields = ["image_tag", "createdAt"]

    save_as = True
    save_on_top = True

    def save_model(self, request, obj, form, change):
        obj.save()
        blurProdImage()


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["title", "hexCode", "index"]
    list_editable = ["hexCode", "index"]
    list_filter = ["active",]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["title", "logo_tag", "active"]
    list_editable = ["active",]
    list_filter = ["active",]
    readonly_fields = ["logo_tag"]

    def save_model(self, request, obj, form, change):
        obj.save()
        blurBrandImage()

 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "image_tag", "index", "active"]
    list_editable = ["active", "index", ]
    list_filter = ["active",]
    # prepopulated_fields = {"blurhash":("title",)}

    def save_model(self, request, obj, form, change):
        obj.save()
        blurCatImage()


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "image_tag", "index", "active"]
    list_editable = ["active", "index"]
    list_filter = ["active",]
    readonly_fields = ["image_tag"]

    def save_model(self, request, obj, form, change):
        obj.save()
        blurSubCatImage()
