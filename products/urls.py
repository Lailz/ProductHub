from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
	path('test/', views.test, name='test'),

	path('list/', views.productlist, name='product_list'),
    path('detail/<slug:product_slug>/', views.productdetail, name='product_detail'),

    path('create/', views.productcreate, name='product_create'),
    #path('update/<int:product_id>/', views.productupdate, name='product_update'),
    #path('delete/<int:product_id>/', views.productdelete, name='product_delete'),

]