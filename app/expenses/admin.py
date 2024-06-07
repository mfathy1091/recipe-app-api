from django.contrib import admin

from .models import Account, Category, Transaction, Transfer


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("account", "type", "category", "amount", "date", "notes")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "type")


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "balance", "type")


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ("date", "amount", "from_account", "to_account")
