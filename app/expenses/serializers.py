from rest_framework import serializers

from .models import Account, Transaction


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['name']

class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'type', 'date', 'notes', 'account']
