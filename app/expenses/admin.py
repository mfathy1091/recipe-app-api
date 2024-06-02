from django.contrib import admin

from .models import Category, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("amount", "category")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")