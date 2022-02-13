# app/users/models.py

# Django modules
from django.db import models
from django_countries.fields import CountryField

# Create your models here.

# NAMA MODEL/TABEL: Profile
class Users(models.Model):

	rol_user 			= models.TextField(blank=True, null=True)
	picture_user		= models.ImageField(
					    	null=True, 
					    	blank=True, 
					    	upload_to='profiles/', 
					    	default="profiles/user-default.png")
	displayname_user	= models.CharField(
					    	max_length=200, 
					    	blank=True, 
					    	null=True)
	username_user		= models.CharField(
					        max_length=200, 
					        blank=True, 
					        null=True)
	password_user		= models.TextField(blank=True, null=True)
	email_user			= models.EmailField(
					    	max_length=100, 
					    	blank=True, 
					    	null=True)
	country_user 		= CountryField()
	city_user			= models.CharField(max_length=100)
	phone_user			= models.CharField(max_length=20)
	address_user		= models.TextField()
	token_user			= models.TextField()
	method_user			= models.TextField()
	wishlist_user		= models.TextField()
	date_created_user 	= models.DateTimeField(auto_now_add=True)
	date_updated_user 	= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('username_user',)
		verbose_name_plural = "Users"
		
	def __str__(self):
		return str(self.username_user)

