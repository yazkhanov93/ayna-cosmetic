import numpy, blurhash
from PIL import Image as IMG
from products.models import *
from media_app.models import *


def blurPostImage():
    try:
        images = PostImage.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in images:
            blur = IMG.open(i.image).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            i.blurhash = blurHash
            i.save()
    except:
        pass


def blurPostVideoCover():
    try:
        posts = PostVideo.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in posts:
            blur = IMG.open(i.videoCover).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            i.blurhash = blurHash
            i.save()
    except:
        pass


def blurCatImage():
    try:
        category = Category.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in category:    
            blur = IMG.open(i.image).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            i.blurhash = blurHash
            i.save()
    except:
        pass


def blurSubCatImage():
    try:
        subCategory = SubCategory.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in subCategory:    
            blur = IMG.open(i.image).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            i.blurhash = blurHash
            i.save()
    except:
        pass


def blurBrandImage():
    try:
        brands = Brand.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in brands:    
            blur = IMG.open(i.logo).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            i.blurhash = blurHash
            i.save()
    except:
        pass


def blurProdImage():
    try:
        images = ProductImage.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in images:
            blur = IMG.open(i.url).convert("RGB")
            blurmini = IMG.open(i.urlMini).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            blurHashMini = blurhash.encode(numpy.array(blurmini))
            i.blurhash = blurHash
            i.save()
    except:
        pass


def blurBannerImage():
    try:
        images = Banner.objects.filter(blurhash__isnull=True).exclude(blurhash="")
        for i in images:
            blur = IMG.open(i.image).convert("RGB")
            blurHash = blurhash.encode(numpy.array(blur))
            i.blurhash = blurHash
            i.save()
    except:
        pass