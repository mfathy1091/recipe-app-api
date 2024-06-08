
from django.contrib import admin
from django.urls import include, path
from expenses.urls import transaction_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/transactions/', include(transaction_router.urls))
]
