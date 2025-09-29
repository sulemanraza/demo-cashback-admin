from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CashbackTransaction
from .resources import CashbackTransactionResource


@admin.register(CashbackTransaction)
class CashbackTransactionAdmin(ImportExportModelAdmin):
    resource_class = CashbackTransactionResource
    list_display = ("user", "merchant", "order_id", "amount", "cashback_amount", "status", "created_at")
    list_filter = ("status", "merchant", "created_at")
    search_fields = ("user__username", "merchant__name", "order_id")
    date_hierarchy = "created_at"

    actions = ["mark_as_confirmed", "mark_as_paid"]

    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status="confirmed")
        self.message_user(request, f"{updated} transactions marked as confirmed.")

    def mark_as_paid(self, request, queryset):
        updated = queryset.update(status="paid")
        self.message_user(request, f"{updated} transactions marked as paid.")

    mark_as_confirmed.short_description = "Mark selected as confirmed"
    mark_as_paid.short_description = "Mark selected as paid"
