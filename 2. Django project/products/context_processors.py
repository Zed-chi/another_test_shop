from .models import Category


def root_categories(request):
    categories = Category.get_root_categories()
    return {"categories": categories}
