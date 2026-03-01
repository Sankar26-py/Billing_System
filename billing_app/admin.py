from django.contrib import admin
from billing_app.models import Product,Purchase,PurchaseItem
# Register your models here.

admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(PurchaseItem)