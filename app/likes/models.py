# app/likes/models.py

# Django modules
from django.db import models

# Locals
from app.orders.models import Orders
from app.accounts.models import Users
from app.marketplace.models import Stores, Products

# Create your models here.


# NAMA MODEL/TABEL: Disputes
class Disputes(models.Model):

	id_order_dispute		= models.ForeignKey(Orders, on_delete=models.CASCADE)
	stage_dispute			= models.TextField()
	transmitter_dispute		= models.ForeignKey(Users, on_delete=models.CASCADE)
	receiver_dispute		= models.ForeignKey(Stores, on_delete=models.CASCADE)
	content_dispute			= models.TextField()
	answer_dispute			= models.TextField()
	date_created_dispute	= models.DateTimeField(auto_now_add=True)
	date_updated_dispute	= models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Disputes"

	def __str__(self):
		return self.stage_dispute


# NAMA MODEL/TABEL: Messages
class Messages(models.Model):

	id_product_message		= models.ForeignKey(Products, on_delete=models.CASCADE)
	transmitter_message		= models.ForeignKey(Users, on_delete=models.CASCADE)
	receiver_message		= models.ForeignKey(Stores, on_delete=models.CASCADE)
	content_message			= models.TextField()
	answer_message			= models.TextField()
	date_created_message 	= models.DateTimeField(auto_now_add=True)
	date_updated_message	= models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Messages"

	def __str__(self):
		return self.transmitter_message
