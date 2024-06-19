from rest_framework.routers import DefaultRouter

from .viewsets import AccountViewSet, CategoryViewSet, TransactionViewSet

transaction_router = DefaultRouter()
transaction_router.register(r'', TransactionViewSet, basename='transactions')

account_router = DefaultRouter()
account_router.register(r'', AccountViewSet, basename='accounts')

Category_router = DefaultRouter()
Category_router.register(r'', CategoryViewSet, basename='categories')
