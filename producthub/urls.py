
from django.contrib import admin
from django.urls import include, path
from products import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),

    path('login/', views.userlogin, name='user_login'),
    path('logout/', views.userlogout, name='user_logout'),
    path('register/', views.register, name='register'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)