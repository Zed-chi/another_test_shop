from django.conf import settings
from django.urls import include, path

from . import views

app_name = "orders"

urlpatterns = [
    path("preorder/", views.preorder, name="preorder"),
    path("checkout/", views.checkout, name="checkout"),
    path("e-pay/", views.pay_order_via_card, name="card_pay"),
    path("detail/<int:pk>", views.order_detail, name="detail"),
    path("", views.orders_list, name="list"),
]
