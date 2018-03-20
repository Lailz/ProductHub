from django.contrib import admin
from .models import Product, Profile

class ProductModelAdmin(admin.ModelAdmin):
	list_display = ["name", "id"]
	class Meta:
		model = Product

admin.site.register(Product, ProductModelAdmin)

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["user", "id"]
	class Meta:
		model = Profile

admin.site.register(Profile, ProfileModelAdmin)