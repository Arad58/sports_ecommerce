from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Product Manager', 'Product Manager'),
        ('Inventory Manager', 'Inventory Manager'),
        ('Order Processor', 'Order Processor'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Customer')

    def __str__(self):
        return self.user.username