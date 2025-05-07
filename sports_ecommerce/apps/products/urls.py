from django.urls import path
from . import views

# URL pattern for the home page
urlpatterns = [
    path('home/', views.home_view, name='home'),
]