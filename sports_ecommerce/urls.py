from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # URL pattern for the accounts
    path('accounts/', include('sports_ecommerce.apps.accounts.urls')),
    path('products/', include('sports_ecommerce.apps.products.urls')),
    path('admin/', admin.site.urls),
]