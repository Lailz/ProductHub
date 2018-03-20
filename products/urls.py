from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
	path('test/', views.test, name='test'),

	path('list/', views.productlist, name='product_list'),
    path('detail/<slug:product_slug>/', views.productdetail, name='product_detail'),

    path('create/', views.productcreate, name='product_create'),
    path('update/<slug:product_slug>/', views.productupdate, name='product_update'),
    path('delete/<slug:product_slug>/', views.productdelete, name='product_delete'),



]