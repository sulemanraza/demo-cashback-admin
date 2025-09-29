from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportModelAdmin
from .models import CustomUser
from .resources import CustomUserResource


@admin.register(CustomUser)
class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource
    model = CustomUser
    list_display = ("username", "email", "wallet_balance", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_joined")
    search_fields = ("username", "email")
    ordering = ("-date_joined",)

    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("wallet_balance",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("wallet_balance",)}),
    )

    actions = ["reset_wallet"]

    def reset_wallet(self, request, queryset):
        updated = queryset.update(wallet_balance=0)
        self.message_user(request, f"{updated} users’ wallet balances reset to 0.")

    reset_wallet.short_description = "Reset wallet balance for selected users"
