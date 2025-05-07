from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product

# User has to log in to access the home page
@login_required
def home_view(request):
    products = Product.objects.all()
    return render(request, 'products/home.html', {'products': products})