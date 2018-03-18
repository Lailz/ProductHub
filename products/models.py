from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.contrib.auth.models import User


class Product(models.Model):
	category_choices = (
			('Books', 'Books'),
			('Electronics', 'Electronics'),
			('Home Appliances', 'Home Appliances'),
			('Kitchen', 'Kitchen')
		)
	name = models.CharField(max_length=150)
	slug = models.SlugField(unique=True)
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

	def get_absolute_url(self):
		return reverse("products:product_detail", kwargs={"product_slug": self.slug})

def create_slug(instance, new_slug=None):
	slug = slugify (instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s"%(slug,qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug=create_slug(instance)

pre_save.connect(pre_save_post_reciever,sender=Product)


