from django.contrib import admin
from .models import *


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'table_id', 'is_active']


@admin.register(Dishes)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'is_active']

@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',  'is_active']

@admin.register(Tables)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'is_active']