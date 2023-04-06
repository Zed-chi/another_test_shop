from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.search_product, name="list"),
]
