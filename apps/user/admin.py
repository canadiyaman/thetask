from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    readonly_fields = ['last_login', 'date_joined']
    list_display = ['username', 'first_name', 'last_name']
