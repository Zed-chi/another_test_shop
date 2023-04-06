from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render, reverse

from .forms import OrderShippingForm
from .models import Order, OrderItem
from django.db.transaction import atomic

SHIPPING_PRICE = 100


@login_required
def complete(request):
    if request.method == "GET":
        return redirect("cart:detail")
    if request.user.cart.get_total_price == 0:
        return redirect("cart:detail")
    form = OrderShippingForm(data=request.POST)
    if form.is_valid():
        with atomic():
            try:
                cd = form.cleaned_data
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
                for cart_item in request.user.cart.items.all():
                    OrderItem.objects.create(
                        order=order,
                        product=cart_item.product,
                        quantity=cart_item.quantity,
                        item_price=cart_item.product.price,
                    )
                order.total_price = order.get_full_price()
                if cd["payment"] == "CASH":
                    order.status = "need_approval"
                order.save()
                request.user.cart.flush()
                messages.success(request, "Order created")
                return redirect(reverse("orders:detail", kwargs={"pk": order.id}))
            except Exception as e:
                raise Exception(e)
                messages.error(request, e)
    else:
        messages.error(request, "invalid form.")
    return redirect("cart:detail")


@login_required
def preorder(request):
    if request.method == "GET":
        return redirect("cart:homepage")
    if request.user.cart.get_total_price == 0:
        return redirect("cart:homepage")
    form = OrderShippingForm()
    return render(request, "orders/pre-order.html", {"form": form})


@login_required
def pay_order_via_card(request, pk):
    if request.method != "POST":
        messages.error(request, "Неверный метод запроса")
        return redirect(reverse("orders:detail", kwargs={"pk": pk}))
    return render(request, "orders/card-pay-dump.html", {"pk": pk})


@login_required
def dump_gate(request, pk):
    if request.method != "POST":
        messages.error(request, "Неверный метод запроса")
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order.status = "paid"
    order.save()
    messages.success(request, "Заказ оплачен")
    return redirect(reverse("orders:detail", kwargs={"pk": pk}))


@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, "orders/detail.html", {"order": order})


@login_required
def orders_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, "orders/list.html", {"orders": orders})
