from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	category_choices = (
			('Books', 'Books'),
			('Electronics', 'Electronics'),
			('Home Appliances', 'Home Appliances'),
			('Kitchen', 'Kitchen')
		)
	name = models.CharField(max_length=150)
	price = models.DecimalField(max_digits=7, decimal_places=3, default=1)
	category = models.CharField(
		max_length=20,
		choices=category_choices,
		default='electronics',
		)
	image = models.ImageField(null=True)
	seller = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name






