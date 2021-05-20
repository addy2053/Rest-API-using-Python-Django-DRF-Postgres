from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    contact = models.CharField(max_length=11, null=False, blank=False)
    address = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=20, )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False)
    products = models.ManyToManyField(Product, blank=False)

    def __str__(self):
        return self.customer.name
