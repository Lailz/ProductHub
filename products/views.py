from django.shortcuts import render, redirect, HttpResponse
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def test(request):
	return HttpResponse("<h1> TEST </h1>")


def productlist(request):
	form = Product.objects.all()

	context = {
	"form": form
	}
	return render(request, 'product_list.html', context)

def productdetail(request, product_id):
	form = Product.objects.get(id=product_id)

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
			return redirect("products:product_list")
	context = {
		"create_form": form,
	}
	return render(request, 'product_create.html', context)

