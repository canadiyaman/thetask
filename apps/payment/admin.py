from django.contrib import admin

from apps.payment.models import PaymentLog


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    list_display = ['user']
    readonly_fields = ['data']
