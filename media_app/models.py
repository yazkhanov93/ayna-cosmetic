from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
import blurhash
from PIL import Image as IMG
import numpy
from products.models import Product


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")
    content = RichTextField(verbose_name="Teks", null=True, blank=True)
    videoCover = models.ImageField(upload_to="video_cover/", blank=True, null=True, verbose_name="suraty")
    video = models.FileField(upload_to="video/", blank=True, null=True, verbose_name="wideo")
    products = models.ManyToManyField(Product, verbose_name="harytlar", blank=True)
    active = models.BooleanField(default=True, verbose_name="aktiw")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="goşulan güni")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="üýtgedilen güni")

    class Meta:
        verbose_name_plural = "Postlar"

    def __str__(self):
        return self.title

    def blurHash(self):
        if self.videoCover:
            img = IMG.open(self.videoCover).convert("RGB")
            blurhasH = blurhash.encode(numpy.array(img))
            return blurhasH

    def image(self):
        img = PostImage.objects.filter(post=self)[:1].get()
        if self.video:
            return str(self.videoCover)
        else:
            return str(img.image)

    def image_tag(self):
        if self.videoCover:
            img_url = str(self.videoCover.url)
        else:
            img_url = PostImage.objects.filter(post=self)[:1].get()
        return mark_safe('<img scr="%s" style="width:45px; heigth:45px;" />' % img_url)

    image_tag.short_description = "Surat"
    image_tag.allow_tags = True


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="post", related_name="images")
    image = models.ImageField(upload_to="post_img/", blank=True, null=True, verbose_name="surat")

    class Meta:
        verbose_name_plural = "Suratlar"

    def blurHash(self):
        if self.image:
            img = IMG.open(self.image).convert("RGB")
            blurhasH = blurhash.encode(numpy.array(img))
            return blurhasH