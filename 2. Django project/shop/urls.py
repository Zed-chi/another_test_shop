from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("search/", include("search.urls")),
    path("orders/", include("orders.urls")),
    path("cart/", include("cart.urls")),
    path("accounts/", include("accounts.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("", include("products.urls")),
    path("", include("main.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
