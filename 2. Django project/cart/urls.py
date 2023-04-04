from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "cart"
urlpatterns = [
    path("add/<int:p_id>", views.add_product, name="add_product"),
]
