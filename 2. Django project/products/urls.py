from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product_list"),
    path(
        "products/<slug:cat_slug>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path(
        "categories/", views.CategoryListView.as_view(), name="category_list"
    ),
    path(
        "categories/<slug:cat_slug>/",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
]
