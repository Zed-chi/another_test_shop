from django.shortcuts import render, redirect
from products.models import Product


def search_product(request):
    if request.method != "GET":
        return redirect("main:homepage")
    query = request.GET["query"]
    products = Product.objects.filter(title__contains=query)
    return render(request, "search/list.html", {"products": products, "query": query})
