# app/marketplace/models.py

# Django modules
from django.db import models

# Locals

# Create your models here.


# NAMA MODEL/TABEL: Categories
class Categories(models.Model):
	name_category			= models.CharField(max_length=100)
	slug					= models.SlugField(max_length=225, unique=True)
	titile_list_category	= models.CharField(max_length=100)
	image_category 			= models.ImageField(upload_to='products/categories/%Y/%m/%d, blank=True')
	icon_category 			= models.ImageField(upload_to='products/categories/icons/%Y/%m/%d, blank=True')
	view_category			= models.IntegerField(default='0')
	date_created_category 	= models.DateTimeField(auto_now_add=True)
	date_updated_category	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name_category',)
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name_category