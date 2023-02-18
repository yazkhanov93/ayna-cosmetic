from django.db import models
from django.utils.safestring import mark_safe
from colorfield.fields import ColorField
import decimal
from PIL import Image as IMG
from PIL import ImageFilter
# import blurhash
import numpy
from django.core.files.images import get_image_dimensions
from django.utils import timezone



class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")
    image = models.ImageField(upload_to="category_img/", verbose_name="suraty", null=True, blank=True)
    blurhash = models.CharField(max_length=255, blank=True, null=True, verbose_name="blurhash",)
    index = models.PositiveIntegerField(default=1, verbose_name="orny")
    active = models.BooleanField(default=True, verbose_name="aktiw")

    class Meta:
        ordering = ("index",)
        verbose_name_plural = "Ugur"

    def __str__(self):
        return self.title

    # def blurHash(self):
    #     img = IMG.open(self.image).convert("RGB")
    #     blurhasH = blurhash.encode(numpy.array(img))
    #     return blurhasH

    def image_tag(self):
        img_url = str(self.image.url)
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % img_url)

    image_tag.short_description = "Suraty"
    image_tag.allow_tags = True


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="ugry", related_name="subcategory")
    title = models.CharField(max_length=255, verbose_name="ady")
    image = models.ImageField(upload_to="subcategory_img/", verbose_name="suraty", null=True, blank=True)
    blurhash = models.CharField(max_length=255, blank=True, null=True, verbose_name="blurhash",)
    index = models.PositiveIntegerField(default=1, verbose_name="orny")
    active = models.BooleanField(default=True, verbose_name="aktiw")

    class Meta:
        ordering = ("index",)
        verbose_name_plural = "Bölümler"

    def __str__(self):
        return self.title

    # def blurHash(self):
    #     img = IMG.open(self.image).convert("RGB")
    #     blurhasH = blurhash.encode(numpy.array(img))
    #     return blurhasH

    def image_tag(self):
        img_url = str(self.image.url)
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % img_url)

    image_tag.short_description = "Suraty"
    image_tag.allow_tags = True


class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")
    logo = models.ImageField(upload_to="brand_img/", verbose_name="logo")
    blurhash = models.CharField(max_length=255, blank=True, null=True, verbose_name="blurhash",)
    active = models.BooleanField(default=True, verbose_name="aktiw")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="goşulan güni")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="üýtgedilen güni")

    class Meta:
        verbose_name_plural = "Brandler"

    def __str__(self):
        return self.title

    def logo_tag(self):
        img_url = str(self.logo.url)
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % img_url)

    logo_tag.short_description = ("Logo")
    logo_tag.allow_tags = True

class Color(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")
    hexCode = ColorField(format="hexa", verbose_name="hex kod", blank=True, null=True)
    index = models.PositiveIntegerField(default=1, verbose_name="orny")
    active = models.BooleanField(default=True, verbose_name="aktiw")

    class Meta:
        ordering = ("index",)
        verbose_name_plural = "Reňkler"

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")
    description = models.TextField(verbose_name="beýany")
    price = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="bahasy")
    discount = models.DecimalField(decimal_places=2, max_digits=12, verbose_name="arzanladyş baha", blank=True, null=True)
    color = models.ForeignKey(Color, related_name="color", on_delete=models.CASCADE, verbose_name="reňkleri", blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="brand", related_name="product")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name="bölüm", related_name="subcategory")
    active = models.BooleanField(default=True, verbose_name="aktiw")
    recommend = models.BooleanField(default=False, verbose_name="maslahat berilyan")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="goşulan güni")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="üýtgedilen güni")

    class Meta:
        verbose_name_plural = "Harytlar"

    def __str__(self):
        return self.title

    def image_tag(self):
        image = ProductImage.objects.filter(product=self)[:1].get()
        img_url = str(image.urlMini.url)
        return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % img_url)

    image_tag.short_description = ('Surat')
    image_tag.allow_tags = True


class ProductGroup(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="haryt", related_name="productGroup")
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="baha")
    quantity = models.PositiveIntegerField(verbose_name="galan sany")
    total_quantity = models.PositiveIntegerField(verbose_name="gelen sany")
    note = models.CharField(max_length=255, verbose_name="bellik", null=True, blank=True)
    createdAt = models.DateField(default=timezone.now, verbose_name="goşulan güni")

    class Meta:
        verbose_name_plural = "Harydyň Tapgyrlary"

    def __str__(self):
        return str(self.product.title)
    

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="haryt")
    url = models.ImageField(upload_to="product_img/", verbose_name="surat")
    urlMini = models.ImageField(upload_to="product_img/", verbose_name="kici surat", blank=True, null=True)
    blurhash = models.CharField(max_length=255, blank=True, null=True, verbose_name="blurhash",)
    active = models.BooleanField(default=True, verbose_name="aktiw")

    class Meta:
        verbose_name_plural = "Suratlar"
    
    def __str__(self):
        return self.product.title

    def imageWidth(self):
        return self.url.width
    
    def imageHeight(self):
        return self.url.height

    # def blurHash(self):
    #     img = IMG.open(self.url).convert("RGB")
    #     image = blurhash.encode(numpy.array(img))
    #     return image

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        resizeWidth = 900
        resizedWidthMini = 300
        if not self.url:
            raise ValidationError("No image")
        else:
            w, h = get_image_dimensions(self.url)
            resizedHeight = resizeWidth * h/w
            img = IMG.open(self.url.path)
            outputSize = (resizeWidth, resizedHeight)
            img.thumbnail(outputSize)
            img.save(self.url.path)
            w, h = get_image_dimensions(self.urlMini)
            resizedHeightMini = resizedWidthMini * h/w
            img_mini = IMG.open(self.urlMini.path)
            outputSizeMini = (resizedWidthMini, resizedHeightMini)
            img_mini.thumbnail(outputSizeMini)
            img_mini.save(self.urlMini.path)
        


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")
    image = models.ImageField(upload_to="banner_img/", verbose_name="suraty")
    blurhash = models.CharField(max_length=255, blank=True, null=True, verbose_name="blurhash",)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="brand")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="bölüm")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="haryt")
    discount = models.BooleanField(default=True, verbose_name="arzanladyş")
    recommend = models.BooleanField(default=True, verbose_name="maslahat berýäris")
    index = models.PositiveIntegerField(default=1, verbose_name="orny")
    active = models.BooleanField(default=True, verbose_name="aktiw")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="goşulan güni")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="üýtgedilen güni")

    class Meta:
        ordering = ("index",)
        verbose_name_plural = "Bannerler"

    def __str__(self):
        return self.title


    def image_tag(self):
        img_url = str(self.image.url)
        return mark_safe('<img scr="%s" style="width:45px; height:45px;"/>' % img_url)

    image_tag.short_description = "Surat"
    image_tag.allow_tags = True


    