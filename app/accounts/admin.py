# app/accounts/admin.py

# Django modules
from django.contrib import admin

# Loclas
from app.accounts.models import Users

# Register your models here.


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
	pass