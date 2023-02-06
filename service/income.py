from products.models import Product, ProductGroup
from incomes.models import Income


def addIncome(*args):
    try:
        product = Product.objects.all()
        t = []
        for i in args:
            for j in i:
                while j["quantity"] > 0:
                    t.append({"productId":j["productId"], "price":j["price"]})
                    j["quantity"] -= 1
        l = []
        for i in t:    
            group = ProductGroup.objects.filter(product=i["productId"], quantity__gt=0).first()
            price = i["price"] - group.price
            l.append({"productId":i["productId"], "price":price})
            group.quantity -=1
            group.save()
        for i in l:
            inc = Income.objects.create(
                productId=product.get(id=i["productId"]),
                price=i["price"],
                quantity=1
            )
            inc.save()
    except:
        pass