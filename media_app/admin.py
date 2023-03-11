from django.contrib import admin
from .models import Post, PostImage, PostVideo
from service.blurhash import blurPostImage, blurPostVideoCover


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


class PostVideoInline(admin.TabularInline):
    model = PostVideo
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, PostVideoInline]
    list_display = ["title", "image_tag"]
    search_fields = ["title"]
    readonly_fields = ["image_tag"]

    def save_model(self, request, obj, form, change):
        obj.save()
        blurPostVideoCover()
        blurPostImage()
