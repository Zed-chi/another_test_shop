from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("preorder/", views.preorder, name="preorder"),
    path("complete/", views.complete, name="complete"),
    path("<int:pk>/proceed_to_pay/", views.pay_order_via_card, name="card_pay"),
    path("<int:pk>/dump_pay_gate/", views.dump_gate, name="dump_gate"),
    path("<int:pk>", views.order_detail, name="detail"),
    path("", views.orders_list, name="list"),
    path("success_pay/", views.success_pay, name="success_pay"),
]
