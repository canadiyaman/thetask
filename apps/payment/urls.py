from django.urls import path

from apps.payment.views import ChargeView

urlpatterns = [
    path('charge/', ChargeView.as_view(), name='charge'),
]
