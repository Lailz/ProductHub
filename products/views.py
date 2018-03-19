from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Product
from .forms import ProductForm, LoginForm, UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
			return redirect("products:product_list")
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


def productlist(request):
	if (request.user.is_anonymous):
		return redirect('user_login')
	form = Product.objects.all()
	query = request.GET.get('q')

	if query:
		form = form.filter(name__contains=query)

	context = {
	"form": form
	}
	return render(request, 'product_list.html', context)

def productdetail(request, product_slug):
	form = get_object_or_404(Product, slug=product_slug)

	context = {
	"form": form
	}
	return render(request, 'product_detail.html', context)

def productcreate(request):
	form = ProductForm()
	if request.method == "POST":
		form = ProductForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			messages.success(request, "Product successfully added!")
			return redirect("products:product_list")
	context = {
		"create_form": form,
	}
	return render(request, 'product_create.html', context)

def productupdate(request, product_slug):
	instance = get_object_or_404(Product, slug=product_slug)
	form = ProductForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		form.save()
		messages.success(request, "Product successfully updated!")
		return redirect(instance.get_absolute_url())

	context = {
		"form": form,
		"instance": instance
	}
	return render(request, 'product_update.html', context)

def productdelete(request, product_slug):
	instance = get_object_or_404(Product, slug=product_slug)
	instance.delete()
	messages.success(request, "Product Successfully Deleted!")
	return redirect("products:product_list")









