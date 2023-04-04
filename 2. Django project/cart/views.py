from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from products.models import Category, Product, CategoryProductRel
from django.conf import settings
from .models import Cart, CartItem


@login_required
def cart_home(request):
    cart = request.user.cart
    return render(request, "cart/home.html", {"cart": cart})


@login_required
def flush_cart(request):
    request.user.cart.flush_cart()
    return redirect("cart:home_page")


@login_required
def add_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_item = CartItem.objects.create(
        cart=request.user.cart,
        product=product,
        quantity=1,
        item_price=product.price,
    )
    return redirect("products_detail", kwargs={"slug": slug})


@login_required
def increase_product_num(request, slug):
    # product = get_object_or_404(Product, slug=slug)
    cart_item = get_object_or_404(
        CartItem, product__slug=slug, cart=request.user.cart
    )
    cart_item.quantity += 1
    cart_item.save()
    return redirect("products_detail", kwargs={"slug": slug})


@login_required
def decrease_product_num(request, slug):
    cart_item = get_object_or_404(
        CartItem, product__slug=slug, cart=request.user.cart
    )
    if cart_item.quantity == 1:
        return delete_product(request, slug)
    cart_item.quantity -= 1
    cart_item.save()
    return redirect("products_detail", kwargs={"slug": slug})


@login_required
def delete_product(request, slug):
    cart_item = get_object_or_404(
        CartItem, product__slug=slug, cart=request.user.cart
    )
    cart_item.delete()
    return redirect("products_detail", kwargs={"slug": slug})
