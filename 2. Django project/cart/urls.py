from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "cart"
urlpatterns = [
    path("flush", views.flush_cart, name="flush_cart"),
    path("add/<slug:slug>", views.add_product, name="add_product"),
    path("inc/<slug:slug>", views.increase_product_num, name="inc_product"),
    path("dec/<slug:slug>", views.decrease_product_num, name="dec_product"),
    path("del/<slug:slug>", views.delete_product, name="delete_product"),
    path("", views.cart_home, name="detail"),
]
