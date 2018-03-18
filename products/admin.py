from django.contrib import admin
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["name", "id"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)