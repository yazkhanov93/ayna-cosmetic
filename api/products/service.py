from products.models import Product

# to get products with different colors
def diffColors(title, pk):
    products = Product.objects.filter(title__icontains=title)
    prodList = []
    for i in products:
        if i.id != pk:
            prodList.append(i)
    return prodList