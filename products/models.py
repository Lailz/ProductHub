from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


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
	user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("products:product_detail", kwargs={"product_slug": self.slug})

	def _get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Product.objects.filter(slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self._get_unique_slug()
		super().save()

class FavoriteProduct(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
	product = models.ForeignKey(Product, on_delete=models.CASCADE)

class FollowUser(models.Model):
	following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
	follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)
	follow_time = models.DateTimeField(auto_now=True, db_index=True)

	def __unicode__(self):
		return str(self.follow_time)

	class Meta:
		ordering = ('-follow_time',)

	def __str__(self):
		return    '{} follows {}'.format(self.follower, self.following)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	birthday = models.DateField(null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()


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


