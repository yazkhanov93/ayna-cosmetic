from django.contrib import admin
from .models import Post, PostImage
from service.blurhash import blurPostImage, blurPostVideoCover


class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ["title", "image_tag", "active", "created_at"]
    list_filter = ["active"]
    list_editable = ["active"]
    search_fields = ["title"]
    readonly_fields = ["image_tag"]

    def save_model(self, request, obj, form, change):
        obj.save()
        blurPostVideoCover()
        blurPostImage()
