from django.contrib import admin

from .models import Account, Category, Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("account", "type", "category", "amount", "date", "notes")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "type")
