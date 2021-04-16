from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    CustomerWalletViewSet,
    PaymentMethodViewSet,
    PaymentTransactionViewSet,
    TaskerPaymentAccountViewSet,
    TaskerWalletViewSet,
)

router = DefaultRouter()
router.register("paymenttransaction", PaymentTransactionViewSet)
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("paymentmethod", PaymentMethodViewSet)
router.register("customerwallet", CustomerWalletViewSet)
router.register("taskerwallet", TaskerWalletViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
