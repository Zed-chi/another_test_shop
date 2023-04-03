from django.db import models
from django.conf import settings

from products.models import Product


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete)

    def flush(self):
        try:
            items = self.items.all()
            for i in items:
                i.delete()
        except:
            pass


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete)
    product = models.ForeignKey(to, on_delete)
    quantity = models.IntegerField()
    item_price = models.DecimalField()
