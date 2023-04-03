from django.urls import path, include
from . import views

urlpatterns = [
    path(
        "categories/", views.CategoryListView.as_view(), name="category_list"
    ),
]
