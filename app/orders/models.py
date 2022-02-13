# app/orders/models.py

# Django modules
from django.db import models
from django_countries.fields import CountryField

# Locals
from app.accounts.models import Users
from app.marketplace.models import Stores, Products

# Create your models here.


# NAMA MODEL/TABEL: Orders
class Orders(models.Model):

	id_store_order		= models.ForeignKey(Stores, on_delete=models.CASCADE)
	id_user_order		= models.ForeignKey(Users, on_delete=models.CASCADE)
	id_product_order	= models.ForeignKey(Products, on_delete=models.CASCADE)
	details_order		= models.CharField(max_length=100)
	quantity_order		= models.FloatField(default='0')
	price_order			= models.DecimalField(max_digits=10, decimal_places=2)
	email_order			= models.CharField(max_length=100)
	country_order		= models.CharField(max_length=100)
	city_order			= models.CharField(max_length=100)
	phone_order			= models.CharField(max_length=100)
	address_order		= models.TextField()
	process_order		= models.TextField()
	status_order		= models.TextField()
	date_created_order 	= models.DateTimeField(auto_now_add=True)
	date_updated_order 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('status_order',)
		verbose_name_plural = "Orders"

	def __str__(self):
		return self.status_order


# NAMA MODEL/TABEL: Sales
class Sales(models.Model):

	id_order_sale		= models.ForeignKey(Orders, on_delete=models.CASCADE)
	unit_price_sale		= models.DecimalField(max_digits=10, decimal_places=2)
	commision_sale		= models.FloatField(default='0')
	payment_method_sale	= models.CharField(max_length=100)
	id_payment_sale		= models.CharField(max_length=100)
	status_sale			= models.TextField()
	date_created_sale	= models.DateTimeField(auto_now_add=True)
	date_updated_sale	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('commision_sale',)
		verbose_name_plural = "Sales"

	def __str__(self):
		return self.commision_sale