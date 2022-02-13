# app/marketplace/models.py

# Django modules
from django.db import models

# Locals
from app.accounts.models import Users

# Create your models here.


# NAMA MODEL/TABEL: Categories
class Categories(models.Model):
	name_category			= models.CharField(max_length=100)
	titile_list_category	= models.CharField(max_length=100)
	slug					= models.SlugField(max_length=225, unique=True)
	image_category 			= models.ImageField(upload_to='products/categories/%Y/%m/%d', blank=True)
	icon_category 			= models.ImageField(upload_to='products/categories/icons/%Y/%m/%d', blank=True)
	view_category			= models.IntegerField(default='0')
	date_created_category 	= models.DateTimeField(auto_now_add=True)
	date_updated_category	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name_category',)
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name_category


# NAMA MODEL/TABEL: Subcategories
class Subcategories(models.Model):
	id_category_subcategory		= models.ForeignKey(Categories, on_delete=models.CASCADE)
	titile_list_category		= models.CharField(max_length=100)
	name_subcategory			= models.CharField(max_length=100)
	slug						= models.SlugField(max_length=225, unique=True)
	image_subcategory 			= models.ImageField(upload_to='products/subcategories/%Y/%m/%d', blank=True, null=True)
	view_subcategory			= models.IntegerField(default='0')
	date_created_subcategory	= models.DateTimeField(auto_now_add=True)
	date_updated_subcategory	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name_subcategory',)
		verbose_name_plural = "Subcategories"

	def __str__(self):
		return self.name_subcategory


# NAMA MODEL/TABEL: Stores
class Stores(models.Model):

	id_user_store		= models.ForeignKey(Users, on_delete=models.CASCADE)
	name_store			= models.CharField(max_length=100)
	slug				= models.SlugField(max_length=225, unique=True)
	logo_store			= models.ImageField(upload_to='products/stores/%Y/%m/%d', blank=True, null=True)
	cover_store			= models.ImageField(upload_to='products/stores/%Y/%m/%d', blank=True, null=True)
	about_store			= models.TextField()
	abstract_store		= models.TextField()
	email_store			= models.CharField(max_length=100)
	country_store		= models.CharField(max_length=50)
	city_store			= models.CharField(max_length=50)
	address_store		= models.TextField()
	phone_store			= models.CharField(max_length=50)
	socialnetwork_store	= models.TextField()
	products_store		= models.TextField()
	date_created_store	= models.DateTimeField(auto_now_add=True)
	date_updated_store	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name_store',)
		verbose_name_plural = "Stores"

	def __str__(self):
		return self.name_store


# NAMA MODEL/TABEL: Products
class Products(models.Model):
	feedback_product		= models.TextField()
	state_product			= models.CharField(max_length=50)
	id_store_product		= models.ForeignKey(Stores, on_delete=models.CASCADE)
	id_category_product 	= models.ForeignKey(Categories, on_delete=models.CASCADE)
	id_subcategory_product	= models.ForeignKey(Subcategories, on_delete=models.CASCADE)
	title_list_product		= models.CharField(max_length=50)
	name_product			= models.CharField(max_length=50)
	slug					= models.SlugField(max_length=225, unique=True)
	image_product			= models.ImageField(upload_to='products/products/%Y/%m/%d, blank=True', null=True)
	price_product			= models.DecimalField(max_digits=10, decimal_places=2)
	shipping_product		= models.CharField(max_length=50)
	stock_product			= models.IntegerField(default='0')
	delivery_time_product	= models.IntegerField(default='0')
	offer_product			= models.CharField(max_length=100)
	description_product		= models.TextField()
	summary_product			= models.TextField()
	details_product			= models.TextField()
	specifications_product	= models.CharField(max_length=50)
	gallery_product			= models.CharField(max_length=50)
	video_product			= models.TextField()
	top_banner_product		= models.CharField(max_length=255)
	default_banner_product	= models.CharField(max_length=255)
	horizontal_slider_product= models.TextField()	
	vertical_slider_product	= models.TextField()
	reviews_product			= models.TextField()
	tags_product			= models.CharField(max_length=50)
	sales_product			= models.IntegerField(default='0')
	views_product 			= models.IntegerField(default='0')
	date_created_product	= models.DateTimeField(auto_now_add=True)
	date_updated_product	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name_product',)
		verbose_name_plural = "Products"

	def __str__(self):
		return self.name_product
