# app/marketplace/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.marketplace.models import (
	Categories
	)

# Register your models here.

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
	pass
