from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_list_or_404,
    get_object_or_404,
)
from django.contrib.auth.decorators import login_required, permission_required
from .models import Order, OrderItem
from .forms import OrderShippingForm


SHIPPING_PRICE = 100


@login_required
def checkout(request):
    if request.method == "GET":
        return redirect("cart:homepage")
    if request.user.cart.get_total_price == 0:
        return redirect("cart:homepage")
    form = OrderShippingForm(data=request.POST)
    if form.is_valid():
        try:
            cd = form.cleaned_data()
            order = Order.objects.create(
                payment=cd["payment"],
                firstname=cd["firstname"],
                lastname=cd["lastname"],
                phonenumber=cd["phonenumber"],
                comment=cd["comment"],
                address=cd["address"],
                user=request.user,
                status="draft",
                shipping_price=SHIPPING_PRICE,
            )
            for cart_item in request.user.cart.items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    item_price=cart_item.product.price,
                )
            order.total_price = order.get_full_price()
            order.save()
        except:
            pass


@login_required
def preorder(request):
    if request.method == "GET":
        return redirect("cart:homepage")
    if request.user.cart.get_total_price == 0:
        return redirect("cart:homepage")
    form = OrderShippingForm()
    return render(request, "orders/pre-order.html", {"form": form})


@login_required
def pay_order_via_card():
    pass


@login_required
def order_detail(request, pk):
    pass


@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/list.html", {"orders": orders})
