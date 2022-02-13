# app/marketplace/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.marketplace.models import (
	Categories, Subcategories,
	Stores, Products
	)

# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
	pass

@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
	pass

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
	pass

@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
	pass
