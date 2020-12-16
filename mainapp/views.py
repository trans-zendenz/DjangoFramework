from django.shortcuts import render
from mainapp.models import Product, ProductCategory

# Create your views here.
def index(request):
    return render(request, "mainapp/index.html")


def products(request, pK=None):
    content = {
        "categories": ProductCategory.objects.all(),
        "products": Product.objects.all(),
    }


    return render(request, "mainapp/products.html", content)


def test_context(request):
    context = {
        "title": "hallo!",
        "username": "Max",
        "products": [
            {"name": "Black hudi", "price": "2333 rub"}
        ],
        "promotion_products": [
            {"name": "Boots", "price": "2999 rub"}
        ],
    }

    products = context["products"]

    return render(request, "mainapp/context.html", context)
