from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Product, Profile, FavoriteProduct, FollowUser
from django.contrib.auth.models import User
from .forms import ProductForm, LoginForm, UserRegisterForm, UserUpdateForm, PasswordUpdateForm, EmailUpdateForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden


def test(request):
	return HttpResponse("<h1> TEST </h1>")

def register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect("profile_update")
	context = {
		"form": form,
	}
	return render(request, 'register.html', context)

def userlogin(request):
	form = LoginForm()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("products:product_list")

			return redirect("products:product_list")
	context = {
		"form": form,
	}
	return render(request, 'login.html', context)

def userlogout(request):
	logout(request)
	return redirect('user_login')

def profileview(request, user_id):
	form = User.objects.get(pk=user_id)
	post = Product.objects.filter(user=form)

	followed_users = []
	follows = request.user.who_is_followed.all()
	for x in follows:
		followed_users.append(x.user)

	context = {
		"user": form,
		"post": post,
		"my_follows": followed_users
	}

	return render(request, 'profile_view.html', context)


def profileupdate(request):
	if request.method == 'POST':
		profile_form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, "Your profile was successfully updated!")
			return redirect("products:product_list")
		else:
			messages.error(request, "Please correct the error below!")
	else:
		profile_form = ProfileForm(instance=request.user.profile)
	context = {
		"profile_form": profile_form,
	}
	return render(request, 'profile_update.html', context)


def productlist(request):
	if (request.user.is_anonymous):
		return redirect('user_login')
	form = Product.objects.all()
	query = request.GET.get('q')

	if query:
		form = form.filter(name__contains=query)

	favorite_products = []
	favorites = request.user.favoriteproduct_set.all()
	for fav in favorites:
		favorite_products.append(fav.product)

	context = {
	"form": form,
	"my_favorites": favorite_products
	}
	return render(request, 'product_list.html', context)

def productdetail(request, product_slug):
	form = get_object_or_404(Product, slug=product_slug)
	user_obj = False
	if form.user == request.user:
		user_obj = True

	context = {
	"form": form,
	"user_obj": user_obj
	}
	return render(request, 'product_detail.html', context)

def productcreate(request):
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES or None)
		if form.is_valid():
			item = form.save(commit = False)
			item.user = request.user
			item.save()
			messages.success(request, "Product successfully added!")
			return redirect("products:product_list")
	context = {
		"create_form": form,
	}
	return render(request, 'product_create.html', context)

def productupdate(request, product_slug):
	instance = get_object_or_404(Product, slug=product_slug)
	user = request.user

	if instance.user == user:
		form = ProductForm(request.POST or None, request.FILES or None, instance = instance)
		if form.is_valid():
			form.save()
			messages.success(request, "Product successfully updated!")
			return redirect(instance.get_absolute_url())
	else:
			return HttpResponseForbidden()

	context = {
		"form": form,
		"instance": instance
	}
	return render(request, 'product_update.html', context)

def productdelete(request, product_slug):
	if (request.user.is_authenticated):
		instance = get_object_or_404(Product, slug=product_slug)
		user = request.user

		if instance.user == user:
			instance.delete()
			messages.success(request, "Product Successfully Deleted!")
			return redirect("products:product_list")
		else:
			return HttpResponseForbidden()

def favoriteproduct(request, product_id):
	instance = get_object_or_404(Product, id=product_id)
	favorite_obj, created = FavoriteProduct.objects.get_or_create(user=request.user, product=instance)

	if created:
		action="favorite"
	else:
		action="unfavorite"
		favorite_obj.delete()

	favorite_count = instance.favoriteproduct_set.all().count()

	context = {
		"action": action,
		"count": favorite_count,
	}
	return JsonResponse(context, safe=False)

def followuser(request, user_id):
    instance = get_object_or_404(User, id=user_id, is_active=True)
    follow_obj, created = FollowUser.objects.get_or_create(follower=request.user, following=instance)

    if created:
    	action="followed"
    else:
    	action="unfollow"
    	follow_obj.delete()

    follow_count = instance.who_is_followed.all().count()

    context = {
        "action": action,
		"count": follow_count,
    }
    return JsonResponse(context, safe=False)









