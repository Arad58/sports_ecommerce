from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('ROLE_ADMIN', 'Admin'),
        ('ROLE_CUSTOMER', 'Customer'),
        ('ROLE_PRODUCT_MANAGER', 'Product Manager'),
        ('ROLE_INVENTORY_MANAGER', 'Inventory Manager'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='ROLE_CUSTOMER')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True
    )