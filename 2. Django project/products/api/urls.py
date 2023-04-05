from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "categories/", views.CategoryListView.as_view(), name="category_list"
    ),
]
