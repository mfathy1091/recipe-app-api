from rest_framework import serializers

from .models import Account, Transaction


class BaseSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    def get_slug(self, obj):
        return obj.name.lower().replace(' ', '-')


class AccountSerializer(BaseSerializer):
    class Meta:
        model = Account
        fields = ['name', 'slug']


class CategorySerializer(BaseSerializer):
    class Meta:
        model = Account
        fields = ['name', 'slug']


class TransactionSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Transaction
        fields = ['amount', 'category', 'type', 'date', 'notes', 'account']
