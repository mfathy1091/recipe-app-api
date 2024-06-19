
from django.contrib import admin
from django.urls import include, path
from expenses.urls import Category_router, account_router, transaction_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/transactions/', include(transaction_router.urls)),
    path('api/categories/', include(Category_router.urls)),
    path('api/accounts/', include(account_router.urls))
]
