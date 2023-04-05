from django.shortcuts import render


# Create your views here.
def checkout(req):
    cart_id = req.POST.get("cart_id", None)
    if not cart_id:
        return redirect("cart:home")
    cart = Cart.objects.get(pk=cart_id)
