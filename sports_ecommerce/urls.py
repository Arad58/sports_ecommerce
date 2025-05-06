from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('accounts/', include('sports_ecommerce.apps.accounts.urls')),
    path('orders/', include('sports_ecommerce.apps.orders.urls')),
    path('products/', include('sports_ecommerce.apps.products.urls')),
    path('admin/', admin.site.urls),
]
