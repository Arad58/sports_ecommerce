from django.test import TestCase
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserModelTests(TestCase):
    def test_create_admin(self):
        admin = CustomUser.objects.create_superuser(
            username="admin",
            email="admin@sports.ie",
            password="Admin12345!",
            role="ROLE_ADMIN"
        )
        self.assertEqual(admin.email, "admin@sports.ie")
        self.assertEqual(admin.role, "ROLE_ADMIN")
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)

    def test_create_customer(self):
        customer = CustomUser.objects.create_user(
            username="customer",
            email="customer@sports.ie",
            password="Customer12345!",
            role="ROLE_CUSTOMER"
        )
        self.assertEqual(customer.email, "customer@sports.ie")
        self.assertEqual(customer.role, "ROLE_CUSTOMER")
        self.assertFalse(customer.is_superuser)
        self.assertFalse(customer.is_staff)

    def test_create_product_manager(self):
        product_manager = CustomUser.objects.create_user(
            username="product_manager",
            email="product_manager@sports.ie",
            password="ProductManager12345!",
            role="ROLE_PRODUCT_MANAGER"
        )
        self.assertEqual(product_manager.email, "product_manager@sports.ie")
        self.assertEqual(product_manager.role, "ROLE_PRODUCT_MANAGER")
        self.assertFalse(product_manager.is_superuser)
        self.assertFalse(product_manager.is_staff)

    def test_create_inventory_manager(self):
        inventory_manager = CustomUser.objects.create_user(
            username="inventory_manager",
            email="inventory_manager@sports.ie",
            password="InventoryManager12345!",
            role="ROLE_INVENTORY_MANAGER"
        )
        self.assertEqual(inventory_manager.email, "inventory_manager@sports.ie")
        self.assertEqual(inventory_manager.role, "ROLE_INVENTORY_MANAGER")
        self.assertFalse(inventory_manager.is_superuser)
        self.assertFalse(inventory_manager.is_staff)