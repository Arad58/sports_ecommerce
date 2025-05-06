from django.shortcuts import render, redirect
from .models import Order, OrderItem, Product

def cart_view(request):
    cart = request.session.get("cart", {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = [{"product": product, "quantity": cart[str(product.id)]} for product in products]

    return render(request, "orders/cart.html", {"cart_items": cart_items})

def checkout_view(request):
    cart = request.session.get("cart", {})

    if request.method == "POST":
        order = Order.objects.create(total_price=sum(Product.objects.get(id=id).price * qty for id, qty in cart.items()))
        for product_id, quantity in cart.items():
            OrderItem.objects.create(order=order, product=Product.objects.get(id=product_id), quantity=quantity)

        request.session["cart"] = {}
        return redirect("orders")

    return render(request, "orders/checkout.html", {"cart": cart})

def orders_view(request):
    orders = Order.objects.all()
    return render(request, "orders/orders.html", {"orders": orders})