from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
	path('test/', views.test, name='test'),

	path('list/', views.productlist, name='product_list'),
    path('detail/<int:product_id>/', views.productdetail, name='product_detail'),

    path('create/', views.productcreate, name='product_create'),

]