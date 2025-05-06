from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.products_view, name='home'),
]