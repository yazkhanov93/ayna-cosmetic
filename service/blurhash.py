import numpy, blurhash
from PIL import Image as IMG
from products.models import *


def blurCatImage():
    category = Category.objects.filter(blurhash__isnull=True).exclude(blurhash="")
    for i in category:    
        blur = IMG.open(i.image).convert("RGB")
        blurHash = blurhash.encode(numpy.array(blur))
        i.blurhash = blurHash
        i.save()


def blurSubCatImage():
    subCategory = SubCategory.objects.filter(blurhash__isnull=True).exclude(blurhash="")
    for i in subCategory:    
        blur = IMG.open(i.image).convert("RGB")
        blurHash = blurhash.encode(numpy.array(blur))
        i.blurhash = blurHash
        i.save()


def blurBrandImage():
    brands = Brand.objects.filter(blurhash__isnull=True).exclude(blurhash="")
    for i in brands:    
        blur = IMG.open(i.logo).convert("RGB")
        blurHash = blurhash.encode(numpy.array(blur))
        i.blurhash = blurHash
        i.save()


def blurProdImage():
    images = ProductImage.objects.filter(blurhash__isnull=True).exclude(blurhash="")
    for i in images:
        blur = IMG.open(i.url).convert("RGB")
        blurHash = blurhash.encode(numpy.array(blur))
        i.blurhash = blurHash
        i.save()


def blurBannerImage():
    images = Banner.objects.filter(blurhash__isnull=True).exclude(blurhash="")
    for i in images:
        blur = IMG.open(i.image).convert("RGB")
        blurHash = blurhash.encode(numpy.array(blur))
        i.blurhash = blurHash
        i.save()