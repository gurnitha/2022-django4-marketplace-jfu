# app/likes/admin.py

# Django modules
from django.contrib import admin

# Locals
from app.likes.models import Disputes, Messages

# Register your models here.

@admin.register(Disputes)
class DisputesAdmin(admin.ModelAdmin):
	pass

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
	pass