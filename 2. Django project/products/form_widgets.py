from django.forms.widgets import Widget
from .models import Category
import json
from django.conf import settings


class CategoryListWidget(Widget):
    """
    Category chain widget
    """

    cat_ids_string = ""
    cat_ids = []
    template_name = "products/widgets/category-list.html"

    def format_value(self, value: str):
        """Splitting  string to id num array"""
        if value:
            return [int(x) for x in value.split(" ") if x.strip()]

    def js_value(self, ids):
        """
        Value for inject to js script
        """
        if ids:
            chosen_items = Category.objects.filter(id__in=ids)
            print(chosen_items)
            items = [
                {"id": item.id, "title": item.title} for item in chosen_items
            ]
            return json.dumps(items)

    def get_context(self, name, value, attrs):
        formatted_value = self.format_value(value)
        js_value = self.js_value(formatted_value)
        last_id = formatted_value[-1] if formatted_value else None
        return {
            "widget": {
                "name": name,
                "is_hidden": self.is_hidden,
                "required": self.is_required,
                "value": value,
                "js_value": js_value,
                "attrs": self.build_attrs(self.attrs, attrs),
                "last_id": last_id,
                "template_name": self.template_name,
                "catUrl": settings.CATEGORIES_URL,
            },
        }
