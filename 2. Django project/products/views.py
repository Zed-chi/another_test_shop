from django.core.paginator import Paginator
from django.views.generic import DetailView, ListView

from .models import Category, Product


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"
    context_object_name = "product"


class CategoryListView(ListView):
    queryset = Category.get_root_categories()
    template_name = "products/categories/list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    template_name = "products/categories/detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = super().get_context_data(**kwargs)
        products = Product.objects.filter(items__category=self.object)
        paginator = Paginator(products, per_page=10)
        if "page" in self.request.GET:
            page_num = self.request.GET["page"]
        else:
            page_num = 1
        page = paginator.get_page(page_num)
        context["page"] = page
        context["products"] = page.object_list
        return context
