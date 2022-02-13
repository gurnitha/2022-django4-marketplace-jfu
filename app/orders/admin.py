# app/order/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.orders.models import Orders

# Register your models here.


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
	pass
