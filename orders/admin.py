from django.contrib import admin
from orders.models import Order, Product, Customer

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Customer)

# Register your models here.
