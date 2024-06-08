from rest_framework.routers import DefaultRouter

from .viewsets import TransactionViewSet

transaction_router = DefaultRouter()
transaction_router.register(r'', TransactionViewSet, basename='transactions')
