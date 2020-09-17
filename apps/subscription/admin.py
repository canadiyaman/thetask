from django.contrib import admin

from apps.subscription.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['is_active', 'subscriber', 'start_date', 'end_date']
