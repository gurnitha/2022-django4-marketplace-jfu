# app/order/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.orders.models import Orders, Sales

# Register your models here.


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
	pass


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
	pass
